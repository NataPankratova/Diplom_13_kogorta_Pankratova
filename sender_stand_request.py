import configuration
import requests
import data
#Создание заказа
def post_new_orders():
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDERS_PATH,
                         json=data.orders_body)
#Получения заказа по треку заказа.
def get_orders_treck(track):
    return requests.get(configuration.URL_SERVICE + configuration.GET_TRACK_PATH + "?t=" + str(track))
