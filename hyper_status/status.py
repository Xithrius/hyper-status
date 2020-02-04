'''
> hyper_status
> Copyright (c) 2020 Xithrius
> MIT license, Refer to LICENSE for more info
'''


import datetime

import colors as c


class Status:
    '''Outputs date, status and/or a custom string.'''
    
    def __init__(self, stat: str, warning: str):
        self.stat = stat
        self.warning = warning
        
        print(self.insert_items())

    def insert_items(self):
        
        lst = [
            self.insert_date()
        ]
        return self._join(lst)

    def insert_date(self, bracket_c=c['bold'], date_c=c['blue']):
        n = datetime.datetime.now()
        lst = [
            
        ]

    def __insert_date(self):
        n = datetime.datetime.now()
        s = [
            f"{c['bold']}[{c['end']} {c.DATE}{n.strftime('%b %d, %Y - %A %I:%M:%S')}{n.strftime('%p').lower()} {c['end']}{c['bold']}]{c['end']}{':' if not warning else ''}",
            f'{c.BOLD}[{c.END} {warning} {c.BOLD}]{c.END}:' if warning else False,
            f'{string} '
        ]

    def warning_string(self, string: str) -> str:
        '''Creates a string with a custom warning
        
        Args:
            string (str): The string containing the warning.

        Returns:
            A string with custom colors.

        Raises:
            ValueError if color and/or warning cannot be found.
        
        '''
        if string in c.values():
            return c[string]
        else:
            raise IndexError(f'Color {string} could not be found in colors.\nRun the {c["underline"]}colors{c["end"]} module to see options.')

    def _join(self, lst: list) -> str:
        return ' '.join(str(y) for y in lst)


Status('warning', 'Cogs have been loaded')
