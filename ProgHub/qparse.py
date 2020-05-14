from selenium import webdriver



class ProgParser(object):

    def __init__(self, driver, lang):
        self.driver = driver
        self.lang = lang

    def parse(self):
        self.go_to_test_page()
        self.parse_question_page()

    def go_to_test_page(self):

        self.driver.get('https://proghub.ru/tests')
        self.driver.get('https://proghub.ru/t/python-3-basic')

    def parse_question_page(self):
        question = Question
        self.fill_question_text(question)
        print(question)

    def fill_question_text(self, question):
        question_text_elem = self.driver.find_elements_by_class_name('question__title')
        question.text = question_text_elem.text


def main():
    driver = webdriver.Chrome()
    parser = ProgParser(driver, 'python')
    parser.parse()


if __name__ == "__main__":
    main()