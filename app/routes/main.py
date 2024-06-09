from ..app import app, ALLOWED_EXTENSIONS
import os
import io
import open3d as o3d
import numpy as np
import tempfile

from flask import render_template, redirect, request, url_for, send_file
from werkzeug.utils import secure_filename

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def simplify_image(filename):
    
    # suffix = allowed_file(filename)
    # print(type(suffix))
    # Create temporary file
    with tempfile.NamedTemporaryFile(delete=False, suffix='.obj') as temp_file:
        temp_file.write(filename.getbuffer())
        temp_filename = temp_file.name

    # Read the mesh
    mesh = o3d.io.read_triangle_mesh(temp_filename)

    # Compute the axis-aligned bounding box
    bbox = mesh.get_axis_aligned_bounding_box()

    # Get the minimum and maximum coordinates of the bounding box
    min_bound = bbox.get_min_bound()
    max_bound = bbox.get_max_bound()

    # Calculate the center of the bounding box
    center = (np.array(min_bound) + np.array(max_bound)) / 2.0
    
    # Calculate the translation vector to move the geometry to the center of the bounding box
    translation = np.array(center) - np.array(mesh.get_center())
      
    # Translate the geometry
    mesh.translate(translation)
   
    # Simplify mesh
    mesh_simplified = mesh.simplify_quadric_decimation(65000)
    
    # Computing normal and rendering it
    mesh_simplified.compute_vertex_normals()
    mesh_simplified.compute_triangle_normals()
    
    # Color mesh
    # mesh_simplified.paint_uniform_color([1, 0.706, 0])

    # Save the simplified mesh to a temporary file
    with tempfile.NamedTemporaryFile(delete=False, suffix='.obj') as output_file:
        o3d.io.write_triangle_mesh(output_file.name, mesh_simplified)
        output_filename = output_file.name

    return output_filename

@app.route("/")
def home():
    return render_template("pages/main.html")

@app.route("/meshed_file", methods=['POST'])
def upload_image():
    if request.method == 'POST':
        if 'file' not in request.files:
            return redirect(request.url)
        
        file = request.files['file']
        if file.filename == '':
            return redirect(request.url) 

        if file and allowed_file(file.filename):
            file_data = io.BytesIO(file.read())
            meshed_image = simplify_image(file_data)

            output_filename = 'remeshed_' + file.filename

            return send_file(meshed_image, mimetype='application/octet-stream', as_attachment=True, download_name=output_filename)
    
    return redirect(url_for(home))

@app.route("/error")
def error_404():
    return render_template("errors/404.html")

@app.route("/error_500")
def error_500():
    return render_template("errors/500.html")

# TEST CASES
@app.route("/load")
def load():
    return render_template("pages_test/load.html")

@app.route("/load_new")
def load4():
    return render_template("pages_test/hover.html")