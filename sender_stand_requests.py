#Гончаров Сергей, Инженер по тестированию плюс, 13-я когорта, Дипломный проект

import requests
import configuration
import data



#Запрос на создание нового заказа
def create_order():
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDER,
           json=data.order_body)



def get_order_body(track_number):
    return requests.get(configuration.URL_SERVICE + configuration.GET_ORDER,
           params={"t": track_number})