import configparser

from setuptools import setup, find_packages

version = configparser.ConfigParser()
version.read('VERSION')

install_requires = [
    'numpy>=1.15',
    'pandas>=0.23.4',
    'certifi>=2018.10.15',
    'mkl-fft>=1.0.10',
    'mkl-random>=1.0.2',
    'psutil>=5.4.8',
    'python-dateutil>=2.7.5',
    'pytz>=2018.7',
    'six>=1.12.0'
]
tests_require = [
    'unittest'
]

scripts = [
    'bin/multi_run.py'
]

setup(
    name='Animal-Courier',
    version=version.get('latest', 'version'),
    packages=find_packages(exclude=['tests']),
    url='https://github.com/dota2-BioTools/Animal-Courier',
    project_urls={
        "issues": "https://github.com/dota2-BioTools/Animal-Courier/issues",
        "releases": "https://github.com/dota2-BioTools/Animal-Courier/releases",
    },
    license='MIT License',
    author='chenyuelong',
    author_email='yuelong_chen@yahoo.com',
    description='''
    This is just a test package for learn something about 'How to create a python package'
    ''',
    exclude_package_date={
        'Animal-Courier': ['.gitignore', '.circleci/*'],
    },
    install_requires=install_requires,
    scripts=scripts,

)
