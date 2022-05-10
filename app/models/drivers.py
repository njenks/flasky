from app import db

class Driver(db.Model): 
    id = db.Column(db.Integer, primary_key=True, autoincrement=True) # PK
    name = db.Column(db.String)
    team = db.Column(db.String)
    country = db.Column(db.String)
    handsome = db.Column(db.Boolean)
    cars = db.relationship("Car", back_populates="driver") 

    def to_dict(self):
        return {
            "id": self.id, 
            "name": self.name, 
            "team": self.team, 
            "country": self.country,
            "handsome": self.handsome
        }