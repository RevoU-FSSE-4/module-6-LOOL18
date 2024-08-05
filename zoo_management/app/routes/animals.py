from flask import Blueprint, request, jsonify
from app.models import Animal, db

animals_bp = Blueprint('animals', __name__, url_prefix='/animals')

@animals_bp.route('', methods=['GET'])
def get_animals():
    animals = Animal.query.all()
    return jsonify([animal.as_dict() for animal in animals])

@animals_bp.route('/<int:id>', methods=['GET'])
def get_animal(id):
    animal = Animal.query.get_or_404(id)
    return jsonify(animal.as_dict())

@animals_bp.route('', methods=['POST'])
def add_animal():
    data = request.get_json()
    new_animal = Animal(**data)
    db.session.add(new_animal)
    db.session.commit()
    return jsonify(new_animal.as_dict()), 201

@animals_bp.route('/<int:id>', methods=['PUT'])
def update_animal(id):
    data = request.get_json()
    animal = Animal.query.get_or_404(id)
    for key, value in data.items():
        setattr(animal, key, value)
    db.session.commit()
    return jsonify(animal.as_dict())

@animals_bp.route('/<int:id>', methods=['DELETE'])
def delete_animal(id):
    animal = Animal.query.get_or_404(id)
    db.session.delete(animal)
    db.session.commit()
    return '', 204