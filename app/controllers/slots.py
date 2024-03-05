from PIL import Image
from PySide6 import QtCore, QtWidgets
from PySide6.QtGui import QPixmap, QImage
from PySide6.QtWidgets import QFileDialog


class CommonSlots:
    def __init__(self):        
        self.brightness_factor = 1
        self.contrast_factor = 1
        self.saturation_factor = 1
        
        self.image = None
        self.image_path = ""
        self.original_image = None
    def set_brightness(self, value: float) -> None:
        """
        Слот для изменения якрости
        Args:
            value (float): Значение слайдера яркости
        """
        self.brightness_factor = (value / 100)
        self.image = adjust_brightness(self.original_image, self.brightness_factor)
        self.update_image()
        
    def set_saturation(self, value: float) -> None:
        """
        Слот для изменения насыщенности
        Args:
            value (float): Значение слайдера насыщенности
        """
        self.saturation_factor = (value / 100)
        self.image = adjust_saturation(self.original_image, self.saturation_factor)
        self.update_image()
        
    def set_contrast(self, value: float) -> None:
        """
        Слот для изменения контраста
        Args:
            value (float): Значение слайдера насыщенности
        """
        self.contrast_factor = (value / 100)
        self.image = adjust_contrast(self.original_image, self.contrast_factor)
        self.update_image()
        
    def update_image(self) -> None:
        """
        Отображает изображение в интерфейсе программы
        """
        # Преобразование изображения в массив байтов
        image_rgb = self.image.convert("RGB")  # Преобразуем в RGB для цветных изображений
        image_array = np.array(image_rgb)
        height, width, channel = image_array.shape
        bytes_per_line = channel * width
        qimage = QImage(image_array.data, width, height, bytes_per_line, QImage.Format_RGB888)

        # Преобразование QImage в QPixmap
        qpixmap = QPixmap.fromImage(qimage)
        self.label.setPixmap(qpixmap)
        
        
        
    def open_image(self) -> None:
        """
        Открывает изображение с помощью файлового диалогового окна и сохраняет путь
        """
        # Открываем файловое диалоговое окно для выбора изображения
        file_dialog = QFileDialog(self)
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
                
                # Отображает изображение в интерфейсе
                self.update_image()

                # Пример: обновляем заголовок окна с именем выбранного файла
                self.setWindowTitle(f"Image Editor - {image_path}")
                
    def save_image(self) -> None:
        """
        Сохраняет текущее изображение по изночальному пути
        """
        if self.image is not None and self.image_path:
            self.image.save(self.image_path)
            
    def export_image(self) -> None:
        """
        Сохраняет текущее изображение по выбранному пути и с выбранным расширением
        """
        if self.image is not None:
            # Открываем диалоговое окно для выбора пути и формата для сохранения
            file_path, _ = QFileDialog.getSaveFileName(self, "Экспорт изображения", "", "Images (*.png *.jpg *.bmp)")
            if file_path:
                # Сохраняем изображение по выбранному пути и формату
                self.image.save(file_path)
                    