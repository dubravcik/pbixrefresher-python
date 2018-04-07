from setuptools import setup

setup(name='pbixrefresher',
      version='0.1.4',
      description='Script for refreshing and publishing Power BI workbooks',
      url='https://github.com/dubravcik/pbixrefresher-python',
      author='Michal Dubravcik',
      author_email='michal.dubravcik@gmail.com',
      license='MIT',
      packages=['pbixrefresher'],
      install_requires=[
          'pywinauto',
          'psutil'
      ],
      scripts=['pbixrefresher/pbixrefresher.py'],
	  entry_points = {
        "console_scripts": ['pbixrefresher = pbixrefresher:main']
        },
      zip_safe=False)