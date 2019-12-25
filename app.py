from flask import Flask, render_template, request, redirect, url_for
import os
from flask_pymongo import PyMongo
import re
from bson.objectid import ObjectId

app = Flask(__name__)
app.config["MONGO_DBNAME"] = 'DataCentricMilestone3'
app.config["MONGO_URI"] = "mongodb+srv://root:r00tUser@cluster0-jhmsx.mongodb.net/DataCentricMilestone3?retryWrites=true"

mongo = PyMongo(app)

@app.route('/')
@app.route('/get_recipes')
def get_recipes():
    #return render_template("recipes.html", 
                           #recipes=mongo.db.recipes.find())
                           
    cuisine = None
    cuisine_mapping = dict(it='Italian Cuisine', ch="Chinese Cuisine", jp="Japanese Cuisine", kr="Korean Cuisine")

    if request.args.get('cuisine'):
        cuisine = cuisine_mapping.get(request.args.get('cuisine'))

        
    if cuisine :
        recipes = mongo.db.recipes.find({ '$or': dict(cuisine=cuisine) })
         
        # Passing result of args into filters
        # And passing each matching _id into filters

        result = []
        for recipe in recipes:
            recipe_ = dict(cuisine=recipe['cuisine'], recipe=recipe['recipe'], allergens=recipe['allergens'], ingredients=recipe['ingredients'],
            methods=recipe['methods'], image=recipe.get('image'), _id=recipe['_id'])
            result.append(recipe_)
    else:
        result=mongo.db.recipes.find()
    
    
    form = FilterForm()
    if request.method == "POST":
        return redirect(url_for('get_recipes', cuisine=form.cuisine.data))
    return render_template("recipes.html", recipes=result, form=form)                           
                           
                           

                           
# "magic code" -- boilerplate
if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)