from distutils.core import setup, Extension
from Cython.Build import cythonize

exts=(cythonize("cy_planeta.pyx"))

setup(ext_modules=exts)
