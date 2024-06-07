from flask import Blueprint, request, jsonify
from app.models import Employee
from app.db import db

employees_bp = Blueprint('employees', __name__)

@employees_bp.route('/', methods=['GET'])
def get_employees():
    employees = Employee.query.all()
    return jsonify([employee.serialize() for employee in employees])

@employees_bp.route('/<int:id>', methods=['GET'])
def get_employee(id):
    employee = Employee.query.get_or_404(id)
    return jsonify(employee.serialize())

@employees_bp.route('/', methods=['POST'])
def add_employee():
    data = request.get_json()
    new_employee = Employee(
        name=data['name'],
        email=data['email'],
        phone_number=data['phone_number'],
        role=data['role'],
        schedule=data['schedule']
    )
    db.session.add(new_employee)
    db.session.commit()
    return jsonify(new_employee.serialize()), 201

@employees_bp.route('/<int:id>', methods=['PUT'])
def update_employee(id):
    data = request.get_json()
    employee = Employee.query.get_or_404(id)

    employee.name = data['name']
    employee.email = data['email']
    employee.phone_number = data['phone_number']
    employee.role = data['role']
    employee.schedule = data['schedule']

    db.session.commit()
    return jsonify(employee.serialize())

@employees_bp.route('/<int:id>', methods=['DELETE'])
def delete_employee(id):
    employee = Employee.query.get_or_404(id)
    db.session.delete(employee)
    db.session.commit()
    return '', 204
