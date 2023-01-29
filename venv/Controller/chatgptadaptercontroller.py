from flask import Blueprint, request, redirect, url_for
import os
import openai
import cohere
from Domain.Recipe import Recipe

co = cohere.Client(api_key='AP7n0AXHe7FNQFKd12cTiN0EcozoztsdpTHMuUfh')

#from Domain.Recipe import Recipe

openai.api_key = os.getenv('OPENAI_API_KEY')
bp = Blueprint('chatgptadaptercontroller', __name__, url_prefix='/chatgptadapter')

@bp.route('/generatesampleprompt', methods=("GET", "POST"))
def generate_prompt():
    #prompt = request.form["ingredients"]
    prompt = "rice"
    #response = openai.Completion.create(
            #model="text-davinci-003",
            #prompt="Make a recipe out of " + prompt + " and give it a fun title",
           # temperature=0.6,
         #   max_tokens=300
        #)

    response = co.generate(
        model='command-xlarge-nightly',
        prompt="Make a recipe out of these ingredients:" + prompt + "with directions, ingredients listed and a fun title based on the ingredients",
        max_tokens=200,
        temperature=0.6,
        stop_sequences=["--"])

    output = "1. \"Chicken Potato Surprise\" Ingredients: 1 lb. boneless, skinless chicken breast, cut into bite-sized pieces 1/2 lb. red potatoes, diced 1/2 onion, diced 1/2 green pepper, diced 1 clove garlic, minced 1 tsp. olive oil 1/2 tsp. salt 1/4 tsp. black pepper Directions: 1. Preheat oven to 375 degrees F (190 degrees C). 2. In a large bowl, combine chicken, potatoes, onion, green pepper, garlic, olive oil, salt, and black pepper. 3. Transfer the mixture to a 9x13 inch baking dish. 4. Bake for 30-40 minutes, or until chicken is cooked through and potatoes are tender. 5. Serve with a side salad or steamed vegetables."
    #startup_idea = response.generations[0].text
    splitOutput = output.split("Ingredients:")
    title = splitOutput[0]
    doubleSplitOutput = splitOutput[1].split("Directions:")
    ingredients = doubleSplitOutput[0].split(",")
    directions = doubleSplitOutput[1]
    print("Title: "+title)
    print("Ingredients: " +ingredients[0])
    print("Directions: "+ directions)


    listOfDirections = []
    tempString = ""
    periodCounter = 0
    for i in range(len(directions)):
        print(directions[i])
        if(directions[i] == '.' and periodCounter<2):
            periodCounter = periodCounter+1
        elif(periodCounter<2 and directions[i] != '.'):
            tempString += directions[i]
        elif(periodCounter==2):
            periodCounter = 0
            listOfDirections.append(tempString)
            print(tempString)
            tempString = ""

    #final step
    listOfDirections.append(tempString)
    print(tempString)
    print("listOfDirections: ")
    print(listOfDirections)
    recipe = Recipe(title=title, ingredients=ingredients, directions=listOfDirections)
    return response.generations[0].text


@bp.route('/generateimage', methods=("GET", "POST"))
def generate_image():
    prompt = request.form["imageDescription"]
    response = openai.Image.create(
            prompt=prompt,
            n=1,
            size="512x512"
        )
    return "<img src=" + response['data'][0]['url'] + ">"