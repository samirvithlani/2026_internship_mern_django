from django.db import models

# Create your models here.
#python class

#parent class Model
#create table student(studentName varchar(100),studentAge int,studentCity varchar(40))
#it will generate pk automatically
class Student(models.Model):
    studentName= models.CharField(max_length=100)
    studentAge = models.IntegerField()
    studentCity = models.CharField(max_length=40)
    studentEmail = models.EmailField(null=True)

    #meta class
    class Meta:
        db_table = "student" #table name

class Product(models.Model):
    productName = models.CharField(max_length=100)
    productPrice = models.IntegerField()
    productDescription = models.TextField()
    productStock = models.PositiveIntegerField()
    productColor = models.CharField(max_length=20,null=True)
    productStatus = models.BooleanField(default=True)
    
    class Meta:
        db_table = "product"


