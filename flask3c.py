from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/echo')
def echo():
    kwarg = {}
    kwarg['thing'] = request.args.get('thing')
    kwarg['place'] = request.args.get('place')
    return render_template('flask3.html', **kwarg)


app.run(port=9999, debug=True)
