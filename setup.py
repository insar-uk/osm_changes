from setuptools import setup, find_packages

setup(
    name="osm_changes",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        "pytest",
        "coverage",
        "numpy",
        "requests",
        "requests_mock",
        "matplotlib",
        "rasterio",
    ],
    include_package_data=True,
    package_data={"osm_changes": ["config/*", "config.json"]},
    test_suite="tests",
)
