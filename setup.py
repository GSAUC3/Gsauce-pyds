from setuptools import setup,find_packages

classifiers=[
    'Operating System :: OS Independent',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 2',
    'License :: OSI Approved :: MIT License'
    
]

setup(name='Gsauce-pyds',
version='0.0.6',
description='Some useful and known data structure.',
author='Rajarshi Banerjee',
author_email='sambaner1050@outlook.com ',
license='MIT',
keywords=['python','linked list', 'singly linked list'],
classifiers=classifiers,
packages=find_packages(),
install_requires=[],

zip_safe=False)