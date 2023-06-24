from setuptools import setup, find_namespace_packages

setup(
    name='bot_assistant',
    version='1.0',
    description='This is a bot-assistant.Bot implemented as a console application.',
    url='https://github.com/NikYurchik/Team-Project',
    author='GoIT Python13 Team2 "Slytherin"',
    author_email='afanasievmaksym2@gmail.com',
    license='UA',
    packages=find_namespace_packages(),
    entry_points={'console_scripts': ['bot = bot_assistant.run:main']}
)