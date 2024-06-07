class Animal(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    species = db.Column(db.String(50), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    gender = db.Column(db.String(10), nullable=False)
    special_requirements = db.Column(db.String(200), nullable=True)

    def serialize(self):
        return {
            'id': self.id,
            'species': self.species,
            'age': self.age,
            'gender': self.gender,
            'special_requirements': self.special_requirements
        }

class Employee(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    phone_number = db.Column(db.String(20), nullable=False)
    role = db.Column(db.String(50), nullable=False)
    schedule = db.Column(db.String(100), nullable=False)

    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'email': self.email,
            'phone_number': self.phone_number,
            'role': self.role,
            'schedule': self.schedule
        }
