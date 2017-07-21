#!/usr/bin/python

import os, stat
from subprocess import call
from shutil import copyfile

def main():
    app_name = "testApp"
    create_folder_structure(app_name)
    package_location = create_package(app_name)
    print "Generated package at " + package_location

def create_folder_structure(app_name):
    staging_path = "./staging/"+app_name
    debian_path = staging_path+"/DEBIAN/"
    install_path = staging_path+"/opt/"+app_name+"/"
    make_path(install_path)
    make_path(debian_path)
    copyfile("./sandbox/"+app_name, install_path+app_name)
    copyfile("./ext/control",debian_path+"control")
    os.chmod(install_path+app_name, 
             stat.S_IRUSR | stat.S_IWUSR | stat.S_IXUSR | stat.S_IROTH | stat.S_IXOTH)

def create_package(app_name):
    os.chdir("./staging")
    call(["dpkg-deb","--build",app_name])
    output = os.getcwd()+"/"+app_name+".deb"
    return output

def make_path(path):
    try: 
        os.makedirs(path)
    except OSError:
        if not os.path.isdir(path):
            raise

if __name__ == "__main__":
    main()
