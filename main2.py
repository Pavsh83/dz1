import subprocess
import string

def check_output(command, text, split_words=False):
    try:
        output = subprocess.check_output(command, shell=True).decode()
        
        if split_words:
            
            output_words = output.translate(str.maketrans('', '', string.punctuation)).split()
            if text in output_words:
                return True
            else:
                return False
        else:
            if text in output:
                return True
            else:
                return False
            
    except subprocess.CalledProcessError:
        return False


command = "ls /"
text = "bin"
result = check_output(command, text, split_words=True)
print(result)
