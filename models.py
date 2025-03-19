from django.db import models

# Create your models here.
Classe Classe(model.Models):
       code = models.Charfield(max_length=100,primary_key=True)
       libclasse = models.Charfield(max_length=100,primary_key=false)
Classe Services(model.Models):
       nom=models.Charfields(max_length=255)
       description=models.Textfield(blank=True)
       prix=models.DecimalFields(max_length=10,decimal_places=2)
       date_creation = models.DaTeTimeField(auto_now=True)
       categories=models.ManyToManyField(Category,related_name='services')
          

          def __str__(self):
              return self .nom
        
