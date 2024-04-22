#создай приложение для запоминания информации
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QApplication, QButtonGroup, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QGroupBox, QRadioButton, QLabel)

app = QApplication([])
window = QWidget()
window.setWindowTitle('Memory Card')

'''Интерфейс приложения Memory Card'''
btn_OK = QPushButton('Ответить')
lb_Question = QLabel('В каком году была основона Москва?')

RadioGroupBox= QGroupBox('Варианты ответов')
rbtn_1 = QRadioButton('1147')
rbtn_2 = QRadioButton('1242')
rbtn_3 = QRadioButton('1861')
rbtn_4 = QRadioButton('1943')

layout_ans1 = QHBoxLayout()
layout_ans2 = QVBoxLayout()
layout_ans3 = QVBoxLayout()
layout_ans2.addWidget(rbtn_1)
layout_ans2.addWidget(rbtn_2)
layout_ans3.addWidget(rbtn_3)
layout_ans3.addWidget(rbtn_4)

layout_ans1.addLayout(layout_ans2)
layout_ans1.addLayout(layout_ans3)

RadioGroupBox.setLayout(layout_ans1)

layout_line1 = QHBoxLayout()
layout_line2 = QHBoxLayout()
layout_line3 = QHBoxLayout()

layout_line1.addWidget(lb_Question, alignment=(Qt.AlignHCenter | Qt.AlignVCenter))
layout_line2.addWidget(RadioGroupBox)

layout_line3.addStretch(1)
layout_line3.addWidget(btn_OK, stretch=2) # кнопка должна быть большой
layout_line3.addStretch(1)

# Теперь созданные строки разместим друг под другой:
layout_card = QVBoxLayout()

layout_card.addLayout(layout_line1, stretch=2)
layout_card.addLayout(layout_line2, stretch=8)
layout_card.addStretch(1)
layout_card.addLayout(layout_line3, stretch=1)
layout_card.addStretch(1)
layout_card.setSpacing(5) # пробелы между содержимым


AnsGroupBox = QGroupBox('Результат теста')
lb_Result = QLabel('прав ты или нет?')
lb_Correct = QLabel('отвеь будет тут!')
layout_res = QVBoxLayout()
layout_res.addWidget(lb_Result, alignment=(Qt.AlignLeft | Qt.AlignTop))
layout_res.addWidget(lb_Correct, alignment=Qt.AlignHCenter, stretch=2)
AnsGroupBox.setLayout(layout_res)
layout_line2.addWidget(AnsGroupBox)

RadioGroupBox.show()
AnsGroupBox.hide()

RadioGroup = QButtonGroup()
RadioGroup.addButton(rbtn_1)
RadioGroup.addButton(rbtn_2)
RadioGroup.addButton(rbtn_3)
RadioGroup.addButton(rbtn_4)

def show_result():
    ''' показатель панель ответов '''
    RadioGroupBox.hide()
    AnsGroupBox.show()
    btn_OK.setText('Следующий вопрос')
def show_question():
    ''' Показатель панель вопросов '''
    RadioGroupBox.show()
    AnsGroupBox.hide()
    btn_OK.setText('Ответить')
    RadioGroup.setExclusive(False)
    rbtn_1.setChecked(False)
    rbtn_2.setChecked(False)
    rbtn_3.setChecked(False)
    rbtn_4.setChecked(False)
    RadioGroup.setExclusive(True)
answers = [rbtn_1, rbtn_2, rbtn_3, rbtn_4]
from random import shuffle 

class Question():
    ''' содержит вопрос, правильный ответ и три неправильных'''
    def __init__(self, question, right_answer, wrong1, wrong2, wrong3):

        self.question = question
        self.right_answer = right_answer
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3
questions_list = []
questions_list.append(Question('Какого цвета нету на флаге Китая', 'Красный', 'Желтый', 'Белый', 'Черный'))
questions_list.append(Question('Государственный язык Аргентины', 'Португальский', 'Испанский', 'Бразильский', 'Английский' ))
questions_list.append(Question('Национальная еда Японии', 'Рис', 'Лапша', 'Креветки', 'Суп'))
questions_list.append(Question('В каком году придумали компьютеры', '1944', '1932', '1954', '1988'))
questions_list.append(Question('У какого животного самый длинный язык', 'хамелеон', 'жираф', 'муравьед', 'Медведь'))
questions_list.append(Question('Какая самая популярная игра в мире', 'fortnite', 'minecraft', 'Cs-Go', 'Roblox'))
questions_list.append(Question('Какая самая большая птица в мире', 'Ястреб', 'обыкновенный страус', 'Императорский пингвин', 'Казуар'))
questions_list.append(Question('Какая самая длинная река в россии', 'Волга', 'Лена', 'Енисей', 'Обь'))
questions_list.append(Question('Продолжи пословицу <<На воре и шапка …>>', 'Блестит', 'Горит', 'Сидит', 'Лежит'))
questions_list.append(Question('Какая самая высокая гора в мире', 'Лхоцзе', 'Чогори', 'Эверест', 'Манаслу'))
def ask(q: Question):
    '''функция записывает значения вопроса и ответов в соответствующие виджеты,
    при этом варианты ответов распределяются случайным образом'''
    shuffle(answers)
    answers[0].setText(q.right_answer)
    answers[1].setText(q.wrong1)
    answers[2].setText(q.wrong2)
    answers[3].setText(q.wrong3)
    lb_Question.setText(q.question)
    lb_Correct.setText(q.right_answer)
    show_question()
def show_correct(res):
    '''показать результат - установим переданный текст в надпись "результат" и покажем нужную панель'''
    lb_Result.setText(res)
    show_result()
def check_answer():
    '''если выбран какой-то вариант ответа, то надо проверить и показать панель ответов'''
    if answers[0].isChecked():
        show_correct('Правильно!')
    else:
        if answers[1].isChecked() or answers[2].isChecked() or answers[3].isShecked():
            show_correct('Неправильно!')
def next_question():
    window.cur_question = window.cur_question + 1
    if window.cur_question >= len(questions_list):
        window.cur_question = 0
    q = questions_list[window.cur_question]
    ask(q)

def click_OK():
    '''определяет, надо ли показывать другой вопрос либо проверить ответ на этот '''
    if btn_OK.text() == 'Ответить':
        check_answer()
    else:
        next_question()

window.cur_question = -1
btn_OK.clicked.connect(click_OK)
next_question()

window.setLayout(layout_card)
window.show()
app.exec()
