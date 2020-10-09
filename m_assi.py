from os import listdir

path = "D:\Documents\Paradox Interactive\Crusader Kings III\.mod assigner\mods"
folders = listdir(path)
y = "\ "
x = y.strip()

print(folders)
for mod_name in folders:
    with open(mod_name + ".mod" , "a") as f:
        path2 = "D:\Documents\Paradox Interactive\Crusader Kings III\.mod assigner\mods" + x +  str(mod_name)
        with open(path2 + x +"descriptor.mod", "r") as f1:
            for text in f1:
                f.write(text)
            f.write("\n" 'path = "mod/' + mod_name + '"')