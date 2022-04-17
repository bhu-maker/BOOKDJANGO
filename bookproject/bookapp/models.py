from django.db import models

# Create your models here.

class bookmodel(models.Model):
    title=models.CharField(max_length=255)
    author=models.CharField(max_length=100)
    price=models.DecimalField(max_digits=5,decimal_places=2,help_text=('format xxx.xx'))
    pages=models.IntegerField(verbose_name=('content'))

    def __str__(self):
        return self.title

class Meta:
      db_table="book"

    


