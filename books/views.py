from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse

from .models import Product, Panier, Article


# Create your views here.


def index(request):
	produits = Product.objects.all()
	context = {
		'produits': produits,
	}
	return render(request, "books/index.html", context)


def detail_produit(request, slug: str):
	produit = get_object_or_404(Product, slug=slug)
	return render(request, "books/detail.html", {"produit": produit})


def add_to_cart(request, slug):
	user = request.user
	produit = get_object_or_404(Product, slug=slug)
	panier, _ = Panier.objects.get_or_create(user=user)
	article, created = Article.objects.get_or_create(user=user, commandee=False, produit=produit)

	if created:
		panier.articles.add(article)
		panier.save()
	else:
		article.quantity += 1
		article.save()

	return redirect(reverse('detail-produit', kwargs={"slug": slug}))


def panier(request):
	paniers = get_object_or_404(Panier, user=request.user)
	return render(request, "books/panier.html", context={"paniers": paniers.articles.all()})


def delete_panier(request):
	if paniers := request.user.panier:
		paniers.articles.all().delete()
		paniers.delete()

	return redirect("index")

