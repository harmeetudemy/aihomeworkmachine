

from flask import Flask, jsonify, request
import chatgpt
app = Flask(__name__)



@app.route("/askgpt", methods=["GET"])
def askgpt():
    string = request.args.get("string")
    result = chatgpt.call_gpt(string)
    #result = ask_gpt(string)
    #print(result)
    return result
    #return jsonify({"result": result})

if __name__ == '__main__':
    app.run()



