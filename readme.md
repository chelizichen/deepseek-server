
# PYTHON

## env

PYTHON 3.9

### Source
````
conda config --show channels
channels:
  - conda-forge
  - bioconda
  - https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud/bioconda/
  - https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud/conda-forge/
  - https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main/
  - https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/free/
  - defaults
  
conda config --show-sources  
==> /Users/leemulus/.condarc <==
channels:
  - conda-forge
  - bioconda
  - https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud/bioconda/
  - https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud/conda-forge/
  - https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main/
  - https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/free/
  - defaults
show_channel_urls: True
restore_free_channel: True
always_yes: True
````

### Libray
- urllib3 1.26.15 (macos)

### INSTALL PACKAGE

````shell
$ pip install -r requirements.txt
````

## dev

````shell
$ uvicorn main:app --reload --port=8080
````

## build

````shell
$ pyinstaller  main.spec --clean -p=/Users/leemulus/miniconda3/envs/AI/lib/python3.9/site-packages
````

## prod

````shell
./dist/main
````