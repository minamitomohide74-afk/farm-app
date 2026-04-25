from flask import Flask,request,jsonify
import json,os
app=Flask(__name__)
F="farm.json"
def ld():
    if os.path.exists(F):
        return json.load(open(F,encoding="utf-8"))
    return {"products":[{"id":1,"name":"にんにく","unit":"kg","stock":120}],"history":[]}
def sv(d):
    json.dump(d,open(F,"w",encoding="utf-8"),ensure_ascii=False)
@app.route("/")
def idx():
    return open("farm.html",encoding="utf-8").read()
@app.route("/api/data")
def get():
    return jsonify(ld())
@app.route("/api/save",methods=["POST"])
def put():
    sv(request.json)
    return jsonify({"ok":True})
if __name__=="__main__":
    app.run(debug=False)
