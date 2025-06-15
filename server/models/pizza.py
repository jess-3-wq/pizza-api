from server.app import db

class Pizza(db.Model):
    __tablename__ = "pizzas"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    restaurant_pizzas = db.relationship("RestaurantPizza", back_populates="pizza")
