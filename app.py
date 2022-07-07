from flask import Flask, render_template, request, jsonify
import json

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/chatbot', methods=('POST','GET'))
def chatbot():
    req = request.get_json(force=True)
    print(req)
    # return jsonify(fulfillmentText = '챗봇 접속 성공')
    return jsonify(fulfillment_messages=[
        {
            "payload":{
                "richContent" : [
                    [
                        {
                            "type" : "image",
                            "rawUrl" : "http://www.pizzaschool.co/data/file/pizza/thumb-1794589283_uVdyjEaC_8484163a9bd7c74740e675f0dca7f08a6f9a67e7_202x150.jpg",
                            "accessibilityText": "피자스쿨 메뉴판"
                        },
                        {
                            "type": "info",
                            "title": "피자스쿨",
                            "subtitle": "피자 메뉴판",
                            "actionLink": "http://www.pizzaschool.co/bbs/board.php?bo_table=pizza"
                        }
                        # 이미지, 카드 등등 정보를 실어서 보낼 수 있음.
                    ]
                ]
            }
        }
    ])
if __name__=='__main__':
    app.run('0.0.0.0', port=5001, debug=True)