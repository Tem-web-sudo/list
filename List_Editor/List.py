import json
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout, QListWidget, QHBoxLayout, QTextEdit, QLineEdit

app = QApplication([])
main_win = QWidget()
main_win.setWindowTitle

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
shelf_1 = QPushButton('Полка 1')
shelf_2 =QPushButton('Полка 2')
shelf_3 =QPushButton('Полка 3')
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

main_win.setLayout(main_layout)







main_win.show()
app.exec()