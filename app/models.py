from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Author(db.Model):
    __tablename__ = "authors"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    bio = db.Column(db.Text)
    books = db.relationship(
        "Book",
        back_populates="author",
        cascade="all, delete-orphan",
        passive_deletes=True,
    )


class Book(db.Model):
    __tablename__ = "books"
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    published_year = db.Column(db.Integer)
    author_id = db.Column(
        db.Integer,
        db.ForeignKey("authors.id", ondelete="CASCADE"),
        nullable=False,
    )
    author = db.relationship("Author", back_populates="books")
