from setuptools import setup, find_packages
from pathlib import Path

this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

setup(
    name="negative-binom",
    version="0.1.1",
    packages=find_packages(),
    install_requires=[],
    author="Kağan Özer",
    description="A binomial function that extends the domain of combinations to include negative integers.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://kaganozer.github.io/negative-binom",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
    ]
)
