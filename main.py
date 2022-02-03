import sys
import requests
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QPixmap


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('untitled.ui', self)
        self.search.clicked.connect(self.show_map)

    def show_map(self):
        print(self.coord1.text())
        print(self.coord2.text())
        map_request = f"https://static-maps.yandex.ru/1.x/?ll={self.coord1.text()},{self.coord2.text()}&z=4&&size=450,450&l=sat "
        print(map_request)
        print('https://static-maps.yandex.ru/1.x/?ll=133.794557,-25.694111&z=4&&size=450,450&l=sat')
        print(map_request == 'https://static-maps.yandex.ru/1.x/?ll=133.794557,-25.694111&z=4&&size=450,450&l=sat')
        response = requests.get(map_request)

        if not response:
            print("Ошибка выполнения запроса:")
            print(map_request)
            print("Http статус:", response.status_code, "(", response.reason, ")")
            sys.exit(1)

        # Запишем полученное изображение в файл.
        map_file = "map.png"
        with open(map_file, "wb") as file:
            file.write(response.content)

        pixmap = QPixmap("map.png")
        self.map_paint.setPixmap(pixmap)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())
