from django.db import models
from PIL import Image
from django.contrib.auth.models import User
# Create your models here.

STATE=(("Andhra Pradesh","Andhra Pradesh"),
    ("Arunachal Pradesh ","Arunachal Pradesh "),
    ("Assam","Assam"),
    ("Bihar","Bihar"),
    ("Chhattisgarh","Chhattisgarh"),
    ("Goa","Goa"),
    ("Gujarat","Gujarat"),
    ("Haryana","Haryana"),
    ("Himachal Pradesh","Himachal Pradesh"),
    ("Jammu and Kashmir ","Jammu and Kashmir "),
    ("Jharkhand","Jharkhand"),
    ("Karnataka","Karnataka"),
    ("Kerala","Kerala"),
    ("Madhya Pradesh","Madhya Pradesh"),
    ("Maharashtra","Maharashtra"),
    ("Manipur","Manipur"),
    ("Meghalaya","Meghalaya"),
    ("Mizoram","Mizoram"),
    ("Nagaland","Nagaland"),
    ("Odisha","Odisha"),
    ("Punjab","Punjab"),
    ("Rajasthan","Rajasthan"),
    ("Sikkim","Sikkim"),
    ("Tamil Nadu","Tamil Nadu"),
    ("Telangana","Telangana"),
    ("Tripura","Tripura"),
    ("Uttar Pradesh","Uttar Pradesh"),
    ("Uttarakhand","Uttarakhand"),
    ("West Bengal","West Bengal"),
    ("Andaman and Nicobar Islands","Andaman and Nicobar Islands"),
    ("Chandigarh","Chandigarh"),
    ("Dadra and Nagar Haveli","Dadra and Nagar Haveli"),
    ("Daman and Diu","Daman and Diu"),
    ("Lakshadweep","Lakshadweep"),
    ("National Capital Territory of Delhi","National Capital Territory of Delhi"),
    ("Puducherry","Puducherry"),
    )
class Customers(models.Model):
    
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name=models.CharField( max_length=50)
    phone=models.CharField( max_length=10)
    locality=models.CharField(max_length=50)
    city=models.CharField( max_length=50)
    state=models.CharField( max_length=50, choices=STATE)
    pincode=models.IntegerField()
    

   

class Product(models.Model):
    types = (
        ('M', 'male'),
        ('F', 'female'),
        ('K', 'kids'),
        ('E', 'electronic'),
    )
    cotegary = (
        ('Jens', 'Jens'),
        ('Saree', 'Saree'),
         ('Lehenga', 'Lehenga'),
        ('Palazzo', 'Palazzo'),
        ('Patiala', 'Patiala'),
        ('T-shirt', 'T-shirt'),
        ('Shampoo', 'Shampoo'),
        ('Dhoti', 'Dhoti'),
        ('Kurta', 'Kurta'),
        ('Coat', 'Coat'),
        ('jellwary', 'jellwary'),
        ('Cooler', 'Cooler'),
        ('Phone', 'Phone'),
        ('TV', 'TV'),
        ('Fan', 'Fan'),
        ('Computer', 'Computer'),
        ('Headphone', 'Headphone'),
        ('Camera', 'Camera'),
        ('Shoes', 'Shoes'),
        ('Pajama', 'Pajama'),
        ('Shirt', 'Shirt'),
        ('Swerter', 'Swerter'),
        ('Suit', 'Suit'),

        
        
    )
    title=models.CharField( max_length=50)
    sell_pr=models.CharField(max_length=50)
    discount_price=models.CharField(max_length=50)
    description=models.TextField()
    brand=models.CharField(max_length=50)
    gender=models.CharField(max_length=30,choices=types,default="M")
    coteg=models.CharField(max_length=30,choices=cotegary,default="Jens")
    img = models.ImageField(upload_to ='uploads/')
    def __str__(self):
        return self.title

    def save(self):
        super().save()  # saving image first

        imgs = Image.open(self.img.path) # Open image using self

        # if imgs.height > 200 or imgs.width > 200:
        #     new_img = (200, 200)
        #     imgs.thumbnail(new_img)
        #     imgs.save(self.img.path)
class Cart(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    product=models.ForeignKey(Product, on_delete=models.CASCADE)
    quantily=models.PositiveIntegerField()
    

class Orderplaces(models.Model):
    order = (
        ('Confirmed', 'Confirmed'),
        ('Packed', 'Packed'),
        ('courier', 'courier'),
        ('picked_up', 'picked_up'),
    )
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    product=models.ForeignKey(Product, on_delete=models.CASCADE)
    costomer=models.ForeignKey(Customers, on_delete=models.CASCADE)
    quantity=models.PositiveIntegerField()
    date = models.DateField()
    exp = models.DateField()
    deliver=models.CharField(max_length=30,choices=order)
    

class Token(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    token=models.CharField(max_length=50)






