#Name: Jose Melquiades Escobar

#Define main():
def main():

    #Declare Local variables
    word_list = []
    all_words_list = []
    all_words_set = set()
    word_set_not_unique = set()
    word_set_unique = set()
    
    #Open file text2.txt for reading. Use 'text2.txt' file
    input_file = open ('text2.txt', 'r')

    #User the set method to find the unique words in the file and store each
    #of them as an element of the set. 

    #Figures out what is not unique in different lines
    for line in input_file:             #go through each line of the file
        clean_line = line.rstrip('\n')  #remove the new line from each line
        word_list = clean_line.split()   
        all_words_list += word_list     #make a list of each individual word
    for num in range (0, len(all_words_list)):
        for number in range (num +1, len(all_words_list)):
            if all_words_list[num] == all_words_list [number]:
                word_set_not_unique.add(all_words_list[number])
    all_words_set.update(all_words_list)
    word_set_unique = all_words_set.difference(word_set_not_unique)

    #display the unique words
    print ('These are the unique words in the text:')
    for word in word_set_unique:
        print (word)
                
    #Close the file.
    input_file.close()

main()


