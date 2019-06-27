Feature: DDG Search

  @fixture.browser.firefox
  Rule: Search phrase
    Background: Access the page
      Given access http://google.com

    Example: Check page layout
      Background: Access the page
        Given access http://ddg.gg
      Then bar is visible in id search_form_input_homepage

    @skip
    Example: Check page layout
      Background: Access the page
        Given access http://ddg.gg
      When search live de python
      And click in id search_button_homepage
      Then dunossauro is found
    
    Example: Check page layout
      Background: Access the page
        Given access http://ddg.gg
      When search hypy python
      And click in id search_button_homepage
      Then avanzzzi is found
