<<<<<<< HEAD
import json
import requests
import base64

def detectGroceries():
   groceries = ["apples", "bananas", "oranges", "bread", 
   "milk", "eggs", "cereal", "chicken", "beef", "pork", "fish", "potatoes", 
   "onions", "carrots", "lettuce", "spinach", "tomatoes", "bell peppers", "avocados", "mangoes", 
   "grapes", "strawberries", "blueberries", "blackberries", "raspberries", "cantaloupe", "honeydew", 
   "watermelon", "pineapple", "peaches", "plums", "applesauce", "orange juice", "apple juice", "tomato sauce", 
   "spaghetti sauce", "olive oil", "vegetable oil", "butter", "margarine", "mayonnaise", "mustard", "ketchup", 
   "relish", "barbecue sauce", "soy sauce", "teriyaki sauce", "hot sauce", "vinegar", "balsamic vinegar", "red wine vinegar", 
   "white wine vinegar", "sugar", "brown sugar", "powdered sugar", "honey", "maple syrup", "corn syrup", "vanilla extract",
    "almond extract", "peanut butter", "jelly", "jam", "marmalade", "parmesan cheese", "cheddar cheese", "mozzarella cheese", 
    "cream cheese", "sour cream", "yogurt", "milk", "buttermilk", "half-and-half", "whipping cream", "chocolate chips", 
    "cocoa powder", "baking powder", "baking soda", "yeast", "flour", "cornmeal", "bread crumbs", "oatmeal", "grits", 
    "rice", "pasta", "noodles", "macaroni", "spaghetti", "lasagna noodles", "couscous", "quinoa", "bulgur", "tortillas", 
    "wraps", "pita bread", "bagels", "english muffins", "bread rolls", "hamburger buns", "hot dog buns", "coffee", "tea"]

   headers = {"Authorization" : "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjoiNjk1Y2VkYTAtMjMyYi00ZTc3LTliYjEtMGIwYWYzYzk4YjZjIiwidHlwZSI6ImFwaV90b2tlbiJ9.w5d9EP--Rk_7q3rVDZtAVEQf5XAaTQzXz2ICN9aS698"}
   url = "https://api.edenai.run/v2/image/object_detection"
   data={"providers": "google"}

   #image processing
   # the encoded image as a string
   with open("C:/Development/McHack10-BackOfTheFridge-BackEnd/venv/static/tomatoes.jpg", "rb") as img_file:
     encoded_image = base64.b64encode(img_file.read())


   # decode the image
   decoded_image = base64.b64decode(encoded_image)

   # save the image to a file
   with open("image.jpg", "wb") as f:
      f.write(decoded_image)

   files = {'file': open("image.jpg",'rb')}

   response = requests.post(url, data=data, files=files, headers=headers)
   result = json.loads(response.text)
   items = result['google']['items']
   print(items)

   ingredientsList = set()
   for item in items:
      if item['label'] not in ingredientsList:
         for grocery in groceries:
            if item['label'].lower() in grocery:
               ingredientsList.add(item['label'])

   return list(ingredientsList)
=======
#from imageai.Classification import ImageClassification
import os

execution_path = os.getcwd()
ingredients = {ingredient.lower() for ingredient in {'Coarse salt', 'Red chili flakes', 'Black peppercorns', 'Coriander', 
'Fennel seeds', 'Paprika', 'Oregano', 'Turmeric', 'Whole nutmeg', 'Bay leaves', 'Cayenne pepper', 'Thyme', 'Cinnamon', 
'Milk', 'Butter', 'Heavy cream', 'Eggs', 'Parmesan', 'Bacon', 'Parsley', 'Celery', 'Carrots', 'Lemons', 'Limes', 'Orange juice',
 'Garlic', 'Shallots', 'Potatoe', 'Onion', 'Tomato', 'Bean', 'Banana', 'Apple'}}

def detectGroceries():
    list_foods = [line.rstrip('\n').lower() for line in open('Common/FridgeItems.dict')]
    #prediction = ImageClassification()
    #prediction.setModelTypeAsResNet50()
    #prediction.setModelPath(os.path.join(execution_path, "Domain", "resnet50-19c8e357.pth"))
    #prediction.loadModel()

    #predictions, probabilities = prediction.classifyImage(os.path.join(execution_path, "static" , "applebanana.jpg"), result_count=5)
    #for eachPrediction, eachProbability in zip(predictions, probabilities):
    #    for ingredient in ingredients:
    #        if eachPrediction in ingredient or ingredient in eachPrediction:
    #            print(ingredient)
>>>>>>> b8cd8627608ae4ff90484d04210cddf6b122a23f
