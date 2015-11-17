def convert_file_to_list(text_file):
    file_open = open(text_file)
    file_list = file_open.readlines()
    file_open.close()
    return file_list 

list_sandi = convert_file_to_list("sandi_fav_foods.txt")
list_katherine = convert_file_to_list("katherine_fav_foods.txt")

def compare_favs(list1, list2):
    if list1[0] == list2[0]:
        print "Our favorite foods are the same!"
    else:
        print "Our favorite foods are different."

compare_favs(list_sandi, list_katherine)
