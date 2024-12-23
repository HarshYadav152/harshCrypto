from setuptools import setup, find_packages

setup(
    name="harshCrypto",  # Replace with your desired package name
    version="1.0.0",  # Start with 0.1.0, increment as needed
    author="Harsh Yadav",
    author_email="harshlms.dev@gmail.com",
    description="A simple module for file encryption and decryption of the file",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/Geeta-Tech/windows-files-locker",  # Link to your project repository
    packages=find_packages(),  # Automatically find package folders
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
    install_requires=[
        "cryptography>=3.0",  # Dependencies for your project
    ],
)
