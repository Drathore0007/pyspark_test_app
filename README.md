# Pyspark Test APP 
This GIT repo is about how to build a basic Pyspark Application and creating proper structure for it.

#### Creating a APP structure with python script (createpypackage.py)
* To create a pyspark package structure use below command
$ *python createpypackage.py project_name PATH(storing_directory_path_where_you_want_create_project)*


or if you are allready in same directory where you want to create you project than no need of giving path sys argument.

when you create a new project with this script, you will get a folder with project name inside the path you have give with below file in it.
* project (folder where all you  code resides)
    * __init__.py
* setup.py (file required to create a egg package)
* requirement.txt (detail  of required module in you project)
* test (all you test case code)



####  Create EGG file from package

* To create you app or to create EGG file use below command in you project folder.  
  $ *python setup.py bdist_egg* 

you need to be in you app directory to build your app with python. this command will create a folder name Dist in you project directory and egg_file_package will be inside that folder.


#### submiting application

./spark-submit --jars jar1.jar,jar2.jar --py-files path/to/my/egg.egg driver.py arg1 arg2

spark-submit --py-files file:///home/dharm/Documents/Doofenshmirtz_Evil_corp_Develpoment/GitHub/pyspark_test/dist/testapp-0.0.1-py3.6.egg wordcount.py 