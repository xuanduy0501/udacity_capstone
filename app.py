from flask import Flask

app = Flask(__name__)

@app.route('/')x
def home():
    html = "<h3>Hello, I'm  duyblx. It's my udacity capston project.</h3>"
    return html.format(format)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80, debug=True) # specify port=80
