from django.db import db

class Product(db.Model):
    name = db.CharField(max_length=200)
    description = db.TextField()
    price = db.DecimalField(max_digits=10, decimal_places=2)
    image = db.ImageField(upload_to='products/', null=True, blank=True) # New Field

    def __str__(self):
        return self.name