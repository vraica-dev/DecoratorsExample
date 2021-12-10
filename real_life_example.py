"""
idea - create a decorator that only logs to a file when an error arises
"""


class ErrorLogger:
    """
    used to log the error details and decorated func details
    """
    def __init__(self, fnc):
        self.fnc = fnc

    def __call__(self, *args, **kwargs):
        import datetime
        try:
            self.fnc(*args, **kwargs)
        except Exception as e:
            with open('errorsFile.txt', 'a') as err_f:
                err_f.write(f'Error -- {e.__doc__} -- ocurred when running < '
                            f'{self.fnc.__name__} > provided with args -- {args} --'
                            f'and kwargs -- {kwargs} -- run  @ {datetime.datetime.now()}\n\n')
            print('Error logged.')
        else:
            return self.fnc(*args, **kwargs)


@ErrorLogger
def read_file(f_path: str) -> None:
    with open(f_path, 'rb') as f_reader:
        [print(line) for line in f_reader.readlines()]


f_path_broken = 'broken_path/broken_file'
read_file(f_path_broken) # prints "Error logged" from decorator; writes error log into the errorsFile file;

f_path_ok = 'errorsFile.txt'
read_file(f_path_ok) # since the file exists, the decorator only returns the function; no error - no logging;
