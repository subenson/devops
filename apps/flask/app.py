"""
DevOps Demo Flask Application
"""
from flask import Flask

app = Flask(__name__)

@app.route("/")
def dev_ops_demo():
    return $

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=1235, debug=True)
