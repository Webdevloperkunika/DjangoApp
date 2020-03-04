from django.shortcuts import render
#from .models import Themes

# Create your views here.
def theme_view(request):
    return render(request, 'Themes/theme_view.html')