from setuptools import find_packages, setup

# find_packages will find all the packages with __init__.py
print(find_packages())

setup(
    name="stonks",
    version="0.0.1",
    description="""
    This package is used for stonks
    """,
    author="Milton",
    author_email="miltonwendel@outlook.com",
    install_requires=["pandas", "matplotlib", "ipynb", "python-dotenv", "requests"],
    packages=find_packages(
        exclude=("explorations", "test"), include=["backend", "frontend", "utils", "features"]
    ),
    # entry_points={"console_scripts": ["dashboard = utils.run_dashboard:run_dashboard"]},
)
