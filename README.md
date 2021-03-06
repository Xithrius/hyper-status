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
Status('This is a test warning. Be warned!', 'warn')
Status('Oh no, something has totally failed!', 'fail')
Status('This is fine. Everything is fine.', 'ok')
Status('Something happened.')
Status()
```
<p align="left">
    <img src="/images/custom.png"/>
</p>


# Changelog

## [v1.3](!https://github.com/Xithrius/Xythrion/releases/tag/v1.3):
#### Changed:
- Put 0's back for now in timestamps so all statuses are aligned.

## [v1.2](!https://github.com/Xithrius/Xythrion/releases/tag/v1.2):
#### Changed:
- Fixed bug where time wouldn't change after Status is called multiple times.

## [v1.1](!https://github.com/Xithrius/Xythrion/releases/tag/v1.1):
#### Changed:
- The way this package is imported. From `from hyper_status.status import Status` to `from hyper_status import Status`

## [v1.0](!https://github.com/Xithrius/Xythrion/releases/tag/v1.0):
#### Added:
- Ability to change colors just by editing the module's color dictionary after importing.
- You don't need to put anything at all in the Status, and it will print just the date.
#### Changed:
- Amounts of colors, and the statuses that go with them. 
- Where the status is placed. The warning string is now the first priority.
#### Removed:
- Wrapper for catching errors, since a person should know how to catch errors and then use this package.

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
