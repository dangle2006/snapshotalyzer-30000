from setuptools import setup

setup(
    name='snapshotalyzer-3000',
    version='1.01',
    author="Danno",
    author_email="danno@email.com",
    description="Snapshotter 3000 is a test tool",
    license="GPLv3+",
    packages=['shotty'],
    url="https://github.com/dangle2006/snapshotalyzer-30000",
    install_requires=[
        'click',
        'boto3'
    ],
    entry_points='''
        [console_scripts]
        shotty=shotty.shotty:cli
    ''',
)
