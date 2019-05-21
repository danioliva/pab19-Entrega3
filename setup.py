from setuptools import setup, find_packages

setup(
    name='pyUnitTestingExamples',
    version='1.0.0',
    description='Class Factorial And Store With Mockito',
    author='Daniel Oliva González',
    author_email='daniolivasek10@gmail.com',
    maintainer='Daniel Oliva González',
    maintainer_email='daniolivasek10@gmail.com',
    license='MIT',
    url='https://github.com/danioliva/pab19-Entrega3.git',
    long_description=open('README.md').read(),
    packages=find_packages(exclude=["test.*", "tests"]),
    python_requires='>=3',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: MIT License',
        'Topic :: Scientific/Engineering :: Artificial Intelligence',
        'Programming Language :: Python :: 3.6'
    ],
    install_requires=[
        'click'
    ]
)