import numpy as np

from PyQt5.QtWidgets import QFileDialog
from PIL import Image
from PyQt5.QtGui import QPixmap, QImage

from app.controllers.utils import adjust_brightness, adjust_contrast, adjust_saturation

class MainController():
    def __init__(self, view):
        self.view = view
        self.connect_signals()
        
        self.brightness_factor = 1
        self.contrast_factor = 1
        self.saturation_factor = 1
        
        self.image = None
        self.image_path = ""
        self.original_image = None
        
    def show(self):
        """Запускает отображение
        """
        self.view.show()
        
    def connect_signals(self):
        """Подключаем слоты к сигналам
        """
        self.view.brightnessSlider.valueChanged['int'].connect(self.set_brightness)
        self.view.saturationSlider.valueChanged['int'].connect(self.set_saturation)
        self.view.contrastSlider.valueChanged['int'].connect(self.set_contrast)
        
    def open_image(self) -> None:
        """Открывает изображение с помощью файлового диалогового окна и сохраняет путь
        """
        # Открываем файловое диалоговое окно для выбора изображения
        file_dialog = QFileDialog(self.view)
        file_dialog.setNameFilter("Images (*.png *.jpg *.bmp)")
        file_dialog.setViewMode(QFileDialog.Detail)
        file_dialog.setFileMode(QFileDialog.ExistingFiles)
        if file_dialog.exec():
            print("File dialog is open")
            selected_files = file_dialog.selectedFiles()
            if selected_files:
                # Выбираем только первый выбранный файл
                image_path = selected_files[0]
                self.image_path = image_path

                # Загружаем изображение с помощью Pillow
                self.image = Image.open(image_path)
                self.original_image = self.image
                
                # Пример: обновляем заголовок окна с именем выбранного файла
                self.view.setWindowTitle(f"Image Editor - {image_path}")
                
                # Отображает изображение в интерфейсе
                self.update_image()
                
    def update_image(self) -> None:
        """Отображает изображение в интерфейсе программы
        """
        # Преобразование изображения в массив байтов
        image_rgb = self.image.convert("RGB")  # Преобразуем в RGB для цветных изображений
        image_array = np.array(image_rgb)
        height, width, channel = image_array.shape
        bytes_per_line = channel * width
        qimage = QImage(image_array.data, width, height, bytes_per_line, QImage.Format_RGB888)
        
        # Преобразование QImage в QPixmap
        qpixmap = QPixmap.fromImage(qimage)
        self.view.mainImage.setPixmap(qpixmap)
        
    def apply_all(self):
        self.image = adjust_brightness(self.original_image, self.brightness_factor)
        self.image= adjust_saturation(self.image, self.saturation_factor)
        self.image = adjust_contrast(self.image, self.contrast_factor)
        
    def set_brightness(self, value: float) -> None:
        """
        Слот для изменения якрости
        Args:
            value (float): Значение слайдера яркости
        """
        self.brightness_factor = (value / 100)
        self.apply_all()
        self.update_image()
        
    def set_saturation(self, value: float) -> None:
        """
        Слот для изменения насыщенности
        Args:
            value (float): Значение слайдера насыщенности
        """
        self.saturation_factor = (value / 100)
        self.apply_all()
        self.update_image()
        
    def set_contrast(self, value: float) -> None:
        """
        Слот для изменения контраста
        Args:
            value (float): Значение слайдера насыщенности
        """
        self.contrast_factor = (value / 100)
        self.apply_all()
        self.update_image() 
        