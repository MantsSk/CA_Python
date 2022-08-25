from flask import Flask, redirect, render_template, request
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///video_games.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class VideoGames(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(300), nullable=False)
    score = db.Column(db.Integer, nullable=False)
    date_added = db.Column(db.DateTime)

db.create_all()

@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == "POST":
        if request.form['name'] != "":
            game_name = request.form['name']
            review_score = request.form['score']
            description = request.form['description']
            date_added = datetime.now()
            new_review = VideoGames(name=game_name, score=review_score, description=description, date_added=date_added)
            try: 
                db.session.add(new_review)
                db.session.commit()
                return redirect('/')
            except Exception as ex:
                return ex
        else: 
            return redirect('/')
    else:  
        game_reviews = VideoGames.query.order_by(VideoGames.date_added).all()
        return render_template('index.html', game_reviews = game_reviews)

@app.route('/delete/<int:id>')
def delete(id):
    review_to_delete = VideoGames.query.get_or_404(id)
    try: 
        db.session.delete(review_to_delete)
        db.session.commit()
        return redirect('/')
    except Exception as ex:
        return ex

@app.route('/update/<int:id>', methods=['GET', 'POST'])
def update(id):
    print(id)
    game_review = VideoGames.query.get_or_404(id)
    if request.method == 'POST':
        if request.form['name'] != "":
            game_review.name = request.form['name']
            game_review.score = request.form['score']
            game_review.description = request.form['description']
            game_review.date_added = datetime.now()
            try: 
                db.session.commit()
                return redirect('/')
            except Exception as ex:
                return ex
        else:
            return "Updating value to nothing, not allowed"
    else: 
        return render_template('update.html', game_review=game_review)

if __name__ == "__main__":
    app.run(debug=True)