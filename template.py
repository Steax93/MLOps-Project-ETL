#This template provides automatickaly creation all necessary folders and files, so you dont need each time write code again
#Just execute this code and it will create for you automaticaly
import os
from pathlib import Path
import logging
#initial a logging stringso you can see the log in your terminal
logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')

#Assign project name
project_name ='mlproject'

list_of_files = [
    ".github/workflows/.gitkeep",#creating inside folder "github" > "workflows" > creating file "gitkeep"
    #after we creating a bunchs of folders with a files inside 
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/utils/common.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/entity/config_entity.py",
    f"src/{project_name}/constants/__init__.py",
    "config/config.yaml",
    "params.yaml",
    "schema.yaml",
    "main.py",
    "app.py",
    "Dockerfile",
    "requirements.txt",
    "setup.py",
    "research/trials.ipynb",
    "templates/index.html"
]

for filepath in list_of_files: # Converting all strings to a paths
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)#Separating folders from the files inside 

    if filedir != "":#This task creating a folder if folder is not empty and providing Log in information
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating directory; {filedir} for the file: {filename}")

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):#This task creating a file if file doesn't exist
        #It will create a new file and get the Log in information
        with open(filepath, "w") as f:
            pass
            logging.info(f"Creating empy file: {filepath}")

    else:
        logging.info(f"{filename} as already exists")# If all good it will give me Log in file is already exists