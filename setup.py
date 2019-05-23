from setuptools import setup, find_packages
from os import path

from bcocr import __version__

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='bcocr',

    version=__version__,
    description='Business Card OCR',

    long_description=long_description,

    long_description_content_type='text/markdown',

    url='https://github.com/zeevosec/business-card-ocr',

    author='Shane O\'Neill',

    author_email='oneill.shane.h@gmail.com',

    classifiers=[
        'Development Status :: 3 - Alpha',

        'License :: OSI Approved :: MIT License',

        'Programming Language :: Python :: 3.5',
    ],
    packages=find_packages(exclude=['contrib', 'docs', 'tests']),  # Required
    python_requires='>=3.5',
    install_requires=['nltk']

)
