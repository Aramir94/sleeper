from setuptools import setup, find_packages

setup(
    name='sleeper',
    version='0.1',
    packages=find_packages(),
    description='A simple Python library for random sleep times based on normal distribution',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='data_jeong',
    author_email='jhs941222@naver.com',
    url='https://github.com/Aramir94/sleeper',
    license='Apache',
    install_requires=[
        'random',
        'time'
    ]
)