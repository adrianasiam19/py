#18gitgit18322
current_users = ['john', 'asiamah', 'kelvin', 'Jonathan', 'sarah']

new_users = ['grace', 'kimberly', 'Jonathan', 'sarah', 'michael']


for user in new_users:
    for current_user in current_users:
        if user == current_user:
         print(f"Enter New name")
    else:
        print(f"The username '{user}' is available.")

        #fizzBuzz:
        for i in range(1, 101):
             if i % 3 == 0 and i % 5 == 0:
               print("FizzBuzz")
             elif i % 3 == 0: print("Fizz")
             elif i % 5 == 0:
              print("Buzz")
        else:
             print(i)
