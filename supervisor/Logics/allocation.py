import random
import pandas as pd
import numpy as np
import datetime
import time
from django.contrib.auth.models import User
from main.models import Allocation_File
class allocations:


    def do_allocations(user_id):
        # do some work
        date_csv = pd.read_csv('./CSVfiles/raw_files/dates.csv')
        name_csv = pd.read_csv('./CSVfiles/raw_files/names.csv')

        data_block_arr = np.array(date_csv)
        name_arr = np.array(name_csv).reshape(-1)

        allocations = dict()
        time_date = dict()
        # try:
                
        for i, j, z in data_block_arr:
                num = 1
                allocatedList = dict()
                while len(allocatedList) < j:
                    nm = random.choice(name_arr.tolist())
                    if nm not in allocatedList.keys():
                        allocatedList[nm] = num
                        num += 1
                    else:
                        continue
                allocations[i] = allocatedList
                time_date[i] = z
        # print(allocations)

        KEYS = list(allocations.keys())

        timestamp_str = str(datetime.datetime.now())
        file_name = timestamp_str.replace(':', '_').replace('.', '_') + '.csv'

        user_instance = User.objects.get(pk=user_id)
        obj = Allocation_File(user_id=user_instance,file_name=file_name)
        obj.save()
        print("File Saved")


        with open(f'./CSVfiles/generated_files/{file_name}', 'w') as f:
                f.write(f'{"Dates"},{"Time"},{"Name"},{"Allocated_Block"}\n')
                for i in KEYS:
                    for j in allocations[i].keys():
                        f.write(f'{i},{time_date[i]},{j},{allocations[i][j]}\n')
        return file_name
        # except Exception as e:
        #     print("Error in allocation.py"+str(e))
    
    def find_allocation_for(name,file_name):
        path = "./CSVfiles/generated_files/"+file_name
        data = pd.read_csv(f'{path}')
        time.sleep(2)
        data = data[data['Name'] == name]

        data = np.array(data)
        return data
         


            
