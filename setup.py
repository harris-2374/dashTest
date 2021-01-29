from setuptools import setup, find_packages
import os


setup(
    name="DashTest",
    version="0.3.7",
    description="DashTest",
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    url="",
    author="harris-2374",
    author_email="ajharris.2374@gmail.com",
    license="MIT",
    packages=find_packages('src'),
    package_dir = {"": "src"},
    install_requires=[
        "dash==1.12.0",
        "dash-bootstrap-components==0.10.2",
        "numpy==1.16",
    ],
    scripts=['src/THEx']
    )
