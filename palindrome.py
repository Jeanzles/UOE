def convert(string):
    list1 = []
    list1[:0] = string
    return list1

text = str(input("give me a word: "))
whole = convert(text)
print(whole)
length = len(whole)
if length > 3:
    middle_len = length//2
    upper_len = whole[middle_len:]
    lower_len = whole[:middle_len]
    rev_upper_len = upper_len[::-1]
    if lower_len == rev_upper_len:
        print("it is a palindrome stooped")
    else:
        print("nope it aint ")
else:
    if whole[0] == whole[-1]:
        print("it is a palindrome m8")
    else:
        print("no it aint bro: ")
