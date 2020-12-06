from selenium import webdriver

class ProgHubParser(object):

    def __init__(self, driver, lang):
        self.driver = driver
        self.lang = lang 

    def parse(self):
        self.go_to_questions_page()

    
    def go_to_questions_page(self):
        self.driver.get('https://proghub.ru/tests')
        blocks = self.driver.find_elements_by_class_name('testCard')

        for elem in blocks:
            print(elem.get_attribute('href'))

def main():
    driver = webdriver.Chrome()
    
    parser = ProgHubParser(driver, 'python')
    parser.parse()

if __name__ == '__main__':
    main()