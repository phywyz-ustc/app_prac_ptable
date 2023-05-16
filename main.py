from flask import Flask, request, render_template
from utils import *
app = Flask(__name__)

#定义输入渲染路由
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/SearchName", methods=["POST"])
def SearchName():
    number = int(request.form["element1"])
    result = GetEleNum(number)
    return render_template("resultEle.html", result=result)

@app.route("/SearchNum", methods=["POST"])
def SearchNum():
    number = int(request.form["number"])
    result = GetEleNum(number)
    return render_template("resultEle.html", result=result)


@app.route("/SearchComText", methods=["POST"])
def SearchComText():
    text = str(request.form["text"])
    result = GetComText(text)
    return render_template("resultCom.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)