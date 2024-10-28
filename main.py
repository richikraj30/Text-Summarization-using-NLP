from text_summarization.pipeline.stage_01_data_ingestion import DataIngestionPipeline
from text_summarization.pipeline.stage_02_data_validation import DataValidationPipeline
from text_summarization.pipeline.stage_03_data_transformation import DataTransformationPipeline
from text_summarization.logging import logger

# Data Ingestion 
STAGE_NAME = "Data Ingestion"

try:
    logger.info(f"Starting {STAGE_NAME} pipeline...")
    pipeline = DataIngestionPipeline()
    pipeline.main()
    logger.info(f"{STAGE_NAME} pipeline completed successfully!")

except Exception as e:
    logger.exception(e)
    raise e

# Data Validation 
STAGE_NAME = "Data Validation"

try:
    logger.info(f"Starting {STAGE_NAME} pipeline...")
    dataValidationPipeline = DataValidationPipeline()
    dataValidationPipeline.main()
    logger.info(f"{STAGE_NAME} pipeline completed successfully!")

except Exception as e:
    logger.exception(e)
    raise e


# Data Transformation
STAGE_NAME = "Data Transformation"

try:
    logger.info(f"Starting {STAGE_NAME} pipeline...")
    dataTransformationPipeline = DataTransformationPipeline()
    dataTransformationPipeline.main()
    logger.info(f"{STAGE_NAME} pipeline completed successfully!")

except Exception as e:
    logger.exception(e)
    raise e


