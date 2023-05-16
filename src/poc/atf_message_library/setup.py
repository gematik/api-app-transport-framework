from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="atf_processor_library",
    version="0.1.0",
    author="Robert Hoffmann",
    author_email="robert.hoffmann@gematik.de",
    description="A Python library for processing and handling ATF messages in FHIR format",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/SvenSommer/POC_App_Transport_Framework",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
    ],
    python_requires=">=3.6",
    install_requires=[
        # Hier können Sie Abhängigkeiten auflisten, die für Ihre Bibliothek erforderlich sind,
        # z.B. "fhir.resources>=6.0.0,<7.0.0"
    ],
)
