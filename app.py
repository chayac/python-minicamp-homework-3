# Initialize Flask
from flask import Flask, render_template, jsonify, request
import sqlite3

# Import initdb for database helper functions
import initdb


app = Flask(__name__)


# Setup your initial route at `/` to return `'Hello World'`.
# Modify your home route (`/`) to return the html template provided below.
@app.route('/')
def index():
    return render_template('home.html')


@app.route('/enternew')
def enternew():
    return render_template('food.html')
    # return jsonify(name=['name'], calories=['calories'],
    #                cuisine=['cuisine'], is_vegetarian=['is_vegetarian'],
    #                is_gluten_free=['is_gluten_free'])


@app.route('/addfood', methods=['GET', 'POST'])
def addfood():
    result = request.form
    query = 'INSERT INTO foods VALUES (?,?,?,?,?)'
    connection = sqlite3.connect('database.db')
    cursor = connection.cursor()
    cursor.execute(query, [result['name'], result['calories'], result['cuisine'], result['is_vegetarian'], result['is_gluten_free']])
    connection.commit()
    connection.close()

    return render_template('result.html')


@app.route('/favorite', methods=['GET'])
def favorite():
    query = "SELECT name FROM foods WHERE name = 'Pizza'"
    connection = sqlite3.connect('database.db')
    cursor = connection.cursor()
    cursor.execute(query)
    results = cursor.fetchall()
    connection.close()

    return jsonify(results)


# `/search` should accept a `GET` request and then access the query parameter `name`
# and use that to perform a `SELECT` query on the database for any row that has a
# matching `name` field.  Return the results as `JSON`.
@app.route('/search', methods=['GET'])
def search():
    result = request.form
    query = "SELECT * FROM foods WHERE name = '?'"
    connection = sqlite3.connect('database.db')
    cursor = connection.cursor()
    cursor.execute(query, [result['name']])
    results = cursor.fetchall()
    connection.close()

    return jsonify(results)
