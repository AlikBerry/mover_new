from django.db import models
   

class ProductTag(models.Model):
    name = models.CharField(max_length=500)
    price = models.CharField(max_length=500)
    size = models.CharField(max_length=500)
    url = models.URLField(max_length=500)
    
    

    def __str__(self):
        return "{} {} {}".format(self.name, self.price, self.size)



    

    
    
