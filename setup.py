from setuptools import setup
  
setup(
    name='awk3',
    version='0.1',
    description='A simple text processor for lazy programmers',
    author='nicoloridulfo',
    packages=['awk3'],
    install_requires=['fire'],
    entry_points={
        'console_scripts': [
            'awk3 = awk3:main'
        ]
    }
)
