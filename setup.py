# -*- coding: utf-8 -*-
import os
import re
from setuptools import setup

# Get README and remove badges.
readme = open('README.rst').read()
readme = re.sub('----.*marker', '----', readme, flags=re.DOTALL)

description = 'Notas de aulas de Métodos Eletromagnéticos'

setup(
    name='Métodos Eletromagnéticos',
    description=description,
#    long_description=readme,
    author='Victor Cezar Tocantins',
    author_email='victorcezar@ufpa.br',
#  url='',
#  license='Apache License V2.0',
# packages=['empymod', 'empymod.scripts'],
#    classifiers=[
#        'Development Status :: 5 - Production/Stable',
#        'License :: OSI Approved :: Apache Software License',
#        'Programming Language :: Python :: 3.6',
#        'Programming Language :: Python :: 3.7',
#        'Programming Language :: Python :: 3.8',
#    ],
#    python_requires='>=3.6',
#    install_requires=[
#        'scipy>=1.0.0',
#        'numba>=0.44',
#    ],
#    use_scm_version={
#        'root': '.',
#        'relative_to': __file__,
#        'write_to': os.path.join('Notas de Aulas', 'version.py'),
#    },
#    setup_requires=['setuptools_scm'],
)
