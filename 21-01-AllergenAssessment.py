"""
Each allergen is found in exactly one ingredient.
Each ingredient contains zero or one allergen.
Allergens aren't always marked.
"""

from collections import defaultdict


def parse_file(input):
    with open(input) as file:
        for line in file:
            yield line[:-1]


def parse_recipe(recipe):
    ingredients, allergens = recipe[:-1].split(' (contains ')
    ingredients = [i for i in ingredients.split()]
    allergens = [a for a in allergens.split(', ')]
    return (ingredients, allergens)


def main(puzzle_input):
    recipes = [parse_recipe(recipe) for recipe in puzzle_input]
    """
    [(['mxmxvkd', 'kfcds', 'sqjhc', 'nhms'], ['dairy', 'fish']),
    (['trh', 'fvjkl', 'sbzzf', 'mxmxvkd'], ['dairy']),
    (['sqjhc', 'fvjkl'], ['soy']),
    (['sqjhc', 'mxmxvkd', 'sbzzf'], ['fish'])]
    """
    allergens = defaultdict(list)
    ingredient_counts = defaultdict(int)
    for ingredients, contains in recipes:
        for allergen in contains:
            allergens[allergen].append(set(ingredients))
        for i in ingredients:
            ingredient_counts[i] += 1

    nonallergens = set(ingredient_counts.keys())
    for ingredients in allergens.values():
        nonallergens.difference_update(set.intersection(*ingredients))

    return sum(ingredient_counts[i] for i in nonallergens)


TEST_INPUT = [(
    """\
mxmxvkd kfcds sqjhc nhms (contains dairy, fish)
trh fvjkl sbzzf mxmxvkd (contains dairy)
sqjhc fvjkl (contains soy)
sqjhc mxmxvkd sbzzf (contains fish)""", 5)]


def test(test_input):
    test_results = []
    for (puzzle_input, expected) in test_input:
        solution = main(puzzle_input.splitlines())
        test_results.append((puzzle_input, solution, expected))
    for puzzle_input, solution, expected in test_results:

        print(puzzle_input,
              'solution:', solution,
              'expected:', expected,
              ('failed', expected - solution) if solution != expected else '')


test(TEST_INPUT)


ingredients = main(parse_file("21-01-input.txt"))
print("solution:", ingredients)
