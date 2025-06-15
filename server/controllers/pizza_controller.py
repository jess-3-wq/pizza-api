from flask import Blueprint

pizza_bp = Blueprint('pizzas', __name__, url_prefix='/pizzas')