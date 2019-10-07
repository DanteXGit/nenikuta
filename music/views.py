from django.shortcuts import render
from .models import track
# Create your views here.
def index(request):
    data = track.objects.all()
    return render(request,"music/index.html",{"tracks":data})