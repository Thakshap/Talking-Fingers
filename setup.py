import setuptools

setuptools.setup(
    name='talking-fingers',
    version='0.1.0',
    description='Python project',
    author='Sneha Ballari',
    author_email='snehasballari01@gmail.com',
    url='https://github.com/snehaballari/Talking-Fingers.git',
    packages=setuptools.find_packages(),
    setup_requires=['nltk', 'joblib','click','regex','sqlparse','setuptools'],
)