#Utils its just a functionality that you will frequently using in your code
#So let's say you want to read a file, so instead of all time write command read
#You can just write this command here and after import from utils
import os
from box.exceptions import BoxValueError
import yaml
from MLOpsproject import logger
import json
import joblib
from ensure import ensure_annotations
from box import ConfigBox
from pathlib import Path
from typing import Any


@ensure_annotations#Creating a decorator
#A decorator is used to modify the behaviour of a function or a class. The way this is achieved is by defining a function (decorator) that returns another function
def read_yaml(path_to_yaml:Path) -> ConfigBox:
    """ reads yaml file and returns
    ARGS:
        path_to_yaml (str): path like input

    Raises:
        ValueError: if yaml file is empty
        e: empty file

    Returns:
        ConfigBox: ConfigBox type

    """

    try:
        with open(path_to_yaml) as yaml_file:
            content = yaml.safe_load(yaml_file)
            logger.info(f"yaml file: {path_to_yaml} loaded successfully")
            return ConfigBox(content)
    except BoxValueError:
        raise ValueError("yaml file is empty")
    except Exception as e:
        raise e
    
@ensure_annotations
def create_directories(path_to_directories: list, verbose=True):# This function need to create a new directories
    #Such as data training, testing, validation etc.
    """ create list of directories

    Args:
        path_to_directories (list): list of path of directories
        ignore_log(bool,optional): ignore is multiple dirs is to be create.Defaults false.
    """
    for path in path_to_directories:
        os.makedirs(path,exist_ok=True)
        if verbose:
            logger.info(f"created directory at:  {path}")

@ensure_annotations
def save_json(path: Path, data: dict):
    """save json data

    Args:
        path (Path): path to json file
        data (dict): data to be save in json file
    """
    with open(path, "w") as f:
        json.dump(data, f, indent=4)

    logger.info(f"json file saved at: {path}")


@ensure_annotations
def load_json(path: Path) -> ConfigBox:
    """load json file data 
    Args:
        path(Path): path to json file
    Returns:
        ConfigBox: data as class attributes instead of dict
    """
    with open(path) as f:
        content = json.load(f)

    logger.info(f"json file loaded succesfully from: {path}")
    return ConfigBox(content)

@ensure_annotations
def save_bin(data: Any, path: Path):
    """ save binary file
    Args:
        data (Any): data to be saved as binary
        path (Path): path to binary
    """
    joblib.dump(value=data,filename=path)
    logger.info(f"binary file saved at: {path}")

@ensure_annotations
def load_bin(path: Path) -> Any:
    """ Load binary data
    Args:
        path (Path): path to binary file
    Returns:
        Any: object stored in the file
    """
    data = joblib.load(path)
    logger.info(f"binary  file loaded from: {path}")
    return data

@ensure_annotations
def get_size(path:Path) -> str:
    """ get size in KB
    Arg:
        path (Path): path of the file
    Returns:
        str: size in KB
    """
    size_in_kb = round(os.path.getsize(path)/1024)
    return print(f"~ {size_in_kb} KB")