from flask import Flask

app = Flask(__name__) #instance of class

@app.route("/") #URL triggering
def index():  #function to display on browser
    return "<h1>Hello World</h1>"

if __name__ == '__main__':  #To activate debugger
        app.run(debug=True)
