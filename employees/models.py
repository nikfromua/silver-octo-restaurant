from django.db import models

class Employee(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    # Тут можна додати інші поля, якщо потрібно

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
