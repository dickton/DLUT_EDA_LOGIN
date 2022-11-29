@echo off
if "%1" == "h" goto begin
mshta vbscript:createobject("wscript.shell").run("""%~0"" h",0)(window.close)&&exit
:begin
python \DLUT_EDA_LOGIN\login.py #Modify your own python script path here

pause