import os
import json
import machinetranslation as mt
from flask import Flask, render_template, request
from machinetranslation import translator

app = Flask("Web Translator")
app.config['EXPLAIN_TEMPLATE_LOADING'] = True
print(os.getcwd())

@app.route("/englishToFrench")
def englishToFrench():
    textToTranslate = request.args.get('textToTranslate')
    translated_text = translator.english_to_french(textToTranslate)
    return translated_text

@app.route("/frenchToEnglish")
def frenchToEnglish():
    textToTranslate = request.args.get('textToTranslate')
    translated_text = translator.french_to_english(textToTranslate)
    return translated_text

@app.route("/")
def renderIndexPage():
    return render_template("index.html", name="blah")
    #return "Hello World"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
