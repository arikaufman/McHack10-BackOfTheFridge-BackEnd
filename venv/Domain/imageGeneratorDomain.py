from flask import Blueprint, request, redirect, url_for
import os
import json
import requests


def generate_image(title):
    #get image url
   url = "https://serpapi.com/search.json?q=" + title + "&tbm=isch&ijn=0&api_key=6c64b8e16a13d62ed54405e008bba9876c2fdfef361b0b80c37b2e3ac5d7afc2"
   print(url)
   response = requests.get(url)
   print(response)
   result = json.loads(response.text)
   imageUrl = result['images_results'][0]["original"]

   return imageUrl