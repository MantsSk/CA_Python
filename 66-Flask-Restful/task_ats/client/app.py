from flask import Flask, render_template, redirect, url_for, request
import requests
import json
from forms import ItemForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'dfgsfdgsdfgsdfgsdf'


@app.route('/')
def index():
    r = requests.get('http://127.0.0.1:8000/items')
    items = json.loads(r.text)
    return render_template("items.html", items=items)


@app.route('/items/<id>')
def item(id):
    r = requests.get(f'http://127.0.0.1:8000/items/{id}')
    item = json.loads(r.text)
    return render_template("item.html", item=item)


@app.route('/items/<id>/update', methods=['GET', 'POST'])
def update_item(id):
    r = requests.get(f'http://127.0.0.1:8000/items/{id}')
    item = json.loads(r.text)
    form = ItemForm()
    if form.validate_on_submit():
        new_item = {
            'title': form.title.data,
            'price': form.price.data,
            'quantity': form.quantity.data
        }
        requests.put(
            f'http://127.0.0.1:8000/items/{id}', json=new_item)
        return redirect(url_for('item', id=id))
    elif request.method == 'GET':
        form.title.data = item['title']
        form.price.data = item['price']
        form.quantity.data = item['quantity']
    return render_template("update_item.html", form=form)


@app.route('/delete/<id>')
def delete_item(id):
    r = requests.delete(f'http://127.0.0.1:8000/items/{id}')
    return redirect(url_for('index'))


@app.route("/items/new", methods=["GET", "POST"])
def new_item():
    form = ItemForm()
    if form.validate_on_submit():
        item = {
            "title": form.title.data,
            "price": form.price.data,
            "quantity": form.quantity.data
        }
        r = requests.post('http://127.0.0.1:8000/items/new', json=item)
        return redirect(url_for('index'))
    return render_template("new_item.html", form=form)


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=True)
