from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import food
# Create your views here.
def food_recipe(request):
    all=food.objects.all()
    return render(request,"home.html",{"item":all, "title":"Foodaholic"})

def food_specific(request,food_id):
	foods=food.objects.get(pk=food_id)
	return render(request,"foods.html",{"dish":foods,"title":foods.title})

def add_recipe(request):

	if request.method=="POST":
            # print(request.POST)
            title=request.POST["title"]
            description=request.POST["description"]
            ingredients=request.POST["ingredients"]
            card_type=request.POST["card_type"]
            image_url=request.POST["image_url"]
            prep_method=request.POST["prep_method"]
            time_to_cook=request.POST["time_to_cook"]
            contribution=request.POST["contribution"]
            new_recipe=food.objects.create(title=title,description=description,contribution=contribution,ingredients=ingredients,card_type=card_type,image_url=image_url,prep_method=prep_method,time_to_cook=time_to_cook)
            return redirect("/")
	return render(request,"addrecipe.html")