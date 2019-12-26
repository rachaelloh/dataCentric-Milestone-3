from flask import Flask, render_template, request, redirect, url_for
import os
from flask_pymongo import PyMongo
import re
from bson.objectid import ObjectId
from selectCuisine import AddForm, FilterForm


app = Flask(__name__)
app.config['SECRET_KEY'] = 'the random string'
app.config['IMAGES_FOLDER'] = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'static/images/') #to store images
app.config["MONGO_DBNAME"] = 'DataCentricMilestone3'
app.config["MONGO_URI"] = "mongodb+srv://root:r00tUser@cluster0-jhmsx.mongodb.net/DataCentricMilestone3?retryWrites=true"

mongo = PyMongo(app)

@app.route('/')
@app.route('/get_recipes')
def get_recipes():
    return render_template("recipes.html", 
                           recipes=mongo.db.recipes.find())


@app.route('/add_recipes')
def add_recipes():
    return render_template('add.html',
                           categories=mongo.db.categories.find())


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)
