import re
from flask import Flask, request, render_template
from jinja2 import evalcontextfilter, Markup, escape
from lib.lang import *
import random

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def gen():
    lang_name = request.form.get('lang_name', '')
    input_text = request.form.get('input_text', '')
    translated = None
    grammar = None
    orpho_dictionary = None
    if request.method == 'POST':
        random.seed(lang_name)
        language = Language(generator)
        translated = language.translate(input_text)
        grammar = print_grammar(language)
        orpho_dictionary = print_dictionary(language)

    return render_template('gen.html',
            lang_name=lang_name,
            input_text=input_text,
            translated=translated,
            grammar=grammar,
            orpho_dictionary=orpho_dictionary
            )



_paragraph_re = re.compile(r'(?:\r\n|\r|\n){2,}')

@app.template_filter()
@evalcontextfilter
def nl2br(eval_ctx, value):
    result = u'\n\n'.join(u'<p>%s</p>' % p.replace('\n', '<br>\n') \
        for p in _paragraph_re.split(escape(value)))
    if eval_ctx.autoescape:
        result = Markup(result)
    return result
