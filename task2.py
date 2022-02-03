import sys
import requests
from PyQt5 import uic, QtCore
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QPixmap


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('untitled.ui', self)
        self.search.clicked.connect(self.show_map)
        self.zoom = 16

    def show_map(self):
        map_request = f"https://static-maps.yandex.ru/1.x/?ll={self.coord1.text()},{self.coord2.text()}&z={self.zoom}&&size=450,450&l=map"
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

    def keyPressEvent(self, event):
        if event.key() == QtCore.Qt.Key.Key_PageUp:
            if self.zoom < 19:
                self.zoom += 1
                self.show_map()
        event.accept()
        if event.key() == QtCore.Qt.Key.Key_PageDown:
            if self.zoom > 2:
                self.zoom -= 1
                self.show_map()
        event.accept()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())