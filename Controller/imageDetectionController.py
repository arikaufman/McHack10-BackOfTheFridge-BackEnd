from flask import Blueprint, request, redirect, url_for
import os
import openai
import cohere
co = cohere.Client(api_key='AP7n0AXHe7FNQFKd12cTiN0EcozoztsdpTHMuUfh')

from Domain.Recipe import Recipe

openai.api_key = os.getenv('OPENAI_API_KEY')
bp = Blueprint('chatgptadaptercontroller', __name__, url_prefix='/chatgptadapter')

@bp.route('/generatesampleprompt', methods=("GET", "POST"))
def generate_prompt():
    prompt = request.form["ingredients"]
    response = openai.Completion.create(
            model="text-davinci-003",
            prompt="Make a recipe out of " + prompt + " and give it a fun title",
            temperature=0.6,
            max_tokens=300
        )