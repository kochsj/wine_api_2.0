from django.db import models
from django.contrib.auth.models import User
import datetime

def year_choices(current):
    return [(year, year) for year in range(current, 1920, -1)]

class Bottle(models.Model):
    current_year = datetime.date.today().year
    YEAR_CHOICES = year_choices(current_year)
    CAB = 'Cabernet Sauvignon'
    CHA = 'Chardonnay'
    MAL = 'Malbec'
    MER = 'Merlot'
    GRI = 'Pinot Gris'
    PIN = 'Pinot Noir'
    RIE = 'Riesling'
    SAV = 'Sauvingnon Blanc'
    SHI = 'Shiraz/Syrah'
    ZIN = 'Zinfandel'
    GRAPE_CHOICES = [
        (CAB, 'Cabernet Sauvignon'),
        (CHA, 'Chardonnay'),
        (MAL, 'Malbec'),
        (MER, 'Merlot'),
        (GRI, 'Pinot Gris'),
        (PIN, 'Pinot Noir'),
        (RIE, 'Riesling'),
        (SAV, 'Sauvingnon Blanc'),
        (SHI, 'Shiraz/Syrah'),
        (ZIN, 'Zinfandel'),
    ]
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    winery = models.CharField(max_length=128)
    grape = models.CharField(choices=GRAPE_CHOICES, default=CAB, max_length=20)
    year = models.IntegerField(choices=YEAR_CHOICES, default=current_year)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.winery

        