from django.db import models

    

# Create your models here.
class farmer(models.Model):
    name_of_organization = models.CharField(max_length=300)
    Full_address_location = models.TextField()
    crop = models.CharField(max_length=500)
    why_do_you_seeking_land = models.TextField()
    how_much_you_invest = models.TextField()
    passport =  models.ImageField(upload_to='media/passport')
    national_ID_card =  models.ImageField(upload_to='media/national')
    farm_location = models.TextField()
    
   
    
class farm(models.Model):
    Retail = 'Retail Farmer'
    comer = 'Commarcial Farmer'
    
    
    farmers = [
        (Retail,('Retail Farmer')),
        (comer,('Commarcial Farmer')),
    ]  
    retails = models.CharField(
        max_length=200,
        choices=farmers,
        default=Retail,blank=True, null=True
        
    )  
    
    
    
    
    
    
    
