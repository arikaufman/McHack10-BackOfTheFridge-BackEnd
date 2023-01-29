import Domain.imageDetectionDomain
from flask import Blueprint

bp = Blueprint('imageGeneratorController', __name__, url_prefix='/imageGenerator')


@bp.route('/generateimage', methods=("GET", "POST"))
def generate_image():
    return generate_image()
    #get image url
   