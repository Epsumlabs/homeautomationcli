from distutils.core import setup

long_description='''
	This project is a command line utility tool, complimented with Epsumlabs Open Source IoT platform project.
'''
setup(
    name='homeautomationcli',
    version='0.0.2',
    packages=['homeautomationcli'],
    url='https://github.com/Epsumlabs/homeautomationcli',
    license='MIT',
    author='saiprasad',
    entry_points = {'console_scripts':['homeautomationcli=homeautomationcli.command_line:main'],},
    scripts=['homeautomationcli/commandline.py'],
    author_email='saiprasad1996@hotmail.com',
    install_requires=[
          'pycrypto',
          'requests'
      ],
    description='Epsum Labs Home Automation CLI',
    long_description=long_description,
    keywords = ['cli', 'homeautomation', 'IoT'],
    classifiers=(
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.5'
    )
)
