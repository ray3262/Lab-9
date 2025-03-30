from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///books.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    author = db.Column(db.String(100), nullable=False)
    name = db.Column(db.String(200), nullable=False)


with app.app_context():
    db.create_all()

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        author = request.form["author"]
        name = request.form["name"]
        
        if author and name:
            new_book = Book(author=author, name=name)
            db.session.add(new_book)
            db.session.commit()
        
        return redirect("/")
    
    books = Book.query.all()
    return render_template("index.html", books=books)

if __name__ == "__main__":
    app.run(debug=True)
