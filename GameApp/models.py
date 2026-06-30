from django.db import models
class Category_Db(models.Model):
    Category_Name = models.CharField(max_length=100,blank=True,null=True)
    Category_Description = models.TextField(blank=True,null=True)
    Category_Image = models.ImageField(upload_to="Game Categories",blank=True,null=True)

class Game_Db(models.Model):
    Game_Category = models.CharField(max_length=100,blank=True,null=True)
    Cover_Image = models.ImageField(upload_to="Games",blank=True,null=True)
    Game_Name = models.CharField(max_length=100,blank=True,null=True)
    Tag_Line = models.CharField(max_length=100,blank=True,null=True)
    Short_Description = models.TextField(blank=True,null=True)
    Summary = models.TextField(blank=True,null=True)
    Genre = models.CharField(max_length=100,blank=True,null=True)
    Game_Style = models.CharField(max_length=100,blank=True,null=True)
    Platform = models.CharField(max_length=100,blank=True,null=True)
    Release_Date = models.CharField(max_length=100,blank=True,null=True)
    Game_Mode = models.CharField(max_length=100,blank=True,null=True)
    Developer = models.CharField(max_length=100,blank=True,null=True)
    Publisher = models.CharField(max_length=100,blank=True,null=True)
    Age_Rating = models.CharField(max_length=100,blank=True,null=True)
    Play_Time = models.CharField(max_length=100,blank=True,null=True)
    Overall_Rating = models.IntegerField(blank=True,null=True)
    Download_Link = models.URLField(blank=True,null=True)
    Image1 = models.ImageField(upload_to="Games",blank=True,null=True)
    Image2 = models.ImageField(upload_to="Games",blank=True,null=True)
    Image3 = models.ImageField(upload_to="Games",blank=True,null=True)
    Trailer = models.FileField(upload_to='Trailers', blank=True, null=True)

class Requirement_Db(models.Model):
    Requirement_Game = models.CharField(max_length=100,blank=True,null=True)
    Minimum_OperatingSystem = models.CharField(max_length=100,blank=True,null=True)
    Maximum_OperatingSystem = models.CharField(max_length=100,blank=True,null=True)
    Minimum_RAM = models.CharField(max_length=100,blank=True,null=True)
    Maximum_RAM = models.CharField(max_length=100,blank=True,null=True)
    Minimum_Processor = models.CharField(max_length=100,blank=True,null=True)
    Maximum_Processor = models.CharField(max_length=100,blank=True,null=True)
    Minimum_Graphics = models.CharField(max_length=100,blank=True,null=True)
    Maximum_Graphics = models.CharField(max_length=100,blank=True,null=True)
    Minimum_Storage = models.CharField(max_length=100,blank=True,null=True)
    Maximum_Storage = models.CharField(max_length=100,blank=True,null=True)
class Upcoming_Db(models.Model):
    Up_Cover_Image = models.ImageField(upload_to="Games",blank=True,null=True)
    Up_Inside_Image = models.ImageField(upload_to="Games",blank=True,null=True)
    Up_Game_Name = models.CharField(max_length=100,blank=True,null=True)
    Up_Tag_Line = models.CharField(max_length=100,blank=True,null=True)
    Up_Short_Description = models.TextField(blank=True,null=True)
    Up_Summary = models.TextField(blank=True,null=True)
    Up_Genre = models.CharField(max_length=100,blank=True,null=True)
    Up_Game_Style = models.CharField(max_length=100,blank=True,null=True)
    Up_Platform = models.CharField(max_length=100,blank=True,null=True)
    Up_Release_Date = models.CharField(max_length=100,blank=True,null=True)
    Up_Game_Mode = models.CharField(max_length=100,blank=True,null=True)
    Up_Developer = models.CharField(max_length=100,blank=True,null=True)
    Up_Publisher = models.CharField(max_length=100,blank=True,null=True)
    Up_Age_Rating = models.CharField(max_length=100,blank=True,null=True)
    Up_Play_Time = models.CharField(max_length=100,blank=True,null=True)
    Up_Overall_Rating = models.IntegerField(blank=True,null=True)
    Up_Trailer = models.FileField(upload_to='Trailers', blank=True, null=True)

class Fan_Favorite_Db(models.Model):
    Fan_Game = models.CharField(max_length=100,blank=True,null=True)
    Fan_Created = models.DateTimeField(auto_now_add=True)
    Fan_Description = models.TextField(blank=True,null=True)
    Fan_Image = models.ImageField(upload_to="fan_favorite",blank=True,null=True)
    Reason1 = models.CharField(max_length=100,blank=True,null=True)
    Reason2 = models.CharField(max_length=100,blank=True,null=True)
    Reason3 = models.CharField(max_length=100,blank=True,null=True)





# Create your models here.
