from flask import Blueprint, render_template, request

# Define a Blueprint for the facts routes
bp = Blueprint('fact', __name__, url_prefix="/facts")

# Define the route for submitting new facts
@bp.route('/new')
def new():
    return render_template('facts/new.html')

# Define the route for listing facts
@bp.route('/', methods=['POST'])
def index():
    print(request.form)
    return 'You submitted a fact!'

