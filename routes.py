from flask import Flask, render_template
app = Flask(__name__)

# two decorators, same function


@app.route('/')
@app.route('/index.html')
def index():
    return render_template('index.html', the_title='What is DevOps?')


@app.route('/sre.html')
def sre():
    return render_template('sre.html', the_title='Site reliability engineering')


@app.route('/twelve.html')
def twelve():
    return render_template('twelve.html', the_title='Twelve-Factor App')


if __name__ == '__main__':
    app.run(debug=True)
