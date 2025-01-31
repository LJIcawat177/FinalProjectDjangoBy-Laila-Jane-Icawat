from django.contrib import admin
from .models import FoodCategories, FoodRecipe, Comment ,Post

admin.site.register(FoodCategories)
admin.site.register(FoodRecipe)
admin.site.register(Comment)
admin.site.register(Post)