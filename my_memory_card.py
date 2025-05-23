from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout, QHBoxLayout, QRadioButton, QGroupBox, QButtonGroup
from random import shuffle, choice



class Question():
    def __init__(self, q, r_A, w_a1, w_a2, w_a3):
        self.question = q
        self.right_answer = r_A
        self.wrong_answer1 = w_a1
        self.wrong_answer2 = w_a2
        self.wrong_answer3 = w_a3
    

def next_question():
    random_q = choice(questions)
    ask(random_q)
    window.total += 1

def ask(q: Question):
    shuffle(buttons)
    buttons[0].setText(q.right_answer)
    buttons[1].setText(q.wrong_answer1)
    buttons[2].setText(q.wrong_answer2)
    buttons[3].setText(q.wrong_answer3)
    question.setText(q.question)
    true_answ.setText(q.right_answer)
    show_question()

def check_answer():
    if buttons[0].isChecked():
        answ.setText('Правильно')
        window.score += 1
        show_result()
    elif buttons[1].isChecked() or buttons[2].isChecked or buttons[3].isChecked:
        answ.setText('Неправильно')
        show_result()

def show_result():
    RadioGroupBox.hide()
    AnsGroupBox.show()
    button.setText('Следующий вопрос')
    print('Статистика:')
    print('-Всего вопросов:',window.total)
    print('-Правильных ответов:',window.score)
    print('Рейтинг:',window.score/window.total*100,'%')

def show_question():
    RadioGroupBox.show()
    AnsGroupBox.hide()
    button.setText('Ответить')

    RadioGroup.setExclusive(False)
    rbtn1.setChecked(False)
    rbtn2.setChecked(False)
    rbtn3.setChecked(False)
    rbtn4.setChecked(False)
    RadioGroup.setExclusive(True)

def start_test():
    if button.text() == 'Ответить':
        check_answer()
        show_result()
    else:
        show_question()
        next_question()

app = QApplication([])

window = QWidget()
window.resize(750,400)
window.setWindowTitle('Memory Card')
window.score = 0
window.total = 0

question = QLabel('Когда умер Пушкин?')

RadioGroupBox = QGroupBox('Варианты ответа:')
AnsGroupBox = QGroupBox('Результаты')
AnsGroupBox.hide()

rbtn1 = QRadioButton('10 февраля 1837')
rbtn2 = QRadioButton('12 августа 1837')
rbtn3 = QRadioButton('25 октября 2024')
rbtn4 = QRadioButton('1 сентября 1939')

buttons = [rbtn1,rbtn2,rbtn3,rbtn4]
shuffle(buttons)

RadioGroup = QButtonGroup()
RadioGroup.addButton(rbtn1)
RadioGroup.addButton(rbtn2)
RadioGroup.addButton(rbtn3)
RadioGroup.addButton(rbtn4)

answ = QLabel('Правильно/Неправильно')
true_answ = QLabel('10 февраля')

answ_layout = QVBoxLayout()
answ_layout.addWidget(answ)
answ_layout.addWidget(true_answ,alignment = Qt.AlignCenter)
layout_quest = QHBoxLayout()
layout_quest_v1 = QVBoxLayout()
layout_quest_v1.addWidget(rbtn1)
layout_quest_v1.addWidget(rbtn3)
layout_quest_v2 = QVBoxLayout()
layout_quest_v2.addWidget(rbtn2)
layout_quest_v2.addWidget(rbtn4)
layout_quest.addLayout(layout_quest_v1)
layout_quest.addLayout(layout_quest_v2)

button = QPushButton('Ответить')

RadioGroupBox.setLayout(layout_quest)
AnsGroupBox.setLayout(answ_layout)

main_v_line = QVBoxLayout()

h_line1 = QHBoxLayout()
h_line1.addWidget(question)
h_line2 = QHBoxLayout()
h_line2.addWidget(RadioGroupBox)
h_line2.addWidget(AnsGroupBox)
h_line3 = QHBoxLayout()
h_line3.addStretch(1)
h_line3.addWidget(button, stretch = 2)
h_line3.addStretch(1)

main_v_line.addLayout(h_line1)
main_v_line.addLayout(h_line2)
main_v_line.addLayout(h_line3)

button.clicked.connect(start_test)

window.setLayout(main_v_line)


questions = []
questions.append(Question('Я недавно был в...',
                          'Анапе',
                          'канаве',
                          'заброшке',
                          'Египте'
                          )),
questions.append(Question('Дэнчик..',
                          'слазит' ,
                          'сидит',
                          'бегает',
                          'чилит'
                            )),
questions.append(Question('Когда умер Пушкин?',
                          '10 февраля',
                          '12 августа',
                          '25 октября',
                          '1 сентября'))
next_question()


window.show()
app.exec_()

