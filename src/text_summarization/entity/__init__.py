from dataclasses import dataclass
from pathlib import Path

# Data ingestion configuration
@dataclass(frozen=True)
class DataIngestionConfig:
    root_dir : Path
    source_url : str
    local_data_file : Path
    unzip_dir : Path

# Data Validation configuration
@dataclass(frozen=True)
class DataValidationConfig:
    root_dir : Path
    STATUS_FILE_NAME : str
    ALL_REQUIRED_FILES : list

# Data Transformation configuration
@dataclass(frozen=True)
class DataTransformationConfig:
    root_dir : Path
    data_path : Path
    tokenizer_name : Path

# Model Training configuration
@dataclass(frozen=True)
class ModelTrainerConfig:
    root_dir : Path
    data_path : Path
    model_cpkt : Path
    num_train_epochs : int
    warmup_steps : int
    per_device_train_batch_size : int
    weight_decay : float
    logging_steps : int
    evaluation_strategy : str
    eval_steps : int
    save_steps : float
    gradient_accumulation_steps : int

# Model Evaluation configuration
@dataclass(frozen=True)
class ModelEvaluatorConfig:
    root_dir : Path
    data_path : Path
    model_path : Path
    tokenizer_path : Path
    metric_file_name : Path