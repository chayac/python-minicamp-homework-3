# Initialize Flask
from flask import Flask, render_template, json, request

# Import initdb for database helper functions
import initdb


app = Flask(__name__)


# Setup your initial route at `/` to return `'Hello World'`.
# Modify your home route (`/`) to return the html template provided below.
@app.route('/')
def index():
    return render_template('home.html')


# Page with form to add new food
@app.route('/enternew')
def enternew():
    return render_template('food.html')


# Add new food to database and return success page
@app.route('/addfood', methods=['GET', 'POST'])
def addfood():
    result = request.form
    engine = initdb.initialize_database()
    initdb.insert_new_food(engine,
                           result['name'],
                           result['calories'],
                           result['cuisine'],
                           result['is_vegetarian'],
                           result['is_gluten_free'])
    message = 'New food added'
    return render_template('result.html', message=message)


@app.route('/favorite', methods=['GET'])
def favorite():
    engine = initdb.initialize_database()
    results = initdb.get_favorite_food(engine, 'pizza')
    return json.dumps([(dict(row.items())) for row in results])


# `/search` should accept a `GET` request and then access the query parameter `name`
# and use that to perform a `SELECT` query on the database for any row that has a
# matching `name` field.  Return the results as `JSON`.
@app.route('/search', methods=['GET'])
def search():
    name = request.args.get('name')
    engine = initdb.initialize_database()
    results = initdb.get_favorite_food(engine, name)
    return json.dumps([(dict(row.items())) for row in results])
