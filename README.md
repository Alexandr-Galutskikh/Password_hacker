# Password_hacker
example1:

> python hack.py localhost 9090

{
    "login" : "su",
    "password" : "fTUe3O99Rre"
}

example2:

> python hack.py localhost 9090

{"login": "admin3", "password": "mlqDz33x"}

Подобрать логин и пароль, через ответы сервера. Получаем через командную строку адрес сервера. Перебираем логины, через список самых популярных логинов. Подбираем пароль через ответ сервера. На верную букву, сервер вызывает исключение, и приходит ответ дольше чем 0.1 секунда по времени. На предыдущих этапах, использовали список самых популярных паролей, и все модификации этих паролей, с заглавными и строчными буквами
