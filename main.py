import smtplib
server = smtplib.SMTP_SSL('smtp.yandex.ru:465')
login = 'alex.chisnikov'
password = 'vuxnivvwfvtjwyhw'
email_from = 'alex.chisnikov@yandex.ru'
email_to = 'chisnikoff@mail.ru'
url_name = 'https://dvmn.org/referrals/1nONToZb43Syef1wxtxbL9fnefqHXxTPicDCCv3A/'
friend_name = 'Игорь'
my_name = 'Алексей'
title = '''\
From: alex.chisnikov@yandex.ru
To: chisnikoff@mail.ru
Subject: Приглашение!
Content-Type: text/plain; charset="UTF-8";\n'''
text = '''
Привет, {fr}! {my} приглашает тебя на сайт {url}!

{url} — это новая версия онлайн-курса по программированию. 
Изучаем Python и не только. Решаем задачи. Получаем ревью от преподавателя. 

Как будет проходить ваше обучение на {url}? 

→ Попрактикуешься на реальных кейсах. 
Задачи от тимлидов со стажем от 10 лет в программировании.
→ Будешь учиться без стресса и бессонных ночей. 
Задачи не «сгорят» и не уйдут к другому. Занимайся в удобное время и ровно столько, сколько можешь.
→ Подготовишь крепкое резюме.
Все проекты — они же решение наших задачек — можно разместить на твоём GitHub. Работодатели такое оценят. 

Регистрируйся → {url}  
На курсы, которые еще не вышли, можно подписаться и получить уведомление о релизе сразу на имейл.'''
text = text.format(url = url_name, fr = friend_name, my = my_name)
letter = title + text
letter = letter.encode("UTF-8")
print(letter)
server.login(login, password)
server.sendmail(email_from, email_to, letter)
server.quit()

