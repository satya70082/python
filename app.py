from flask import Flask, send_from_directory

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello, Flask App!"

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(
        directory='.',
        path='favicon.ico',
        mimetype='image/vnd.microsoft.icon'
    )

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
