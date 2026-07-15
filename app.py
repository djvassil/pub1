from flask import Flask, request
import requests
import yaml

app = Flask(__name__)


@app.route("/")
def home():
    return "SCA test application — deliberately uses outdated dependencies."


@app.route("/fetch")
def fetch():
    # Uses the (outdated) requests library
    url = request.args.get("url", "https://example.com")
    resp = requests.get(url)
    return resp.text


@app.route("/parse")
def parse():
    # Uses the (outdated) PyYAML library
    data = request.args.get("data", "key: value")
    parsed = yaml.safe_load(data)
    return str(parsed)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
