from django.db import models
CHOICE = (
	("day","Recipes_of_the_day"),
	("breakfast","BREAKFAST"),
	("lunch","LUNCH"),
	("dinner","DINNER")
)

class food(models.Model):

    title = models.CharField(max_length=100,null=True,blank=True)
    image_url=models.TextField(null=True,blank=True)      
    contribution=models.CharField(max_length=100,null=True,blank=True)
    description = models.TextField()
    card_type = models.CharField(choices=CHOICE, default="day", max_length=100)
    time_to_cook=models.CharField(max_length=100,null=True,blank=True)
    ingredients=models.TextField()
    prep_method=models.TextField()

    def __str__(self):
        return self.title