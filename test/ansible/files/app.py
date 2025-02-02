from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return "Hola desde el esclavo!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000) # Escucha en todas las interfaces