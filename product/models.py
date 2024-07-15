from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=30)
    price = models.FloatField()

    def __str__(self) -> str:
        return self.name
    
    # para mostrar o preço formatado com duas casas decimais
    def exibe_price(self):
        return "{:.2f}".format(self.price)

