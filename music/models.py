from django.db import models

# Create your models here.
class track(models.Model):
    track_name = models.CharField(max_length = 60)
    track_deck = models.TextField()
    track_date = models.DateField()
    track_url = models.TextField()
    short_url = models.CharField(max_length = 50,default='Short url')
    buy_url = models.TextField(default = "Buy Url")
    def __str__(self):
        return "Трек"
    class Meta:
        ordering = ('-track_date',)
