# spb_medicine

Данный репозиторий предназначается для хранения данных по треку №1 "Доступные лекарства для всех" хакатона HACK AI, проводимого в Санкт-Петербурге (команда GPOWER).

Версия python: 3.7.0
Версия ОС: Windows 10 21h1

## Импортируемые библиотеки: 
- pandas (0.23.4), numpy (1.19.5) - работа с табличными данными
- seaborn (0.11.2), matplotlib (2.2.3) - визуализация
- sklearn (0.19.2) - API для создания математических моделей

## Файлы в репозитории:
- Презентация.pdf - презентация проекта в формате PDF
- Презентация.pptx - презентация проекта в формате PPTX
- Data_Preproccessing.ipynb - ноутбук с предобработкой данных (объединение, слияние с внешней информацией) и выгрузкой в формат CSV. Для успешной загрузки в папке с ноутбуком должны лежать файлы формата CSV с данными по складским запасам, реализации препаратов, а также внешние данные: заболеваемость COVID-19, температура, население и координаты городов с наибольшим населением
- Model.ipynb - ноутбук с моделированием объединенных данных и выгрузкой полученных результатов в формат JSON. Для успешной загрузки в папке с ноутбуком должны лежать файлы формата CSV с объединенными данными

Архив с исполняемым файлом программы GPOWER по ссылке:
GPOWER.rar - архив, содержащий в себе:
- GPOWER.exe - исполняемый файл программы с пользовательским интерфейсом реализации простроенных моделей
- results_final.json - файл формата JSON, содержащий в себе веса моделей
- button.png - файл-изображение кнопок
- прочие файлы .dll, .json и т. д., содержащие в себе необходимые библиотеки для работы приложения

## Необходимы ссылки для запуска файлов .ipynb:
- https://drive.google.com/file/d/12_R2Nt5YwHuXMMl8MP7lzvokLtqnzlAL/view?usp=sharing - данные о лекарствах на складах
- https://drive.google.com/file/d/1nbElTzDtn1TGxyIBay7sBC5jq5NKwTRi/view?usp=sharing - данные о реализованных лекарствах
- https://drive.google.com/file/d/14CWDYLqUMt3OH7BhGyYbEu4xiqiXV3r9/view?usp=sharing - данные о заражаемости COVID-19
- https://drive.google.com/file/d/1z1emKPcQXlcJ__WYefKSkPgZs_RRA7lQ/view?usp=sharing - данные о погоде
- https://drive.google.com/file/d/18NIGQFF2P9OAqTYWUK9UY8tjAs7pngvT/view?usp=sharing - данные о населении и координатах
- https://drive.google.com/file/d/1-35qLzp1DOFXFcN6KzxjPD4juk3F7al8/view?usp=sharing - единый набор данных (объединённый с использованием файла Data_Preproccessing.ipynb<p>
- https://drive.google.com/file/d/1gW0z6V39oQN624JThpFtYdKuaDOYyyvy/view?usp=sharing - архив с исполняемым файлом программы GPOWER

Примечание: отдельные файлы с данными нужны для работы файла Data_Preproccessing.ipynb; единый набор данных нужен для работы файла Model.ipynb и программы с графическим интерфейсом, поставляемой в архиве

## Порядок запуска файлов .ipynb:
- предварительно установить python необходимой версии и все библиотеки, указанные в пункте "Импортируемые библиотеки"
- нажать на необходимый файл .ipynb ![image](https://user-images.githubusercontent.com/67440069/141663617-df0a8fad-faa4-4788-a3f6-a054a69870fb.png)
- нажать на кнопку Raw ![image](https://user-images.githubusercontent.com/67440069/141663650-cebf1b31-91e7-4f60-8b02-50eb2b43df2b.png)
- навести курсор мыши на текст, нажать левую клавишу мыши, далее на клавиатуре нажать комбинацию клавишь Ctrl+A ![image](https://user-images.githubusercontent.com/67440069/141663688-8440ed43-3349-42d7-b89e-4cc9b2979c65.png)
- навести курсор мыши на синюю область на экране, нажать правую кнопку мыши и в всплывающем окне нажать левой кнопкой мыши на пункт "копировать"
- на рабочем компьютере создать директорию, в ней создать пустой текстовый файл
- открыть созданный текстовый файл, нажать правую кнопку мыши при наведённом курсоре на пустое поле в файле, в всплывающем окне нажать левой кнопкой мыши на пункт "вставить"
- поменять расширение файла с .txt на .ipynb
- в директорию загрузить файлы из пункта "Необходимы ссылки для запуска файлов .ipynb"

