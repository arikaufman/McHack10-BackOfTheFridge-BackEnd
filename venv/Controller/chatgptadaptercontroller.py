from flask import Blueprint, request, redirect, url_for, jsonify
import os
import openai
import cohere
from Domain.Recipe import Recipe

co = cohere.Client(api_key='AP7n0AXHe7FNQFKd12cTiN0EcozoztsdpTHMuUfh')

#from Domain.Recipe import Recipe

bp = Blueprint('chatgptadaptercontroller', __name__, url_prefix='/chatgptadapter')

@bp.route('/generatesampleprompt', methods=("GET", "POST"))
def generate_prompt():
    #prompt = request.form["ingredients"]
    prompt = "tomato chicken pepper peas"
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
    print(response.generations[0].text)

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
    print("Title: "+title)
    while '' in ingredients:
        ingredients.remove('')
    print("Ingredients: ")
    print(ingredients)
    while '' in directions:
        directions.remove('')
    print("Directions: ")


    counter = 1
    for i in range(len(directions)):
        if(str(counter) in directions[i]):
            temp = directions[i]
            directions[i] = temp[3:]
        counter= counter+1
    print(directions)


    #listOfDirections = []
    #tempString = ""
    #periodCounter = 0
    #for i in range(len(directions)):
    #    if(directions[i] == '.' and periodCounter<2):
    #        periodCounter = periodCounter+1
    #    elif(periodCounter<2 and directions[i] != '.'):
    #        tempString += directions[i]
     #   elif(periodCounter==2):
     #       periodCounter = 0
     #       listOfDirections.append(tempString)
     #       tempString = ""

    #final step
    #listOfDirections.append(tempString)

    #for i in range(len(listOfDirections)):
    #    listOfDirections[i].replace('\r\n', '')

    #print(tempString)
    #print("listOfDirections: ")
    #print(listOfDirections)
    recipe = Recipe(title=title, ingredients=ingredients, directions=directions)
    #return response.generations[0].text
    return jsonify(recipe.__dict__)

