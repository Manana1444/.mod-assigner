import os

py_file= os.path.abspath(__file__) # path to main.py
py_dir = os.path.dirname(py_file) # path to the parent dir of main.py

mod_path = py_dir + "/mods"
folders = os.listdir(mod_path)

print(folders)
for mod_name in folders:
    with open(mod_name + ".mod" , "a") as f:
        path2 = mod_path + "/" +  str(mod_name)
        with open(path2 + "/" +"descriptor.mod", "r") as f1:
            for text in f1:
                f.write(text)
            f.write("\n" 'path = "mod/' + mod_name + '"')