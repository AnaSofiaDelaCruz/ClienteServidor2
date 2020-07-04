from django.db import models

# Create your models here.

class Example1(models.Model):
    name = models.CharField(max_length = 255, null = False)
    #age=models.IntegerField(max_length=2)
    age = models.IntegerField(null=False,default=1)
    address = models.CharField(max_length=200, null = False,default='')
    curp = models.CharField(max_length=16, null = False,default='')


    
    def __str__(self):
        return self.name,self.age,self.address,self.curp
        

    class Meta:
        db_table = 'Example1'
