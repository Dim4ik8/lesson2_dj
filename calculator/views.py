from django.shortcuts import render, reverse
from django.http import HttpResponse

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

template_name = 'calculator/index.html'


def home_view(request):
    return HttpResponse('Меню готовых блюд')


#
def omlet(request):
    num = request.GET.get("persons", 1)

    context = {
        'recipe':
            {
                'яйца, шт': 2 * int(num),
                'молоко, л': 0.1 * int(num),
                'соль, ч.л.': 0.5 * int(num),

            }
    }

    return render(request, template_name, context)


def pasta(request):
    num = request.GET.get("persons", 1)

    context = {
        'recipe':
            {
                'макароны, г': 0.3 * int(num),
                'сыр, г': 0.05 * int(num),

            }
    }

    return render(request, template_name, context)


def buter(request):
    num = request.GET.get("persons", 1)

    context = {
        'recipe':
            {
                'хлеб, ломтик': 1 * int(num),
                'колбаса, ломтик': 1 * int(num),
                'сыр, ломтик': 1 * int(num),
                'помидор, ломтик': 1 * int(num),

            }
    }

    return render(request, template_name, context)
