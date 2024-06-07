from setuptools import setup
setup(
    name='ical_to_gcal_sync',
    description='Basic Python script to pull events from an iCal feed and push to Google Calendar',
    long_description=open('README.md').read(),
    url='https://github.com/andrewramsay/ical_to_gcal_sync',
    author='Andrew Ramsay',
    license='MIT',
    license_files=['LICENSE.txt'],
    version='0.1',
    packages=['ical_to_gcal_sync'],
    package_dir={'ical_to_gcal_sync': '.'},
    package_data={'ical_to_gcal_sync': ['config.py.example']},
    install_requires=open('requirements.txt').readlines(),

    classifiers=[
        'Topic :: Office/Business',
        'Topic :: Office/Business :: Office Suites',
        'Topic :: Office/Business :: Scheduling',

        'License :: OSI Approved :: MIT License',

        'Operating System :: OS Independent',

        'Programming Language:: Python:: 3.7',
        'Programming Language:: Python:: 3.8',
        'Programming Language:: Python:: 3.9',
        'Programming Language:: Python:: 3.10',
        'Programming Language:: Python:: 3.11',
        'Programming Language:: Python:: 3.12',
    ]
)

