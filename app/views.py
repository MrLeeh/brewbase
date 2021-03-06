"""
views.py,

copyright (c) 2016 by Stefan Lehmann,
licensed under the MIT license

"""
from flask import render_template, request, redirect, url_for, abort, jsonify
from app import app, db
from .forms import RecipeForm
from .models import Recipe, RecipeMalt, RecipeHop, RecipeMisc, RecipeMash, \
    Malt, Hop, MashTemplate


@app.route('/recipes')
def handle_recipes():
    pass


@app.route('/protocols')
def handle_protocols():
    pass


@app.route('/recipes/create/', methods=['GET', 'POST'])
def create_recipe():
    recipe = Recipe()
    form = RecipeForm(obj=recipe)
    if request.method == 'POST' and form.validate():
        form.populate_obj(recipe)
        db.session.add(recipe)
        db.session.commit()

        return redirect(url_for('recipe_list'))

    return render_template('recipe/edit.html', form=form, recipe=recipe)


@app.route('/recipes/<int:recipe_id>/edit/', methods=['GET', 'POST'])
def edit_recipe(recipe_id):
    recipe = db.session.query(Recipe).get(recipe_id)
    if recipe is None:
        abort(404)

    if len(recipe.malts) == 0:
        recipe.malts = [RecipeMalt()]

    if len(recipe.hops) == 0:
        recipe.hops = [RecipeHop()]

    if len(recipe.miscs) == 0:
        recipe.miscs = [RecipeMisc()]

    if len(recipe.mash) == 0:
        recipe.mash = [RecipeMash()]

    form = RecipeForm(obj=recipe)

    if form.validate_on_submit():
        form.populate_obj(recipe)
        db.session.commit()

        # remove loose items
        loose_items = db.session.query(RecipeMalt).filter(
            RecipeMalt.recipe_id.is_(None)).all()

        loose_items.extend(db.session.query(RecipeHop).filter(
            RecipeHop.recipe_id.is_(None)).all())

        loose_items.extend(db.session.query(RecipeMisc).filter(
            RecipeMisc.recipe_id.is_(None)).all())

        for item in loose_items:
            db.session.delete(item)
        db.session.commit()

        return redirect(url_for('recipe_list'))

    return render_template(
        'recipe/edit.html', form=form, recipe=recipe,
        maltlist=Malt.query.order_by(Malt.name).all(),
        hoplist=Hop.query.order_by(Hop.name).all(),
        mash_templates=MashTemplate.query.all()
    )


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


@app.route('/recipes/<int:recipe_id>/copy/<string:new_recipe_name>')
def copy_recipe(recipe_id, new_recipe_name):
    recipe = Recipe.query.get(recipe_id)
    new_recipe = recipe.copy()
    new_recipe.name = new_recipe_name

    # copy malts
    for malt in recipe.malts:
        new_malt = malt.copy()
        new_malt.recipe = new_recipe

    # copy hops
    for hop in recipe.hops:
        new_hop = hop.copy()
        new_hop.recipe = new_recipe

    # copy miscs
    for misc in recipe.miscs:
        new_misc = misc.copy()
        new_misc.recipe = new_recipe

    # copy mash steps
    for mash in recipe.mash:
        new_mash = mash.copy()
        new_mash.recipe = new_recipe

    db.session.add(new_recipe)
    db.session.commit()
    return redirect(url_for('recipe_list'))


@app.route('/recipes/<int:recipe_id>/')
def recipe_detail(recipe_id):
    pass


@app.route('/')
@app.route('/index')
@app.route('/recipes/')
def recipe_list():
    recipes = db.session.query(Recipe)
    return render_template('recipes.html', recipes=recipes)
