#создай приложение для запоминания информации
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import(
    QApplication, QWidget, QLabel, QRadioButton, QVBoxLayout, QHBoxLayout, QGroupBox, QPushButton, QButtonGroup, QMessageBox
)
import random

class Question:
    def __init__(self, text, right_answer, wrong1, wrong2, wrong3):
        self.text = text
        self.right_answer = right_answer
        self.wrong1 = wrong2
        self.wrong2 = wrong2
        self.wrong3 = wrong3

def ask(q: Question):
    question_text.setText(q.text)
    random.shuffle(buttons)
    buttons[0].setText(q.right_answer)
    buttons[1].setText(q.wrong1)
    buttons[2].setText(q.wrong2)
    buttons[3].setText(q.wrong3)

questions = [
    Question('смеяться или плакать', 'Смеяться', 'Плакать', 'Не знаю', 'И то и то'),
    Question('что? ... когда?', 'где?', 'где?', 'где?', 'где?'),
    Question('День недели', '04.11', '04.10', '04.12', '04.13'),
    Question('День рождения автора данного проекта', '22.04', '08.08', '31.02', '04.11'),
    Question('Дальше я не придумал', 'ок', 'печально', 'хорошо', 'где?'),
    Question('как к вам относятся одноклассники', 'тест психология', 'хооршо', 'плохо', 'где я?'),
    Question('как вы относитесь к психотропным веществам', 'очень плохо', 'колюсь', 'да', 'где?'),
    Question('Этикет программирование', 'обязан', 'нет', 'что?', 'где?'),
    Question('Pithon start 2 years', 'да', 'нет', 'что?', 'где?'),
    Question('через сколько дней Нью Э', '7 недель', '8 недель', '5 недель', '6 недель'),
]

def show_answers():
    if button_group.checkedButton() == None:
        retorn
    
    btn.setText('Следующий ')
    for rbtn in buttons:
        if rbtn.isChecked():
            if rbtn.text() == buttons[0].text():
                rbtn.setStyleSheet('color: green')
                main_win.score += 1
            else:
                rbtn.setStyleSheet('color: red')
                buttons[0].setStyleSheet('color: purple')
            break

def show_question():
    btn.setText('Перейти к следующему вопросу')
    button_group.setExclusive(False)
    for rbtn in buttons:
        rbtn.setStyleSheet('')
        rbtn.setChecked(False)
    button_group.setExclusive(True)
    next_question()

def next_question():
    if main_win.q_index >= len(questions):
        main_win.q_index = 0
        random.shuffle(questions)
        show_score()
        main_win.score = 0
    q = questions[main_win.q_index]
    main_win.q_index += 1
    ask(q)

def start_test():
    if btn.text() == 'Перейти к следующему вопросу':
        show_answers()
    else:
        show_question()

def show_score():
    percent = main_win.score / main_win.total * 100
    percent = round(percent, 2)
    text = 'Уважвемый Даниил!\n'
    text += f'Вы ответили на {main_win.score} из {main_win.total} questions\n'
    text += f'Процент правильных ответов: {percent}%.\n'
    text += 'Тест начинается заново!'


    msg = QMessageBox()
    msg.setWindowTitle('Результат опроса')
    msg.setText(text)
    msg.exec()

#подключение библиотек
app = QApplication([])
main_win = QWidget()
main_win.setWindowTitle('Master card')
main_win.resize(640, 360)
main_win.q_index= 0
main_win.total = len(questions)
main_win.score = 0

question_text = QLabel('у')
grp_box = QGroupBox('Выберете один из ответов')
button_group = QButtonGroup()
radio1 = QRadioButton('у')
radio2 = QRadioButton('у1')
radio3 = QRadioButton('у')
radio4 = QRadioButton('у')
btn = QPushButton('Ответить')
result_text = QLabel('у')

button_group.addButton(radio1)
button_group.addButton(radio2)
button_group.addButton(radio3)
button_group.addButton(radio4)


main_layout = QVBoxLayout()
main_h1 = QHBoxLayout()
main_h2 = QHBoxLayout()
main_h3 = QHBoxLayout()
grp_main_layout = QHBoxLayout()
grp_v1 = QVBoxLayout()
grp_v2 = QVBoxLayout()

grp_v1.addWidget(radio1)
grp_v1.addWidget(radio2)
grp_v2.addWidget(radio3)
grp_v2.addWidget(radio4)
grp_main_layout.addLayout(grp_v1)
grp_main_layout.addLayout(grp_v2)
grp_box.setLayout(grp_main_layout)

main_h1.addWidget(question_text, alignment=Qt.AlignCenter)
main_h2.addWidget(grp_box)
main_h3.addStretch(1)
main_h3.addWidget(btn, stretch=2)
main_h3.addStretch(1) 
main_layout.addLayout(main_h1)
main_layout.addLayout(main_h2)
main_layout.addLayout(main_h3)
main_win.setLayout(main_layout)


btn.clicked.connect(start_test)

# создаем список с радиоFM
buttons = [radio1, radio2, radio3, radio4]
random.shuffle(questions)
ask(questions[main_win.q_index])
main_win.q_index += 1

main_win.show()
app.exec()