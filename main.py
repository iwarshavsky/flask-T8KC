from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <html>
        <head><title>Job Page</title></head>
        <body style="margin:0; padding:0;">
            <h1>ImagenAI Job Posting</h1>
            <iframe 
                src="https://www.comeet.com/jobs/imagen-ai/78.00F" 
                width="100%" 
                height="800" 
                style="border:none;">
            </iframe>

        </body>
    </html>
    """


if __name__ == '__main__':
    app.run(debug=True, port=os.getenv("PORT", default=5000))
