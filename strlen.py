def string_length(given_string):
    count=0
    #given_string = "Test"
    for i in given_string:
        count= count+1

    return count


s=input("Enter the string to find length")
print(string_length(s))

        
