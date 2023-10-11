#!/usr/bin/env python3

from distutils.core import setup

setup(name='btl',
      version='1.0',
      description='Python Utilities for BTL QA/QC Jig',
      author='Anthony LaTorre',
      author_email='alatorre@caltech.edu',
      packages=['btl'],
      scripts=['analyze-waveforms','qaqc-gui','qaqc-client', 'integrate-waveforms']
     )
