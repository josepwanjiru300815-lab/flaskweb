from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return """
    <html>
        <head>
            <title>Flask Web Control</title>
        </head>

        <body style="text-align:center;font-family:Arial;margin-top:60px;">
            <h1>ESP32 Flask Control Panel</h1>

            <a href="/on">
                <button style="padding:20px;background:green;color:white;font-size:18px;">
                    TURN ON
                </button>
            </a>

            <a href="/off">
                <button style="padding:20px;background:red;color:white;font-size:18px;">
                    TURN OFF
                </button>
            </a>

        </body>
    </html>
    """

@app.route('/on')
def on():
    return "Command: ON"

@app.route('/off')
def off():
    return "Command: OFF"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)