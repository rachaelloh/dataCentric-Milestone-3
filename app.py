from flask import Flask, render_template, request, redirect, url_for
import os
from flask_pymongo import PyMongo
import re
from bson.objectid import ObjectId


app = Flask(__name__)
app.config["MONGO_DBNAME"] = 'DataCentricMilestone3'
app.config["MONGO_URI"] = "mongodb+srv://root:r00tUser@cluster0-jhmsx.mongodb.net/DataCentricMilestone3?retryWrites=true&w=majority"

mongo = PyMongo(app)

@app.route('/')
@app.route('/get_recipes')
def get_recipes():
    return render_template("recipes.html", recipe = mongo.db.recipe.find())


@app.route('/add_recipes', methods=['GET', 'POST'])
def add_recipes():
    return render_template('add.html', categories = mongo.db.categories.find())
                           
@app.route('/insert_recipe', methods=['POST'])
def insert_recipe():
    recipe =  mongo.db.recipe
    recipe.insert_one(request.form.to_dict())
    return redirect(url_for('get_recipes'))
    
@app.route('/edit_recipe/<recipe_id>')
def edit_recipe(recipe_id):
    the_recipe =  mongo.db.recipe.find_one({"_id": ObjectId(recipe_id)})
    all_categories =  mongo.db.categories.find()
    return render_template('edit.html', recipe=the_recipe, categories=all_categories)

@app.route('/view_recipe/<recipe_id>', methods=["GET", "POST"])
def view_recipe(recipe_id):
    the_recipe = mongo.db.recipe.find({"_id": ObjectId(recipe_id)})
    ingredients = mongo.db.recipe.find({"_id": ObjectId(recipe_id)})
    cooking_steps = mongo.db.recipe.find({"_id": ObjectId(recipe_id)})
    return render_template("view.html", recipe=the_recipe, ingredients=ingredients, cooking_steps=cooking_steps)

@app.route('/update_recipe/<recipe_id>', methods=["POST"])
def update_recipe(recipe_id):
    recipe = mongo.db.recipe
    recipe.update( {'_id': ObjectId(recipe_id)},
    {
        'recipe_name':request.form.get('recipe_name'),
        'category_name':request.form.get('category_name'),
        'ingredients': request.form.get('ingredients'),
        'cooking_steps':request.form.get('cooking_steps')
    })
    return redirect(url_for('get_recipes'))

@app.route('/delete_recipe/<recipe_id>')
def delete_recipe(recipe_id):
    mongo.db.recipe.remove({'_id': ObjectId(recipe_id)})
    return redirect(url_for('get_recipes'))
    
@app.route('/category_search', methods=['GET', 'POST'])
def category_search():
    search_term = []
    if request.method == 'POST':
        search_term = request.form['category_name']
    return render_template('catSearch.html', the_recipe=mongo.db.recipe.find_one({"category_name": search_term}))


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)
