"""
Locators.py
This is a Python file for Web Locators
"""
class TestLocators:
    # Login locators
    username_name = "username"
    password_name = "password"
    login_button = "//button[@type='submit']"
    forget_password ="//*[@id='app']/div[1]/div/div[1]/div/div[2]/div[2]/form/div[4]/p"
    reset_password_btn = "//button[@type='submit']"
    reset_message = "//*[@id='app']/div[1]/div[1]/div/h6"

    # Admin headers locators
    admin_text = "Admin"
    title = "OrangeHRM"
    user_management = "//*[@id='app']/div[1]/div[1]/header/div[2]/nav/ul/li[1]"
    job = "//*[@id='app']/div[1]/div[1]/header/div[2]/nav/ul/li[2]"
    organization = "//*[@id='app']/div[1]/div[1]/header/div[2]/nav/ul/li[3]"
    qualifications = "//*[@id='app']/div[1]/div[1]/header/div[2]/nav/ul/li[4]"
    nationalities = "//*[@id='app']/div[1]/div[1]/header/div[2]/nav/ul/li[5]"
    corporate_branding = "//*[@id='app']/div[1]/div[1]/header/div[2]/nav/ul/li[6]"
    configuration = "//*[@id='app']/div[1]/div[1]/header/div[2]/nav/ul/li[7]"

    # Side pane locators
    admin = "//*[@id='app']/div[1]/div[1]/aside/nav/div[2]/ul/li[1]"
    pim = "//*[@id='app']/div[1]/div[1]/aside/nav/div[2]/ul/li[2]"
    leave = "//*[@id='app']/div[1]/div[1]/aside/nav/div[2]/ul/li[3]"
    time = "//*[@id='app']/div[1]/div[1]/aside/nav/div[2]/ul/li[4]"
    recruitment = "//*[@id='app']/div[1]/div[1]/aside/nav/div[2]/ul/li[5]"
    my_info = "//*[@id='app']/div[1]/div[1]/aside/nav/div[2]/ul/li[6]"
    performance = "//*[@id='app']/div[1]/div[1]/aside/nav/div[2]/ul/li[7]"
    dashboard = "//*[@id='app']/div[1]/div[1]/aside/nav/div[2]/ul/li[8]"
    directory = "//*[@id='app']/div[1]/div[1]/aside/nav/div[2]/ul/li[9]"
    maintenance = "//*[@id='app']/div[1]/div[1]/aside/nav/div[2]/ul/li[10]"
    claim = "//*[@id='app']/div[1]/div[1]/aside/nav/div[2]/ul/li[11]"
    buzz = "//*[@id='app']/div[1]/div[1]/aside/nav/div[2]/ul/li[12]"
    cancel_button = "//*[@id='app']/div[1]/div[1]/form/div[4]/button[1]"
