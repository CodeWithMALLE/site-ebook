
from django.contrib import admin
from django.urls import path
from books.views import index, detail_produit, add_to_cart, panier, delete_panier
from accounts.views import signup, logout_user, login_user
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("", index, name='index'),
    path('admin/', admin.site.urls),
    path('signup/', signup, name='signup'),
    path("logout/", logout_user, name="logout"),
    path("login/", login_user, name="login"),
    path("panier/", panier, name="panier"),
    path("panier/delete/", delete_panier, name="delete-panier"),
    path("produit/<str:slug>/", detail_produit, name="detail-produit"),
    path("produit/<str:slug>/add-to-cart/", add_to_cart, name="add-to-cart")
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

