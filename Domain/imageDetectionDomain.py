# from imageai.Detection import ObjectDetection
# import os
# import torch


# def recognize_food():
#     execution_path = os.getcwd()

#     detector = ObjectDetection()
#     detector.setModelTypeAsRetinaNet()
#     detector.setModelPath( os.path.join(execution_path , "resnet50_coco_best_v2.1.0.h5"))
#     detector.loadModel()
#     detections = detector.detectObjectsFromImage(input_image=os.path.join(execution_path , "applebanana.jpg"), output_image_path=os.path.join(execution_path , "imagenew.jpg"))

#     for eachObject in detections:
#         print(eachObject["name"] , " : " , eachObject["percentage_probability"] )

# def load_food_name(food_type):
#     names = [line.rstrip('\n').lower() for line in open('common/' + food_type + '.dict')]
#     return names