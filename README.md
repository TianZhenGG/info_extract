# 事件抽取模型 base:python3

#### 依赖安装（gpu，显卡必备）

####安装anaconda(https://www.anaconda.com/)
> 安装显卡驱动，执行nvidia-smi查看是否安装成功
> 安装anaconda
> conda install paddlepaddle-gpu==2.0.2 cudatoolkit=10.2 --channel https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud/Paddle/
> pip install -r ./requirements.txt

[for your tips]: <> (pip install paddlepaddle-gpu -i https://mirror.baidu.com/pypi/simple)

#### 模型下载&使用

```
hub install ernie_tiny==1.1.0
```

更多预训练模型参考 [PaddleHub语义模型](https://www.paddlepaddle.org.cn/hublist?filter=en_category&value=SemanticModel)

**使用时修改 sequence_label.py 中的 model_name = "ernie_tiny"**

### 模型训练

需要在data下放训练集(train.json)、验证集(test.json)、测试集(test.json,可用dev.json代替)、预测集(test1.json)和事件schema文件(event_schema.json)，可从[比赛官网](https://aistudio.baidu.com/aistudio/competition/detail/32?isFromCcf=true)下载

- 训练触发词识别模型

```
sh run_trigger.sh 0 ./data/train/ save_model/trigger
```

模型保存在models/trigger、预测结果保存在data/test1.json.trigger.pred

- 训练论元角色识别模型

```
sh run_role.sh 0 ./data/train/ save_model/role
```
模型保存在models/role、预测结果保存在data/test1.json.role.pred

#### 合并触发词和元角色模型并预测结果

```
python data_process.py --trigger_file data/train/test1.json.trigger.pred --role_file data/train/test1.json.role.pred --schema_file data/train/event_schema.json --save_path data/train/result.json
```
整体预测结果保存在 data/train/result.json

#### 服务部署
```
###下载模型save_model放在textclassfy下面

python3 main.py
测试接口： 
apt-get install curl
curl -X POST -H 'Content-Type: application/json' http://0.0.0.0:8080/sendmsg -d '{"text":"今天天气怎么样"，"id":"uuid-sdadsd-dsdss-sdasaa"}'

```
#### docker运行
```
制作镜像： cd docker && docker build --network host -t mytextclassfy .
运行镜像： docker run --network host  -v ${PWD}/save_model:/opt/textclassfy/ -p 8080:8080  -it  mytextclassfy bash
```


