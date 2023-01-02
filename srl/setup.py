from distutils.core import setup, Extension
from Cython.Build import cythonize
import numpy

package = Extension('calgorithm', ['E:\emnlp20_depsrl\srl\calgorithm.pyx'], include_dirs=[numpy.get_include()])
setup(ext_modules=cythonize([package]))