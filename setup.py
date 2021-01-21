from setuptools import setup

setup(
    name='rzp_ocr',
    packages=['rzp_ocr'],
    include_package_data=True,
    install_requires=['flask', 'boto3'],
)