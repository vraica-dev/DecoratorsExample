"""
idea - create a decorator that parse the arg from the func and return only the file name;
       e.g from  <C:\Test\test\Pictures\CaptureETA.JPG'> only <CaptureETA.JPG> will be returned;
"""

my_file = r'V:\Test\test\Pictures\CaptureETA.JPG'


def keep_filename_only(fnc):
    """
    decorator that returns the filename only from a path
    """

    def wrapper(*args, **kwargs):
        try:
            interim_output = fnc(*args, **kwargs)
            output = interim_output.split("\\")[-1]
        except TypeError:
            return fnc(*args, **kwargs)
        else:
            return f'File name is {output}'

    return wrapper


@keep_filename_only
def get_file_path(f_path: str) -> str:
    """
    returns full path of the file - not decorated;  e.g. File path\name is --  V:\Test\test\Pictures\CaptureETA.JPG
    returns only the file name - when decorated;  e.g. File name is CaptureETA.JPG
    """
    return f'File path is --  {f_path}'


print(get_file_path(my_file)) # because it's decorated, will rpint only CaptureETA.JPG
