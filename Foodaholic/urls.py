from django.contrib import admin
from django.urls import path,include
from recipe.views import food_recipe,food_specific,add_recipe

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include("authentication.urls")),
    path('',food_recipe),
    path('food/<int:food_id>/',food_specific),
    path('add_recipes',add_recipe),
]
