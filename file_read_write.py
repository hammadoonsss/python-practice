import json

def get_file(file_name):
    
    filepath =f"/home/hammdoon/Downloads/txtFiles/{file_name}"
    
    with open(filepath, 'r')as f:
        data = f.read()
        print('data', data)
        
def write_file(file_name, data):
    
    filepath =f"/home/hammdoon/Downloads/txtFiles/{file_name}"
    
    with open(filepath, 'w')as f:
        f.write(data)
        

write_file('ABC.txt', ' the data')
get_file('ABC.txt')