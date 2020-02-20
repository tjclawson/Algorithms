#!/usr/bin/python

import math


def recipe_batches(recipe, ingredients):
    max_batches = float('inf')
    for ing in recipe:
        if ing not in ingredients.keys() or ingredients.get(ing) < recipe.get(ing):
            return 0
        batch_amount = ingredients.get(ing) // recipe.get(ing)
        if batch_amount < max_batches:
            max_batches = batch_amount

    return max_batches


if __name__ == '__main__':
    # Change the entries of these dictionaries to test
    # your implementation with different inputs
    recipe = {'milk': 100, 'butter': 50, 'flour': 5}
    ingredients = {'milk': 132, 'butter': 48, 'flour': 51}
    print("{batches} batches can be made from the available ingredients: {ingredients}.".format(
        batches=recipe_batches(recipe, ingredients), ingredients=ingredients))
