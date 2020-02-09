# bikin server
from flask import Flask, send_from_directory, abort, jsonify, render_template

server = Flask(__name__)

employees = [
    {'id':1, 'nama':'Andi', 'usia':20, 'kota':'jakarta'},
    {'id':2, 'nama':'Andi', 'usia':21, 'kota':'jakarta'},
    {'id':3, 'nama':'Andi', 'usia':22, 'kota':'jakarta'},
    {'id':4, 'nama':'Andi', 'usia':23, 'kota':'jakarta'},
    {'id':5, 'nama':'Andi', 'usia':24, 'kota':'jakarta'}
]
#home route 
@server.route('/')
def home():
    return '<h1>welcome to my server!</h1>'

# if __name__== '__main__':
#     server.run(debug = True)  ## debug agar bisa restart sendiri servernya ketika ada  perubahan

#render html
@server.route('/html')
def html():
    return render_template('html.html')

# if __name__ == '__main__':
#     server.run(debug = True)


#ketik lorem

# send data from flask, render html
@server.route('/data')
def data():
    nama = 'Andi'
    kota = 'Jakarta'
    return render_template('data.html', data = {'name':nama, 'city':kota})

# if __name__ == '__main__':
#     server.run(debug = True, host = 'localhost',
#     port = 1234)

# route dengan response json. import jsonify
@server.route('/karyawan')
def karyawan():
    return jsonify(employees)

# if __name__ == '__main__':
#     server.run(debug = True, host = 'localhost',
#     port = 1234)

#dynamis route: karyawan/1
# @server.route('/karyawan/<int:id>')
# def Employees(id):
#     return jsonify(employees[id-1])

#import abort, agar kalau out of range id nya keluar servererror
@server.route('/karyawan/<int:id>')
def Employees(id):
    if id > len(employees) or id < 1:
        abort(404)
    else:
        return jsonify(employees[id-1])


# if __name__ == '__main__':
#     server.run(debug = True, host = 'localhost',
#     port = 1234)
##bisa masuk ke:
# http://localhost:1234/karyawan/1

#render static file: storage
@server.route('/file/<path:namaFile>')
def myFile(namaFile):
    return send_from_directory('storage', namaFile)
# http://localhost:1234/file/CN.pdf

# route untuk error 404
@server.errorhandler(404)
def notFound(id):
    return render_template('error.html')

if __name__ == '__main__':
    server.run(debug = True, host = 'localhost',
    port = 1234)



##tugas
# 1. biodata:
# homeabout
# education
# skills
# experiences

# 2. digidb => flask response:
# /table => HTML tabel data digidb
# /json => JSON data digimon