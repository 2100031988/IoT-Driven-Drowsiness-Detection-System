"""Setup script for installing dependencies"""
from setuptools import setup, find_packages

setup(
    name="drowsiness_detection",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        'opencv-python>=4.8.1',
        'numpy>=1.26.2',
        'dlib>=19.24.2',
        'imutils>=0.5.4',
        'scipy>=1.11.4',
    ],
    python_requires='>=3.8',
)