import basic
from string_with_arrows import *
while True :
    text = input('basic> ')
    if text.strip() == "" : continue
    result,error = basic.run('<stdin>',' '+text)

    if error :
        error.as_string()
        # result  = f'{error.error_name}: {error.details}\n'
        # result += f'File {error.pos_start.filename}, line {error.pos_start.line + 1}'
        # result += '\n\n' + string_with_arrows(error.pos_start.file_text, error.pos_start, error.pos_end)
        # result += "Error Detected"
        result  = f'{error.error_name}: {error.details}\n'
        result += f'File {error.pos_start.fn}, line {error.pos_start.ln + 1}'
        result += '\n\n' + string_with_arrows(error.pos_start.ftxt, error.pos_start, error.pos_end)
        result += "Error Detected"
        print(result)
        continue
    
    elif result : print(repr(result))