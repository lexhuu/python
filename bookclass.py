class book:
    def __init__(self, title,author):
        print(title,'by',author)
class ebook(book):
        def __init__(self):
            self.title=input("Enter the title:")
            self.author=input("Enter the author`:")
            super().__init__(self.title ,self.author)
 
            
book1=ebook()