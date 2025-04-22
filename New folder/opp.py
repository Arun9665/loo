
import random

guess_number:random = random.randint(1,10)
guess:None = None



guess_nm = input("enter yours choise number -:")

while guess:
    
    if guess_nm < guess_number:
        print('ye chhote numbe hain aur choise kare')

    elif guess_nm > guess_number:
        print('ye number high hain aur choise kare')

    else:
        print("invaliv choise hain ! try again")

        