import tkinter as tk

borrowed_books = []

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.borrowed = False

    def borrow(self):
        self.borrowed = True
        return f"{self.title}이(가) 대출되었습니다."

    def return_book(self):
        self.borrowed = False
        return f"{self.title}이(가) 반납되었습니다."


def update_borrowed_list():
    text = ", ".join([b.title for b in borrowed_books])
    borrowed_label.config(text=f"대출중: {text}")


def borrow_book():
    title = entry_title.get()
    author = entry_author.get()

    if title == "" or author == "":
        result_label.config(text="입력값이 비었습니다.", fg="red")
        return

    for b in borrowed_books:
        if b.title == title and b.author == author:
            result_label.config(text=f"{title}은(는) 이미 대출중입니다.", fg="red")
            return

    new_book = Book(title, author)
    borrowed_books.append(new_book)
    result_label.config(text=new_book.borrow(), fg="blue")
    update_borrowed_list()


def return_book():
    title = entry_title.get()
    author = entry_author.get()

    if title == "" or author == "":
        result_label.config(text="입력값이 비었습니다.", fg="red")
        return

    for b in borrowed_books:
        if b.title == title and b.author == author:
            borrowed_books.remove(b)
            result_label.config(text=b.return_book(), fg="green")
            update_borrowed_list()
            return

    result_label.config(text=f"{title}은(는) 대출목록에 없습니다.", fg="red")


root = tk.Tk()
root.title("도서대출관리프로그램 v2")
root.geometry("430x280")

tk.Label(root, text="제목").pack()
entry_title = tk.Entry(root)
entry_title.pack()

tk.Label(root, text="저자").pack()
entry_author = tk.Entry(root)
entry_author.pack()

frame_btn = tk.Frame(root)
frame_btn.pack(pady=8)

tk.Button(frame_btn, text="대출", width=10, command=borrow_book).pack(side="left", padx=5)
tk.Button(frame_btn, text="반납", width=10, command=return_book).pack(side="left", padx=5)

result_label = tk.Label(root, text="")
result_label.pack(pady=10)

borrowed_label = tk.Label(root, text="대출중: ")
borrowed_label.pack()

root.mainloop()
