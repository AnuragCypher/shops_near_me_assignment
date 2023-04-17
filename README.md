# shops_near_me_assignment
steps to run the application
1. your system needs to have geoDjango service available (install GDAL into your system, and set the path for couple of env variables)
  OSGeo4W installer for windows installation,
  to set env variables in windows use these commands in terminal =>>
  set OSGEO4W_ROOT=C:\OSGeo4W64,
  set GDAL_DATA=%OSGEO4W_ROOT%\share\gdal,
  set PROJ_LIB=%OSGEO4W_ROOT%\share\proj,
  set PATH=%PATH%;%OSGEO4W_ROOT%\bin,
  reg ADD "HKLM\SYSTEM\CurrentControlSet\Control\Session Manager\Environment" /v Path /t REG_EXPAND_SZ /f /d "%PATH%",
  reg ADD "HKLM\SYSTEM\CurrentControlSet\Control\Session Manager\Environment" /v GDAL_DATA /t REG_EXPAND_SZ /f /d "%GDAL_DATA%",
  reg ADD "HKLM\SYSTEM\CurrentControlSet\Control\Session Manager\Environment" /v PROJ_LIB /t REG_EXPAND_SZ /f /d "%PROJ_LIB%",
  
  (https://docs.djangoproject.com/en/4.1/ref/contrib/gis/install/) refer this link
 
2. create and activate the virtual environment
3. install requirements.txt 
4. run python manage.py migrate
5. create superuser for using django-admin pannel to manage shops DB
6. run the server python mange.py runserver
7. follow the routes to access find_shops_near_me implementation
8. you will reach the page where where yoy can give thed asked input to a form and hit search and you will get all the shops near you.
9. DB will already have shops data for thane city in maharashtra.
