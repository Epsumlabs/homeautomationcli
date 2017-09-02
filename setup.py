from distutils.core import setup

setup(
    name='homeautomationcli',
    version='0.0.1_Beta',
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
    keywords = ['cli', 'homeautomation', 'IoT'],
)
