from setuptools import setup

NAME = "sort_data"

setup(
    name=NAME,
    version="1.0.0",
    py_modules=[NAME],
    entry_points={
        "console_scripts": [
            f"{NAME}=sort_data:main",
        ],
    },
    install_requires=['tqdm']
)