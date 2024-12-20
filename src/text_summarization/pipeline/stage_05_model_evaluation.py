from text_summarization.config.configuration import ConfigurationManager
from text_summarization.components.model_evaluation import ModelEvaluation
from text_summarization.logging import logger



class ModelEvaluationPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        model_evaluation_config = config.get_model_evaluation_config()
        model_evaluation = ModelEvaluation(config = model_evaluation_config)
        model_evaluation.evaluate()