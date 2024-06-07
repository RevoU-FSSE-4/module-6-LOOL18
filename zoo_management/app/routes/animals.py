from flask import Blueprint, request, jsonify
from app.models import Animal
from app.db import db

animals_bp = Blueprint('animals', __name__)

@animals_bp.route('/', methods=['GET'])
def get_animals():
    animals = Animal.query.all()
    return jsonify([animal.serialize() for animal in animals])

@animals_bp.route('/<int:id>', methods=['GET'])
def get_animal(id):
    animal = Animal.query.get_or_404(id)
    return jsonify(animal.serialize())

@animals_bp.route('/', methods=['POST'])
def add_animal():
    data = request.get_json()
    new_animal = Animal(
        species=data['species'],
        age=data['age'],
        gender=data['gender'],
        special_requirements=data.get('special_requirements')
    )
    db.session.add(new_animal)
    db.session.commit()
    return jsonify(new_animal.serialize()), 201

@animals_bp.route('/<int:id>', methods=['PUT'])
def update_animal(id):
    data = request.get_json()
    animal = Animal.query.get_or_404(id)

    animal.species = data['species']
    animal.age = data['age']
    animal.gender = data['gender']
    animal.special_requirements = data.get('special_requirements')

    db.session.commit()
    return jsonify(animal.serialize())

@animals_bp.route('/<int:id>', methods=['DELETE'])
def delete_animal(id):
    animal = Animal.query.get_or_404(id)
    db.session.delete(animal)
    db.session.commit()
    return '', 204
