#def convert_file_to_list(text_file):
#   file_open = open(text_file)
#   file_list = file_open.readlines()
#   file_open.close()
#   return file_list 
# more concise code below

def convert_file_to_list(text_file):
    with open (text_file) as file_open:
        file_list = file_open.readlines()
    return file_list

list_sandi = convert_file_to_list("sandi_fav_foods.txt")
list_katherine = convert_file_to_list("katherine_fav_foods.txt")

def compare_favs(list1, list2):
    if list1[0] == list2[0]:
        print "Our favorite foods are the same!"
    else:
        print "Our favorite foods are different."

compare_favs(list_sandi, list_katherine)

def compare_favs2(list1, list2):
    if list1[0] in list2:
        print "We both love", list1[0]
    elif list1[1] in list2:
        print "We both love", list1[1]
    elif list1[2] in list2:
        print "We both love", list1[2]
    else:
        print "Our favorite foods are different."

compare_favs2(list_sandi, list_katherine)

        