from setuptools import setup

setup(name='pbixrefresher',
      version='0.1.3',
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
      zip_safe=False)