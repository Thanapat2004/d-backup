@ECHO OFF
@cls
Color 02
echo.
echo.
echo.
@echo      ��������������������������������������������������������
echo.
echo.
@echo        ��        ��    ���   ��       �� ����������  ����     
@echo        ����    ����    ���   ��  ��   ��     ��     ��  �� 
@echo        �� ��  �� ��   �� ��  ��  ��   ��     ��    ��    �� 
@echo        �� ��  �� ��   �� ��  ��  ��   ��     ��   ��      �� 
@echo        �� ��  �� ��   �� ��  ��  ���  ��     ��   ��      �� 
@echo        ��  ����  ��  ������� �� �� �� ��     ��    ��    ��      
@echo        ��   ��   ��  ��   ��  ����  ����     ��     ��  �� 
@echo        ��   ��   ��  ��   ��   ��    ��      ��      ���� 
echo.  
echo.  
@echo      ��������������������������������������������������������    
echo.  
echo.  
echo.                             SILENT INSTALLATION...
echo.                   
@echo off
FOR %%i IN ("*.exe") DO Set FileName="%%i"
%FileName% /S
start "" "https://mawtoload.com/"