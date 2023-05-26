from flask import Flask, render_template, request, redirect

app = Flask(__name__)


@app.route("/")
def hello_world():
    return render_template('index.html')

@app.route("/<string:page_name>")
def works(page_name):
    return render_template(page_name)

@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        data = request.form.to_dict()
        print(data)
        return redirect('/thankyou.html')
    else:
        return 'I could not steal it'