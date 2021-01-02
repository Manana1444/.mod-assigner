import os
import shutil

py_file = os.path.abspath(__file__)
py_dir = os.path.dirname(py_file)

mods_path = py_dir + "/mods"
folders = os.listdir(mods_path)

for mod_name in folders:
    with open(mod_name + ".mod", "a") as mod_f:  # creates a .mod file for every dir in folders
        path2 = mods_path + "/" + str(mod_name)
        with open(path2 + "/descriptor.mod", "r") as desc:
            for text in desc:  # copies contents from descriptor.mod
                mod_f.write(text)  # and pastes them in mod_name.mod
            mod_f.write("\n" 'path = "mod/' + mod_name + '"')  # writes the path to the mod in your_game/mod dir
        shutil.move(mod_name + ".mod", py_dir + "/mod-files")
