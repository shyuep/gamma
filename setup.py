#!/usr/bin/env python

from setuptools import setup, find_packages
import os

module_dir = os.path.dirname(os.path.abspath(__file__))

if __name__ == "__main__":
    setup(
        name='gamma',
        version='0.0.1',
        description='gamma',
        long_description=open(os.path.join(module_dir, 'README.md')).read(),
        url='https://github.com/computron/mqm',
        author='Shyue Ping Ong',
        author_email='shyuep@gmail.com',
        license='BSD',
        packages=find_packages(),
        package_data={},
        zip_safe=False,
        install_requires=['monty>=0.8.0', 'numpy', 'pandas', 'requests'],
        extras_require={},
        classifiers=['Programming Language :: Python :: 2.7',
                     'Development Status :: 4 - Beta',
                     'Operating System :: OS Independent'],
        test_suite='nose.collector',
        tests_require=['nose'],
        # entry_points={
        #     'console_scripts': [
        #     ]
        # }
    )
