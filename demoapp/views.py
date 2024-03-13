from django.shortcuts import render
from django.views.generic import View
from django.http import HttpResponse

class FirstView(View):
    def get(self,request,*args,**kwargs):
        # return HttpResponse("hello guys!!!!!!!!!!!! Welcome to first view!!!")\
        profile={
        "name":"sreedhini",
        "age": 23,
        "place":"kasargod"
    }

        return render(request,"first_view.html",profile)



def my_view(request):
    context = {
        'title': 'Function-Based View Example',
        'products': [
            {'name': 'Laptop', 'price': 1000},
            {'name': 'Phone', 'price': 500},
            {'name': 'Tablet', 'price': 300}
        ]
    }
    return render(request, 'fn_view.html', context)
