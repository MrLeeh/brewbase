"""
views.py,

copyright (c) 2016 by Stefan Lehmann,
licensed under the MIT license

"""
from flask import render_template, request, redirect, url_for
from app import app, db
from .forms import RecipeForm
from .models import Recipe


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')


@app.route('/recipes')
def handle_recipes():
    pass


@app.route('/protocols')
def handle_protocols():
    pass


@app.route('/recipes/create/', methods=['GET', 'POST'])
def create_recipe():
    form = RecipeForm(request.form)
    if request.method == 'POST' and form.validate():
        recipe = Recipe()
        form.populate_obj(recipe)
        db.session.add(recipe)
        db.session.commit()

        return redirect(url_for('index'))

    return render_template('edit_recipe.html', form=form)


@app.route('/recipes/<int:recipe_id>/edit/')
def edit_recipe(recipe_id):
    pass


@app.route('/recipes/<int:recipe_id>/delete/', methods=['DELETE'])
def delete_recipe(recipe_id):
    pass


@app.route('/recipes/<int:recipe_id>/')
def recipe_detail(recipe_id):
    pass


@app.route('/recipes/')
def show_recipes():
    recipes = db.session.query(Recipe)
    return render_template('recipes.html', recipes=recipes)
