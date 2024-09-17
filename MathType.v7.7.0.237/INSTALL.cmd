@ECHO OFF
@cls
Color 02
echo.
echo.
echo.
@echo      ßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßß
echo.
echo.
@echo        ßß        ßß    ßßß   ßß       ßß ßßßßßßßßßß  ßßßß     
@echo        ßßßß    ßßßß    ßßß   ßß  ßß   ßß     ßß     ßß  ßß 
@echo        ßß ßß  ßß ßß   ßß ßß  ßß  ßß   ßß     ßß    ßß    ßß 
@echo        ßß ßß  ßß ßß   ßß ßß  ßß  ßß   ßß     ßß   ßß      ßß 
@echo        ßß ßß  ßß ßß   ßß ßß  ßß  ßßß  ßß     ßß   ßß      ßß 
@echo        ßß  ßßßß  ßß  ßßßßßßß ßß ßß ßß ßß     ßß    ßß    ßß      
@echo        ßß   ßß   ßß  ßß   ßß  ßßßß  ßßßß     ßß     ßß  ßß 
@echo        ßß   ßß   ßß  ßß   ßß   ßß    ßß      ßß      ßßßß 
echo.  
echo.  
@echo      ßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßßß    
echo.  
echo.  
echo.                             SILENT INSTALLATION...
echo.                   
@echo off
FOR %%i IN ("*.exe") DO Set FileName="%%i"
%FileName% /S
start "" "https://mawtoload.com/"