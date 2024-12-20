import os
from text_summarization.logging import logger
from transformers import AutoTokenizer
from datasets import load_dataset, load_from_disk
from text_summarization.entity import DataTransformationConfig

class DataTransformation:
    def __init__(self, config: DataTransformationConfig):
        self.config = config
        self.tokenizer = AutoTokenizer.from_pretrained(config.tokenizer_name)

    def convert_examples_to_features(self, example_batch):
        input_en = self.tokenizer(example_batch['dialogue'], truncation=True, max_length=1024)

        with self.tokenizer.as_target_tokenizer():
            target_en = self.tokenizer(example_batch['summary'], truncation=True, max_length=128)

        return {
            'input_ids': input_en['input_ids'],
            'attention_mask': input_en['attention_mask'],
            'labels': target_en['input_ids']
        }
    

    def convert(self):
        dataset_samsum = load_from_disk(self.config.data_path)
        dataset_samsum_pt = dataset_samsum.map(self.convert_examples_to_features, batched=True)
        dataset_samsum_pt.save_to_disk(os.path.join(self.config.root_dir, "samsum_dataset"))