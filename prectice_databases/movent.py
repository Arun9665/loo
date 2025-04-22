
def is_palindrome(string):
    # Remove spaces and convert to lowercase for comparison
    cleaned_string = ''.join(filter(str.isalnum, string)).lower()
    return cleaned_string == cleaned_string[::-1]

def main():
    user_input = input("Koi word ya phrase enter karein: ")
    if is_palindrome(user_input):
        print("Yeh ek palindrome hai!")
    else:
        print("Yeh palindrome nahi hai!")

if __name__ == "__main__":
    main()
