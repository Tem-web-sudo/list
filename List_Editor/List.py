import json
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout, QListWidget, QHBoxLayout, QTextEdit, QLineEdit

app = QApplication([])
main_win = QWidget()
main_win.setWindowTitle('Библиотека')

main_layout = QHBoxLayout()
left_stuff = QVBoxLayout()
right_stuff = QVBoxLayout()
shelf_buttons = QHBoxLayout()
book_buttons = QHBoxLayout()

book_list = QListWidget()
book_name = QLineEdit()
book_desc = QTextEdit()
book_shelf =QLineEdit()
#change shelf to genre
shelf_1 = QPushButton('Детские книги')
shelf_2 =QPushButton('Биографий')
shelf_3 =QPushButton('Манги')
add_book_button =QPushButton('Добавить книгу')
del_book_button =QPushButton('Удалить книгу')
edit_book_button =QPushButton('Изменить книгу')

shelf_buttons.addWidget(shelf_1)
shelf_buttons.addWidget(shelf_2)
shelf_buttons.addWidget(shelf_3)

book_buttons.addWidget(add_book_button)
book_buttons.addWidget(del_book_button)
book_buttons.addWidget(edit_book_button)

right_stuff.addLayout(shelf_buttons)
right_stuff.addWidget(book_name)
right_stuff.addWidget(book_shelf)
right_stuff.addWidget(book_desc)
right_stuff.addLayout(book_buttons)

left_stuff.addWidget(book_list)

main_layout.addLayout(left_stuff, 30)
main_layout.addLayout(right_stuff, 70)


books = {}
biograph = {}
mangas = {}

main_win.setLayout(main_layout)
with open('book_kids.json', 'r', encoding='utf-8') as file:
    books = json.load(file)

with open('Biography.json', 'r', encoding='utf-8') as file:
    biograph = json.load(file)

with open('manga.json', 'r', encoding='utf-8') as file:
    mangas = json.load(file)
book_list.clear()
for book in books:
    book_list.addItem(book)

book_name.setPlaceholderText('Имя книги....')
book_desc.setPlaceholderText('Описание книги....')
book_shelf.setPlaceholderText('Жанр книги....')
def add_book():
    book = book_name.text()
    op = add_book_button.text()
    if op == 'Добавить книгу':
        with open('book_kids.json', 'r', encoding='utf=8') as file:
            books = json.load(file)
        books[book] = ''
        with open('book_kids.json', 'w', encoding='utf=8') as file:
            json.dump(books, file)
            book_list.clear()
            for book in books:
                book_list.addItem(book)
    if op == 'Добавить биографию':
        with open('Biography.json', 'r', encoding='utf=8') as file:
            biograph = json.load(file)
        biograph[book] = ''
        with open('Biography.json', 'w', encoding='utf=8') as file:
            json.dump(biograph, file)
            book_list.clear()
            for book in biograph:
                book_list.addItem(book)
    if op == 'Добавить мангу':
        with open('Manga.json', 'r', encoding='utf=8') as file:
            mangas = json.load(file)
        mangas[book] = ''
        with open('Manga.json', 'w', encoding='utf=8') as file:
            json.dump(mangas, file)
            book_list.clear()
            for book in mangas:
                book_list.addItem(book)
def del_book():
    global books, biograph, mangas
    if book_list.selectedItems():
         book = book_list.selectedItems()[0].text()
    if book in books:
        with open('book_kids.json', 'r', encoding='utf-8') as file:
            books = json.load(file)
        del books[book]
        with open('book_kids.json', 'w', encoding='utf=8') as file:
            json.dump(books, file)
        book_list.clear()
        for book in books:
            book_list.addItem(book)
    if book in biograph:
        with open('Biography.json', 'r', encoding='utf-8') as file:
            biograph = json.load(file)
        del biograph[book]
        with open('Biography.json', 'w', encoding='utf=8') as file:
            json.dump(biograph, file)
        book_list.clear()
        for book in biograph:
            book_list.addItem(book)
    if book in mangas:
        with open('Manga.json', 'r', encoding='utf-8') as file:
            mangas = json.load(file)
        del mangas[book]
        with open('Manga.json', 'w', encoding='utf=8') as file:
            json.dump(mangas, file)
        book_list.clear()
        for book in mangas:
            book_list.addItem(book)
def edit_book():
    global books, biograph, mangas
    if book_list.selectedItems():
        book = book_list.selectedItems()[0].text()
    if book in books:
        with open('book_kids.json', 'r', encoding='utf-8') as file:
            books = json.load(file)
        text_book = book_desc.toPlainText()
        books[book] = text_book
        with open('book_kids.json', 'w', encoding='utf=8') as file:
            json.dump(books, file)
        book_list.clear()
        for book in books:
            book_list.addItem(book)
    if book in biograph:
        with open('Biography.json', 'r', encoding='utf-8') as file:
            biograph = json.load(file)
        text_book = book_desc.toPlainText()
        biograph[book] = text_book
        with open('Biography.json', 'w', encoding='utf=8') as file:
            json.dump(biograph, file)
        book_list.clear()
        for book in biograph:
            book_list.addItem(book)
    if book in mangas:
        with open('Manga.json', 'r', encoding='utf-8') as file:
            mangas = json.load(file)
        text_book = book_desc.toPlainText()
        mangas[book] = text_book
        with open('Manga.json', 'w', encoding='utf=8') as file:
            json.dump(mangas, file)
        book_list.clear()
        for book in mangas:
            book_list.addItem(book)  
def desc_book():
    global books, biograph, mangas
    book = book_list.selectedItems()[0].text()
    if book in books:
        with open('book_kids.json', 'r', encoding='utf=8') as file:
            books = json.load(file)
        info_book = books[book]
        book_desc.setText(info_book)
    if book in biograph:
        with open('Biography.json', 'r', encoding='utf=8') as file:
            biograph = json.load(file)
        info_book = biograph[book]
        book_desc.setText(info_book)
    if book in mangas:
        with open('Manga.json', 'r', encoding='utf=8') as file:
            mangas = json.load(file)
        info_book = mangas[book]
        book_desc.setText(info_book)


def kids():
    with open('book_kids.json', 'r', encoding='utf-8') as file:
        books = json.load(file)
    book_list.clear()
    add_book_button.setText('Добавить книгу')
    del_book_button.setText('Удалить книгу')
    edit_book_button.setText('Изменить книгу')
    for book in books:
        book_list.addItem(book)
def bio():
    with open('Biography.json', 'r', encoding='utf-8') as file:
        biograph = json.load(file)
    book_list.clear()
    add_book_button.setText('Добавить биографию')
    del_book_button.setText('Удалить биографию')
    edit_book_button.setText('Изменить биографию')
    for book in biograph:
        book_list.addItem(book)
def manga():
    with open('Manga.json', 'r', encoding='utf-8') as file:
        mangas = json.load(file)
    book_list.clear()
    add_book_button.setText('Добавить мангу')
    del_book_button.setText('Удалить мангу')
    edit_book_button.setText('Изменить мангу')
    for book in mangas:
        book_list.addItem(book)

add_book_button.clicked.connect(add_book)
del_book_button.clicked.connect(del_book)
edit_book_button.clicked.connect(edit_book)
book_list.itemClicked.connect(desc_book)
shelf_1.clicked.connect(kids)
shelf_2.clicked.connect(bio)
shelf_3.clicked.connect(manga)

main_win.show()
app.exec()