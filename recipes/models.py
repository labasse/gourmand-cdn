from django.db import models
from django.core.validators import RegexValidator
from tinymce import models as tinymce_models


class Category(models.Model):
    name = models.CharField(max_length=20)
    order = models.IntegerField(default=100)

    def __str__(self):
        return self.name
    

class Recipe(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    description = models.TextField()
    quantity = models.CharField(max_length=50)
    instructions = tinymce_models.HTMLField()
    image = models.ImageField(default="img/default.png", upload_to="img/")
    likes = models.IntegerField(default=0)
    vegan = models.BooleanField(default=False)
    published = models.DateTimeField(auto_now_add=True)
    password = models.CharField(
        max_length=200, 
        null=True, 
        blank=True, 
        validators=[RegexValidator(
            regex='^(?=.*\d)(?=.*[a-z])(?=.*[A-Z]).{8,}$',
            message='Le mot de passe doit contenir au moins 8 caractères, dont au moins un chiffre, une minuscule et une majuscule'
        )]
    )
    
    def __str__(self):
        return f"{self.category.name} / {self.title}"
    

class Ingredient(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    optional = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.recipe.pk} - {self.name}"
    
