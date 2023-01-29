from flask import Blueprint, request, redirect, url_for
import os
import openai
import cohere
co = cohere.Client(api_key='AP7n0AXHe7FNQFKd12cTiN0EcozoztsdpTHMuUfh')

from Domain.Recipe import Recipe

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

    response = co.generate(
        model='command-xlarge-nightly',
        prompt="Make a recipe out of these ingredients:" + prompt + "with directions and a recipe title",
        max_tokens=200,
        temperature=0.6,
        stop_sequences=["--"])
    #startup_idea = response.generations[0].text
    #title =
    #recipe = Recipe()
    return response.generations[0].text
        #response.choices[0].text
