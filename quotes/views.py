from django.shortcuts import render

# Create your views here.
import random
from django.shortcuts import render
from .models import Quote

def quote_view(request):
    quotes = list(Quote.objects.all())
    quote = random.choice(quotes) if quotes else None
    return render(request, 'quotes/quote.html', {'quote': quote})
