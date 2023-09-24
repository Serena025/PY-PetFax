from flask import Blueprint, render_template

fact_bp = Blueprint('fact', __name__, url_prefix="/facts")

@fact_bp.route('/new')
def new(): 
    return render_template('facts/new.html')
