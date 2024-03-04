# Custom Middelwear

from django.shortcuts import redirect

def alreadyLogedIn(view_func):
    def wrapper_func(request,*args,**kwargs):
        if request.user.is_authenticated:
            return redirect('dashboard')
        else:
            return view_func(request,*args,**kwargs)
    return wrapper_func