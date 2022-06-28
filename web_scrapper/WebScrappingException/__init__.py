#import os
import sys

class WebScrappingException(Exception):

    def __init__(self, error_message : Exception, error_details : sys):
        self.error_message = WebScrappingException.get_detailed_error(\
                                error_message = error_message,\
                                error_details = error_details
                                )

    @staticmethod
    def get_detailed_error(error_message : Exception, error_details : sys):
        """
        Provides the detailed error message using error_message as object or type of Exception
        and error_details as object of sys
        """
        #exc_type, exc_obj, exc_tb = error_details.exc_info()
        _, _, exc_tb = error_details.exc_info()
        exception_line_number = exc_tb.tb_frame.f_lineno
        line_number = exc_tb.tb_lineno
        file_name = exc_tb.tb_frame.f_code.co_filename

        error_message = f"""
            Error occured in script: 
            [ {file_name} ] at 
            try block line number: [{line_number}] \
            and exception block line number: [{exception_line_number}] 
            error message: [{error_message}]
        """
        return error_message

    def __str__(self):
        return self.error_message


    def __repr__(self) -> str:
        return WebScrappingException.__name__.str()
