from flask import Flask, json, jsonify
import requests






app = Flask(__name__)



#Home
#Display count of persons and persosn properties
@app.route("/")
def home_page():
    _result={'status':'ok', 'message':'WelCome To API Server'}
    return jsonify(_result)

@app.route("/sendmsg/<id>")
def sendMessage(id):
    _url="https://api.telegram.org/bot233935395:AAGlA52RnM74d_H3HKCaj4RBi37Oah5FqAc/sendMessage?chat_id=-1001141238059&parse_mode=HTML&text="+id
    _resultOfTel=requests.get(_url)
    _result={'status':'ok', 'message':str(_resultOfTel)}
    return jsonify(_result)

if __name__ == '__main__':
    app.run(debug=True, port=8090)
    

    
