#!/usr/bin/env python

from setuptools import setup
import sys

assert sys.version_info.major == 3 and sys.version_info.minor >= 6, \
    "Safety Starter Agents is designed to work with Python 3.6 and greater. " \
    + "Please install it before proceeding."

setup(
    name='safe_rl',
    packages=['safe_rl'],
    install_requires=[
        'gym~=0.15.3',
        'joblib==0.14.0',
        'matplotlib==3.1.1',
        'mpi4py==3.1.4',
        'mujoco-py<2.2,>=2.1',
        'numpy==1.23.5',
        'seaborn==0.8.1',
        'tensorflow==2.15.0',
    ],
)
