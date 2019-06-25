Power BI refresher
======
Script for automation of refreshing Power BI workbooks.  Built on Python 3.6 and pywinauto.

Developed for Power BI Desktop June 2019 Update (2.70.5494.561) on Windows 10 with English locale.



Installation
------
Install using `pip`

```
pip install pbixrefresher
```

Usage
-----
```
pbixrefresher <WORKBOOK> [-workspace <WORKSPACE>] [--refresh-timeout <REFRESH_TIMEOUT>] [--no-publish]

where <WORKBOOK> is path to .pbix file
      --workspace <text> is name of online Power BI service work space to publish in (default My workspace)
      --refresh-timeout <number> is time in seconds to wait to refresh end (default 30000)
      --no-publish is switch to just refresh and save the workbook and skip publishing to online service (default False)
      --init-wait <number> is time to wait until Power BI Desktop starts (default 15)
```

Scheduling in Windows Task Scheduler
-----
Please keep in mind that this script uses GUI of Power BI Desktop and it needs that a user is logged in Windows session. You should also deactivate lock screen time. Ideally you should schedule the script on a computer where the GUI is not used to not interfere the scripting, for example dedicated Virtual Machine.

1. Open Task Scheduler
2. Click Create Basic Task
3. Fill a Name and click Next
4. Set a trigger and click Next
5. Pick Start a program as an action and click Next
6. in Program/script type absolute path to pbixrefresher.exe in your scripts folder in Python installation path (for example "C:\ProgramData\Anaconda3\Scripts\pbixrefresher.exe")

   in Arguments type file name of the workbook (for example "sample.pbix")
   
   in Start in type absolute path workbook (for example "C:\workbooks\")
7. Confirm and Finish


See how it works
-----
[![pbixrefresher](http://img.youtube.com/vi/8HSK_-1ULro/0.jpg)](https://www.youtube.com/watch?v=8HSK_-1ULro "pbixrefresher")

Bug reporting
-----
Create Github issue. Please write version of your Power BI Desktop, OS and attach command line result and screenshot.
