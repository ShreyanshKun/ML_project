import sys 

def error_message_detail(error, error_detail:sys):
    _, _, exc_tb = error_detail.exc_info()
    file_name = exc_tb.tb_frame.f_code.co_filename
    error_message = "Error occured in python script name [{0}] line number [{1}] and the error msg is [{2}]".format(
        file_name, exc_tb.tb_lineno, str(error)
    )
    
    # FIX 1: Added the return statement
    return error_message


class CustomException(Exception):
    # FIX 2: Corrected the spelling to __init__
    def __init__(self, error_message, error_detail:sys):
        
        # FIX 3: Added parentheses to super()
        super().__init__(error_message)
        
        self.error_message = error_message_detail(error_message, error_detail=error_detail)

    def __str__(self):
        return self.error_message