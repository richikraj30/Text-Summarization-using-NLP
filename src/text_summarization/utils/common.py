import os
from box.exceptions import BoxValueError
import yaml
from text_summarization.logging import logger
from ensure import ensure_annotations
from box import ConfigBox
from pathlib import Path
from typing import Any


# @ensure_annotations
# def read_yaml(file_path: Path) -> ConfigBox:
#     try:
#         with open(file_path) as yaml_file:
#             yaml_data = yaml.safe_load(yaml_file)
#             logger.info(f"Successfully loaded YAML data from {file_path}")
#             return ConfigBox(yaml_data)
#     except BoxValueError:
#         raise ValueError("yaml file is empty or contains invalid data")
    
#     except Exception as e:
#         raise e

@ensure_annotations
def read_yaml(file_path: Path) -> ConfigBox:
    try:
        with open(file_path) as yaml_file:
            yaml_data = yaml.safe_load(yaml_file)
            logger.info(f"Successfully loaded YAML data from {file_path}")
            return ConfigBox(yaml_data)
    except ValueError:
        raise ValueError("YAML file is empty or contains invalid data")
    except Exception as e:
        logger.error(f"Error loading YAML file from {file_path}: {e}")
        raise e    

@ensure_annotations
def create_directories(directory_paths: list, verbose=True):

    for path in directory_paths:
        os.makedirs(path, exist_ok=True)
        if verbose:
            logger.info(f"Created directory: {path}")


@ensure_annotations
def get_size(directory_path: Path) -> str:
    size_in_kb = round(os.path.getsize(directory_path) / 1024)
    return f"~ {size_in_kb} KB"


