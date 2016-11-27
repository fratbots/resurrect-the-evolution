from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def gen():
    lang_name = ''
    input_text = ''
    if request.method == 'POST':
        lang_name = request.form['lang_name']
        input_text = request.form['input_text']
        pass
    return render_template('gen.html',
            seed=lang_name,
            input_text=input_text
            )
