def write_file(file_name, file_content):
   file = f'{file_name}.txt'
   with open(f'{file}', mode='w', encoding='utf-8') as log_file:
        log_file.write(file_content)
        
def append_file(file_name, append_content):
    file = f'{file_name}.txt'
    with open(f'{file}', mode='a', encoding='utf-8') as log_file:
        log_file.write(append_content)

def read_file(file_name):
    file = f'{file_name}.txt'
    with open(f'{file}', encoding='utf-8') as log_file:
        return log_file.read()


