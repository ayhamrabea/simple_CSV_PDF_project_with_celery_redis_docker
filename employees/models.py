from django.db import models

# Create your models here.

class ProjectStatus(models.IntegerChoices):
    WORKING = 1 , 'working'
    NOT_WORKING = 2 , 'not working'



class Employ(models.Model):

    name = models.CharField(max_length=150)
    age = models.IntegerField()
    job_title = models.CharField(max_length=150 , null=type)
    status = models.IntegerField(choices=ProjectStatus.choices , default=ProjectStatus.WORKING)    
    phone = models.IntegerField()
    email = models.EmailField(max_length=254)
    addres = models.CharField(max_length=250)
    bio = models.TextField()
    created_at = models.DateTimeField( auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    
    

    class Meta:
        verbose_name = ("Employ")
        verbose_name_plural = ("Employs")

    def __str__(self):
        return self.name

