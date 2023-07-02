from setuptools import setup, find_packages

setup(
    name='ml_project',
    version='0.1',
    author="Rushikesh Surywanshi"
    author_email="rushikeshsurywanshi007@gmil.com"
    packages=find_packages(),
    install_requires=[
        'pandas',
        'scikit-learn',
        'flask',
        # Add any other dependencies required for your project
    ],
)
