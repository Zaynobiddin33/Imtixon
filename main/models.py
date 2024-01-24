from django.db import models

# Create your models here.


#blog web sahifadagi tadbirlar qismiga yangi tadbir qo'shish uchun
class Party(models.Model):                    
    name = models.CharField(max_length =255)
    price = models.IntegerField()
    text = models.TextField()
    img = models.ImageField()

    def __str__(self) -> str:
        return self.name
    


#asosiy va blog web sahifadagi Hodimlar qismiga hodim yaratish uchun
class Cheff(models.Model):                      
    name = models.CharField(max_length = 100)
    role = models.CharField(max_length = 255)
    text = models.TextField()
    img = models.ImageField()

    def __str__(self) -> str:
        return self.name



#menyuga Yangi taom qo'shish uchun
class Food(models.Model):                      
    name = models.CharField(max_length = 255)
    ingridients = models.CharField(max_length = 255)
    price = models.DecimalField(max_digits = 6, decimal_places = 2)
    img = models.ImageField()
    meal_time = models.SmallIntegerField()      # taom qaysi vaqtda taklif qilinishini belgilaydi -- 1: nonushta, 2: tushlik, 3: kechki ovqat

    def __str__(self) -> str:
        return self.name
    

# Forma to'ldirish orqali joy band qilish uchun
class BookTable(models.Model):                  
    name = models.CharField(max_length = 255)
    email = models.EmailField(null = True)
    phone = models.CharField(max_length = 15)
    date = models.DateField()
    time = models.TimeField()
    people = models.IntegerField()
    message = models.TextField(null = True)

    def __str__(self) -> str:
        return self.name
    


# asosiy va blog qismlardagi korxona suratlari galereyasini shakllantirish uchun   
class Gallery(models.Model):                   
    img = models.ImageField()


#Contact sahifsidagi bog'lanish formasi uchun
class Contact(models.Model):                    
    name = models.CharField(max_length = 120)
    phone = models.CharField(max_length = 15)
    email = models.EmailField(null = True)
    text = models.TextField()

    def __str__(self) -> str:
        return self.name




