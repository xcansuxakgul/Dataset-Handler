from setuptools import setup, find_packages

setup(
    name="dataset_handler",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        "Pillow",
        "pandas",
        "scikit-learn",
    ],
    description="A dataset handling library",
    author="Emine Cansu Akgül",
    author_email="eminecansuakgul@gmail.com",
    url="",
)