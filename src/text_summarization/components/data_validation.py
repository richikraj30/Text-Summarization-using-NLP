import os
import urllib.request as request
import zipfile
from text_summarization.logging import logger
from text_summarization.utils.common import get_size
from text_summarization.entity import (DataValidationConfig)
from pathlib import Path

class DataValidation:
    def __init__(self, config: DataValidationConfig):
        self.config = config

    def validate_all_files(self) -> bool:
        try:
            validationStatus = None
            all_files = os.listdir(os.path.join("artifacts", "data_ingestion", "samsum_dataset"))

            for file in all_files:
                if file in self.config.ALL_REQUIRED_FILES:
                    validationStatus = True
                    with open(self.config.STATUS_FILE_NAME, "w") as file:
                        file.write(f"Validation status: {validationStatus}")
                    logger.info(f"Validation status: {validationStatus}")
                else:
                    validationStatus = False
                    with open(self.config.STATUS_FILE_NAME, "w") as file:
                        file.write(f"Validation status: {validationStatus}")
                    logger.warning(f"Validation status: {validationStatus}")
            
            return validationStatus
        
        except Exception as e:
            raise e
