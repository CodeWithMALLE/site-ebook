from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.utils.text import slugify

from store.settings import AUTH_USER_MODEL


# Create your models here.


class Product(models.Model):
	name = models.CharField(max_length=50, verbose_name="Nom du livre")
	price = models.FloatField(default=0.0)
	slug = models.SlugField(blank=True)
	stock = models.IntegerField(default=0)
	description = models.TextField(blank=True)
	img = models.ImageField(upload_to="products", blank=True, null=True)

	def __str__(self):
		return f"{self.name} {self.stock}"

	def save(self, *args, **kwargs):
		self.slug = slugify(self.name)
		super().save(*args, **kwargs)

	def get_absolute_url(self):
		return reverse("detail-produit", kwargs={"slug": self.slug})


class Article(models.Model):
	user = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.CASCADE)
	produit = models.ForeignKey(Product, on_delete=models.CASCADE)
	quantity = models.IntegerField(default=1)
	commandee = models.BooleanField(default=False)
	date_commande = models.DateTimeField(blank=True, null=True)

	def __str__(self):
		return f"{self.produit.name} ({self.quantity})"


class Panier(models.Model):
	user = models.OneToOneField(AUTH_USER_MODEL, on_delete=models.CASCADE)
	articles = models.ManyToManyField(Article)

	def __str__(self):
		return self.user.username

	def delete(self, *args, **kwargs):

		for article in self.articles.all():
			article.commandee = True
			article.date_commande = timezone.now()
			article.save()

		self.articles.clear()

		super().delete(*args, **kwargs)


