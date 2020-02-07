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

    def __init__(self, status: str, warn_str: str):
        self.status = status
        self.warning = warning
        self.c = c

    def __call__(self, func: callable):
        
        def execute(*args, **kwargs):
            try:
                func(*args, **kwargs)
            except Exception as e:
                self.p(type(e).__name__, f'Fatal error occured:', exception_c=True)

        return execute

    def _join(self, lst: list, bind=' ') -> str:
        return bind.join(str(y) for y in lst)

    def insert_items(self, status: str, warning: str, n=datetime.datetime.now(), starter='~>', exception_c=False) -> str:
        '''Gets information collected so far and returns the custom status.

        Args:
            n (str): the datetime.datetime object to be formatted.

        Returns:
            A joined list of all formatted items.

        Raises:
            Possible IndexErrors if color cannot be found.

        '''
        # Bold, and the color indicating the end of the previous one
        b = self.c['bold']
        e = c['end']

        # Removing 0s from the timestamp
        t = []
        for i in n.strftime('%I %M %S').split():
            t.append(int(i) if i[0] != '0' else int(i[1]))

        # Formatting the time
        n = f"{n.strftime('%b %d %Y, %A')} {self._join(t, ':')}{n.strftime('%p').lower()}"

        title = status.title()

        if exception_c:
            title = exception_c
            _color = 'fail'

        if status in self.c.keys():
            status = self.c[status]
        
        # Putting everything into a list.
        lst = [
            # Formatted date within brackets.
            f"{starter} {b}[{e} {self.c['date']}{n}{e} {b}]{e} >",
            # The status given by the user
            f"{b}[{e} {status}{title}{e} {b}]{e}:",
            # Putting the warning string into the status, with a small amount of formatting.
            f"{self.warning.capitalize()}{'.' if self.warning[-1] not in ['.', '!', '?'] else ''}"
        ]

        # Returns the list as a string, joined together by a space.
        print(self._join(lst))


@Status()
def preview():
    Status('warning', 'This is a test warning. Be warned!')
    Status('fail', 'Oh no, something has totally failed!')
    Status('ready', 'This is fine. Everything is fine.')
    x = int('a')


if __name__ == "__main__":
    preview()
