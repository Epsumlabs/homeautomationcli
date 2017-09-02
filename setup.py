from distutils.core import setup

setup(
    name='homeautomationcli',
    version='0.0.1',
    packages=['homeautomationcli'],
    url='',
    license='MIT',
    author='saiprasad',
    entry_points = {'console_scripts':['homeautomationcli=homeautomationcli.command_line:main'],},
    scripts=['homeautomationcli/commandline.py'],
    author_email='saiprasad1996@hotmail.com',
    install_requires=[
          'pycrypto',
          'requests'
      ],
    description='Epsum Labs Home Automation CLI'
)
