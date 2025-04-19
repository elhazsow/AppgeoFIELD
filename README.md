# APPgeoFIELD

## Description
GeoDjango Project is a web application built with Django and GeoDjango, designed to manage and visualize geographic data. It provides tools for users to efficiently handle spatial data, perform geospatial queries, and render maps.
 It aims to provide insights for farmers by offering vegetation indices such as NDVI (Normalized Difference Vegetation Index), CGI (Crop Growth Index), and NDWI (Normalized Difference Water Index).

 ![App screen shot](data/AppGeoField.PNG?raw=true)

## Installation
Follow these steps to install and set up the project locally:
Sign up for Google Earth Engine [here](https://earthengine.google.com/signup/) and [deploy app engine with Earth Engine]((https://developers.google.com/earth-engine/guides/app_engine_intro?hl=fr#deploying-app-engine-apps-with-earth-engine).

1. **Clone the repository:**
    ```bash
    git clone https://github.com/elhazsow/geodjango.git
    cd geodjango
    ```
    2. **Configure Google Earth Engine:**
        - Sign up for Google Earth Engine [here](https://earthengine.google.com/signup/).
        - Install the Earth Engine Python API:
            ```bash
            pip install earthengine-api
            ```
        - Authenticate the Earth Engine API using the provided config file:
            ```bash
            earthengine authenticate --config-file path/to/config/file
            ```       
    
  
2. **Create a virtual environment:**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install the dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4. **Set up the database:**
    ```bash
    python manage.py migrate
    ```

5. **Create a superuser:**
    ```bash
    python manage.py createsuperuser
    ```

6. **Run the development server:**
    ```bash
    python manage.py runserver
    ```

## Usage
To use the project, follow these steps:

1. Open your web browser and go to `http://127.0.0.1:8000/`.
2. Log in with the superuser credentials you created.
3. Start managing and visualizing your geographic data.
![App screen shot](data/CaptureAppGeo.PNG?raw=true)


## License
This project is licensed under the MIT License.
