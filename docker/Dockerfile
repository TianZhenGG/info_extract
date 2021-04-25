FROM digglerz/python3.8

RUN sed -i s@/archive.ubuntu.com/@/mirrors.aliyun.com/@g /etc/apt/sources.list && \
    apt-get update &&  \
    apt-get install -y \
        libsm6          \
        libxrender1     \
        libgomp1        \    
        libxext-dev      \
        libglib2.0-dev \
        libgl1-mesa-glx \
        vim && \
        pip install --upgrade --force pip
ADD resource.tar.gz /opt/
WORKDIR /opt/textclassfy
RUN python -m pip install -r requirements.txt -i https://mirror.baidu.com/pypi/simple && \
    hub install ernie_tiny==1.1.0
CMD python3 main.py
EXPOSE 8080
