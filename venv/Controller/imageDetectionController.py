from flask import Blueprint, request, redirect, url_for, jsonify
import os
import cohere
from Domain import imageDetectionDomain
from Domain.Ingredients import Ingredients
co = cohere.Client(api_key='AP7n0AXHe7FNQFKd12cTiN0EcozoztsdpTHMuUfh')

bp = Blueprint('imageDetectionController', __name__, url_prefix='/imageDetection')

@bp.route('/detectGroceries', methods=("GET", "POST"))
def detect_groceries():
    ingredientsArray = imageDetectionDomain.detectGroceries()
    ingredientsReturn = Ingredients(ingredients=ingredientsArray)
    return jsonify(ingredientsReturn.__dict__)