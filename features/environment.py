from behave import use_fixture
from fixtures.firefox import browser_firefox


def before_tag(context, tag):
    if tag == "fixture.browser.firefox":
        use_fixture(browser_firefox, context, timeout=10)
    if tag == "skip":
        context.scenario.skip()
