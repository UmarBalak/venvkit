from setuptools import setup

setup(
    name= "venvkit",
    version="0.1",
    py_modules=["venvkit"],
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    install_requires=[],
    entry_points={
        "console_scripts": [
            "vk=venvkit:venvkit_run",
        ]
    },
    classifiers=[
        'Intended Audience :: Developers',
    ],
)
