import smtplib
import os
from dotenv import load_dotenv
server = smtplib.SMTP_SSL('smtp.yandex.ru:465')
email_from = 'alex.chisnikov@yandex.ru'
email_to = 'chisnikoff@mail.ru'
title = '''\
From: alex.chisnikov@yandex.ru
To: chisnikoff@mail.ru
Subject: Приглашение!
Content-Type: text/plain; charset="UTF-8";\n'''
text = '''
Привет, %friend_name%! %my_name% приглашает тебя на сайт %website%!

%website% — это новая версия онлайн-курса по программированию.
Изучаем Python и не только. Решаем задачи. Получаем ревью от преподавателя.

Как будет проходить ваше обучение на %website%?

→ Попрактикуешься на реальных кейсах.
Задачи от тимлидов со стажем от 10 лет в программировании.
→ Будешь учиться без стресса и бессонных ночей.
Задачи не «сгорят» и не уйдут к другому. Занимайся в удобное время и ровно столько, сколько можешь.
→ Подготовишь крепкое резюме.
Все проекты — они же решение наших задачек — можно разместить на твоём GitHub. Работодатели такое оценят.

Регистрируйся → %website%
На курсы, которые еще не вышли, можно подписаться и получить уведомление о релизе сразу на имейл.'''
url_name = 'https://dvmn.org/referrals/1nONToZb43Syef1wxtxbL9fnefqHXxTPicDCCv3A/'
friend_name = 'Игорь'
my_name = 'Алексей'
text = text.replace('%friend_name%', friend_name)
text = text.replace('%my_name%', my_name)
text = text.replace('%website%', url_name)
letter = title + text
load_dotenv()
login = os.getenv("YA_LOGIN")
password = os.getenv("YA_PASSWORD")
letter = letter.encode("UTF-8")
server.login(login, password)
server.sendmail(email_from, email_to, letter)
server.quit()