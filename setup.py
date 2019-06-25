from setuptools import setup

setup(name='pbixrefresher',
      version='0.1.8',
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
	  entry_points = {
        "console_scripts": ['pbixrefresher = pbixrefresher.pbixrefresher:main']
        },
      zip_safe=False)