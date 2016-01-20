import os


name_of_main_file = "inż"
path_to_tex_files = "../tex"

list_of_words = ["a", "i", "o", "u", "w", "z", "ze", "od", "do", "że", "iż",
                 "poprzez", "spod", "sponad", "znad", "po", "za", "nad", "pod", "na",
                 "oraz", "ale", "lub", "albo", "bądź", "czy", "by", "aby", "jak", "ponieważ", "bo",
                 "który", "która", "które", "którego", "krótemu", "której", "którym"]
uppercased = [word.title() for word in list_of_words]
list_of_words += uppercased

for file in filter(lambda x: x.endswith(".tex"), os.listdir(path_to_tex_files)):
    if not file.startswith(name_of_main_file):
        print("fixing: " + file)
        with open(os.path.join(path_to_tex_files, file), encoding='utf-8') as f:
            lines = f.readlines()
        with open(os.path.join(path_to_tex_files, file), encoding='utf-8', mode="w") as out:
            for line in lines:
                if not (line.startswith("\\") or line.startswith("%")):
                    for word in list_of_words:
                        line = line.replace(" " + word + " ", " " + word + "~")
                        if line.startswith(word + " "):
                            line = line.replace(word + " ", word + "~", 1)
                out.write(line)
