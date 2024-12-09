
import os

def go_to_cwd(script_path):
    """This function sets the cwd for running the script commands,
     It can be useful while changing environments to access relative paths
     The current working directory will be same where Main.py file is placed"""
    script_dir = os.path.dirname(script_path)
    os.chdir(script_dir)
    print(f"current_working_Directory is set to be -> {script_dir}")


def mv(source_path,target_path):
    import shutil
    """This function take source and target path as input and moves the file on target path"""
    shutil.move(source_path,target_path)
    print(f"source file -> {source_path}, has been copied to target path -> {target_path} ")

