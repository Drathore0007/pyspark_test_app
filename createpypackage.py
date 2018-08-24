import os 
import shutil
import sys

def createpypackage( project, path='./',):
    
    if os.path.exists(path+project):
        shutil.rmtree(path+project)
        
    os.mkdir(path+project)
    os.mkdir(path+project+'/'+project)
    os.mknod(path+project+'/'+ '.python-version')
    os.mknod(path+project+ '/'+'requirement.py')
    os.mknod(path+project+'/' +'setup.py')

    os.mkdir(path+project+'/'+"test")
    os.mknod(path+project+'/'+project +'/'+'__init__.py')

if len(sys.argv) == 3:
    dir_path = sys.argv[1]
    project_name = sys.argv[2]
    createpypackage(project_name, path= dir_path)
else:
    project_name = sys.argv[1]
    createpypackage(project_name)

