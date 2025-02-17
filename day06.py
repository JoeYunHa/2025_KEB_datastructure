students = []

try:
    file = input("file name : ")
    fp = open(file,'r')
    readme_list = fp.readlines()
    rls = readme_list[0].split(' ')
    print(readme_list)
    print(rls)
    fp.close()
except FileNotFoundError as err :
    print(f"{file} does not exist . {err}")
