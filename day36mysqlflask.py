from flask import Flask, request, redirect, render_template, jsonify
import mysql.connector as mc
app = Flask(__name__)

## for sql bukan mongodb
dbku = mc.connect(
    host = 'localhost', user='root',
    passwd='12344321', database='testing'
)

@app.route('/')
def home():
    return render_template('form.html')

@app.route('/form', methods=['POST'])   ###/form will go to html form
def form():
    if request.method == 'POST':
        body = request.form
        print(body['nama'])
        x = dbku.cursor()
        data = (body['nama'], body['usia'])
        sql = f'insert into datadiri (nama, usia) values {data}'
        x.execute(sql)
        dbku.commit()
        return redirect('/data')
        # return 'data sudah masuk'


@app.route('/data', methods=['GET', 'POST', 'PUT', 'DELETE'])   ## lewat postman bisa untuk nambah ke database
def data():
    if request.method == 'GET':
        x = dbku.cursor()
        x.execute('select * from datadiri')
        hasil = x.fetchall() ##will extract all the rows at once in tuple form. fetchone=only get one row. fetchmany(2)=only get 2 two rows
        hasil = list(map(lambda i:{'id':i[0], 
        'nama': i[1], 'usia': i[2]}, hasil))
        print(hasil)
        return jsonify(hasil)
    elif request.method == 'POST':
        body = request.json
        x = dbku.cursor()
        data = (body['nama'], body['usia'])
        sql = f'insert into datadiri (nama, usia) values {data}'
        x.execute(sql)
        dbku.commit()
        return 'POST'
    # elif request.method == 'POST':
    #     return 'POST'

@app.route('/data/<int:no>', methods=['GET', 'POST'])
def datas(no):
    if request.method == 'GET':
        x = dbku.cursor()
        sql = f'select * from datadiri where id = {no}'
        x.execute(sql)
        hasil = x.fetchall()
        hasil = list(map(lambda i:{'id':i[0], 
        'nama': i[1], 'usia': i[2]}, hasil))
        print(hasil)
        return jsonify(hasil)
    # elif request.method == 'POST':
    #     body = request.json
    #     x = dbku.cursor()
    #     data = (body['nama'], body['usia'])
    #     sql = f'insert into datadiri (nama, usia) values {data}'
    #     x.execute(sql)
    #     dbku.commit()
    #     return 'POST'


if __name__ == '__main__':
    app.run(debug = True)



##ujian modul2
# mysql
# numpy
# pandas : mean, median, mode, quartil 25 50 75
# distribusi: histogram.
# df(dataframe) join merge pivot

# matplotlib
# seaborn
# plotly


##baca2 liburan:
#tableau.com
#powerbi