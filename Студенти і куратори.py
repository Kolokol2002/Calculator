class Human:
    def __init__(self, name):
        self.name = name

    def answer_question(self, question):
        return "Очень интересный вопрос! Не знаю."


class Student(Human):
    def ask_question(self, someone, question):
        return f"{someone.name}, {question}\n" + someone.answer_question(question) + "\n"


class Curator(Human):
    def answer_question(self, question):
        if question == "мне грустненько, что делать?":
            return "Держись, всё получится. Хочешь видео с котиками?"
        else:
            return super().answer_question(question)


class Mentor(Human):
    def answer_question(self, question):
        if question == "мне грустненько, что делать?":
            return "Отдохни и возвращайся с вопросами по теории."
        else:
            return super().answer_question(question)

class CodeReviewer(Human):
    def answer_question(self, question):
        if question == "что не так с моим проектом?":
            return "О, вопрос про проект, это я люблю."
        else:
            return super().answer_question(question)


student1 = Student('Тимофей')
curator = Curator('Марина')
mentor = Mentor('Ира')
reviewer = CodeReviewer('Евгений')
friend = Human('Виталя')

print(student1.ask_question(curator, 'мне грустненько, что делать?'))
print(student1.ask_question(mentor, 'мне грустненько, что делать?'))
print(student1.ask_question(reviewer, 'когда каникулы?'))
print(student1.ask_question(reviewer, 'что не так с моим проектом?'))
print(student1.ask_question(friend, 'как устроиться на работу питонистом?'))
print(student1.ask_question(mentor, 'как устроиться работать питонистом?'))