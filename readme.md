
# PYTHON

## env

PYTHON 3.9

## Windows2Linux

windows 需要使用 wsl
````
wsl --install
````

- nautilus 
- miniconda
- git

````shell
$ conda create -n dpsk python=3.9
````

然后使用pycharm 添加解释器，连接 miniconda/envs 下的虚拟环境



### Source

````
$ pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple/
````


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

