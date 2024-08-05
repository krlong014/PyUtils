import setuptools

setuptools.setup(
    name="PyUtils", # Replace with your own username
    version="0.1",
    author="Katharine Long",
    author_email="katharine.long@ttu.edu",
    description="Simple development utilities",
    long_description="Profilers, Loggers, Tabbers, etc",
    long_description_content_type="text/markdown",
    url="https://github.com/krlong014/PyUtils",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: LGPL License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.8',
)
