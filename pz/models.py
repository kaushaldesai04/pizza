from django.db import models
from multiselectfield import MultiSelectField


# Create your models here.
class pizza(models.Model):
    TYPES=(
        ('Regular','Regular'),
        ('Square','Square'),
    )
    TOPINGS=(
        ('Onion','Onion'),
        ('Tomato','Tomato'),
        ('Corn','Corn'),
        ('Capsicum','Capsicum'),
        ('Cheese','Cheese'),
        ('Jalapeno','Jalapeno'),
    )
    type=models.CharField(max_length=128,choices=TYPES)
    size=models.CharField(max_length=128)
    topings=MultiSelectField(choices=TOPINGS)



