from setuptools import setup, find_packages

setup(
    name='jsonapi',
    version='1.0',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    author='Yuxuan Ren',
    author_email='ren.yuxu@northeastern.edu',
    description='A Python package for custom JSON encoding and decoding.',
    install_requires=[],
)