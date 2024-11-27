from setuptools import setup, find_packages

setup(
    name="kaiascan-sdk-py",
    packages=find_packages(where="src", exclude=["tests*"]),
    install_requires=[
        "requests>=2.25.1",
    ],
)
