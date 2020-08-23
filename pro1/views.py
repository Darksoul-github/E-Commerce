from django.shortcuts import render
from django.contrib.auth.models import User
from pro1.models import *
from pro1.forms import *
from django.http import HttpResponse
from django.db.models import Q
from django.shortcuts import get_object_or_404
# Create your views here
form=None
comment={}
def home(request,form=form):
    m=Item.objects.all()
    cat=Category.objects.all()
    context={'cartname':m,'forms':form, 'category':cat}

    return render(request,'shop\home.html',context)

def item(request,subcategory,form=form):
   m=SubCategory2.objects.get(subcat_name=subcategory)
   ite=Item.objects.filter(sub_cat2=m)
   head={}
   for x in ite:
       for y in x.spec_property.all():
           l=[]
           head[y.name.name]=l
   for x in ite:
       for y in x.spec_property.all():
           if y.property not in  head[y.name.name]:
                  head[y.name.name].append(y.property) 
   context={'cartname':ite,'forms':form,'specialprop':head,'sub':subcategory}
   return render(request,'shop\items.html',context)

def categorysearch(request,subcategory,search):
       m=SubCategory2.objects.get(subcat_name=subcategory)
       ite=Item.objects.filter(sub_cat2=m)

       for x in ite:
               k=Item.objects.filter(Q(sub_cat2=m) & Q(spec_property__property__contains=search))
       context={'cartname':k, 'sub':subcategory}
       return render(request,'shop\items.html',context)

def profile(request,form=form):
    m=Item.objects.all()
    f=UserProfile.objects.get(user_name=User.objects.get(username=request.user.username))
    obj={'User':f,'cartname':m,'forms':form}
    return render(request,'registration\profile.html',obj)

def search(request):
    return HttpResponse('HI')
   


  



   

