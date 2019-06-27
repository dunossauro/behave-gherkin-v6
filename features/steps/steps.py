from behave import given, then, when


@given('access {url}')
def step_impl(context, url):
    context.browser.get(url)


@then('bar is visible in id {element_id}')
def check_id_in_page(context, element_id):
    assert context.browser.find_element_by_id(element_id)
    assert False


@when('search {text}')
def search_text(context, text):
    context.browser.find_element_by_id(
        'search_form_input_homepage'
    ).send_keys(text)


@when('click in id {element_id}')
def click_id_in_page(context, element_id):
    context.browser.find_element_by_id(element_id).click()


@then('{text} is found')
def text_found(context, text):
    assert text in context.browser.page_source
