from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def gen():
    lang_name = request.form.get('lang_name', '')
    input_text = request.form.get('input_text', '')
    if request.method == 'POST':
        pass
    return render_template('gen.html',
            lang_name=lang_name,
            input_text=input_text
            )
