# Overview

A tiny application that allows one to intercept the arguments to executables. Useful for debugging dynamic application calls by simply replacing the target executable with this python one. 

## Building

`pipenv run pyinstaller .\printargs.py` to generate executable (and add the `-F` switch to bundle it into one file)