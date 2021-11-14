# spb_medicine

Данный репозиторий предназначается для хранения данных по треку №1 "Доступные лекарства для всех" хакатона HACK AI, проводимого в Санкт-Петербурге (команда GPOWER).

Версия python: 3.7.0

Импортируемые библиотеки: 
- pandas (0.23.4), numpy (1.19.5) - работа с табличными данными
- seaborn (0.11.2), matplotlib (2.2.3) - визуализация
- sklearn (0.19.2) - API для создания математических моделей

Файлы в репозитории:
- Презентация.pdf - презентация проекта в формате PDF
- Презентация.pptx - презентация проекта в формате PPTX
- Data_Preproccessing.ipynb - ноутбук с предобработкой данных (объединение, слияние с внешней информацией) и выгрузкой в формат CSV. Для успешной загрузки в папке с ноутбуком должны лежать файлы формата CSV с данными по складским запасам, реализации препаратов, а также внешние данные: заболеваемость COVID-19, температура, население и координаты городов с наибольшим населением
- Model.ipynb - ноутбук с моделированием объединенных данных и выгрузкой полученных результатов в формат JSON. Для успешной загрузки в папке с ноутбуком должны лежать файлы формата CSV с объединенными данными
- GPOWER.rar - архив, содержащий в себе:
- - GPOWER.exe - исполняемый файл программы с пользовательским интерфейсом реализации простроенных моделей
- - results_final.json - файл формата JSON, содержащий в себе веса моделей
- - button.png - файл-изображение кнопок
- - прочие файлы .dll, .json и т. д., содержащие в себе необходимые библиотеки для работы приложения
