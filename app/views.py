"""
views.py,

copyright (c) 2016 by Stefan Lehmann,
licensed under the MIT license

"""
from flask import render_template, request, redirect, url_for, abort, jsonify
from app import app, db
from .forms import RecipeForm
from .models import Recipe


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

        return redirect(url_for('recipe_list'))

    return render_template('recipe/edit.html', form=form)


@app.route('/recipes/<int:recipe_id>/edit/', methods=['GET', 'POST'])
def edit_recipe(recipe_id):
    recipe = db.session.query(Recipe).get(recipe_id)
    if recipe is None:
        abort(404)
    form = RecipeForm(request.form, recipe)
    if request.method == 'POST' and form.validate():
        form.populate_obj(recipe)
        db.session.commit()
        return redirect(url_for('recipe_list'))
    return render_template('recipe/edit.html', form=form)


@app.route('/recipes/<int:recipe_id>/delete/', methods=['DELETE'])
def delete_recipe(recipe_id):
    recipe = db.session.query(Recipe).get(recipe_id)
    if recipe is None:
        resp = jsonify({'status': 'Not found'})
        resp.status = 404
        return resp
    db.session.delete(recipe)
    db.session.commit()
    return jsonify({'status': 'OK'})


@app.route('/recipes/<int:recipe_id>/')
def recipe_detail(recipe_id):
    pass


@app.route('/')
@app.route('/index')
@app.route('/recipes/')
def recipe_list():
    recipes = db.session.query(Recipe)
    return render_template('recipes.html', recipes=recipes)
