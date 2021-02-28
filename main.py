from instabot import Bot

"""Colocando este codigo: mi_bot = Bot(filter_users=False) envia solicitudes a cuentas privadas
"""

mi_bot = Bot()
mi_bot.login(username='vladimirgutierrez7', password='password_example')
mi_bot.follow_followers('padavidnesher')
