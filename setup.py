import os
import sys
import torch
from setuptools import setup, find_packages
from torch.utils.ffi import create_extension

this_file = os.path.abspath(__file__)

sources = ['src/transducer.c']
headers = ['src/transducer.h']

args = ["-std=c99"]
if sys.platform == "darwin":
    args += ["-DAPPLE"]
else:
    args += ["-fopenmp"]

ffi = create_extension(
    name="transducer._ext.transducer",
    package=True,
    headers=headers,
    sources=sources,
    extra_compile_args=args
)
ffi = ffi.distutils_extension()

setup(
    name="transducer",
    version="1.0",
    description="A Fast Sequence Transducer Implementation with PyTorch Bindings",
    url="https://github.com/awni/transducer",
    author="Awni Hannun",
    license="Apache",
    packages=find_packages(),
    py_modules=['decoders'],
    ext_modules=[ffi],
)
