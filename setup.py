from setuptools import setup, find_packages
import pathlib

HERE = pathlib.Path(__file__).parent

README = (HERE/"Readme.md").read_text()

classifiers = [
    'Operating System :: OS Independent',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 2',
    'License :: OSI Approved :: MIT License'

]

setup(name='Gsauce-pyds',
      version='1.0.0',
      description='Some useful and known data structure.',
      long_description=README,
      long_description_content_type='text/markdown',
      url='https://github.com/GSAUC3/Gsauce-pyds',
      author='Rajarshi Banerjee',
      author_email='sambaner1050@outlook.com ',
      license='MIT',
      keywords=['python', 'linked list', 'singly linked list','Binary Search Tree','Binary Tree'],
      classifiers=classifiers,
      packages=find_packages(),
      install_requires=[],

      zip_safe=False)
