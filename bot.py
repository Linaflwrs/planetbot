import logging 
import ephem #модуль ипортируется вначале кода
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

logging.basicConfig(filename='bot.log', level=logging.INFO)

def talk_to_me(update, context):
    user_text = update.message.text 
    print(user_text)
    update.message.reply_text(user_text)

def main():
    
    mybot = Updater("1310987028:AAFOWcGGxF7Uz8Qzm55qDuxU-idpYJix5hY", use_context=True)
    dp = mybot.dispatcher
    dp.add_handler(CommandHandler('planet', get_constellation))
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))
    logging.info("bot was waiting ffor you")
    mybot.start_polling()
    mybot.idle()

def greet_user(update, context):
    print('Вызван /start')
    update.message.reply_text('Привет, пользователь! Ты вызвал команду /start')

def get_constellation(update, context):
    print('Вызвана планета/start')
    planet_name = update.message.text.split()[-1] #сплит разделит текст от user по пробелу на отдельный словарь и добавили последний элемент из списка
    planets = {'Mercury': ephem.Mercury('2020/12/05'), 'Venus': ephem.Venus('2020/12/05'), 'Mars': ephem.Mars('2020/12/05'), 'Jupiter': ephem.Jupiter('2020/12/05'), 'Saturn': ephem.Saturn('2020/12/05'), 'Uranus': ephem.Uranus('2020/12/05'), 'Neptune': ephem.Neptune('2020/12/05'), 'Pluto': ephem.Pluto('2020/12/05')}
    # Создан словарь планет с указанной датой - ключем
    if planet_name in planets:
        planet = planets[planet_name]
        constellation = ephem.constellation(planet)
        update.message.reply_text(constellation)# мы скопировали из функции talk to me ответ полученный в консоли и перенаправляем в ответ на телеграмм
    else: 
        update.message.reply_text('Wrong: This planet not definde')#дополнительный ответ в случае неправильного ввода
     
main()

