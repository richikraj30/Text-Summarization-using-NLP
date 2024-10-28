import os
from text_summarization.constants import *
from text_summarization.utils.common import read_yaml, create_directories
from transformers import AutoModelForSeq2SeqLM, AutoTokenizer, Trainer, TrainingArguments, DataCollatorForSeq2Seq
from datasets import load_dataset, load_from_disk
import torch
from text_summarization.entity import ModelTrainerConfig

class ModelTrainer:
    def __init__(self, config : ModelTrainerConfig):
        self.config = config

    def train_model(self):
        device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
        tokenizer = AutoTokenizer.from_pretrained(self.config.model_cpkt)
        model_pegasus = AutoModelForSeq2SeqLM.from_pretrained(self.config.model_cpkt).to(device)
        seq2seq_data_collator = DataCollatorForSeq2Seq(tokenizer, model= model_pegasus)

        # Load dataset
        dataset_samsum_pt = load_from_disk(self.config.data_path)

        training_args = TrainingArguments(
            output_dir=self.config.root_dir,
            num_train_epochs=self.config.num_train_epochs,
            per_device_train_batch_size=self.config.per_device_train_batch_size,
            per_device_eval_batch_size=self.config.per_device_train_batch_size,
            warmup_steps=self.config.warmup_steps,
            weight_decay=self.config.weight_decay,
            logging_steps=self.config.logging_steps,
            evaluation_strategy=self.config.evaluation_strategy,
            eval_steps=self.config.eval_steps,
            save_steps=self.config.save_steps,
            gradient_accumulation_steps=self.config.gradient_accumulation_steps
        )

        trainer = Trainer(
            model=model_pegasus,
            args=training_args,
            train_dataset=dataset_samsum_pt["test"],
            eval_dataset=dataset_samsum_pt["validation"],
        )
        trainer.train()

        model_pegasus.save_pretrained(os.path.join(self.config.root_dir, "pegasus-samsum-model"))
        tokenizer.save_pretrained(os.path.join(self.config.root_dir, "tokenizer"))