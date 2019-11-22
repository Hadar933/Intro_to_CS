from wave_helper import *
import os.path
import math

INVALID_PICK = 'Invalid option.Please try again.'
INVALID_FILE = 'Invalid file. Please try again.'


def ask_for_edit_file():
    """
    requests file to edit from user once edit option was chosen
    :return: file
    """
    print('Please provide the name of the file you would like to change')
    edit_file = input()
    while load_wave(edit_file) is -1: # wave helper returns -1
        print(INVALID_FILE)
        edit_file = input() #requests name until name is ok
    while load_wave(edit_file) is not -1:
        return edit_file


def ask_for_merge_files():
    """
    requests files to merge from user once merge option was chosen
    :return: files
    """
    print('Please provide the names of the files you would like to merge')
    merge_file1, merge_file2 = input().split(" ") #splits the names
    while load_wave(merge_file1) is -1 or load_wave(merge_file2) is -1:
        print(INVALID_FILE)
        merge_file1,merge_file2 = input().split(" ")
    while load_wave(merge_file1) is not -1 and load_wave(merge_file2) \
            is not -1:
        return merge_file1, merge_file2


def ask_for_melody_file():
    """
    requests file containing melody from user once compose option was chosen
    :return: file
    """
    print('Please provide the file containing the melody instructions')
    melody_file = input()
    if os.path.isfile(melody_file) is False:
        print(INVALID_FILE)
        melody_file = input()
    return melody_file


def start_menu():
    """
    main menu that shows up first and calls all the rest of the funcions
    :return:
    """
    print('Welcome! What would you like to do?')
    print('1.Change wav file')
    print('2.Merge two wav files')
    print('3.Compose melody in wav format')
    print('4.Exit the program \n')
    print('Type the desired number, followed by Enter')
    VALID_CHOICES = [1,2,3,4]
    choice = int(input())
    while choice not in VALID_CHOICES:
        print(INVALID_PICK)
        choice = int(input())
    # each choice navigate to a different menu
    if choice == 1:
        edit_menu()
    if choice == 2:
        merge_menu()
    if choice == 3:
        composer_menu()
    if choice == 4:
        exit()


def composer_menu():
    """
    receives all data from the supported functions and goes to transition menu
    :return:
    """
    file_name = ask_for_melody_file()
    composed_file = composer(file_name)
    transition_menu(composed_file)


def merge_menu():
    """
    receives all data from the supported functions and goes to transition menu
    :return:
    """
    file_name1,file_name2 = ask_for_merge_files()
    file = merge_files(file_name1,file_name2)
    transition_menu(file)


def edit_menu():
    """
    user picks which change he would like to create
    then navigated accordingly
    :return:
    """
    file_name = ask_for_edit_file()
    print('What changes would you like to make?')
    print('1.Reverse')
    print('2.Increase speed')
    print('3.Decrease speed')
    print('4.increase volume')
    print('5.Decrease volume')
    print('6.Low pass filter \n')
    print('Type the options number, followed by Enter')
    choice = int(input())
    if choice == 1:
        reverser(file_name)
    if choice == 2:
        increase_speed(file_name)
    if choice == 3:
        decrease_speed(file_name)
    if choice == 4:
        increase_volume(file_name)
    if choice == 5:
        decrease_volume(file_name)
    if choice == 6:
        low_pass_filter(file_name)


# CHANGE FILE FUNCTIONS #


def reverser(file_name):
    """
    reverses the list that represents the file, then navigates to
    transition menu
    """
    file_content = load_wave(file_name)
    frame_rate = file_content[0]
    audio_data = file_content[1]
    reversed_audio_data = audio_data[::-1] #reverse process
    reversed_file = frame_rate, reversed_audio_data
    transition_menu(reversed_file)


def increase_speed(file_name):
    """
    removes even index list's values, then navigates to transition menu
    """
    file_content = load_wave(file_name)
    frame_rate = file_content[0]
    audio_data = file_content[1]
    del audio_data[1::2] #removing all even index items
    increased_speed_file = frame_rate, audio_data
    transition_menu(increased_speed_file)


def decrease_speed(file_name):
    """ decreases the speed of the audio by creating extra items in the list
    that are made up of the oter items averages. then navigates to transition
     menu
    """
    combined_values = []
    file_content = load_wave(file_name)
    frame_rate = file_content[0]
    audio_data = file_content[1] #relating to this list as immutable
    audio_data_copy = audio_data #new list that will change
    for i in range(len(audio_data)-1):
        for j in range(2):
            #avg of first item
            first_avg = int(0.5*(audio_data[i][j]+audio_data[i+1][j]))
            #avg of second item
            second_avg = int(0.5*(audio_data[i][j+1]+audio_data[i+1][j+1]))
            combined_avg_value = [first_avg,second_avg]
            combined_values.append(combined_avg_value)
            audio_data_copy = audio_data_copy[:i+1]+[combined_values[i]]+\
                              audio_data_copy[i+1:] #add the value in the
                                                    #needed place
            break
    decreased_speed_file = frame_rate, audio_data_copy
    transition_menu(decreased_speed_file)


def increase_volume(file_name):
    """
    increases the volume by multiplying the values by 1.2, then navigates to
     transition menu
    """
    file_content = load_wave(file_name)
    frame_rate = file_content[0]
    audio_data = file_content[1]
    for i in range(len(audio_data)):
        for j in range(2):
            while -32768<int(1.2*audio_data[i][j])<32767: #min and max vals
                audio_data[i][j] = int(1.2*audio_data[i][j])
                break
            if int(1.2*(audio_data[i][j]))>32767: #item is bigger than max
                audio_data[i][j] = 32767
            if int(1.2*(audio_data[i][j]))< -32768: #item is smaller than max
                audio_data[i][j] = -32768
    increased_vol_file = frame_rate, audio_data
    transition_menu(increased_vol_file)


def decrease_volume(file_name):
    """
    turns down the volume by multiplying all values by 0.8, then navigates
     to transition menu. this function is similar to the previous one
    """
    file_content = load_wave(file_name)
    frame_rate = file_content[0]
    audio_data = file_content[1]
    for i in range(len(audio_data)):
        for j in range(2):
            x = int(audio_data[i][j])
            y = int(0.8 * (audio_data[i][j]))
            while -32768 < int(0.8 * audio_data[i][j]) < 32767:
                audio_data[i][j] = int(0.8 * audio_data[i][j])
                break
            if int(0.8 * (audio_data[i][j])) > 32767:
                audio_data[i][j] = 32767
            if int(0.8 * (audio_data[i][j])) < -32768:
                audio_data[i][j] = -32768
    decreased_vol_file = frame_rate, audio_data
    transition_menu(decreased_vol_file)


def low_pass_filter(file_name):
    """
    dims down the audio file by replacing each item in the list with the
    average of the values surrounding it, then navigates to transition menu
    """
    file_content = load_wave(file_name)
    frame_rate = file_content[0]
    audio_data = file_content[1]
    audio_data_copy = audio_data
    for i in range(1,len(audio_data)-1):
        for j in range(1):
            # creating the averages:
            first_avg = int((1/3)*(audio_data[i-1][j]+audio_data[i][j]
                                   +audio_data[i+1][j]))
            audio_data_copy[i][j] = first_avg
            second_avg = int((1/3)*((audio_data[i-1][j+1])+audio_data[i][j+1]
                                    +audio_data[i+1][j+1]))
            audio_data_copy[i][j+1] = second_avg

    # first item in list: #
    audio_data_copy[0][0] = int(0.5*(audio_data[0][0]+audio_data[1][0]))
    audio_data_copy[0][1] = int(0.5 * (audio_data[0][1] + audio_data[1][1]))

    # last item in list: #
    audio_data_copy[len(audio_data)-1][0] = \
        int(0.5 * (audio_data[len(audio_data)-1][0] +
                   audio_data[len(audio_data)-2][0]))

    audio_data_copy[len(audio_data)-1][1] = \
        int(0.5 * (audio_data[len(audio_data)-1][1] +
                   audio_data[len(audio_data)-2][1]))

    low_filter_pass_file = frame_rate, audio_data_copy
    transition_menu(low_filter_pass_file)


def text_file_reader(file):
    """
    reads a text file
    :param file: txt file
    :return: file as a list
    """
    item_list = []
    with open(file, 'r') as word_list:
        segment = word_list.readlines()
        for item in segment:
            for letter in item:
                if letter == " " or letter == "\n":
                    continue
                item_list.append(letter)
    return item_list


def composer(filename):
    """
    creates a new file of melody according to a txt file containing the
    instructions
    :param filename: txt file containing melody instructions
    :return: new melodo wav file
    """
    lst = text_file_reader(filename)
    lst_as_tuples = []
    # constants:
    SAMPLE_RATE_UNIT = 125
    SAMPLE_RATE = 2000
    PI = math.pi
    MAX_VOLUME = 32767
    freq_dict = {'A':440,'B':494,'C':523,'D':587, #frequencies
                 'E':659,'F':698,'G':784,'Q':0}
    samples = []
    #creating tuples from the given file, for easier usage
    for i in range(0,len(lst),2):
        for j in range(i+1,len(lst)):
            value_tuple = lst[i],lst[j]
            lst_as_tuples.append(value_tuple)
            break
    #naming several more values based on said tuple
    for tuple in lst_as_tuples:
        note = tuple[0]
        time = int(tuple[1])
        frequency = freq_dict[note]
        sample_per_cycle = SAMPLE_RATE/frequency

        for i in range(time*SAMPLE_RATE_UNIT): # only exception case
            if note == 'Q':
                sample = freq_dict['Q']
                samples.append([sample,sample])
            else: # uses the formule to genetare new melody
                sample = int(MAX_VOLUME*math.sin(2*PI*i/sample_per_cycle))
                samples.append([sample,sample])
    new_melody = (SAMPLE_RATE,samples)
    return new_melody


def gcd(x, y):
    """
    generates the greatest common dividor according to euclids algorithm
    :param x: first num
    :param y: second num
    :return: gcd
    """
    while y > 0:
        x, y = y, x % y
    return x


def merge_files(file1, file2):
    """
    merging files that might or might not be different
    :return: new merged file
    """
    avg = [] # list of avg values from the files
    file_content1 = load_wave(file1)
    frame_rate1 = file_content1[0]
    audio_data1 = file_content1[1]

    file_content2 = load_wave(file2)
    frame_rate2 = file_content2[0]
    audio_data2 = file_content2[1]

    # FRAME RATES ARE EQUAL:
    #averages the values, then adds the rest of the items from the longer
    #file to the list of avgs
    if frame_rate2 == frame_rate1:
        for val1, val2 in zip(audio_data1, audio_data2):
            avg.append([(val1[0] + val2[0]) // 2, (val1[1] + val2[1]) // 2])
        if len(avg) < len(audio_data1):
            avg.extend(audio_data1[len(avg):])
        elif len(avg) < len(audio_data2):
            avg.extend(audio_data2[len(avg):])
        return frame_rate1, avg

    # FRAME RATES AREN'T EQUAL- (two options)
    if frame_rate2 != frame_rate1:
        audio_data2_copy = audio_data2
        audio_data1_copy = audio_data1
        #using gcd to know how much values are needed
        gc = gcd(frame_rate1, frame_rate2)
        num_of_samples1 = int(frame_rate1 / gc)
        num_of_samples2 = int(frame_rate2 / gc)

        # OPTION ONE
        if num_of_samples2 > num_of_samples1:
            # adding only items that are between samples (and repeating)
            audio_data2_copy = [x for i, x in enumerate(audio_data2_copy)
                                if i % num_of_samples2 in
                                (range(num_of_samples1))]
            for val1, val2 in zip(audio_data1, audio_data2_copy):
                avg.append([(val1[0] + val2[0]) // 2,
                            (val1[1] + val2[1]) // 2])
            if len(avg) < len(audio_data2):
                avg.extend(audio_data2[len(avg):])
            elif len(avg) < len(audio_data1):
                avg.extend(audio_data1[len(avg):])
            return frame_rate1, avg

        # OPTION TWO #
        if num_of_samples2 < num_of_samples1:
            # adding only items that are between samples (and repeating)
            audio_data1_copy = [x for i, x in enumerate(audio_data1_copy)
                                if i % num_of_samples1 in
                                (range(num_of_samples2 + 1))]
            for val1, val2 in zip(audio_data1_copy, audio_data2):
                avg.append([(val1[0] + val2[0]) // 2,
                            (val1[1] + val2[1]) // 2])
    if len(avg) < len(audio_data1):
        avg.extend(audio_data1[len(avg):])
    elif len(avg) < len(audio_data2):
        avg.extend(audio_data2[len(avg):])
        return frame_rate2, avg


def transition_menu(file):
    """
    edited files arrive here for final user operations - save or change.
    each choise navigates the user to the related outcome
    """
    print('Changes had been made! How would you like to proceed?')
    print('1.Save')
    print('2.Make changes')
    print('Type the desired number, followed by Enter')
    choice = int(input())
    VALID_CHOICES = [1,2]
    while choice not in VALID_CHOICES:
        print(INVALID_PICK)
        choice = int(input())
    if choice == 1:
        print('How would you like to call your file? (make sure to add .wav)')
        file_name = input()
        save_wave(file[0],file[1],file_name) #saving the created file
        print('Saved! Enjoy')
    if choice == 2: #navigating to edit menu for additional change
        edit_menu()


if __name__ == "__main__":
    start_menu()