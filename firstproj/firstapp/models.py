from django.db import models

# Create your models here.

class MenuCategory(models.Model):
    menu_category_name = models.CharField(max_length=50)
    def __str__(self):
        return self.menu_category_name
    

class Menu(models.Model):
    menu_item = models.CharField(max_length=50)
    category_name = models.ForeignKey(MenuCategory, on_delete=models.PROTECT, default=None)
    def __str__(self):
        return f"{self.menu_item}, {self.category_name} cuisine"

class Person(models.Model): 
    last_name = models.TextField() 
    first_name = models.TextField()
    class Meta: 
        permissions = [('can_change_last_name', 'Can change last_name')]
    def __str__(self): 
        return f"{self.last_name}, {self.first_name}"


class Employee(models.Model):
    name = models.CharField(max_length=100)   
    email = models.EmailField()   
    contact = models.CharField(max_length=15)   
    class Meta:   
        db_table = "Employee"
    
    def __str__(self): 
        return f"{self.name}, {self.email}"