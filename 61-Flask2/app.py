from flask import Flask, render_template, request
from posts import data
from forms import ContactsForm
import os

app = Flask(__name__)
SECRET_KEY = os.urandom(32)
app.config['SECRET_KEY'] = SECRET_KEY


@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        author = request.form['author']
        date = request.form['date']
        title = request.form['title']
        content = request.form['content']
        data.append({
            'date': date,
            'author': author,
            'title': title,
            'content': content,
            'status': 'published'
        })
    return render_template('index.html', posts=data, page_title="Home")


@app.route('/<string:title>')
def article(title):
    return render_template('article.html', title=title, posts=data)


@app.route('/add_article')
def add_article():
    return render_template('add_article.html')


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/contact_us', methods=['POST', 'GET'])
def contact_us():
    form = ContactsForm()
    if form.validate_on_submit():
        return render_template('contact_success.html', form=form)
    return render_template('contact_us.html', form=form)


if __name__ == '__main__':
    app.run(port=8000, debug=True)
