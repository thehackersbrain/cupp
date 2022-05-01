from setuptools import setup, find_packages
from cupp import __version__


with open('README.md') as readme:
    long_description = readme.read().strip()


setup(
    name='cupp',
    version=__version__,
    description='Common User Password Profiler',
    author='Gaurav Raj',
    url='https://github.com/thehackersbrain/cupp',
    author_email='techw803@gmail.com',
    license='MIT',
    long_description=long_description,
    long_description_content_type='text/markdown',
    keywords=['cupp', 'common user password profiler', 'wordlist',
              'hacking', 'python', 'thehackersbrain', 'gauravraj'],
    packages=find_packages(),
    install_requires=['rich'],
    entry_points={'console_scripts': ['cupp=cupp.__main__:main']},
    zip_safe=False,
)
