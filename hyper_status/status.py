'''
> hyper_status
> Copyright (c) 2020 Xithrius
> MIT license, Refer to LICENSE for more info
'''


import datetime

from colors import colors as c


class Status:
    '''Outputs date, status and/or a custom string.'''
    
    def __call__(self, status: str, warning: str):
        '''Creates attributes of the class and calls the creation of items.

        Args:
            status (str): The status of whatever is occuring, (failed, warning, ready)
            warning (str): The warning that would alert the user more specifically of what's happening.

        '''
        self.status = status.lower()
        self.warning = warning
        self.c = {
            'fail': c['red'],
            'ready': c['green'],
            'date': c['gold'],
            'warning': c['purple'],
            'b': c['bold'],
            'u': c['underline']
        }

    def _join(self, lst: list, bind=' ') -> str:
        '''Custom function of join() but only for joining lists.

        Args:
            lst (list): The list that would be binded together by the next argument.
            bind (str): The seperator between every item in the list.

        Returns:
            a list connected by the bind.

        Raises:
            None, unless fatal, not catched.

        '''
        return bind.join(str(y) for y in lst)

    def catch_error(func):
        '''Wrapper for catching errors for any function from the user.

        Args:
            func (callback): The function that will be ran and tested for errors.

        '''
        def wrapper(*args, **kwargs):
            '''Catches the error

            Args:
                whatever is passed into the callable this function is wrapped around.

            Returns:
                The result if no errors occured.

            Raises:
                IndexError: If the color cannot be found, this error is raised.
                Exception: Any other fatal error.

            '''
            try:
                # Attempts to run the function
                func(*args, **kwargs)
            except Exception as e:
                # traceback.print_exception(type(e), e, e.__traceback__, file=sys.stderr)
                self.insert_items(type(e), e, starter='')

        return wrapper

    def catch_color_error(func):
        '''Wrapper for catching any color selection error.

        Args:
            func (callback): The function that will be tested for specifically index errors..
        
        '''
        def wrapper(*args, **kwargs):
            '''Catches the error

            Args:
                whatever is passed into the callable this function is wrapped around.

            Returns:
                The result if no errors occured.

            Raises:
                IndexError: If the color cannot be found, this error is raised.
                Exception: Any other fatal error.

            '''
            try:
                # Attempts to run the function
                result = func(*args, **kwargs)
                print(result)

            # Exceptions if something went really wrong.
            except IndexError:
                print(f'Color could not be found in colors.\nRun the {c["underline"]}colors{c["end"]} module to see options.')
            
            except Exception as e:
                print(f'Fatal error occured:\n{e}')
        
        return wrapper

    @catch_color_error
    def insert_items(self, n=datetime.datetime.now(), starter='~>', exception_c=False) -> str:
        '''Gets information collected so far and returns the custom status.

        Args:
            n (str): the datetime.datetime object to be formatted.

        Returns:
            A joined list of all formatted items.

        Raises:
            Possible IndexErrors if color cannot be found.

        '''
        # Bold, and the color indicating the end of the previous one
        b = self.c['b']
        e = c['end']

        # Removing 0s from the timestamp
        t = []
        for i in n.strftime('%I %M %S').split():
            t.append(int(i) if i[0] != '0' else int(i[1]))

        # Formatting the time
        n = f"{n.strftime('%b %d %Y, %A')} {self._join(t, ':')}{n.strftime('%p').lower()}"

        title = self.status.title()
        _color = self.status

        if exception_c:
            title = exception_c
            _color = 'fail'

        # Putting everything into a list.
        lst = [
            # Formatted date within brackets.
            f"{starter} {b}[{e} {self.c['date']}{n}{e} {b}]{e} >",
            # The status given by the user
            f"{b}[{e} {self.c[_color]}{title}{e} {b}]{e}:",
            # Putting the warning string into the status, with a small amount of formatting.
            f"{self.warning.capitalize()}{'.' if self.warning[-1] not in ['.', '!', '?'] else ''}"
        ]

        # Returns the list as a string, joined together by a space.
        print(self._join(lst))


@Status.catch_error
def preview():
    Status('warning', 'This is a test warning. Be warned!')
    Status('fail', 'Oh no, something has totally failed!')
    Status('ready', 'This is fine. Everything is fine.')
    x = int('a')


if __name__ == "__main__":
    # If this specific file is called, and not imported.
    # Outputs a preview of what you can do with this package.
    preview()
