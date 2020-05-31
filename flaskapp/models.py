from flaskapp import db

class cardioData(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(20), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    height = db.Column(db.Integer, nullable=False)
    weight = db.Column(db.Integer, nullable=False)
    gender = db.Column(db.Integer,nullable=False)
    systolic = db.Column(db.Integer, nullable=False)
    diastolic = db.Column(db.Integer, nullable=False)
    cholestrol = db.Column(db.Integer, nullable=False)
    glucose = db.Column(db.Integer, nullable=False)
    alcohol = db.Column(db.Integer)
    physical = db.Column(db.Integer)
    smoking = db.Column(db.Integer)
    disease = db.Column(db.Integer)

    def __repr__(self):
        return f"User('{self.name}','{self.height}','{self.age}','{self.weight}','{self.gender}','{self.cholestrol}','{self.glucose}','{self.alcohol}')"