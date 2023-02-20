from django.shortcuts import render
from apptest.models import customer
def x (request):

    if request.method == "POST":
            desc = request.POST['description']
            c = customer(name="name",description=desc)
            c.save()
            
    return render(request,"x.html")

    




