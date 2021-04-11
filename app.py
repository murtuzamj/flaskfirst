from flask import Flask
import yfinance as yf
app = Flask(__name__)

@app.route("/stockinfo")
def hello():
    return "hello"
    #mystockinfo = yf.Ticker(stockname)
    #return mystockinfo.info

if __name__ == "__main__":
    app.run()
