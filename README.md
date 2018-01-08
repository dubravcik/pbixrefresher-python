Power BI refresher
======
Script for automation of refreshing Power BI workbooks.  Built on Python 3.6 and pywinauto.

Developed for Power BI Desktop 2.53.4954.621 64-bit (December 2017) on Windows 10 with English and Czech locale. Other locales should work as well but they haven't been tested.



Installation
------
Install using `pip`

```
pip install pbixrefresher
```

Usage
-----
```
pbixrefresher <WORKBOOK> [-workspace <WORKSPACE>]

where <WORKBOOK> is path to .pbix file
      <WORKSPACE> is name of online Power BI service work space to publish in. Default is My workspace
```

See how it works
-----
[![pbixrefresher](http://img.youtube.com/vi/8HSK_-1ULro/0.jpg)](https://www.youtube.com/watch?v=8HSK_-1ULro "pbixrefresher")

Bug reporting
-----
Create Github issue. Please write version of your Power BI Desktop, OS and attach command line result and screenshot.
