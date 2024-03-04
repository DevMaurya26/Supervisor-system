from django.shortcuts import redirect

def is_admin(view_func):
    def wrapper_func(request,*args,**kwargs):
        if request.user.is_staff:
            return view_func(request,*args,**kwargs)
        else:
            return redirect('dashboard')
    return wrapper_func