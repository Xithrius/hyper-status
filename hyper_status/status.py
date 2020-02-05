'''
> hyper_status
> Copyright (c) 2020 Xithrius
> MIT license, Refer to LICENSE for more info
'''


import datetime

from colors import colors as c


class Status:
    '''Outputs date, status and/or a custom string.'''
    
    def __init__(self, status: str, warning: str):
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
        
        self.insert_items()

    def catch_error(func):
        '''Wrapper for catching any possible error while creating the status.

        Args:
            func (callback): The function that will be tested.  

        Returns:
            The wrapper.

        Raises:
            IndexError: If the color cannot be found, this error is raised.
            Exception: Any other fatal error.
        
        '''
        def wrapper(*args, **kwargs):
            try:
                result = func(*args, **kwargs)
                print(result)

            except IndexError:
                return print(f'Color could not be found in colors.\nRun the {c["underline"]}colors{c["end"]} module to see options.')
            
            except Exception as e:
                return print(f'Fatal error occured:\n{e}')
        
        return wrapper

    def _join(self, lst: list, bind=' ') -> str:
        return bind.join(str(y) for y in lst)

    @catch_error
    def insert_items(self, n=datetime.datetime.now()) -> str:
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

        # Formatting the time
        n = f"{n.strftime('%b %d, %Y - %A %I:%M:%S')}{n.strftime('%p').lower()}"

        # Putting everything into a list.
        lst = [
            # Formatted date within brackets.
            f"~> {b}[ {self.c['date']}{n}{e} ]{e} >",            
            # The status given by the user
            f"{b}[ {self.c[self.status]}{self.status.title()}{e} ]{e}:", 
            # Putting the warning string into the status, with a small amount of formatting.
            f"{self.warning.capitalize()}{'.' if self.warning[-1] not in ['.', '!', '?'] else ''}"
        ]

        # Returns the list as a string, joined together by a space.
        return self._join(lst)


if __name__ == "__main__":
    # If this specific file is called, and not imported.
    Status('warning', 'This is a test warning. Be warned!')
    Status('fail', 'Oh no, something has totally failed!')
    Status('ready', 'This is fine. Everything is fine.')
