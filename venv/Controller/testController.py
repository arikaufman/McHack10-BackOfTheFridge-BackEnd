from flask import Blueprint, jsonify
import json
from Domain.Recipe import Recipe

bp = Blueprint('testController', __name__, url_prefix='/testController')

@bp.route('/samplerecipe')
def get():
    steps = ["""Mix together 1 cup plain Greek yogurt, 1 minced garlic clove, 1 tablespoon lemon juice, and 1/4 teaspoon salt in a bowl.""",
            """Cut 2 boneless, skinless chicken breasts into bite-sized pieces and season with salt and pepper.""",
            """Serve the chicken over rice or with pita bread."""]
    sampleRecipe = Recipe("A fun Tzatziki Chicken", steps, ["chicken", "tzatziki"])
    return jsonify(sampleRecipe.__dict__)
