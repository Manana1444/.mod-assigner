import os
import shutil

py_file = os.path.abspath(__file__)
py_dir = os.path.dirname(py_file)

mods_path = py_dir + "/mods"
destination = py_dir + "/mod-files"
folders = os.listdir(mods_path)

for mod_name in folders:
    mod_name_mod = (mod_name + ".mod")
    with open(mod_name_mod, "a") as mod_f:  # creates a .mod file for every dir in folders
        path2 = mods_path + "/" + str(mod_name)
        with open(path2 + "/descriptor.mod", "r") as desc:
            for text in desc:  # copies contents from descriptor.mod
                mod_f.write(text)  # and pastes them in mod_name.mod
            mod_f.write("\n" 'path = "mod/' + mod_name + '"')  # writes the path to the mod in your_game/mod dir
        shutil.move(mod_name_mod, os.path.join(destination, os.path.basename(mod_name_mod)))
