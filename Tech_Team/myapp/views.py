from django.shortcuts import render, render_to_response, get_object_or_404
from .models import Product

def main_page(request):
	context = {
		'product': Product.objects.all()
	}
	return render(request, 'main_page.html', context)

# Create your views here.
