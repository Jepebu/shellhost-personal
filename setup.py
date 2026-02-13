import configparser

# --- WORKAROUND FOR PYTHON 3.12+ ---
# Restore SafeConfigParser (which was removed) as an alias for ConfigParser
if not hasattr(configparser, 'SafeConfigParser'):
    configparser.SafeConfigParser = configparser.ConfigParser
# -----------------------------------

from setuptools import setup, find_packages, Extension
import sys

extra_compile_args = []
if sys.platform != "win32":
    extra_compile_args = ["-fPIC", "-Wall"]

module_c = Extension(
    'shellparser',
    sources=['src/shellparser.c']
)

setup(
    name="pyshell",
    version="1.0",
    ext_modules=[module_c],
    description="Turn Python functions into interactive shell commands.",
    long_description="Provides an isolated interactive shell environment that you can import Python functions into as shell commands.",
    author="M. Bragg",
    author_email="mbragg@spear.ai",
    url="...",
    license="...",
    packages=find_packages(),
)
