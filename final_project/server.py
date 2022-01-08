from machinetranslation import translator
from flask import Flask, render_template, request

app = Flask("Web Translator", static_folder="static")

@app.route("/")
def renderIndexPage():
    return render_template('index.html')

@app.route("/english_to_french", methods=['GET'])
def englishToFrench():
    textToTranslate = request.args.get('textToTranslate')
    translation = translator.english_to_french(textToTranslate)
    return translation
   

@app.route("/french_to_english", methods=['GET'])
def frenchToEnglish():
    textToTranslate = request.args.get('textToTranslate')
    translation = translator.french_to_english(textToTranslate)
    return translation

if __name__ == "__main__":
    app.run(debug=True, port=8080)
