from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def romantic_page():
    return render_template('romantic.html')

if __name__ == '__main__':
    app.run(debug=True)