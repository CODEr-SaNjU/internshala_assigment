from django.db import models
from django.dispatch import receiver
from django.core.signals import request_finished
from django.db.models.signals import post_save,pre_save
# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=20)
    message = models.TextField(max_length=400)
    file_name= models.FileField(upload_to ='uploads/', max_length=254)
    
    def __str__(self):
        return self.name
    
# def update_user_data(sender,instance,created,update_fields ,**kwargs):
#     update_fields = []
#     if change:
#         if Model.initial['name'] != models.cleaned_data['name']:
#             update_fields.append('name')
#             print("name filed is updated {}".format(instance))
#         elif Model.initial['message'] != models.cleaned_data['message']:
#             update_fields.append('message')
#             print("name filed is updated {}".format(instance))
#         elif Model.initial['file_name'] != models.cleaned_data['file_name']:
#             update_fields.append('message')
#             print("name filed is updated {}".format(instance))
#     else:
#         print("sorry you have do nothing change")
@receiver(pre_save, sender=Product)
def created_user_data(sender,instance,update_fields, **kwargs):
    if instance.id is None:
        print(" your data is created  {}".format(instance.name))
                
    else:
        product = Product.objects.get(id=instance.id)
        if product.name != instance.name:
            print("your object name is change {}".format(instance.name))
        elif product.message != instance.message:
            print("your data is {}".format(instance.name),"is update your message={}".format(instance.message))
        elif product.name != instance.name and product.message != instance.message:
            print("your object name  and  message is change {}".format(instance.message))
        elif product.file_name != instance.file_name:
            print("your object name  and  message is change {}".format(instance.file_name))
pre_save.connect(created_user_data,sender=Product)
post_save.connect(created_user_data,sender=Product)