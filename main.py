from text_summarization.pipeline.stage_01_data_ingestion import DataIngestionPipeline
from text_summarization.pipeline.stage_02_data_validation import DataValidationPipeline
from text_summarization.pipeline.stage_03_data_transformation import DataTransformationPipeline
from text_summarization.pipeline.stage_04_model_training import ModelTrainingPipeline
from text_summarization.pipeline.stage_05_model_evaluation import ModelEvaluationPipeline
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


# Model Training

STAGE_NAME = "Model Training"

try:
    logger.info(f"Starting {STAGE_NAME} pipeline...")
    modelTrainingPipeline = ModelTrainingPipeline()
    modelTrainingPipeline.main()
    logger.info(f"{STAGE_NAME} pipeline completed successfully!")

except Exception as e:
    logger.exception(e)
    raise e


# Model Evaluation

STAGE_NAME = "Model Evaluation"

try:
    logger.info(f"Starting {STAGE_NAME} pipeline...")
    modelEvaluationPipeline = ModelEvaluationPipeline()
    modelEvaluationPipeline.main()
    logger.info(f"{STAGE_NAME} pipeline completed successfully!")

except Exception as e:
    raise e

