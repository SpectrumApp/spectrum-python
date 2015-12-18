import os
from setuptools import setup, find_packages

f = open(os.path.join(os.path.dirname(__file__), 'README.rst'))
readme = f.read()
f.close()

setup(
    name='spectrum-python',
    version="0.9.6",
    description='spectrum-python is a Python Logging Handler for Spectrum (devspectrum.com)',
    long_description=readme,
    author='Frank Wiles',
    author_email='frank@revsys.com',
    url='https://github.com/SpectrumApp/spectrum-python/',
    include_package_data=True,
    packages=find_packages(),
    zip_safe=False,
    install_requires=['requests-futures==0.9.5', "autobahn[asyncio]"],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
        'Topic :: System :: Logging',
    ],
)
