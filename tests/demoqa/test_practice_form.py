import allure
from allure_commons.types import Severity

from pages.registration_page import RegistrationPage


@allure.tag("web")
@allure.label("owner", "aa.eliseev")
@allure.severity(Severity.CRITICAL)
@allure.feature("Форма регистрации")
@allure.story("Заполнение формы регистрации")
@allure.title("Отправка формы регистрации и проверка корректности отправленных значений")
@allure.link("https://github.com", name="github")
def test_practice_form(setup_browser):
    registration = RegistrationPage()

    registration.browser_open("/automation-practice-form")

    """ WHEN """
    registration.fill_first_name("Алексей")
    registration.fill_last_name("Елисеев")
    registration.fill_email("qaguru@test.com")
    registration.fill_gender_male()
    registration.fill_mobile_number("9999999999")

    registration.fill_birthday("1992", "April", "04")
    registration.fill_subjects("English")
    registration.fill_hobbies()

    registration.upload_picture("test_image.jpg")
    registration.fill_current_address("Test Country, test city, test street, test house")
    registration.fill_state_and_city()
    registration.click_submit_button()

    """ THEN """
    registration.assert_value("Алексей Елисеев", "qaguru@test.com", "Male", "9999999999", "04 April,1992",
                              "English",
                              "Reading, Sports", "test_image.jpg",
                              "Test Country, test city, test street, test house",
                              "NCR Noida")
