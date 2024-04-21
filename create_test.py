# Наталья Панкратова, 13-я когорта - Финальный проект. Инженер по тестированию плюс.
import sender_stand_request
# Тест 1
def test_status_response_receipt_of_the_order_for_the_track():
    track = sender_stand_request.post_new_orders().json()["track"]
    orders_response = sender_stand_request.get_orders_treck(track)
    assert orders_response.status_code == 200