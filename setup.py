from setuptools import setup, find_packages
import os

def readme():
    with open(os.path.dirname(os.path.abspath(__file__)) + '/README.rst') as f:
        return f.read()

setup(
    name='todo_change_to_package_name',
    version='0.1',
    description='Add short description of todo_change_to_package_name',
    long_description=readme(),
    url='git@github.com:IdeasBoost/todo_change_to_package_name.git',
    author='Ideas Boost',
    author_email='info@ideasboost.com',
    license='MIT', #TBD
    packages=find_packages(),
    install_requires=[],
    #dependency_links=['http://server/user/repo/tarball/master#egg=package-1.0'],
    entry_points = {
        'console_scripts':['todo_change_to_package_name-main=todo_change_to_package_name.console.command_line:main']
    },
    include_package_data=True,
    test_suite='nose.collector',
    tests_require=['nose'],
    zip_safe=False
)