from django.db import models
import uuid 

# Create your models here.
#create a model with name Organization with fields name, address, phone_number, email and Unique UUID

class Organization(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    address = models.TextField()
    phone_number = models.CharField(max_length=15)
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.name
