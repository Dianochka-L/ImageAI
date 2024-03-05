from PIL import Image, ImageDraw, ImageFont, ImageFilter, ImageEnhance
from app.controllers.errors import InvalidFactor, InvalidFilter
from typing import Tuple


def save_image(image: Image, path: str) -> None:
    """
    Функция сохраняет изображение, которе ей передают
    Args:
        im (Image): фотография, которую нужно сохранить
        path (str): путь, по которому нужно сохранить изображние
    """
    image.save(path)

def scale_image_by_factor(image: Image, factor: int) -> Image:
    """
    Увеличивает/сжимает изображение на коэффициент
    Args:
        image (Image): изображение, которое нужно трансформировать
        factor (int): коэффициент для трансформации

    Returns:
        Image: сжатое/увеличенное изображение
    """
    if factor <= 0:
        raise InvalidFactor("Коэффициент должен быть больше нуля")
    return image.resize(round(image.width * factor), round(image.height * factor))

def rotate_image(image: Image, angle: int) -> Image:
    """
    Поворачивает изабражение на указанный угол
    Args:
        image (Image): изображение для поворота
        angle (int): угол для поворота

    Returns:
        Image: повернутое изображение
    """
    return image.rotate(angle, expand=True)

def add_text(image: Image, text: str, topleft: int, size: int, colour: Tuple[int]) -> Image:
    """
    Добавляет текст на изображение в указанное место
    Args:
        image (Image): изображние, на которое добавляется текст
        text (str): текст, которй нужно добавить
        topleft (int): расположение верхнего левого угла тектового поля
        size (int): размер шрифта
        colour (Tuple[int]): цвет шрифта

    Returns:
        Image: Изобаржение с добавленным текстом
    """
    font = ImageFont.truetype("./fonts/FiraSans-Regular.ttf", size)
    draw = ImageDraw.Draw(image)
    draw.text(topleft, text, font=font, fill=colour)
    return image

def apply_filter(image: Image, filter_name: str) -> Image:
    filters = {
        "Blur": ImageFilter.BLUR,
        "Contour": ImageFilter.CONTOUR,
        "Detail": ImageFilter.DETAIL,
        "Edge Enhance": ImageFilter.EDGE_ENHANCE,
        "Edge Enhance More": ImageFilter.EDGE_ENHANCE_MORE,
        "Emboss": ImageFilter.EMBOSS,
        "Find Edges": ImageFilter.FIND_EDGES,
        "Sharpen": ImageFilter.SHARPEN,
        "Smooth": ImageFilter.SMOOTH,
        "Smooth More": ImageFilter.SMOOTH_MORE,
        "Box Blur": ImageFilter.BoxBlur(10),
        "Gaussian Blur": ImageFilter.GaussianBlur(25),
        "Unsharp Mark": ImageFilter.UnsharpMask,
    }
    if filter_name not in filters:
        raise InvalidFilter("Указанный фильтр не найден")
    return image.filter(filters[filter_name])

def adjust_brightness(image: Image, brightness_factor: float) -> Image:
    """
    Изменяет яркость изображения.
    Args:
        image (Image): Изображение, яркость которого нужно изменить.
        brightness_factor (float): Коэффициент изменения яркости.
                                  1.0 означает неизмененную яркость.
                                  Значение < 1.0 означает уменьшение яркости.
                                  Значение > 1.0 означает увеличение яркости.
    Returns:
        Image: Измененное изображение.
    """
    if brightness_factor <= 0:
        raise InvalidFactor("Коэффициент изменения якркости должен быть больше нуля")
    
    enhancer = ImageEnhance.Brightness(image)
    adjusted_image = enhancer.enhance(brightness_factor)
    return adjusted_image

def adjust_saturation(image: Image, saturation_factor: float) -> Image:
    """
    Изменяет насыщенность изображения.
    Args:
        image (Image): Изображение, насыщенность которого нужно изменить.
        saturation_factor (float): Коэффициент изменения насыщенности.
                                   1.0 означает неизмененную насыщенность.
                                   Значение < 1.0 означает уменьшение насыщенности.
                                   Значение > 1.0 означает увеличение насыщенности.
    Returns:
        Image: Измененное изображение.
    """
    if saturation_factor <= 0:
        raise InvalidFactor("Коэффициент изменения насыщенности должен быть больше нуля")
    
    enhancer = ImageEnhance.Color(image)
    adjusted_image = enhancer.enhance(saturation_factor)
    return adjusted_image

def adjust_contrast(image: Image, contrast_factor: float) -> Image:
    """
    Изменяет контраст изображения.
    Args:
        image (Image): Изображение, контраст которого нужно изменить.
        contrast_factor (float): Коэффицинет изменения контраста.
                                 1.0 означает неизмененный контраст.
                                 Значение < 1.0 означает уменьшение контраста.
                                 Значение > 1.0 означает увеличение контраста.
    Returns:
        Image: Измененное изображение.
    """
    if contrast_factor <= 0:
        raise InvalidFactor("Коэффициент изменеия контарста должен быть больше нуля")
    
    enhancer = ImageEnhance.Contrast(image)
    adjusted_image = enhancer.enhance(contrast_factor)
    return adjusted_image
