from server.app import create_app, db
from server.models.restaurant import Restaurant
from server.models.pizza import Pizza
from server.models.restaurant_pizza import RestaurantPizza

app = create_app()

with app.app_context():
    
    Restaurant.query.delete()
    Pizza.query.delete()
    RestaurantPizza.query.delete()


    r1 = Restaurant(name="Pizza Planet", address="123 Space St.")
    r2 = Restaurant(name="Mama Mia's", address="456 Pasta Ave")

    p1 = Pizza(name="Pepperoni", ingredients="Cheese, Pepperoni, Tomato")
    p2 = Pizza(name="Margherita", ingredients="Cheese, Basil, Tomato")

    db.session.add_all([r1, r2, p1, p2])
    db.session.commit()

    rp1 = RestaurantPizza(price=10, restaurant_id=r1.id, pizza_id=p1.id)
    rp2 = RestaurantPizza(price=12, restaurant_id=r2.id, pizza_id=p2.id)

    db.session.add_all([rp1, rp2])
    db.session.commit()

    print(" Database seeded!")
