from django.db import models

class Contact_Db(models.Model):
    Name = models.CharField(max_length=100,blank=True,null=True)
    Mobile = models.IntegerField(blank=True,null=True)
    Email = models.EmailField(blank=True,null=True)
    City = models.CharField(max_length=100,blank=True,null=True)
    Message = models.TextField(blank=True,null=True)

class Login_Db(models.Model):
    Profile_Image = models.ImageField(upload_to="user_image",blank=True,null=True)
    Name = models.CharField(max_length=100,blank=True,null=True)
    Email = models.EmailField(blank=True,null=True)
    Mobile = models.IntegerField(blank=True,null=True)
    Password = models.CharField(max_length=100,blank=True,null=True)
    Re_Password = models.CharField(max_length=100,blank=True,null=True)
class Comment_Db(models.Model):
    Game_Name = models.CharField(max_length=100,blank=True,null=True)
    User_Image = models.CharField(max_length=255, blank=True, null=True)
    User_Name = models.CharField(max_length=100,blank=True,null=True)
    Created_Time = models.DateTimeField(auto_now_add=True)
    Comment = models.TextField(blank=True,null=True)
class Favorite_Db(models.Model):
    Fav_Cover = models.CharField(max_length=255,blank=True,null=True)
    Fav_Gname = models.CharField(max_length=100,blank=True,null=True)
    Fav_Age = models.CharField(max_length=100,blank=True,null=True)
    Fav_Overall = models.IntegerField(blank=True,null=True)
    Fav_User = models.CharField(max_length=255,blank=True,null=True)
    Fav_ID = models.IntegerField(blank=True,null=True)

class Blog_Share(models.Model):
    Blog_Name = models.CharField(max_length=100,blank=True,null=True)
    Blog_Email = models.EmailField(blank=True,null=True)
    Blog_Fav = models.CharField(max_length=100,blank=True,null=True)
    Blog_Feedback = models.TextField(blank=True,null=True)






# Create your models here.
