from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <html>
        <head><title>Flask HTML Example</title></head>
        <body>
            <h1>Hello, world!</h1>
            <p>This HTML was returned directly as a string.</p>
        </body>
    </html>
    """


if __name__ == '__main__':
    app.run(debug=True, port=os.getenv("PORT", default=5000))
