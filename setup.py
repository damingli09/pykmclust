from setuptools import setup

setup(
    name='pykmclust',
    version='0.0.1',    
    description='A Python package for kmeans with custom distance metrics',
    url='https://github.com/damingli09/pykmclust',
    author='Daming Li',
    author_email='daming.li@yale.edu',    
    license='GNU GPL',
    packages=['pykmclust'],
    install_requires=['scipy',
                      'numpy',
                      ],

    classifiers=[
        'Development Status :: 1 - Planning',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: GNU General Public License',  
        'Operating System :: POSIX :: Linux',        
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
)  