def change(string):
    if string[0:2] == 'Is' or string[0:2]=='is':
        final = string
    else:
        final = "Is "+string
    return final

string = input("Enter A String : ")
final = change(string)
print(final)