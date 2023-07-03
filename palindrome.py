text=input("Enter the string to test or exit to end the palindrome test: ")
text=text.lower()
if text=="exit":
    print("Exiting the program")
else:
    if text.isalnum():
        text_r=text[::-1]
        print(text_r)
        if text_r==text:
            print("You entered a palindrome")
        else:
            print("Text entered was not a palindrome")
    else:
        text_an=""
        for ch in text:
            if ch.isalnum():
                text_an=text_an+ch
            else:
                continue
        print(text)
        print(text_an)
        text_r=text_an[::-1]
        print(text_r)
        if text_r==text_an:
            print("You entered a palindrome")
        else:
            print("You didnot entered a palindrome")
        

    
