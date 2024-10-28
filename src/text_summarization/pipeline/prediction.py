# from text_summarization.config.configuration import ConfigurationManager
# from transformers import AutoTokenizer, pipeline


# class PredictionPipeline:
#     def __init__(self):
#         self.config = ConfigurationManager().get_model_evaluation_config()


#     def predict(self, text):
#         tokenizer = AutoTokenizer.from_pretrained(self.config.tokenizer_path)
#         gen_kwargs = {"length_penalty" : 0.8, "num_beams" : 8, "max_length" : 128}

#         model = pipeline('text-summarizer', model=self.config.model_path, tokenizer=tokenizer)

#         print("Dialogue:", text)

#         output = model(text, **gen_kwargs)[0]['summary_text']
#         print("\nGenerated Summary:", output)
#         print(output)

#         return output

from text_summarization.config.configuration import ConfigurationManager
from transformers import AutoTokenizer, pipeline

class PredictionPipeline:
    def __init__(self):
        self.config = ConfigurationManager().get_model_evaluation_config()

    def predict(self, text):
        tokenizer = AutoTokenizer.from_pretrained(self.config.tokenizer_path)
        gen_kwargs = {"length_penalty": 0.8, "num_beams": 8, "max_length": 128}

        # Change 'text-summarizer' to 'summarization'
        model = pipeline('summarization', model=self.config.model_path, tokenizer=tokenizer)

        print("Dialogue:", text)

        output = model(text, **gen_kwargs)[0]['summary_text']
        print("\nGenerated Summary:", output)

        return output
