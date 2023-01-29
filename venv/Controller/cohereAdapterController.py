from flask import Blueprint, request, redirect, url_for, jsonify
import os
import cohere
from Domain.Recipe import Recipe
from Domain.imageGeneratorDomain import generate_image

co = cohere.Client(api_key='AP7n0AXHe7FNQFKd12cTiN0EcozoztsdpTHMuUfh')

#from Domain.Recipe import Recipe

bp = Blueprint('cohereAdapterController', __name__, url_prefix='/cohereAdapterController')

@bp.route('/generatesampleprompt', methods=["POST"])
def generate_prompt():
    data = request.get_json()
    #prompt = request.form["ingredients"]
    parsedString = ""
    for item in data["ingredients"]:
        parsedString += item + " "

    response = co.generate(
        model='command-xlarge-nightly',
        prompt="Make a recipe out of these ingredients: " + parsedString + "with directions, ingredients listed and a fun title based on the ingredients",
        max_tokens=200,
        temperature=0.6,
        stop_sequences=["--"])

    splitOutput = response.generations[0].text.split("Ingredients:")
    title = splitOutput[0]
    if("Directions" in response.generations[0].text):
        doubleSplitOutput = splitOutput[1].split("Directions:")
    elif("Instructions" in response.generations[0].text):
        doubleSplitOutput = splitOutput[1].split("Instructions:")
    elif ("Information" in response.generations[0].text):
        doubleSplitOutput = splitOutput[1].split("Information")
    elif ("Preparation" in response.generations[0].text):
        doubleSplitOutput = splitOutput[1].split("Preparation")
    elif ("With directions" in response.generations[0].text):
        doubleSplitOutput = splitOutput[1].split("With directions")


    ingredients = doubleSplitOutput[0].split("\n")
    directions = doubleSplitOutput[1].split("\n")
    title.replace('\r\n', '')

    for i in range(len(ingredients)):
        ingredients[i].replace('\r\n', '')
    while '' in ingredients:
        ingredients.remove('')
    while '' in directions:
        directions.remove('')


    counter = 1
    for i in range(len(directions)):
        if(str(counter) in directions[i]):
            temp = directions[i]
            directions[i] = temp[3:]
        counter= counter+1
    
    convertedTitle = ""
    if title[0] == "i":
        for i in range(0, len(title)):
            if i > 2:
                convertedTitle += title[i]


    
    recipe = Recipe(title=convertedTitle, ingredients=ingredients, directions=directions, linkUrl = generate_image(title))
    return jsonify(recipe.__dict__)
