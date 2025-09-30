import data
import sender_stand_request

def positive_assert_kit(name):
    #Creacion de un nuevo kit
    create_kit_response = sender_stand_request.create_kit(name)
    #Ultimo registro en la base de datos al crear un kit
    get_database_kit_response = sender_stand_request.get_database_kits(name)

    #Se ha creado el kit con exito
    assert create_kit_response.status_code == 201
    #El valor de la clave nombe de la respuesta es igual al enviado en la solicitud.
    assert create_kit_response.json()["name"] == name
    #El nombre registrado en la base de datos es igual al enviado en la solicitud.
    assert get_database_kit_response == name

def negative_assert_kit(name):
    #Creacion de un nuevo kit
    create_kit_response = sender_stand_request.create_kit(name)
    #Ultimo registro en la base de datos al crear un kit.
    get_database_kit_response = sender_stand_request.get_database_kits(name)

    #No se creo un kit
    assert create_kit_response.status_code == 400
    #Se envia un mensaje de error
    assert create_kit_response.json()["message"] == "El nombre debe contener sólo letras latino, un espacio y un guión. De 2 a 15 caracteres"
    #No se realizo un nuevo registro
    assert get_database_kit_response == "Not new record"


#Positive tests
def test_crete_kit_1_character_user_success_response():
    positive_assert_kit(data.name_1_characters)

def test_crete_kit_511_character_user_success_response():
    positive_assert_kit(data.name_511_characters)

def test_crete_kit_special_character_user_success_response():
    positive_assert_kit(data.name_special_characters)

def test_crete_kit_space_character_user_success_response():
    positive_assert_kit(data.name_space_characters)

def test_crete_kit_number_character_user_success_response():
    positive_assert_kit(data.name_number_characters)


#Negative tests
def test_crete_kit_0_characters_error_response():
    negative_assert_kit(data.name_0_characters)

def test_crete_kit_512_characters_error_response():
    negative_assert_kit(data.name_512_characters)

def test_crete_kit_None_character_error_response():
    negative_assert_kit(data.name_no_characters)

def test_crete_kit_number_characters_error_response():
    negative_assert_kit(data.name_different_type_characters)