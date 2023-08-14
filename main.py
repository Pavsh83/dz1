import subprocess

def check_command_output(command, text):
    try:
        result = subprocess.run(command, shell=True, capture_output=True, text=True)
        return text in result.stdout
    except Exception as e:
        print(f"Ошибка при выполнении команды: {e}")
        return False


command = "ls" 
text_to_check = "file.txt"  

if check_command_output(command, text_to_check):
    print("Команда выполнена успешно, текст найден в выводе.")
else:
    print("Команда не выполнена или текст не найден в выводе.")
