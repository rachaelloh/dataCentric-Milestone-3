from flask_wtf import FlaskForm
from wtforms import validators, ValidationError
from wtforms.validators import DataRequired
from wtforms import TextField, TextAreaField, SubmitField, FileField, SelectField



class AddForm(FlaskForm):
    cuisine = SelectField("Cuisine Name",
                                    choices = [('', 'Select a Cuisine'), 
                                    ('it', 'Italian Cuisine'),
                                    ('ch', 'Chinese Cuisine'), 
                                    ('jp', 'Japanese Cuisine'), 
                                    ('kr', 'Korean Cuisine')])
    file = FileField('Add Cuisine Image')                    
    recipe = TextField("Recipe Name", validators=[DataRequired()])
    ingredients = TextAreaField("Recipe Ingredients", validators=[DataRequired()])
    methods = TextAreaField("Recipe Methods", validators=[DataRequired()])
    
    def validate_cuisine(self, cuisine):
        if cuisine.data == "":
            raise ValidationError("Kindly select a cuisine")
            
            #FILTER CUISINE
            
class FilterForm(FlaskForm):
    cuisine = SelectField("Cuisine Name",
                                    choices = [('', 'Select a Cuisine'), 
                                    ('it', 'Italian Cuisine'),
                                    ('ch', 'Chinese Cuisine'), 
                                    ('jp', 'Japanese Cuisine'), 
                                    ('kr', 'Korean Cuisine')])