from setuptools import setup

setup(
    name="solution",
    version="1.0.0",
    py_modules=["edit_prepared_data", "sort_data"],
    entry_points={
        "console_scripts": [
            "edit_prepared_data=edit_prepared_data:main",
            "sort_data=sort_data:main",
        ],
    },
    install_requires=["tqdm"]
)
