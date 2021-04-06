if __name__ == '__main__':
    print("Started : Ransom Note - Link : ")
    print("hackerrank.com/challenges/ctci-ransom-note/problem?h_l=interview&playlist_slugs%5B%5D=interview"
          "-preparation-kit&playlist_slugs%5B%5D=dictionaries-hashmaps")



def checkMagazine(magazine, note):
    mag = magazine.split(" ")
    mag_size = len(mag)
    no_te = note.split(" ")
    note_size = len(no_te)

    for word in mag :
        if word in no_te:
            note_size = note_size - 1
            no_te.remove(word)
            if note_size < 1 :
                print("Yes")

    if note_size > 0:
        return "No"
        # print("No")
    # else:
    #     return "Yes"
        # print("Yes")