from flask import Flask, render_template
from .models import db, Author, Book


def create_app():
    app = Flask(__name__)
    app.config.from_object("config.Config")

    db.init_app(app)
    with app.app_context():
        db.create_all()

    # Register web blueprints (split by entity)
    from .web.authors import authors_bp
    from .web.books import books_bp
    app.register_blueprint(authors_bp)  # /authors
    app.register_blueprint(books_bp)  # /books

    @app.get("/")
    def home():
        return render_template(
            "home.html",
            author_count=Author.query.count(),
            book_count=Book.query.count(),
        )

    return app
