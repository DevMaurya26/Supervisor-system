from django.shortcuts import render
from django.http import FileResponse
from Logics.fileReader import saveAtServer
from Logics.allocation import allocations
from django.contrib.auth.decorators import login_required
from .middelware import is_admin
from .models import Allocation_File
from django.contrib.auth.models import User

save = saveAtServer()
final_file_name = ''
# Create your views here.


def index(request):
    return render(request, 'main/index.html')

@is_admin
def create(request):
    flag1 = False
    flag2 = False
    user_instance = User.objects.get(pk=request.user.id)
    user_files = Allocation_File.objects.filter(user_id=user_instance)

    data ={
        'Done' : 'Done Uploading ✅',
        'error' : 'Please Upload the CSV files first 📂',
        'err_flag' : True,
        'user_files' : user_files,
        'user_instance' : user_instance,
    }
    if request.method == 'POST':
        # print(request.FILES)

        if 'date_csv' in request.FILES:
            uploaded_file = request.FILES['date_csv']
            flag1 = save.read_date_csv(uploaded_file)

        if 'name_csv' in request.FILES:
            uploaded_file = request.FILES['name_csv']
            flag2 = save.read_name_csv(uploaded_file)

        print(flag1,"------",flag2)
        if flag1 and flag2:
            final_file_name = allocations.do_allocations(request.user.id)
            with open('./CSVfiles/generated_files/0files.txt', 'a') as f:
                f.write(final_file_name+'\n')

            data['err_flag'] = False
    
    db = Allocation_File.objects.filter(user_id=request.user.id)
    print(db)

    return render(request, 'main/create.html',data)

@login_required(login_url='login')
def generated(request):
    UserName = request.user.username
    with open('./CSVfiles/generated_files/0files.txt', 'r') as f:
        name = f.read().split('\n')
        print(name)
    data = allocations.find_allocation_for(UserName,name[-2])
    return render(request, 'main/table_data.html',{'data':data})


@login_required(login_url='login')
def download(request, file_name):
    response = FileResponse(open(f'./CSVfiles/generated_files/{file_name}', 'rb'))

    response['Content-Disposition'] = f'attachment; filename="Block_Allocation: {file_name[:10]}.csv"'

    return response