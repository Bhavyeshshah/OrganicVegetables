from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now
# Create your models here.
class Addproducts(models.Model):
     id = models.AutoField(primary_key=True)
     product_name= models.CharField(max_length=100)
     section = models.CharField(max_length=100, default=True, blank=True)
     price = models.IntegerField(default=0)
     discount_price= models.CharField(max_length=100, default=True, blank=True)
     discount_percentage = models.CharField(max_length=100, default=True, blank=True)
     value = models.CharField(max_length=100)
     description = models.TextField(default="")
     image=models.ImageField(upload_to='pics')
     liked = models.ManyToManyField(User,default=None,blank=True,related_name='Liked')
     def num_likes(self):
          return self.liked.all().count()

LIKE_CHOICES = (
     ('Like','Like'),
     ('Unlike','Unlike')
)

class Like(models.Model):
     user = models.ForeignKey(User, on_delete=models.CASCADE)
     product = models.ForeignKey(Addproducts, on_delete=models.CASCADE)
     value = models.CharField(choices=LIKE_CHOICES,default='Like',max_length=10)

class Orders(models.Model):
     #user = models.OneToOneField(User, on_delete=models.CASCADE)
     order_id= models.AutoField(primary_key=True)
     items_json= models.CharField(max_length=5000)
     amount = models.IntegerField(default=0)
     name= models.CharField(max_length=90)
     username = models.CharField(max_length=111)
     email= models.CharField(max_length=111)
     address= models.CharField(max_length=700)
     city= models.CharField(max_length=111)
     state= models.CharField(max_length=111)
     zip_code= models.CharField(max_length=111)
     phone = models.CharField(max_length=14, default="")

class OrderUpdate(models.Model):
    update_id= models.AutoField(primary_key=True)
    order_id= models.IntegerField(default="")
    update_desc= models.CharField(max_length=5000)
    timestamp= models.DateField(auto_now_add= True)

class Contact(models.Model):
     first_name = models.CharField(max_length=5000)
     last_name = models.CharField(max_length=5000)
     email = models.CharField(max_length=5000)
     feedback = models.TextField()

class Commentsss(models.Model):
     com_id = models.AutoField(primary_key=True)
     pr_id = models.IntegerField(blank=True)
     reply_id = models.IntegerField(default=0,blank=True)
     comment = models.TextField()
     user = models.ForeignKey(User, on_delete=models.CASCADE)
     product = models.ForeignKey(Addproducts, on_delete=models.CASCADE)
     #parent = models.ForeignKey('self', on_delete=models.CASCADE, default="", blank=True)
     timestamp = models.DateTimeField(default=now)


class Reply(models.Model):
     re_id = models.AutoField(primary_key=True)
     pr_id = models.IntegerField(blank=True)
     reply_id = models.IntegerField(default=0,blank=True)
     comment = models.TextField()
     user = models.ForeignKey(User, on_delete=models.CASCADE)
     product = models.ForeignKey(Addproducts, on_delete=models.CASCADE)
     #parent = models.ForeignKey(Com , on_delete=models.CASCADE, blank=True,null=True)
     timestamp = models.DateTimeField(default=now)


'''class AddComments(models.Model):
     com_id = models.AutoField(primary_key=True)
     pr_id = models.IntegerField()
     comment = models.TextField()
     user = models.ForeignKey(User, on_delete=models.CASCADE)
     product = models.ForeignKey(Addproducts, on_delete=models.CASCADE)
     #parent = models.ForeignKey('self', on_delete=models.CASCADE, default="", blank=True)
     timestamp = models.DateTimeField(default=now)'''