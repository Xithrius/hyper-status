'''
> hyper_status
> Copyright (c) 2020 Xithrius
> MIT license, Refer to LICENSE for more info
'''


import datetime


c = {
    'date': '\033[93m',
    'fail': '\033[91m',
    'warning': '\033[95m',
    'ok': '\033[92m',
    'bold': '\033[1m',
    'under': '\033[4m',
    'end': '\033[0m'
}


class Status:

    def __init__(self, *args, **kwargs):
        self.args = args
        self.kwargs = kwargs
        self.c = c

    def __call__(self, func: callable):
        
        def execute(*args, **kwargs):
            try:
                func(*args, **kwargs)
            except Exception as e:
                self.insert_items(type(e).__name__, f'Fatal error occured:', exception_c=True)

        return execute

    def _join(self, lst: list, _sep=' ') -> str:
        return _sep.join(str(y) for y in lst)

    def insert_items(self, )


@Status()
def preview():
    Status('warning', 'This is a test warning. Be warned!')
    Status('fail', 'Oh no, something has totally failed!')
    Status('ready', 'This is fine. Everything is fine.')
    x = int('a')


if __name__ == "__main__":
    preview()
