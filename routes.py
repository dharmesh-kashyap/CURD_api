from flask import Blueprint, request, jsonify
from extensions import db
from models import Book, Member
from datetime import datetime

api = Blueprint('api', __name__)

@api.route('/books', methods=['GET'])
def get_books():
    books = Book.query.all()
    return jsonify([{"id": book.id, "title": book.title, "author": book.author, "isbn": book.isbn, "available_copies": book.available_copies} for book in books])

@api.route('/books', methods=['POST'])
def add_book():
    data = request.json
    book = Book(**data)
    db.session.add(book)
    db.session.commit()
    return jsonify({"message": "Book added successfully"}), 201

@api.route('/books/<int:book_id>', methods=['PUT'])
def update_book(book_id):
    data = request.json
    book = Book.query.get_or_404(book_id)
    book.title = data.get('title', book.title)
    book.author = data.get('author', book.author)
    book.isbn = data.get('isbn', book.isbn)
    book.available_copies = data.get('available_copies', book.available_copies)
    db.session.commit()
    return jsonify({"message": "Book updated successfully"})

@api.route('/books/<int:book_id>', methods=['DELETE'])
def delete_book(book_id):
    book = Book.query.get_or_404(book_id)
    db.session.delete(book)
    db.session.commit()
    return jsonify({"message": "Book deleted successfully"})

@api.route('/members', methods=['GET'])
def get_members():
    members = Member.query.all()
    return jsonify([{"id": member.id, "name": member.name, "email": member.email, "joined_date": member.joined_date.strftime('%Y-%m-%d')} for member in members])

@api.route('/members', methods=['POST'])
def add_member():
    data = request.json
    if 'joined_date' in data:
        data['joined_date'] = datetime.strptime(data['joined_date'], '%Y-%m-%d').date()
    
    member = Member(**data)
    db.session.add(member)
    db.session.commit()
    return jsonify({"message": "Member added successfully"}), 201
