from setuptools import setup, find_packages

setup(
    name='Maksekeskus-Python',
    version='1.0.0',
    packages=find_packages(),
    url='https://github.com/Jointts/maksekeskus_python',
    license='MIT License',
    author='Joonas',
    author_email='joonaslume@gmail.com',
    description='Maksekeskus payment python integration',
    install_requires=[
        'requests'
    ]
)
