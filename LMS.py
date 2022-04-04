print("Welcome to the Library Management System")

while True:
    name = input("Enter your name: \n ")
    name_book = input("Enter the name of the book that you wanna take: \n ")
    date = input(" Enter the date at which you've issued it: \n ")

    books = { "Rahul":"The subtle art of not giving a f*ck" }

    books[name] = name_book

    print("Your data has been recorded")

    question = input(" Do you want to say something: \n ")
    if question == "yes":
        question1 = input(" What you want to say: \n ")
        if "remove" in question1:
            remove_book = input(" Enter which your name: \n ")
            books.pop(remove_book)
            print(" your records has been removed ")
    else:
        break        

    user_choice = input("Do you want to see the name of the book that you've purchased: \n ")
    if user_choice == "no":
        break
    elif user_choice == "yes":
        user_name = input("Enter your name: \n ")

        print(books[user_name])
        break

