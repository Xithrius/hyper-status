'''
> hyper_status
> Copyright (c) 2020 Xithrius
> MIT license, Refer to LICENSE for more info
'''


import datetime

from hyper_status import colors as c


class Status:
    """Status Print outputs date, status, and maybe a custom string."""

    def insert_items(self, warning: str, string: str) -> str:
        """Inserting colors and dates into warning string.

        Args:
            warning: string of what the warning should say
            string: description of the warning
        
        Returns:
            A string with a date, warning, and string.
        
        """
        n = datetime.datetime.now()
        s = [
            f"{c.BOLD}[{c.END} {c.DATE}{n.strftime('%b %d, %Y - %A %I:%M:%S')}{n.strftime('%p').lower()} {c.END}{c.BOLD}]{c.END}{':' if not warning else ''}",
            f'{c.BOLD}[{c.END} {warning} {c.BOLD}]{c.END}:' if warning else False,
            f'{string} '
        ]
        return ' '.join(str(y) for y in s if y)

    def _join(self, string: str) -> str:
        return ' '.join(str(y) for y in string)

    def warning_string(self, string: str) -> str:
        '''Creates a string with a custom warning
        
        Args:
            string (str): The string containing the warning.

        Returns:
            A string with custom colors.

        Raises:
            ValueError if color and/or warning cannot be found.
        
        '''
        pass

    def old_w(self, string):
        """Returns a warning string."""
        print(self.insert_items(f'{c.WARNING}Warning{c.END}', self._join(string)))

