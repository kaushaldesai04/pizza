from django.shortcuts import render, redirect
from. models import pizza
from django.contrib import messages
import pymongo

def home(request):              #home page

    return render(request,'home.html')
def show(request):              #show data of existing pizzas before and after filtering

    data=pizza.objects.all()
    size=[]
    for i in data:
        if i.size not in size:
            size.append(i.size)


    if request.method=="POST":

        filtype=request.POST.getlist('type')
        filsize=request.POST.getlist('size')
        filtype=tuple(filtype)
        filsize=tuple(filsize)
        print(filsize)
        if len(filtype)>=1 and len(filsize)>=1:
            data=pizza.objects.filter(type__in=filtype,size__in=filsize)
            return render(request, 'show.html', {"pizza": data, "list": size})
        elif len(filtype)>=1 and len(filsize)<1:
            data = pizza.objects.filter(type__in=filtype)
            return render(request, 'show.html', {"pizza": data, "list": size})
        elif len(filtype) < 1 and len(filsize) >= 1:
            data = pizza.objects.filter(size__in=filsize)
            return render(request,'show.html',{"pizza":data,"list":size})
    return render(request,'show.html',{"pizza":data,"list":size})

def edit(request):                  #edit existing pizzas from user login
    data1 = pizza.objects.all()
    if request.method=="POST":
        ID=request.POST['id']
        type=request.POST['type']
        size=request.POST['size']
        topings=request.POST.getlist('topings')
        data=pizza.objects.get(id=ID)
        if len(ID)>=1:
            data.id=ID
        if len(type)>=1:
            data.type=type
        if len(size)>=1:
            data.size=size
        if len(topings)>=1:
            data.topings=topings
        elif len(ID)<1 and len(type)<1 and len(size)<1 and len(topings)<1:
            messages.info(request,"Enter data")
        data.save()
        return redirect('show')
    else:
        return render(request,'edit.html',{'pizza':data1})

def delete(request):        #delete existing pizzas
    data1=pizza.objects.all()
    if request.method=='POST':
        ID = request.POST['id']
        data=pizza.objects.get(id=ID)
        if len(ID)>=1:
            data.delete()
        elif len(ID)<1:
            messages.info(request,"Enter ID of pizza to delete")
        return redirect('show')
    else:
        return render(request,'delete.html',{'pizza':data1})

def makepizza(request):             #Creating new pizzas
   if request.method=="POST":
       type=request.POST['type']
       size=request.POST['size']
       topings=request.POST.getlist('topings')
       data=pizza()
       data.type=type
       data.size=size
       data.topings=topings
       if len(type) >=1 or len(size) >=1 or len(topings)>=1:
            data.save()
            messages.info(request, "Pizza created")
       else:
           messages.info(request, "Enter valid data")
       return redirect('makepizza')
   else:
      return render(request,'makepizza.html')
