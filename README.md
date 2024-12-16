# DaSCH Mesh

DaSCH Mesh is a Python application designed to efficiently convert 3D images stored in the OBJ format (.obj) into optimized and lightweight versions. Using a method similar to quadratic edge collapse decimation simplification (common in desktop software like MeshLab), it reduces the number of polygons in the mesh while preserving its overall shape, resulting in a smaller file size with minimal visual degradation.

## Features

- Convert 3D objects from OBJ format into optimized and lightweight versions.
- User-friendly interface with a focus on simplicity and ease of use.
- Modular code structure for better maintainability and future expansion.

## Folder Structure

The application is organized as follows:

```
dasch_converter/
|
├── app/            # Main application folder
│   ├── __pycache__/ # Compiled Python files
│   ├── routes/      # Contains Flask route definitions
│   ├── statics/     # Static files such as CSS, JavaScript, and images
│   ├── templates/   # HTML templates for the web interface
│   ├── tests/       # Unit tests for the application
│   ├── __init__.py  # Initializes the Flask application
│   ├── app.py       # Main application logic
│   └── config.py    # Configuration settings for the application
├── LICENSE.md       # MIT License file
├── README.md        # Project documentation
├── requirements.txt # Lists required libraries and dependencies
└── run.py           # Script to start the Flask server
```

## Requirements

To run DaSCH Mesh, you need the following Python libraries:

```txt
addict==2.4.0
attrs==23.2.0
blinker==1.7.0
certifi==2024.2.2
charset-normalizer==3.3.2
click==8.1.7
ConfigArgParse==1.7
contourpy==1.2.1
cycler==0.12.1
dash==2.16.1
dash-core-components==2.0.0
dash-html-components==2.0.0
dash-table==5.0.0
dominate==2.9.1
fastjsonschema==2.19.1
Flask==3.0.3
Flask-Bootstrap==3.3.7.1
fonttools==4.51.0
idna==3.7
importlib_metadata==7.1.0
itsdangerous==2.1.2
Jinja2==3.1.3
joblib==1.4.0
jsonschema==4.21.1
jsonschema-specifications==2023.12.1
jupyter_core==5.7.2
kiwisolver==1.4.5
MarkupSafe==2.1.5
matplotlib==3.8.4
nbformat==5.10.4
nest-asyncio==1.6.0
numpy==1.26.4
open3d==0.18.0
packaging==24.0
pandas==2.2.2
pillow==10.3.0
platformdirs==4.2.0
plotly==5.20.0
pyparsing==3.1.2
pyquaternion==0.9.9
python-dateutil==2.9.0.post0
python-dotenv==1.0.1
pytz==2024.1
PyYAML==6.0.1
referencing==0.34.0
requests==2.31.0
retrying==1.3.4
rpds-py==0.18.0
scikit-learn==1.4.2
scipy==1.13.0
six==1.16.0
tenacity==8.2.3
threadpoolctl==3.4.0
tqdm==4.66.2
traitlets==5.14.2
typing_extensions==4.11.0
tzdata==2024.1
urllib3==2.2.1
visitor==0.1.3
Werkzeug==3.0.2
```

## Installation and Setup

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/ballestrimg/dasch_mesh.git
   cd dasch_mesh
   ```

2. **Create a Virtual Environment:**
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install the Dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the Application:**
   ```bash
   python app.py
   ```

5. **Access the App:**
   Open your browser and go to `http://127.0.0.1:5000`.

## Usage

1. Upload an image in `.jpg`, `.jpeg`, or `.png` format via the web interface.
2. The app will process the image and provide a lightweight version for download.

## Running Tests

To ensure the application is functioning correctly, you can run the tests provided in the `tests/` folder:

```bash
pytest tests/
```

## Contribution

Contributions are welcome! Feel free to fork the repository, make changes, and submit a pull request. Ensure your changes pass all tests before submitting.

## License

This project is licensed under the MIT License. See the [LICENSE](https://github.com/ballestrimg/dasch_mesh/blob/main/LICENCE.md) file for more details.
