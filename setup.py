from setuptools import setup

setup(name='pickler-magic',
      version='1.0',
      author='Dmitry Lunin',
      packages=['pickler'],
      requires=['IPython'],
      description='IPython Notebook magic to make and load pickle dumps of all assignments in a cell or a line',
      url='https://github.com/DLunin/pickler',
      download_url='https://github.com/DLunin/pickler/archive/1.0.tar.gz')
