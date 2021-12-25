from django.shortcuts import render

DATA = {
    'omlet': {
        'яйца, шт': 2,
        'молоко, л': 0.1,
        'соль, ч.л.': 0.5
    },
    'pasta': {
        'макароны, кг': 0.3,
        'сыр, кг': 0.05
    },
    'buter': {
        'хлеб, ломтик': 1,
        'колбаса, ломтик': 1,
        'сыр, ломтик': 1,
        'помидор, ломтик': 1
    },
    'charlotte': {
        'яйца, шт': 4,
        'мука, кг': 0.2,
        'сахар, кг': 0.2,
        'яблоки, кг': 0.5
    }
}


def recipes(request, recipe):
    if recipe in DATA:
        compound = DATA[recipe].copy()
        for ingredient, amount in compound.items():
            servings = int(request.GET.get('servings', 1))
            compound[ingredient] = amount * servings
    else:
        compound = {}
    context = {
        'recipe': compound
    }
    return render(request, 'calculator/index.html', context)
