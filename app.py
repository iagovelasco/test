import os
from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/')
def index_page():
        return render_template('index.html')

@app.route('/quemSomos')
def quemSomos_page():
        return render_template('quemSomos.html')

@app.route('/cadastro')
def cadastro_page():
        return render_template('cadastro.html')

# P
if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port= port)
