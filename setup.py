from distutils.core import setup

setup(
    name='qhue',
    version='1.0',
    install_requires=['requests'],
    packages=['qhue'],
    package_dir={'qhue': 'qhue'},
)
