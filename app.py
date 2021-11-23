from flask import Flask 

app = Flask(__name__)

# @app.route("/")
# def hello_world():
#     return "Hello, World!"

@app.route("/fancy")
def Hello_World_fancy(): 
    return """
    <html>
    <body>
    <h1>Greetings!</h1>
    <p>Hello, world!</p>

    </body>
    </html>
    """
