from flask import Flask, render_template

from scr.articles import articles

# iš flask bibliotekos importuojame klasę Flask ir f-ją render_template.
app = Flask(__name__)
# inicijuojame klasės Flask objektą, priskiriame kintamąjam app.

@app.route('/')
def index():
    return render_template('index.html', data=articles)


@app.route('/about')
def about():
    return render_template('about.html')


if __name__ == '__main__':
  app.run(host='127.0.0.1', port=8000, debug=True)

# patikrinę, ar programa leidžiama ne iš kito failo, leidžiame mūsų app, su parametrais. debug = True klaidos atveju mums rodys informatyvias žinutes naršyklėje.
