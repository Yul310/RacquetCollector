from django.db import models
from django.urls import reverse
from datetime import date

STRINGS = (
    ('C', 'Confidential'),
    ('L', 'Luxilon Alu Power'),
    ('G', 'Grapple Snake')
)

class User(models.Model):
    name = models.CharField(max_length=20)
    description = models.TextField(max_length=50)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('users_detail', kwargs={'racquet_id': self.id})





# Create your models here.
class Racquet(models.Model):
    name = models.CharField(max_length=100)
    brand = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    users = models.ManyToManyField(User)


    def __str__(self):
        return self.name
    
     # Add this method
    def get_absolute_url(self):
        return reverse('detail', kwargs={'racquet_id': self.id})

    


class Restring(models.Model):
    date = models.DateField('Restring Date')
    string = models.CharField(
        max_length=20,
        choices=STRINGS,
        default=STRINGS[0][0]
    )
    racquet = models.ForeignKey(Racquet, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.get_string_display()} on {self.date}"

    class Meta:
        ordering = ['-date']