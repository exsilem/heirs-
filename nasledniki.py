all_class_family = {}
parent = []

def input_family():
    buff=input()
    if len(buff)>1:
        child, parent = input().split(':', ' ')
        #parent = parent.split()
        add_family(child,parent)
    else:
        add_family(buff, None)

def add_family(child, parent):
    all_class_family[child] = parent
    print(all_class_family)

def search_family(parent, child):
    for k in all_class_family.keys():
        if k == child:
            parent_class.add(all_class_family[k])
            print(parent_class)
    if parent in parent_class:
        print('Yes')
    elif len(parent_class) == 0:
        print('No')
    else:
        serch_in_set(parent_class, parent)

def serch_in_set(set_class, parent):
    lenght = len(set_class)
    for i in set_class:
        for k in all_class_family.keys():
            if k == i:
                set_class.add(all_class_family[k])
                print(set_class)
    if parent in set_class:
        print('Yes')
    elif lenght == len(set_class):
        print('No')
    else:
        serch_in_set(parent_class, parent)
        

n = int(input())
for i in range(n):
    input_family()

n = int(input())
for i in range(n):
    parent, child = input().split()
    parent_class = set()
    search_family(parent, child)
    

