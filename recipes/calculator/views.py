from django.shortcuts import render

DATA = {
    'omlet': {
        'яйца, шт': 2,
        'молоко, л': 0.1,
        'соль, ч.л.': 0.5,
    },
    'pasta': {
        'макароны, г': 0.3,
        'сыр, г': 0.05,
    },
    'buter': {
        'хлеб, ломтик': 1,
        'колбаса, ломтик': 1,
        'сыр, ломтик': 1,
        'помидор, ломтик': 1,
    },

}


def recipes(request, recipe):
    if recipe in DATA:
        compound = DATA[recipe].copy()
        for a, b in compound.items():
            servings = int(request.GET.get('servings', 1))
            compound[a] = b * servings
    else:
        compound = {}
    context = {
        'recipe': compound
    }
    return render(request, 'calculator/index.html', context)
