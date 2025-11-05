import tkinter as tk

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.borrowed = False

    def borrow(self):
        if not self.borrowed:
            self.borrowed = True
            return f"{self.title}이(가) 대출되었습니다."
        else:
            return f"{self.title}은(는) 이미 대출중입니다."

    def return_book(self):
        if self.borrowed:
            self.borrowed = False
            return f"{self.title}이(가) 반납되었습니다."
        else:
            return f"{self.title}은(는) 대출되지 않은 상태입니다."


def borrow_book():
    b = Book(entry_title.get(), entry_author.get())
    msg = b.borrow()
    result_label.config(text=msg)


def return_book():
    b = Book(entry_title.get(), entry_author.get())
    msg = b.return_book()
    result_label.config(text=msg)


root = tk.Tk()
root.title("도서대출관리프로그램")
root.geometry("300x200")

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

root.mainloop()
