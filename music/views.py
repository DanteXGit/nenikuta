from django.shortcuts import render
from .models import track
from .forms import Buy
import requests
# Create your views here.
def index(request):
    key = "48e7qUxn9T7RyYE1MVZswX1FRSbE6iyCj2gCRwwF3Dnh5XrasNTx3BGPiMsyXQFNKQhvukniQG8RTVhYm3iPq18AaSqHW8Xm6Y4H1Z2gUHthx5B6vN8o4qqVkk118k9tbZeN8pF79cdd4uRyQyRa45SxiN4tkKBNq1NuYaVSGapNcek9QBne8DaPhtUnk"
    data = track.objects.all()
    return render(request,"music/index.html",{"tracks":data,"key":key})

    