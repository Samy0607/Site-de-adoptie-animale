from django.db import models


# Create your models here.

class Animale(models.Model):
    nume = models.CharField(max_length=60)
    varsta = models.IntegerField(null=False)
    gen = models.CharField(max_length=1, choices=[("F", "Female"), ("M", "Male")])
    specie = models.CharField(max_length=6, choices=[("caine", "Caine"), ("pisica", "Pisica"), ("iepure", "Iepure")])

    def __str__(self):
        return f"{self.nume} - {self.varsta} - {self.gen} - {self.specie}"