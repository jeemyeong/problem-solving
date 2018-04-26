def has_extension(file):
    return len(file) > 2 and "." in file[1:len(file)-1] and "." != file[-1]

def solve(string):
    # * split string with \n so that each file or folder can be put into array
    # * iterator array to check it's length
    # * check whether it is file or folder
    # if it's folder, its length should be saved into array for its tab count
    # child has one more tab count than its parent
    
    # split string with \n
    lst = string.split("\n")

    # array to save folder's length at each tab count
    folder_length_at_each_tab = []

    # max_length will be returned
    max_length = 0

    # iterate file or folder in array
    for file_or_folder in lst:
        tab_cnt = file_or_folder.count('\t')
        file_or_folder = file_or_folder.replace('\t', '')
        is_file = False
        if has_extension(file_or_folder): is_file = True
        
        # If file, max_length should be calculated with length + length of parent's folder
        if is_file:
            if tab_cnt == 0:
                max_length = max(max_length, len(file_or_folder))
                continue
            max_length = max(max_length, folder_length_at_each_tab[tab_cnt-1] + len(file_or_folder) + 1)
        # if folder, its length should be saved into array for its tab count
        if not is_file:
            if len(folder_length_at_each_tab) == tab_cnt: folder_length_at_each_tab.append(0)
            if tab_cnt == 0:
                folder_length_at_each_tab[tab_cnt] = len(file_or_folder)
            else:
                folder_length_at_each_tab[tab_cnt] = folder_length_at_each_tab[tab_cnt-1] + len(file_or_folder) + 1
    return max_length
            

solve("aaaaaaaaaaaaaaaaaaaaa/sth.png.")