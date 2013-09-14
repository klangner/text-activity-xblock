'''
Created on 14-09-2013

@author: Krzysztof Langner
'''
from setuptools import setup

setup(
    name='text-activity-xblock',
    version='0.1',
    description='Text activity',
    py_modules=['textactivity'],
    install_requires=['XBlock'],
    entry_points={
        'xblock.v1': [
            'textactivity = textactivity:TextActivityBlock',
        ]
    }
)