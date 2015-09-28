import os
from setuptools import setup, find_packages

setup(
    name='spectrum-python',
    version="0.0.1",
    description='spectrum-python is a Python Logging Handler for Spectrum (devspectrum.com)',
    long_description='',
    author='Frank Wiles',
    author_email='frank@revsys.com',
    url='https://github.com/SpectrumApp/spectrum-python/',
    include_package_data=True,
    packages=find_packages(),
    zip_safe=False,
    install_requires=['requests-futures==0.9.5'],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
    ],
)
