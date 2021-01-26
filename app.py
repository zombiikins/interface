from flask import Flask, render_template, url_for

app = Flask(__name__)

@app.route("/")
def index():
  return render_template('index.html')

@app.route("/add")
def add():
  return render_template('add.html')

@app.route("/read")
def read():
  return render_template('read.html')

@app.route("/update")
def update():
  return render_template('update.html')


if __name__ == "__main__":
  app.run(debug=True)