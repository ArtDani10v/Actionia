# backend/setup.py

from setuptools import setup, find_packages

setup(
    name="Actionia",  # Имя проекта
    version="0.1",  # Начальная версия
    author="ArtDani10v",  # Имя разработчика
    author_email="artdanilovru@gmail.com",  # Электронная почта
    description="Инновационный проект для автоматизации бизнес процессов",
    packages=find_packages(),  # Автоматически находит и добавляет все пакеты
    install_requires=[
        'flask==2.0.3',
        'python-dotenv==0.19.2',
    ],  # Здесь мы можем указать зависимости (если есть)
)
