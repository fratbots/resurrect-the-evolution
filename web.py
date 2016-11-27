from flask import Flask, request, render_template
from lib.lang import *
import random

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def gen():
    lang_name = request.form.get('lang_name', '')
    input_text = request.form.get('input_text', '')
    if request.method == 'POST':

        random.seed(lang_name)
        language = Language(generator)

        translated = language.translate(input_text)
        print_grammar(language)
        print_dictionary(language)

        return translated


    return render_template('gen.html',
            lang_name=lang_name,
            input_text=input_text
            )
