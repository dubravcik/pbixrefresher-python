Power BI refresher
======
Script for automation of refreshing Power BI workbooks built with pywinauto.

Developed for Power BI Desktop 2.52.4921.682 64-bit (november 2017) on Windows 10 with English and Czech locale. Other locales should work as well but they haven't been tested.



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


Bug reporting
-----
Create Github issue. Please write version of your Power BI Desktop, OS and attach command line result and screenshot.