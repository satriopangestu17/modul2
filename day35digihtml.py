import pandas as pd
import numpy as np
from flask import Flask, send_from_directory, abort, jsonify, render_template
dj = pd.read_csv('digimon.json'
)
print(dj)

djdig = (dj.columns[::].tolist())

df = pd.read_csv('digimon.csv',
delimiter = ',', header =0
)

print(df)

# for template html. ketik hmtl pilih html:5
server = Flask(__name__)

# route dengan response json. import jsonify
@server.route('/')
def home():
    return jsonify(djdig)


@server.route('/digi/<path:namaFile>')  ##harus sama namaFile
def myFile(namaFile):
    return send_from_directory('digicsv', namaFile)

@server.route('/tabel/<path:table>')
def filetable(table):
    return send_from_directory('templates', table)

@server.route('/table')
def html():
    return render_template('table.html')

if __name__ == '__main__':
    server.run(debug = True)


#HTML, <script> element digunakan untuk menulis script, 
# atau lebih tepatnya adalah untuk menyisipkan script (seperti JavaScript) pada sisi client, 
# baik itu ditulis secara langsung di dalam element <script>, 
# maupun merujuk sumber file eksternal dengan attribute src.



# employees = [
#     {'id':1, 'nama':'Andi', 'usia':20, 'kota':'jakarta'},
#     {'id':2, 'nama':'Andi', 'usia':21, 'kota':'jakarta'},
#     {'id':3, 'nama':'Andi', 'usia':22, 'kota':'jakarta'},
#     {'id':4, 'nama':'Andi', 'usia':23, 'kota':'jakarta'},
#     {'id':5, 'nama':'Andi', 'usia':24, 'kota':'jakarta'}
# ]

# print(employees)

