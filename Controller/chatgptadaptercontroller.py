from flask import Blueprint, request, redirect, url_for
import os
import openai

openai.api_key = os.getenv('OPENAI_API_KEY')
bp = Blueprint('chatgptadaptercontroller', __name__, url_prefix='/chatgptadapter')

@bp.route('/generatesampleprompt', methods=("GET", "POST"))
def generate_prompt():
    prompt = request.form["ingredients"]
    response = openai.Completion.create(
            model="text-ada-001",
            prompt="Make a recipe out of " + prompt,
            temperature=0.6,
            max_tokens=300
        )
    return response.choices[0].text

@bp.route('/generateimage', methods=("GET", "POST"))
def generate_image():
    prompt = request.form["imageDescription"]
    response = openai.Image.create(
            prompt=prompt,
            n=1,
            size="512x512"
        )
    return "<img src=" + response['data'][0]['url'] + ">"