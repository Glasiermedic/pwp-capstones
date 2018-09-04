DEBUG =False
import re

   
class User(object):
    def __init__(self, name, email):
        self.name  = name
        self.email = email
        self.user_books = {}
        
    def get_email(self):
        return self.email
        
    def change_email(self, address):
        old_email = self.email
        self.email = address
        print("{name}'s email address ({old_email}) was changed for '{new_email}'".format(name = self.name, old_email = old_email, new_email = self.email))

    def __repr__(self):
        return "User {name}, email: {email}, books read: {books_n}".format(name = self.name, email = self.email, books_n = len(self.user_books))

    def __eq__(self, other_user):
         if self.name == other_user.name and self.email == other_user.email:
            return True
         else:
            return False
    
    def read_book(self,book,rating="none"):
        self.user_books[book] = rating
        
    def get_average_rating(self):
        """Return user's average rating, rounded to one decimal place."""
        total_rating = 0
        number_rated_books = 0
        for rating in self.user_books.values():
            try:
                total_rating += rating
                number_rated_books += 1
            except TypeError: #book has rating of None
                pass
        return round(total_rating / number_rated_books, 1)
                
    def __hash__(self):
        return (hash((self.title, self.isbn)))





class Book:
    def __init__(self, title, isbn):
        self.title = title
        self.isbn  = isbn
        self.rating = []
    
    def get_title(self):
        return self.title
    
    def get_isbn(self):
        return self.isbn
    
    def set_isbn(self,new_isbn):
        self.isbn = new_isbn
        print("The book's isbn has been updated")
        
    def add_rating(self, rating):
        if rating != None:
            if rating >= 0 and rating <= 4:
                self.rating.append(rating)
            else:
                print("Invalid Rating")
            
    def __eq__(self, other_book):
        if self.title == other_book.title and  self.isbn == other_book.isbn:
            return True
        return False
    
    def get_average_rating(self):
        if sum(self.rating) > 0:
            return round(sum(self.rating) / len(self.rating), 2)
        else:
            return 0
        
    def __hash__(self):
        return (hash((self.title, self.isbn)))  
    
    def __repr__(self):
        return self.title



    
class Fiction(Book):
    def __init__(self, title, author, isbn,):
        super().__init__(title,isbn)
        if author:
            self.author = author

    def get_author(self):
        return self.author

    def __repr__(self):
        return "{title} by {author}".format(title = self.title, author = self.author)



    
class Non_Fiction(Book):
    def __init__(self, title, subject, level, isbn):
        super().__init__(title, isbn)
        self.subject = subject
        self.level = level
        
    def get_subject(self):
        return self.subject
    
    def get_level(self):
        return self.level
    
    def __repr__(self):
        return "{title}, a {level} level manual on {subject}".format(title = self.title, level = self.level, subject = self.subject)
    

    
                     
                     
class TomeRater(object):
    def __init__(self):
        self.users = {}
        self.user_books = {}
        
    def create_book(self,title, isbn):
        return Book(title,isbn)
         
    
    def create_novel(self, title, author, isbn):
        if type(author)!= str:
            return Fiction(title,isbn)
        else:
            return Fiction(title,author, isbn)
    
    def create_non_fiction(self,title, subject, level, isbn):
        return Non_Fiction(title, subject, level, isbn)
        
     
    def add_book_to_user(self,book, email, rating=None):
        if email not in self.users:
                print ("No user with email " + email + "!")
        else:
            self.users[email].read_book(book, rating)
            book.add_rating(rating)
            if book in self.user_books:
                self.user_books[book] += 1
            else:
                self.user_books[book] = 1
       
                
    def add_user(self, name, email, user_books = None):
        user = User(name, email)
        self.users[user.email] = user  # self used if calling against object
        # print(type(self.users))
        if user_books is not None:
            if user_books is list:
                for i in user_books:
                    # print(i)
                    self.add_book_to_user(i, email, None)
        
            

    def print_catalog(self):
        for book in self.user_books.keys():
            print (book)
    
    def print_users(self):
        for user in self.users.values():
            print (user)
            
    def get_most_read_book(self):
        max_book = "none"
        max_count = 0
        for book, value  in self.user_books.items():
            if value > max_count:
                max_count = value
                max_book = book
        return book
    
    def highest_rated_book(self):
        high_book = "none"
        high_count = 0
        for book in self.user_books.keys():
            if book.get_average_rating() > high_count:
                high_count = book.get_average_rating()
                high_book=book
        return high_book
    
    def most_positive_user(self):
        high_user = None
        highest_rating = 0 
        for user in self.users.values():
            if user.get_average_rating() > highest_rating:
                highest_user = user
                highest_rating = user.get_average_rating()
        return highest_user
    
    def get_n_most_read_books(self, nth):
        if nth > len(self.user_books):
            print("We are limited to {num} since we still don't have many book reviewers.".format(num=len(self.books)))
            nth = len(self.books)
        previous_max = float("inf")
        result = []
        for item in range(nth):
            max_times_read = float("-inf")
            for book, times_read in self.user_books.items():
                if times_read > max_times_read and times_read <= previous_max and book not in result: 
                    top_book = book
                    max_times_read = times_read
                    
            result.append(top_book)
            previous_max = max_times_read
        return result
    
    # TOME RATER DUBUG
if DEBUG == True:
    fiction = Fiction("Moby Dick", "Dik Mob", 1234567)
    non_f = Non_Fiction("Moby Dick, True Story", "Survival on the deep blue", "hardcore", 1234567)
    max_b = User("Max B", "max_sux@a.mail.com")
    alek_r = User("Alek R", "alekr@mail.com")
    max_b.change_email("maxb@boss.com")
    moby = Book("Moby Dick", 1234561)
    moby.set_isbn(1231231)
    print(moby)
    print(max_b)
    print("**DEBUG** TOME RATER")
    #Tome_Rater = TomeRater()
    book1 = Tome_Rater.create_book("Society of Mind", 12345678)
    Tome_Rater.add_user("David Marr", "david@computation.org")
    Tome_Rater.add_book_to_user(non_f, "alan@turing.com", 3)
    print(Tome_Rater)

    print(book1.title)
    print("compare", max_b == alek_r)
    print("compare", max_b == max_b)
    print(fiction)
    print(non_f.get_subject())
    print("**END DEBUG**")
    Tome_Rater.print_catalog()

            
            
        
                
            
        
        
        
    
                     
                
                     
                   
                     