
linkedin_url = "https://br.linkedin.com/"
jobs_linkedin_url = "https://www.linkedin.com/jobs/search/?currentJobId=3916088648&f_AL=true&f_TPR=r86400&f_WT=2&geoId=106057199&keywords=(sdet%20OR%20qa%20OR%20quality%20assurance%20OR%20teste%20OR%20automa%C3%A7%C3%A3o)&location=Brazil&origin=JOB_SEARCH_PAGE_SEARCH_BUTTON&refresh=true"

scroll_div="(//div[contains(@class, 'jobs-search-results-list')])[3]"

job_cards = "//div[@data-view-name='job-card']"
promoted_job_cards = "//div/ul/li[text()='Promoted']"

login_button_xpath = "/html/body/nav/a[3]"

username_input_text_xpath = "//*[@id='session_key']"
password_input_text_xpath = "//*[@id='session_password']"

press_login_button_xpath = "//button[@data-id='sign-in-form__submit-btn']"

messages_in_dashboard_xpath = "//*[@id='messaging-nav-item']/a"
new_message_button_xpath = '//*[@data-control-name="compose_message"]'

message_for_who_input_text = 'msg-connections-typeahead__search-field'
message_text_css_selector = 'div.msg-form__contenteditable > p'
