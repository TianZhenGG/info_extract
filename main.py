import os
import json
from flask import Flask,request


app = Flask(__name__)

@app.route('/sendmsg',methods=['POST'])
def hello_world():
    data = request.json
    with open('data/predict/test1.json','w') as fw:
        json.dump(data,fw)
        # ensure_ascii = False, sort_keys = True, indent = 4
    os.system('cmd/script/run_trigger_predict.sh \
               1 \
               data/predict \
               save_model/trigger')
    os.system('cmd/script/run_role_predict.sh \
                1 \
                data/predict \
                save_model/role')
    os.system('python cmd/script/data_process.py \
                        --trigger_file data/predict/test1.json.trigger.pred \
                        --role_file data/predict/test1.json.role.pred \
                        --schema_file data/predict/event_schema.json \
                        --save_path data/predict/result.json')

    with open('data/predict/result.json','r') as fr:
        result = fr.read()
    return result
 
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
