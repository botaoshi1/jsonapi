from setuptools import setup, find_packages

setup(
    name="jsonapi",
    version="0.0.1",
    description="jsonapi for assignment2 of CS5500",
    author="Botao Shi",
    author_email="shi.bot@northeastern.edu",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    url='https://github.com/botaoshi1/jsonapi'
)