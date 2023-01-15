from fixture.application import Application


class Yakaboo:
    def init_fixture(self):
        self.fixture = Application()

    def destroy_fixture(self):
        self.fixture.destroy()

    def open_website(self):
        pass