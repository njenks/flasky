from app import db

class Car(db.Model): 
    id = db.Column(db.Integer, primary_key=True, autoincrement=True) # PK
    driver_id = db.Column(db.Integer, db.ForeignKey('driver.id'))
    mass_kg = db.Column(db.Integer)
    driver = db.relationship("Driver", back_populates="cars")

    def to_dict(self):
        return { 
            "id": self.id, 
            "driver": self.driver.name,
            "mass_kg": self.mass_kg, 
            "team": self.driver.team
        }

    def to_dict_basic(self):
        return {
            "id": self.id, 
            "mass_kg": self.mass_kg
        }