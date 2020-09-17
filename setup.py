from setuptools import setup, find_packages
import pathlib

here = pathlib.Path(__file__).parent.resolve()
long_description = (here / 'README.md').read_text(encoding='utf-8')

setup(
    name="linear_prog",
    version="1.0.0",
    description='A project for solving linear programming problem',
    author='Ashish Kumar',
    packages=find_packages(where='src'),
    )
 #"Django >= 1.1.1",
 #"pytest",
