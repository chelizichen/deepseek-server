
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

### MYSQL8

````shell
docker run --name=mysql8 \
-e MYSQL_ROOT_PASSWORD=lzy20211121 \
-v /path/to/mysql8/data:/var/lib/mysql \
-p 13306:3306 \
--restart=always \
-d docker.1ms.run/library/mysql:8.0.33
````
- jdbc 链接是需要这样指定参数
- jdbc:mysql://124.220.19.199:13306?allowPublicKeyRetrieval=true&useSSL=false

--name=mysql8：为容器指定一个名称（如 mysql8）。

-e MYSQL_ROOT_PASSWORD=<你的root密码>：设置 MySQL 的 root 用户密码。

-v /path/to/mysql8/data:/var/lib/mysql：将宿主机的目录挂载到容器的 MySQL 数据目录，确保数据持久化。

-p 13306:3306：将宿主机的 13306 端口映射到容器的 3306 端口（避免与现有 MySQL 端口冲突）。

--restart=always：确保容器在重启后自动启动。

-d：以后台模式运行容器。

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

