#Гончаров Сергей, Инженер по тестированию плюс, 13-я когорта, Дипломный проект

import sender_stand_requests



def get_order_track():
    track_number = sender_stand_requests.create_order()
    return track_number.json()["track"]



def test_create_and_get_order_track_success_response():
    track_number = get_order_track()
    get_response = sender_stand_requests.get_order_body(track_number)
    #Проверка, что код ответа равен 200
    assert get_response.status_code == 200