from behave import fixture
from selenium import webdriver
from selenium.webdriver.firefox.options import Options


@fixture
def browser_firefox(context, timeout=30, **kwargs):
    options = Options()
    options.headless = True
    context.browser = webdriver.Firefox(options=options)
    yield context.browser
    context.browser.quit()
