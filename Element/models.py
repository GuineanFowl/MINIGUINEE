from django.contrib.auth.models import User
from django.db import models

class Categorie(models.Model):
    nom = models.CharField(max_length=255)

    class Meta:
        ordering = ('nom',)
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.nom

class Element(models.Model):
    categorie = models.ForeignKey(Categorie, related_name='Elements', on_delete=models.CASCADE)
    nom = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    prix = models.FloatField()
    image = models.ImageField(upload_to='Images_element', blank=True, null=True)
    est_vendu = models.BooleanField(default=False)
    creer_par = models.ForeignKey(User, related_name='Elements', on_delete=models.CASCADE)
    date_creation = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nom