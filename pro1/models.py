from django.db import models
class SpecCategory(models.Model):
    name=models.CharField(max_length=30)

    def __str__(self):
        return self.name
class SpecProperty(models.Model):
    name=models.ForeignKey(SpecCategory,on_delete=models.CASCADE)
    property=models.CharField(max_length=20)
    def __str__(self):
        return self.property + " " + str(self.name)

class Category(models.Model):
    cart_name=models.CharField(max_length=20)
    def __str__(self):
        return self.cart_name

class SubCategory1(models.Model):
    cat=models.ForeignKey(Category,on_delete=models.CASCADE)
    subcat_name=models.CharField(max_length=20)
    def __str__(self):
        return str(self.cat) + " " +"-->"+" "+ self.subcat_name

class SubCategory2(models.Model):
    cat=models.ForeignKey(SubCategory1,on_delete=models.CASCADE)
    subcat_name=models.CharField(max_length=20)
    def __str__(self):
        return str(self.cat) + " " +"-->"+" "+ self.subcat_name


class Item(models.Model):
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    sub_cat1=models.ForeignKey(SubCategory1,on_delete=models.CASCADE)
    sub_cat2=models.ForeignKey(SubCategory2,on_delete=models.CASCADE)
    name=models.CharField(max_length=30)
    price=models.IntegerField(default=0)
    img=models.ImageField()
    description=models.CharField(max_length=1000)
    Quantity=models.IntegerField(default=0)
    spec_property=models.ManyToManyField(SpecProperty)

    def __str__(self):
        return self.name






    
