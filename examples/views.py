from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def get_template(request):
    context = {
        'title': 'Заголовок из контекста',
        "my_list": [1, 2, 3, 4]
    }
    return render(request, "examples/test_template.html", context=context)