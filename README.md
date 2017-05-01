# Getting Started

git clone https://github.com/kedmenec/commerce_api.git
cd commerce_api

# Create and activate virtualenv/condaenv
conda create --name commerce_api python=3.5
pip install -r requirements

# Run some tests
python manage.py test

# Edit DB Connections details in commerce_api/settings.py to use the database server you wish to.  Tested with postgres 9.6.

# initialise the db
python manage.py migrate

# Create the super user
python manage.py createsuperuser

# Load the test product data
python manage.py load_products

# Start the dev server
python manage.py runserver


