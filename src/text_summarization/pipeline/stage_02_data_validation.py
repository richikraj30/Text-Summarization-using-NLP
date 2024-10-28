from text_summarization.config.configuration import ConfigurationManager
from text_summarization.components.data_validation import DataValidation
from text_summarization.logging import logger


class DataValidationPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        data_validation_config = config.get_data_validation_config()
        data_validation = DataValidation(config = data_validation_config)
        data_validation.validate_all_files()
        # data_validation.download_file()
        # data_validation.extract_zip_file()