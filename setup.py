from distutils.core import setup

setup(
    name='jarmanifestreader',  # How you named your package folder (MyLib)
    packages=['jarmanifestreader'],  # Chose the same as "name"
    version='0.1.1',  # Start with a small number and increase it with every change you make
    license='MIT',  # Chose a license from here: https://help.github.com/articles/licensing-a-repository
    description='Returns the contents of the manifest file of a given jar file in the dictionary format',
    # Give a short description about your library
    author='BADARI NARAYANA',  # Type in your name
    author_email='badari412@gmail.com',  # Type in your E-Mail
    url='https://github.com/badari412/jarmanifestreader',  # Provide either the link to your github or to your website
    download_url='https://github.com/badari412/jarmanifestreader/archive/v0.1.1.tar.gz',  # I explain this later on
    keywords=['PYTHON', 'JAR', 'MANIFEST', 'MANIFESTREADER', 'READER'],  # Keywords that define your package best

    classifiers=[
        'Development Status :: 5 - Production/Stable',
        # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
        'Intended Audience :: Developers',  # Define that your audience are developers
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',  # Again, pick a license
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',  # Specify which python versions that you want to support
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
)
