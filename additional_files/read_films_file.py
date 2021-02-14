from collections import OrderedDict


def read_to_location2():
    path = "test_file.list"

    def read_films(path):
        for line in open(path, "r"):
            yield line

    films = list(read_films(path))

    with open("location2.list", "w") as new_list:
        for ln in films:
            line = ln.split("\t")
            my_final_list = list(OrderedDict.fromkeys(line))
            line = "\t".join(my_final_list)
            new_list.write(f"{line}")



path = "location5.list"

def read_films(path):
    for line in open(path, "r"):
        yield line

films = list(set((read_films(path))))

with open("location6.list", "w") as new_films_list:
    for i in films:
        new_films_list.write(i)
        #     new_films_list.write("\t".join(new_line))



# with open("location4.list", "w") as new_films_list:

#     for i in films:
#         line = i.split("\t")
#         line[0] = "\t".join(line[0].split('('))

#         new_films_list.write("\t".join(line))
    

# with open("test_file.list", "w") as new_films_list:
#     for line in films:
