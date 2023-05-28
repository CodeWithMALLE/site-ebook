from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.

# AbstractUser et AbstractBaseUser


class Shopper(AbstractUser):
	class Meta:
		verbose_name = "Compte Utilisateur"
		verbose_name_plural = "Les comptes d'utilisateurs"

