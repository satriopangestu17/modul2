from flask import Flask, send_from_directory, abort, jsonify, render_template

server = Flask(__name__)

#home route 
@server.route('/')
def home():
    return render_template('homepage.html')

@server.route('/digi')
def dig():
    return jsonify('digimon.json')

if __name__ == '__main__':
    server.run(debug = True, host = 'localhost',
    port=2345)

# a = ['andi', 'budi', 'caca']

# b = []
# for i in range(len(a)):
#     for j in a[i]:
#         print(a[0])#b.append(j)
# print(b)