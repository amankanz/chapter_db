from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

all_books = []


@app.route('/')
def home():
    return render_template("index.html", books=all_books)


@app.route("/add", methods=["GET", "POST"])
def add():
    global all_books
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

