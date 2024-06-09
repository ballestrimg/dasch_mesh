from flask import Flask
from .config import Config
import os
from flask_bootstrap import Bootstrap

app = Flask(
    __name__,
    static_folder = 'statics',
    template_folder='templates'
)
app.config.from_object(Config)
app.config['UPLOAD_FOLDER'] = os.path.join('statics', 'upload')
app.config['ALLOWED_EXTENSIONS'] = {
    'glb', 'gltf', 'jpg', 'mtl', 'obj', 'ply', 'png', 'stl', 'tiff'}

ALLOWED_EXTENSIONS = app.config['ALLOWED_EXTENSIONS']

Bootstrap(app)

from .routes import main