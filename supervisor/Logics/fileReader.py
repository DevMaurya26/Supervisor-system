class saveAtServer:

    def read_name_csv(self, fileObject)->bool:
        print(fileObject)
        try:
              
            decoded_data = fileObject.read().decode('utf-8')
            with open('./CSVfiles/raw_files/names.csv', 'w',newline='') as file:
                    file.write((decoded_data))
        except Exception as e:
            print("Error in FileRead.py creatation of file Names.csv"+e)
            return False
        return True
    
    def read_date_csv(self, fileObject)->bool:
        print(fileObject)
        try:
            decoded_data = fileObject.read().decode('utf-8')
            with open('./CSVfiles/raw_files/dates.csv', 'w',newline='') as file:
                    file.write((decoded_data))
        except Exception as e:
            print("Error in FileRead.py creatation of file Dates.csv"+e)
            return False    
        return True
        
