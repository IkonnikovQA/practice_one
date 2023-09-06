import time

from selene import browser, have, be
from faker import Faker
faker_data = Faker('ru_RU')


def test_demoqa_forms():
    browser.open('https://demoqa.com/automation-practice-form')
    browser.element('[id="firstName"]').should(be.visible).type(faker_data.first_name())
    browser.element('[id="lastName').should(be.visible).type(faker_data.last_name())
    browser.element('[id="userEmail"]').should(be.visible).type(faker_data.email())
    browser.element('[for="gender-radio-1"]').click()
    browser.element('[id="userNumber"]').should(be.visible).type(faker_data.msisdn())
    browser.element('[id="dateOfBirthInput"]').click()
    browser.element('[class="react-datepicker__year-select"]').click().type("1992").click()
    browser.element('[class="react-datepicker__month-select"]').click().type("May").click()
    browser.element('[class="react-datepicker__day react-datepicker__day--013"]').click()
    browser.element('[for="hobbies-checkbox-1"]').click()
    browser.element('[for="hobbies-checkbox-2"]').click()
    browser.element('[for="hobbies-checkbox-3"]').click()
    browser.element('#uploadPicture').send_keys('C:/Users/atlet/Desktop/newnewnew')
    browser.element('[id="currentAddress"]').send_keys("Where money, Lebovski?")
