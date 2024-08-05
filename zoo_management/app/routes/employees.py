from flask import Blueprint, request, jsonify
from app.models import Employee, db

employees_bp = Blueprint('employees', __name__, url_prefix='/employees')

@employees_bp.route('', methods=['GET'])
def get_employees():
    employees = Employee.query.all()
    return jsonify([employee.as_dict() for employee in employees])

@employees_bp.route('/<int:id>', methods=['GET'])
def get_employee(id):
    employee = Employee.query.get_or_404(id)
    return jsonify(employee.as_dict())

@employees_bp.route('', methods=['POST'])
def add_employee():
    data = request.get_json()
    new_employee = Employee(**data)
    db.session.add(new_employee)
    db.session.commit()
    return jsonify(new_employee.as_dict()), 201

@employees_bp.route('/<int:id>', methods=['PUT'])
def update_employee(id):
    data = request.get_json()
    employee = Employee.query.get_or_404(id)
    for key, value in data.items():
        setattr(employee, key, value)
    db.session.commit()
    return jsonify(employee.as_dict())

@employees_bp.route('/<int:id>', methods=['DELETE'])
def delete_employee(id):
    employee = Employee.query.get_or_404(id)
    db.session.delete(employee)
    db.session.commit()
    return '', 204
