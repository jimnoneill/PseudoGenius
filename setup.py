from setuptools import setup, find_packages

setup(
    name="PseudoGenius",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        "biopython",
        "pandas",
        "transformers",
        "datasets",
        "numpy",
        # add any other packages you need
    ],
    # If you have scripts to be installed, list them here
    entry_points={
        'console_scripts': [
            'pseudogenius=pseudogenius.command_line:main',
        ],
    },
)
