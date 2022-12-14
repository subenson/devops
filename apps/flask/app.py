"""
DevOps Demo Flask Application
"""
from flask import Flask

app = Flask(__name__)

@app.route("/")
def dev_ops_demo():
    """Index route."""
    version = "1.0"
    with open("version", encoding="utf-8") as version_file:
        version = version_file.read()

    return f"DevOps Demo V{version}"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=1235, debug=True)
