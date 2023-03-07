from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QLineEdit, QMessageBox

class LibraryManagementSystem(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Library Management System")
        self.setGeometry(100, 100, 400, 300)

        self.title_label = QLabel("Library Management System", self)
        self.title_label.move(120, 20)
        self.title_label.resize(200, 20)

        self.book_name_label = QLabel("Book Name:", self)
        self.book_name_label.move(50, 70)

        self.book_name_textbox = QLineEdit(self)
        self.book_name_textbox.move(120, 70)
        self.book_name_textbox.resize(200, 20)

        self.author_label = QLabel("Author:", self)
        self.author_label.move(50, 110)

        self.author_textbox = QLineEdit(self)
        self.author_textbox.move(120, 110)
        self.author_textbox.resize(200, 20)

        self.add_button = QPushButton("Add Book", self)
        self.add_button.move(50, 160)
        self.add_button.clicked.connect(self.add_book)

        self.remove_button = QPushButton("Remove Book", self)
        self.remove_button.move(180, 160)
        self.remove_button.clicked.connect(self.remove_book)

        self.book_list_label = QLabel("Books in Library:", self)
        self.book_list_label.move(50, 200)

        self.book_list_textbox = QLabel("", self)
        self.book_list_textbox.move(50, 230)
        self.book_list_textbox.resize(300, 50)
        self.book_list_textbox.setWordWrap(True)

        self.book_list = []

    def add_book(self):
        book_name = self.book_name_textbox.text()
        author = self.author_textbox.text()
        if book_name and author:
            self.book_list.append((book_name, author))
            self.update_book_list()
            self.book_name_textbox.setText("")
            self.author_textbox.setText("")
        else:
            QMessageBox.warning(self, "Warning", "Please enter book name and author.")

    def remove_book(self):
        book_name = self.book_name_textbox.text()
        author = self.author_textbox.text()
        if book_name and author:
            for i, book in enumerate(self.book_list):
                if book[0] == book_name and book[1] == author:
                    del self.book_list[i]
                    self.update_book_list()
                    self.book_name_textbox.setText("")
                    self.author_textbox.setText("")
                    return
            QMessageBox.warning(self, "Warning", "Book not found in library.")
        else:
            QMessageBox.warning(self, "Warning", "Please enter book name and author.")

    def update_book_list(self):
        book_list_text = ""
        for book in self.book_list:
            book_list_text += f"{book[0]} by {book[1]}\n"
        self.book_list_textbox.setText(book_list_text)


if __name__ == '__main__':
    app = QApplication([])
    library_management_system = LibraryManagementSystem()
    library_management_system.show()
    app.exec_()
