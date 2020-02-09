from flask import Flask, request, redirect, render_template, jsonify
app = Flask(__name__)


@app.route('/')
def beranda():
    return render_template('home.html')

@app.route('/')
def home():
    return redirect('/')
# untuk ngebalikkin lagi ke beranda

x = [
    {'no':1, 'nama': 'Andi'},
    {'no':2, 'nama': 'Budi'},
    {'no':3, 'nama': 'Caca'}
]


@app.route('/data/<int:no>')
def data(no):
    return jsonify(x)

@app.route('/test', methods=['GET', 'POST'])
def test():
    if request.method == 'GET':
        return 'Anda nge-GET'
    elif request.method == 'POST':
        body = request.json
        print(body['kota'])
        return jsonify({
            'status': 'Data sukses terkirim',
            'kota': body['kota']
        })
    # if request.method == 'POST':
    #     body = request.json
    #     print(body)
    #     return jsonify({
    #         'status': 'data sukses terkirim',
    #         'nama': body['name'],
    #         'usia': body['age']
    #     })
    else:
        return 'Anda request selain GET & POST'
##to connect with postman. GET, POST

if __name__ == '__main__':
    app.run(debug = True)











## to access must be used same wifi connection

