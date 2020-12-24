"""
Arrange the ingredients alphabetically by their allergen
and separate them by commas to produce your canonical dangerous ingredient list.
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
    print('ingredient_counts', ingredient_counts)
    print('allergens', allergens)
    sum(i for i in ingredient_counts.values() if i > 1)

    nonallergens = set(ingredient_counts.keys())
    all_ingredients = set(ingredient_counts.keys())
    allergen_lookup = {}
    for ingredients in allergens.values():
        nonallergens.difference_update(set.intersection(*ingredients))
    print('nonallergens', nonallergens)
    dangerous_ingredients = all_ingredients - nonallergens
    print('dangerous_ingredients', dangerous_ingredients)
    for allergen, ingredients in allergens.items():
        allergen_lookup[allergen] = list(set.intersection(*ingredients))

    canonical_dangerous_ingredient = set()
    while any(len(a) > 1 for a in allergen_lookup.values()):
        for allergen, ingredient in allergen_lookup.items():
            if len(ingredient) == 1 and ingredient[0] not in canonical_dangerous_ingredient:
                canonical_dangerous_ingredient.add(ingredient[0])
            elif len(ingredient) > 1:
                for i in canonical_dangerous_ingredient:
                    if i in ingredient:
                        allergen_lookup[allergen].remove(i)

    print(allergen_lookup)
    # Sort allergens alphabetically
    ingredients = ','.join(v[0] for k, v in sorted(allergen_lookup.items(), key= lambda k:k[0] ) )
    return ingredients


TEST_INPUT = [(
    """\
mxmxvkd kfcds sqjhc nhms (contains dairy, fish)
trh fvjkl sbzzf mxmxvkd (contains dairy)
sqjhc fvjkl (contains soy)
sqjhc mxmxvkd sbzzf (contains fish)""", "mxmxvkd,sqjhc,fvjkl")]


def test(test_input):
    test_results = []
    for (puzzle_input, expected) in test_input:
        solution = main(puzzle_input.splitlines())
        test_results.append((puzzle_input, solution, expected))
    for puzzle_input, solution, expected in test_results:

        print(puzzle_input,
              'solution:', solution,
              'expected:', expected,
              )


test(TEST_INPUT)


ingredients = main(parse_file("21-01-input.txt"))
print("solution:", ingredients)
