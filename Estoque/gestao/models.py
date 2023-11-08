from django.db import models

# Create your models here.
class Funci(models.Model):
    nome= models.CharField(max_length=100)
    email= models.EmailField(max_length=100,primary_key=True,unique=True)
    gerente= models.BooleanField(default=False,null=False)
    def __str__(self):
        return self.email

class estoque(models.Model):
    idSto= models.AutoField(primary_key=True)
    proNome= models.CharField(max_length=150,default='')
    quanEsto= models.PositiveIntegerField(default=0)
    funci = models.ForeignKey(Funci, on_delete=models.CASCADE,null=True)
    def __str__(self):
        return self.proNome
    
