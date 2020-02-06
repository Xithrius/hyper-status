<h1 align="center">hyper-status</h1>

<h3 align="center">A status indicator that you can modify.</h3>

<p align="center">
    <img src="https://img.shields.io/apm/l/vim-mode.svg"/>
    <img src="https://img.shields.io/badge/python-3.8.0-green.svg">
</p>

<p align="center">
    <a href="#examples">examples</a> -
    <a href="#changelog">Changelog</a>
</p>


# Examples
```python
# Custom print example
Status('warning', 'This is a test warning. Be warned!')
Status('fail', 'Oh no, something has totally failed!')
Status('ready', 'This is fine. Everything is fine.')
```
<p align="left">
    <img src="/images/examples/custom.png"/>
</p>

```python
# Simple catch error example
@Status.catch_error
def main():
    x = int('a')

main()
```
<p align="left">
    <img src="/images/examples/error.png"/>
</p>


# Changelog

## [v0.2](!https://github.com/Xithrius/Xythrion/releases/tag/v0.2):
#### Added:
- Wrapper that now catches any incorrect indexes of colors.
- If status file is called, then there will be some examples of what you can get out of the status.
#### Changed:
- Comments for readability.
- Colors within the timestamps. 
- Different formatting for the change log.
#### Removed:
- 0s before times in timestamps.

## [v0.1](!https://github.com/Xithrius/Xythrion/releases/tag/v0.1):
#### Added:
- Files imported from [Xythrion](!https://github.com/Xithrius/Xythrion).
#### Changed:
- How the comments are formatted.
#### Removed:
- Useless classmethods that didn't do anything useful.
