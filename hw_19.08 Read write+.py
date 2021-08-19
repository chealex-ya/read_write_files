import os

file_path1 = os.path.join(os.getcwd(), "1.txt")
file_path2 = os.path.join(os.getcwd(), "2.txt")
file_path3 = os.path.join(os.getcwd(), "3.txt")
file_path123 = os.path.join(os.getcwd(), "123.txt")


def len_count(file_path):
    with open (file_path) as file:
        counter = 0
        for line in file:
            counter += 1
        return(counter)

def name(file_path):
    with open(file_path) as file:
        name = file_path.split('/')[-1]
        return(name)

def data(file_path):
    with open(file_path) as file:
        data = file.readlines()
        return(data)

doc_dict = {}
def create_dict(file_path):
    flen = len_count(file_path)
    doc_dict[file_path] = [flen]

create_dict(file_path1)
create_dict(file_path2)
create_dict(file_path3)

sorted_doc = dict(sorted(doc_dict.items(), key=lambda element: element[1]))

for k, v in sorted_doc.items():
    with open(file_path123, "a") as file:
        file.write(str(k.split('/')[-1]) + "\n" + str(v) + "\n" + str(data(k)) + "\n" + "\n")