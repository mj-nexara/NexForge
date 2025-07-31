# NexForge/setup.py
from setuptools import setup, find_packages

setup(
    name='nexforge',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        'click',
        'rich',
        'cryptography',
        'ipfshttpclient',
        'didkit'
    ],
    entry_points={
        'console_scripts': [
            'nexforge = core.cli:main'
        ]
    },
    author='MJ Ahmad',
    description='Ethical Python tools for the Nexara ecosystem',
)
