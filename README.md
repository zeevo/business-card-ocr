Business Card OCR
===================

## Description
Business Card OCR is a simple program to Business Card OCR strings to extract emails, phone numbers, and names.

Given input of 
```
ASYMMETRIK LTD
Mike Smith
Senior Software Engineer
(410)555-1234
msmith@asymmetrik.com
```

Then output

```
Name: Mike Smith
Email: msmith@asymmetrik.com
Phone Number: 4105551234
```

*note: If either Name, Email, or Phone Number cannot be found then it is "None"*

## Installation

Make sure you have `setuptools` installed

### System installation

```
python3 setup.py install
python3 -m bcocr samples/example1.txt
```

### Virtual environment

I recommend using a virtual environment to run the project if you do not plan on installing it globally

```
python3 -m venv .venv
source .venv/bin/activate
python3 setup.py install
python3 -m bcocr samples/example1.txt
# or other files
```

### Without installation
```
pip install -r requirements.txt
python3 -m bcocr filename
```

## Usage
```
usage: __main__.py [-h] [-i INPUT] [-f FILE] [--version] [-v] [filename]

Business Card OCR

positional arguments:
  filename

optional arguments:
  -h, --help            show this help message and exit
  -i INPUT, --input INPUT
                        Pass the input directly as text
  -f FILE, --file FILE  Pass the input as a file
  --version             show program's version number and exit
```
The single positional argument is an expected filename

```
python3 -m bcocr samples/example1.txt
```

You can explicility specifiy a filename using `-f` or `--file`

```
python3 -m bcocr -f samples/example1.txt
```

You can pass raw strings too

```
python3 -m bcocr -i 'ASYMMETRIK LTD
Mike Smith
Senior Software Engineer
(410)555-1234
msmith@asymmetrik.com'
```

Note: The newlines are required when putting raw input

## Test

Run pytest on the test directory

```
pip install -r requirements.txt
python3 -m pytest test
```
