# Pizza Restaurant API
Pizza API Challenge
A simple API for managing Restaurants, Pizzas, and their relationships.
Built with Flask, SQLAlchemy, Flask-Migrate, and SQLite.

 Project Setup
1. Clone and install dependencies

Copy 
git clone <your-repo-url>
cd pizza-api-challenge
pipenv install
pipenv shell
2️. Set up the database
Initialize migrations:

Copy code
flask --app server.app db init
Create migration & apply it:

Copy code
flask --app server.app db migrate -m "Initial migration"
flask --app server.app db upgrade
Verify tables:

Copy code
sqlite3 app.db ".tables"

3️. Seed the database
Copy code
python -m server.seed
SHOULD BRING =>"Database seeded!"
4️.Run the server
Copy code
flask --app server.app run
 Server running on http://127.0.0.1:5000/
 API Endpoints
 Restaurants
Method	Endpoint	Description
GET	/restaurants	List all restaurants
GET	/restaurants/<int:id>	Get restaurant details + pizzas
DELETE	/restaurants/<int:id>	Delete a restaurant and its restaurant_pizzas

If restaurant not found → { "error": "Restaurant not found" } with 404.

Pizzas
Method	Endpoint	Description
GET	/pizzas	List all pizzas

 Restaurant Pizzas (Join Table)
Method	Endpoint	Description
POST	/restaurant_pizzas	Add pizza to restaurant with price

Request Body:

json
Copy code
{
  "price": 10,
  "pizza_id": 1,
  "restaurant_id": 1
}
Validation:

price must be between 1 and 30.

On error → { "errors": ["Price must be between 1 and 30"] } with 400.

Success Response:

json
Copy code
{
  "id": 1,
  "price": 10,
  "pizza_id": 1,
  "restaurant_id": 1,
  "pizza": {
    "id": 1,
    "name": "Pepperoni",
    "ingredients": "Cheese, Pepperoni, Tomato"
  },
  "restaurant": {
    "id": 1,
    "name": "Pizza Planet",
    "address": "123 Space St."
  }
}
 Testing
Recommended: Import challenge-1-pizzas.postman_collection.json in Postman.

Test each route.

Check success & error responses.

Try bad price values for validation.

 Models
Model	Fields	Relationships
Restaurant	id, name, address	has many RestaurantPizzas
Pizza	id, name, ingredients	has many RestaurantPizzas
RestaurantPizza	id, price, restaurant_id, pizza_id	belongs to Restaurant & Pizza

 Validation & Cascading
 RestaurantPizza.price must be 1–30.

 Deleting a Restaurant deletes related RestaurantPizzas.


 Project Structure

server/
 ├── app.py
 ├── config.py
 ├── seed.py
 ├── models/
 │   ├── restaurant.py
 │   ├── pizza.py
 │   └── restaurant_pizza.py
 ├── controllers/
 │   ├── restaurant_controller.py
 │   ├── pizza_controller.py
 │   └── restaurant_pizza_controller.py
 ├── migrations/
 └── app.db

