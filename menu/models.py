from django.db import models

# Create your models here.
class Страва(models.Model):
    назва = models.CharField(max_length=200)
    опис = models.TextField()
    ціна = models.DecimalField(max_digits=5, decimal_places=2)
    дата_додавання = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.назва