from imageai.Classification import ImageClassification
import os

execution_path = os.getcwd()
ingredients = {ingredient.lower() for ingredient in {'Coarse salt', 'Red chili flakes', 'Black peppercorns', 'Coriander', 
'Fennel seeds', 'Paprika', 'Oregano', 'Turmeric', 'Whole nutmeg', 'Bay leaves', 'Cayenne pepper', 'Thyme', 'Cinnamon', 
'Milk', 'Butter', 'Heavy cream', 'Eggs', 'Parmesan', 'Bacon', 'Parsley', 'Celery', 'Carrots', 'Lemons', 'Limes', 'Orange juice',
 'Garlic', 'Shallots', 'Potatoe', 'Onion', 'Tomato', 'Bean', 'Banana', 'Apple'}}

def detectGroceries():
    list_foods = [line.rstrip('\n').lower() for line in open('Common/FridgeItems.dict')]
    prediction = ImageClassification()
    prediction.setModelTypeAsResNet50()
    prediction.setModelPath(os.path.join(execution_path, "Domain", "resnet50-19c8e357.pth"))
    prediction.loadModel()

    predictions, probabilities = prediction.classifyImage(os.path.join(execution_path, "static" , "applebanana.jpg"), result_count=5)
    for eachPrediction, eachProbability in zip(predictions, probabilities):
        for ingredient in ingredients:
            if eachPrediction in ingredient or ingredient in eachPrediction:
                print(ingredient)