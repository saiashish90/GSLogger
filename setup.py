from setuptools import find_packages, setup

setup(
    name="GLogger",
    packages=find_packages(include=["lib"]),
    version="0.1.0",
    description="Grafana and slack logger library",
    author="Sai Ashish",
    license="MIT",
)
