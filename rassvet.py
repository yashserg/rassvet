# -*- coding: utf-8 -*-
import telebot
import random
from datetime import datetime

rassvet = telebot.TeleBot("556858523:AAGyteW9z5FMQuW8rgo1me8FehZY3oZ4FaU")

#Встречаем гостей
greeting = [u'бармен', u'официант', u'кок', u'алоха', u'привет', u'здорово', u'как жизнь']
greeting_answer = ['Здорово, морячок!', 'Как сам, братишка?', 'Виделись!', 'Ты кто?', 'Выпить пришел?', 'Есть свежий ром!', 'Тихо! Капитан на камбузе...']

#КинДзаДза
kindzadza = [u'ку', u'пепелац', u'кю']
kindzadza_answer = ['КЮ!', 'Я очень люблю ПЖ!', 'Радиус своей планеты думай!', 'Скрипач не нужен, родной...', 'Как же вы это пепелац без гравицапы выкатываете из гаража?..', 'У тебя в голове мозги или кю?!']

#Напитки - тут только РОМ
drinks = [u'ром', u'рому', u'рому!', u'виски', u'выпьем', u'налей', u'наливай']
drinks_answer = ['С тобой - выпью. Нравишься ты мне, флибустьер.', 'Чем закусим, пират?', 'Только с разрешения капитана!', 'Тебе 18-то есть?! Паспорт покажи!!! А, ну если такая сабля...', 'Угости бармена, друг!', 'Держи, пока кэп не видит']

#Тут РОМа нет!
otherdrinks = [u'пивка', u'дай пива', u'пива', u'пиво', u'виски', u'водка', u'квас', u'вода', u'воды', u'текила', u'текилы', u'коньяк', u'писко', u'мескаль', u'вотка', u'вотки', u'налей водички', u'коньяку', u'пивка', u'вина', u'винца', u'грог', u'грога', u'грогу', u'глинтвейн', u'бренди', u'джин', u'джина', u'джину', u'спирта', u'спирту', u'спирт', u'самогона', u'самогону', u'самогонки', u'самогон', u'первак', u'перваку']
otherdrinks_answer = ['Ты мне объясни, как это из рома сделать?', 'В море? Где я тебе возьму это в море?!', 'Капитан сказал составить список всех, кто пьёт не ром. Как фамилия, матрос?', 'Тебе умыться или выпить?! Умывальник на баке!']

#Ищем капитана
cap = [u'где капитан', u'капитан', u'кэп']
cap_answer = ['Кэп в каюте, встать не может.', 'Ты мне расскажи, я ему передам!', 'Найди Ксю или Билли Бонса, они знают.']

#Закуска
food = [u'закуска', u'сосиски!', u'сосиски']
food_answer = ['Нету.', 'Приноси - зажарим!', 'Где???']

#ы
yyy = [u'ы', u'ыыы']
yyy_answer = ['ЫЫЫЫЫЫЫЫ....']

#команды
other = [u'угощаю', u'держи']
other_answer = ['Ну спасибо!', 'Эх, сейчас нажремся, пока капитан не видит!']

#Сиськи!
breasts = [u'сиськи', u'сиськи!']
breast_answer = ['Покажи!', 'Ты смотри! Точно, сиськи!', 'Какой размер интересует?', 'Сиськи в тесте - это вкусно!..']

#battle
battle = [u'атакуем', u'атака', u'атакуем!', u'атака!', u'в атаку', u'в атаку!', u'деф', u'деф!', u'в бой', u'в бой!', u'на абордаж', u'враги не дремлют', u'к бою', u'к бою!', u'враг не дремлет']
battle_answer = ['Сабли из ножен! Крюки готовь!', 'Неплохо бы покурить перед боем...', 'Пиастры - в море!', 'Мушкеты заряжай!']

#время
bottime = [u'бармен время', u'бармен сколько времени', u'бармен который час']

#спокиноки
goodnight = [u'бармен спокойной ночи', u'бармен сладких снов']
goodnight_answer = ['Спокойной ночи. Битву не проспи!']


@rassvet.message_handler(content_types=["text"])

def handle_text(message):

	print(message.text)

	if message.text.lower() in greeting:

		ind = random.randint(0,len(greeting_answer)-1)

		rassvet.send_message(message.chat.id, greeting_answer[ind])

	elif message.text.lower() in kindzadza:

		ind = random.randint(0,len(kindzadza_answer)-1)

		rassvet.send_message(message.chat.id, kindzadza_answer[ind])

	elif message.text.lower() in drinks:

		ind = random.randint(0,len(drinks_answer)-1)

		rassvet.send_message(message.chat.id, drinks_answer[ind])

	elif message.text.lower() in otherdrinks:

		ind = random.randint(0,len(otherdrinks_answer)-1)

		rassvet.send_message(message.chat.id, otherdrinks_answer[ind])

	elif message.text.lower() in cap:

		ind = random.randint(0,len(cap_answer)-1)

		rassvet.send_message(message.chat.id, cap_answer[ind])

	elif message.text.lower() in food:

		ind = random.randint(0,len(food_answer)-1)

		rassvet.send_message(message.chat.id, food_answer[ind])

	elif message.text.lower() in yyy:

		ind = random.randint(0,len(yyy_answer)-1)

		rassvet.send_message(message.chat.id, yyy_answer[ind])

	elif message.text.lower() in breasts:

		ind = random.randint(0,len(breast_answer)-1)

		rassvet.send_message(message.chat.id, breast_answer[ind])

	elif message.text.lower() in battle:

		ind = random.randint(0,len(battle_answer)-1)

		rassvet.send_message(message.chat.id, battle_answer[ind])

	elif message.text.lower() in bottime:

		now = datetime.strftime(datetime.now(), "%Y.%m.%d %H:%M:%S")

		rassvet.send_message(message.chat.id, now)

	elif message.text.lower() in goodnight:

		ind = random.randint(0,len(goodnight_answer)-1)

		rassvet.send_message(message.chat.id, goodnight_answer[ind])

		
#	else:
#		rassvet.send_message(message.from_user.id, "Семь футов под килем, моряк! Иди к морскому дьяволу!")

rassvet.polling(none_stop=True, interval=0)

# Тут обработаем требования '/start' и '/help'.
@rassvet.message_handler(commands=['start', 'help'])
def handle_start_help(message):
    pass

 # Здесь потом будут файлы и аудио. Не знаю зачем, но пригодится.
@rassvet.message_handler(content_types=['document', 'audio'])
def handle_document_audio(message):
    pass

rassvet.polling(none_stop=True, interval=0)

