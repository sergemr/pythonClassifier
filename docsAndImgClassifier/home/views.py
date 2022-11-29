from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.edit import CreateView
from django.views.generic.list import ListView
# Create your views here.


# def say_hello(request):
#    return render(request, 'playground/hello.html', {'name': 'Django'})
class home(ListView):
    template_name = "welcome.html"
    context_object_name = 'latest_question_list'

    def queryset(self):
        """Return the last five published questions."""
        return [1, 2, 3]
