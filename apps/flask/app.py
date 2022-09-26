"""
DevOps Demo Flask Application
"""
from flask import Flask

app = Flask(__name__)

@app.route("/")
def dev_ops_demo():
    """Index route"""
    return "DevOps Demo"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80, debug=True)
