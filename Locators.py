class Home_Locators:

    # Увійти до особистого кабінету
    def customer_menu(self):
        return 'customer_menu'

    # Вийти з особистого кабінету
    def customer_menu_show_btn(self):
        return 'customer_menu_show_btn'


class Main_Categories:
    # Категорії товарів (class="nav-container")

    # Книжка
    def books(self):
        return "//div[@class='left-side']/ul[1]/li[1]/a"

    # Електронні книжка
    def el_books(self):
        return "//div[@class='left-side']/ul[1]/li[2]/a"

    # Аудіокниги
    def audio_books(self):
        return "//div[@class='left-side']/ul[1]/li[3]/a"

    # Настільні ігри
    def board_games(self):
        return "//div[@class='left-side']/ul[1]/li[4]/a"

    # Творчість, хобі
    def hobbies(self):
        return "//div[@class='left-side']/ul[1]/li[5]/a"

    # Книжкові аксесуари
    def accessories(self):
        return "//div[@class='left-side']/ul[1]/li[6]/a"

    # Блокноти
    def notebooks(self):
        return "//div[@class='left-side']/ul[1]/li[7]/a"

    # Подарунки
    def presents(self):
        return "//div[@class='left-side']/ul[1]/li[8]/a"

    # Акції та знижки
    def promotions(self):
        return "//div[@class='left-side']/ul[2]/li[1]/a"

    # Подарункові сертифікати
    def certificates(self):
        return "//div[@class='left-side']/ul[2]/li[2]/a"

    # Очікувані – Книжки
    def expected_books(self):
        return "//div[@class='left-side']/ul[2]/li[3]/a"

    # Остання ціна
    def last_price(self):
        return "//div[@class='left-side']/ul[2]/li[4]/a"

    # Доставка 365
    def delivery_365(self):
        return "//div[@class='left-side']/ul[2]/li[5]/a"


class Header_Categories:
    # Інфо-категорії (class="cms-list")

    # Акції
    def prom(self):
        return "//ul[@class='cms-list']/li[1]/a"

    # Про Yakaboo
    def about(self):
        return "//ul[@class='cms-list']/li[2]/a"

    # Доставка
    def delivery(self):
        return "//ul[@class='cms-list']/li[3]/a"

    # Оплата
    def payment(self):
        return "//ul[@class='cms-list']/li[4]/a"

    # Контакти
    def contacts(self):
        return "//ul[@class='cms-list']/li[5]/a"

    # Блог (редірект на https://blog.yakaboo.ua/)
    def blog(self):
        return "//ul[@class='cms-list']/li[6]/a"

    # Блок зміни мови сайту

    # RU версія сайту

    # UA версія сайту