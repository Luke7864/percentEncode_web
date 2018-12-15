from flask import *

def plainTohex(a):
    a=hex(ord(a))
    return a

app=Flask(__name__)

@app.route("/")
def main():
    return render_template('main.html')

@app.route("/encode",methods=["POST"])
def encode():
    plain=request.form['plain']
    data=plain

    data = list(data)

    num = 0
    for i in data:
        data[num] = plainTohex(data[num])
        data[num] = data[num].replace('0x', '%')
        num += 1

    result = ''
    for i in data:
        result = result + i
    send="PLAIN TEXT : "+plain+"  /   URL ENCODED : "+result
    return send


if __name__=="__main__":
    app.run(debug=False, host='0.0.0.0', port=80)