from django.db import models

class FoodCategories(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField()

    def __str__(self):
        return self.name

class FoodRecipe(models.Model):
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to='food_images/')  
    description = models.TextField()
    recipe = models.TextField()
    category = models.ForeignKey(FoodCategories, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Comment(models.Model):
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comment by {self.id}"

class Post(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='posts/')
    description = models.TextField()
    recipe = models.TextField()
    category = models.ForeignKey(FoodCategories, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name
