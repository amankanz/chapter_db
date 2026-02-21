from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Integer, String, Float
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

app = Flask(__name__)

# all_books = []

class Base(DeclarativeBase):
    pass

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///chapter-collection.db"

# A SQLAlchemy instance (db)
db = SQLAlchemy(model_class=Base)
db.init_app(app)

# Define the Book model class
class Book(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    auther: Mapped[str] = mapped_column(String(250), nullable=False)
    rating: Mapped[float] = mapped_column(Float, nullable=False)

with app.app_context():
    db.create_all()



@app.route('/')
def home():
    result = db.session.execute(db.select(Book).order_by(Book.title))
    all_books = result.scalars().all()
    return render_template("index.html", books=all_books)


@app.route("/add", methods=["GET", "POST"])
def add():
    # global all_books
    if request.method == "POST":
        print(request.form)
        data = request.form.to_dict()
        # print(data)

        # title = request.form.get("title")
        # author = request.form.get("author")
        # rating = request.form.get("rating")
        #
        # new_book = {"title": title, "author": author, "rating": rating}
        # all_books.append(new_book)

        all_books.append(data)
        return redirect(url_for("home"))

    return render_template("add.html")


if __name__ == "__main__":
    app.run(debug=True)

