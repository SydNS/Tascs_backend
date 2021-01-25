from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

from django.utils import timezone

# Models
class Tasks(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=400)
    created_at = models.DateTimeField(default=timezone.now)
    created_by = models.CharField(max_length=50, blank=True, null=True)
    priority = models.IntegerField(validators=[MinValueValidator(1),
                                               MaxValueValidator(5)])

class TascsUAccount(models.Model):
    name = models.CharField(max_length=20, unique=True)
    lastname = models.CharField(max_length=20, unique=True)
    Uemail = models.EmailField(max_length=30, unique=True)
    password = models.CharField(max_length=20)
    residence = models.CharField(max_length=30)
    country_of_origin = models.CharField(max_length=30)
    reg_date = models.DateTimeField(default=timezone.now)
    # photo = models.ImageField(upload_to="images/%Y/%b/%a/%d/%H/%M", null=True, blank=False)


    class Meta:
        ordering = ('reg_date',)

    def __str__(self):
        name = str(self.name).upper()
        name2 = str(self.lastname).upper()
        Uname = name + ' ' + name2
        return Uname