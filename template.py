import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format = '[%(asctime)s]:%(levelname)s:%(message)s:%(lineno)s:%(funcname)s:%(lineno)s:%(message)s:')


project_name = "ChickenDiseaseCNNClassifier"

list_of_files = [
    ".github/workflows/.gitkeep",
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/utils/common.py",
    f"src/{project_name}/logging/__init__.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/constants/__init__.py"
    "config/config.yaml",
    "dvc.yaml",
    "params.yaml",
    "app.py",
    "main.py",
    "Dockerfile",
    "requirements.txt",
    "setup.py",
    "research/trails.ipynb",
    "test.py"
    ]

for filepath in list_of_files:
    file_path = Path(filepath) # it will provide path type ex : windows path, linux path like based on os
    filedir, filename = os.path.split(file_path) # splitting the path where we have '/'

    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating directory: {filedir} for the file {filepath}")

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0): # getsize providing the file size
        with open(filepath,'w') as f:
            pass
            logging.info(f"Creating empty file: {filepath}")
    else:
        logging.info(f"{filename} is already exists")

