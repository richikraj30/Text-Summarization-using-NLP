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