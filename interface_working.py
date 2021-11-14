# -*- coding: utf-8 -*-
"""
Created on Sat Nov 13 16:08:38 2021

@author: jeka_
"""
from tkinter import Button, PhotoImage, LabelFrame, Tk, Entry, Label
from tkinter import messagebox as mb
from tkinter import filedialog as fd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from numpy import array, exp, column_stack
import pandas as pd
import patch
from matplotlib import backend_bases
from tkinter import ttk
import json

root = Tk()

class Block():
    def __init__(self, master):
        
        # словарь для приведения данных из таблиц к виду int
        self.regions ={'Адыгея': 1.0,'Алтай': 4.0,'Алтайский край': 22.0,
                     'Амурская обл.': 28.0,'Архангельская обл.': 29.0,
                     'Астраханская обл.': 30.0,'Башкортостан': 2.0,
                     'Белгородская обл.': 31.0,'Брянская обл.': 32.0,
                     'Бурятия': 3.0,'Владимирская обл.': 33.0,
                     'Волгоградская обл.': 34.0,'Вологодская обл.': 35.0,
                     'Воронежская обл.': 36.0,'Дагестан': 5.0,
                     'Еврейская АО': 79.0,'Забайкальский край': 75.0,
                     'Ивановская обл.': 37.0,'Ингушетия': 6.0,
                     'Иркутская обл.': 38.0,'Кабардино-Балкария': 7.0,
                     'Калининградская обл.': 39.0,'Калмыкия': 8.0,
                     'Калужская обл.': 40.0,'Камчатский край': 41.0,
                     'Карачаево-Черкесия': 9.0,'Карелия': 10.0,
                     'Кемеровская обл.': 42.0,'Кировская обл.': 43.0,
                     'Коми': 11.0,'Костромская обл.': 44.0,
                     'Краснодарский край': 23.0,'Красноярский край': 24.0,
                     'Крым': 91.0,'Курганская обл.': 45.0,
                     'Курская обл.': 46.0,'Ленинградская обл.': 47.0,
                     'Липецкая обл.': 48.0,'Магаданская обл.': 49.0,
                     'Марий Эл': 12.0,'Мордовия': 13.0,
                     'Москва': 77.0,'Московская обл.': 50.0,
                     'Мурманская обл.': 51.0, 'Ненецкий АО': 83.0,
                     'Нижегородская обл.': 52.0,'Новгородская обл.': 53.0,
                     'Новосибирская обл.': 54.0,'Омская обл.': 55.0,
                     'Оренбургская обл.': 56.0,'Орловская обл.': 57.0,
                     'Пензенская обл.': 58.0,'Пермский край': 59.0,
                     'Приморский край': 25.0,'Псковская обл.': 60.0,
                     'Ростовская обл.': 61.0,'Рязанская обл.': 62.0,
                     'Самарская обл.': 63.0,'Санкт-Петербург': 78.0,
                     'Саратовская обл.': 64.0,'Саха (Якутия)': 14.0,
                     'Сахалинская обл.': 65.0,'Свердловская обл.': 66.0,
                     'Севастополь': 92.0,'Северная Осетия': 15.0,
                     'Смоленская обл.': 67.0,'Ставропольский край': 26.0,
                     'Тамбовская обл.': 68.0,'Татарстан': 16.0,
                     'Тверская обл.': 69.0,'Томская обл.': 70.0,
                     'Тульская обл.': 71.0,'Тыва': 17.0,
                     'Тюменская обл.': 72.0,'Удмуртия': 18.0,
                     'Ульяновская обл.': 73.0,'ХМАО - Югра': 86.0,
                     'Хабаровский край': 27.0,'Хакасия': 19.0,
                     'Челябинская обл.': 74.0,'Чечня': 20.0,
                     'Чувашия': 21.0,'Чукотский АО': 87.0,
                     'Ямало-Ненецкий АО': 89.0,'Ярославская обл.': 76.0}        

        # части интерфейса
        # кнопки
        self.bgcolor = '#DAE2E3'
        # кртинка кнопки должна лежать в одной директории с программой
        self.bt_img = PhotoImage(file = 'button.png')
        self.bt_img = self.bt_img.subsample(17,17)
        self.download_data = Button(master, text = 'Load data', compound= "center", 
                                    image = self.bt_img, bg = self.bgcolor, 
                                    relief = 'flat', borderwidth = 0, highlightthickness = 0, 
                                    bd = 0, command = self.load_data, font=("helvetica", 12), fg = 'white')
        
        self.download_data.grid(column = 0, row = 0, ipadx = 5, ipady = 5, padx = 5, pady = 5)
        self.predict_data = Button(master, text = 'Predict', image = self.bt_img, 
                                   compound= "center", bg = self.bgcolor,
                                   relief = 'flat', borderwidth = 0, highlightthickness = 0,
                                   bd = 0, font=("helvetica", 12), fg = 'white', command = self.predict_b)
        self.predict_data.grid(column = 1, row = 0, ipadx = 5, ipady = 5, padx = 5, pady = 5)
        self.save_data = Button(master, text = 'Save data', compound= "center", 
                                image = self.bt_img, command = self.save_file, 
                                bg = self.bgcolor,relief = 'flat', borderwidth = 0, 
                                highlightthickness = 0, bd = 0, font=("helvetica", 12), fg = 'white')
        self.save_data.grid(column = 2, row = 0, ipadx = 5, ipady = 5, padx = 5, pady = 5)
        self.show_data = Button(master, text = 'Show data',
                                command = self.show_graph, compound= "center",
                                image = self.bt_img, bg = self.bgcolor,
                                relief = 'flat', borderwidth = 0,
                                highlightthickness = 0, bd = 0, font=("helvetica", 12), fg = 'white')
        self.show_data.grid(column = 0, row = 3, rowspan = 2 , ipadx = 5, ipady = 5, padx = 5, pady = 5)
        
        self.lbl_1 = Label(text = 'Впишите МНН в виде \'МНН №***\'',
                         borderwidth = 0, highlightthickness = 0, bd = 0, bg = self.bgcolor)
        self.lbl_1.grid(column = 1, row = 3, ipadx = 5, ipady = 5, padx = 5, pady = 5)
        
        self.choose_mnn = Entry(master, width = 20)
        self.choose_mnn.grid(column = 2, row = 3, ipadx = 5, ipady = 5, padx = 5, pady = 5)
        
        self.lbl_2 = Label(text = 'Впишите регион в виде числа',
                         borderwidth = 0, highlightthickness = 0, bd = 0, bg = self.bgcolor)
        self.lbl_2.grid(column = 1, row = 4, ipadx = 5, ipady = 5, padx = 5, pady = 5)
        self.sorted_regions = list(self.regions.values())
        self.sorted_regions.sort()
        self.choose_reg = ttk.Combobox(master, values = list( array(self.sorted_regions, dtype = 'int32') ),
                        state = 'readonly', width = 17)
        self.choose_reg.grid(column = 2, row = 4, ipadx = 5, ipady = 5, padx = 5, pady = 5)
        
        # графики
        # патч для смены стиля навигационного тулбара
        # взят отсюда:
        # https://github.com/daniilS/Musketeer/blob/main/musketeer/patchMatplotlib.py
        # тоже должен лежать в одной папке
        # нужен лишь для красоты, можно удлаить
        patch.applyPatch()
        
        backend_bases.NavigationToolbar2.toolitems = (
        ('Home', 'Reset original view', 'home', 'home'),
        ('Back', 'Back to  previous view', 'back', 'back'),
        ('Forward', 'Forward to next view', 'forward', 'forward'),
        ('Pan', 'Pan axes with left mouse, zoom with right', 'move', 'pan'),
        ('Zoom', 'Zoom to rectangle', 'zoom_to_rect', 'zoom'),
        (None, None, None, None),
        ('Save', 'Save the figure', 'filesave', 'save_figure')
        )
        self.frame_1 = LabelFrame(master, bd = 0)
        self.frame_1.grid(row = 1,column = 0, columnspan = 3)
        self.figure1 = plt.Figure(figsize=(7,3), dpi=100)
        self.figure1.patch.set_facecolor(self.bgcolor)
        self.ax1 = self.figure1.add_subplot(111)
        self.line1 = FigureCanvasTkAgg(self.figure1, self.frame_1)
        self.line1.get_tk_widget().pack()
        self.toolbar1 = NavigationToolbar2Tk(self.line1, self.frame_1)
        self.toolbar1.config(background=self.bgcolor)
        self.toolbar1._message_label.config(background=self.bgcolor)
        self.toolbar1.pack()
        self.toolbar1.update()
        
        self.frame_4 = LabelFrame(master, bd = 0)
        self.frame_4.grid(row = 2, column = 0, columnspan = 3)
        self.figure4 = plt.Figure(figsize=(7,3), dpi=100)
        self.figure4.patch.set_facecolor(self.bgcolor)
        self.ax4 = self.figure4.add_subplot(111)
        self.line4 = FigureCanvasTkAgg(self.figure4, self.frame_4)
        self.line4.get_tk_widget().pack()
        self.toolbar4 = NavigationToolbar2Tk(self.line4, self.frame_4)
        
        self.toolbar4.config(background=self.bgcolor)
        self.toolbar4._message_label.config(background=self.bgcolor)
        self.toolbar4.pack()
        self.toolbar4.update()
        
        # флаги
        self.pred_flag = False
        self.data_loaded = False
        
    def show_graph(self)->None:
        """Функция для показа и обновления содержимого графиков.
        """
        if (self.pred_flag == True):
            # количество месяцев на графике
            self.all_mounths = ['Янв', 'Фев', 'Март',
                           'Апр', 'Май', 'Июнь',
                           'Июль','Авг', 'Сент',
                           'Окт', 'Ноя', 'Дек']
            
            self.ax1.clear()
            self.ax4.clear()
            
            self.ax1.plot(range(0, self.mounths), self.price_max[:self.mounths], color = 'red', label = 'Максимальная цена - факт')
            self.ax1.plot(range(0, self.mounths), self.pred_price_max[:self.mounths], color = 'red', linestyle='dashed', label = 'Максимальная цена - прогноз')
            
            self.ax1.plot(range(0, self.mounths), self.price_min[:self.mounths], color = 'blue', label = 'Минимальная цена - факт')
            self.ax1.plot(range(0, self.mounths), self.pred_price_min[:self.mounths], color = 'blue', linestyle='dashed', label = 'Минимальная цена - прогноз')
            
            self.ax1.plot(range(0, self.mounths), self.price_avg[:self.mounths], color = 'black', label = 'Средняя цена - факт')
            self.ax1.plot(range(0, self.mounths), self.pred_price_avg[:self.mounths], color = 'black', linestyle='dashed', label = 'Средняя цена - прогноз')
            
            self.ax1.set_title('Цена МНН по месяцам', fontsize = 10)
            self.ax1.legend(loc = 'upper right', fontsize = 5)
            self.ax1.set_xticks(range(0, self.mounths))
            self.ax1.set_xticklabels(labels = self.all_mounths[:self.mounths], rotation = 'vertical', fontsize = 7);
            self.ax1.set_ylabel('Цена, коп.', fontsize = 7)

            self.ax4.plot(range(0, self.mounths), self.count[:self.mounths], color = 'red', label = 'Количество - факт')
            self.ax4.plot(range(0, self.mounths), self.pred_count[:self.mounths], color = 'black', linestyle='dashed', label = 'Количество - прогноз')
            self.ax4.set_title('Количество товара по месяцам', fontsize = 10)
            self.ax4.legend(loc = 'upper right', fontsize = 7)
            self.ax4.set_xticks(range(0,self.mounths))
            self.ax4.set_xlabel('Месяц', fontsize = 7)
            self.ax4.set_xticklabels(labels = self.all_mounths[:self.mounths], rotation = 'vertical', fontsize = 7);
            self.ax4.set_ylabel('Количество, шт.', fontsize = 5)
    
            self.line1.draw()
            self.line4.draw()
        else:
            mb.showerror('Ошибка', 'Не выполнено предсказание данных')
            
            
        
    def load_data(self)->None:
        """На вход ничего не получает, ничего не возращает, работает с переменными класса.
        Пользователь выбирает директорию и файл. Можно открывать только CSV."""
        file_name = fd.askopenfilename()
        if (file_name != ''):
            try:
                self.data = pd.read_csv(file_name)
                self.data_loaded = True
                self.pred_flag = False
            except:
                mb.showerror('Ошибка', 'Ошибка чтения файла')

    
    def predict_b(self)->None:
        """Получение, фибльтрация и предсказание данных значений.
        Все производится в рамках переменных класса."""
        if (self.data_loaded == True):
            if (self.choose_reg.get() != ''):
                if (self.choose_mnn.get() != ''):
                    try:
                        # Существующие данные фактические
                        
                        # два основных фильтра
                        
                        # регион
                        self.region = int(self.choose_reg.get())
                        # МНН
                        self.current_mnn = self.choose_mnn.get()
                        
                        # общий фильтр
                        self.df_cut_region = self.data[(self.data['Код субъекта'] == self.region) & 
                                                       (self.data['МНН'] == self.current_mnn)].sort_values(by ='Месяц').groupby(by = 'Месяц').sum()
                        # максимум месяцев на графике
                        self.mounths = self.df_cut_region.shape[0]
                        # далее отсюда снимаются конкретные данные
                        self.price_min = self.df_cut_region['min_3']
                        self.price_avg = self.df_cut_region['avg_3']
                        self.price_max = self.df_cut_region['max_3']
                        self.count = self.df_cut_region['Count_3']
    
                        # даже если данных много, то оптимизация такая:
                        # считается только тот МНН, который сейчас выбран
                        # парсинг json # parse_json(json, mnn, region) -> dict_region
                        file = open('results_final.json', encoding = 'utf8')
                        dct = json.load(file)
                        file.close()
                        
                        self.weights_filtered = parse_json(dct, mnn = self.current_mnn, region = self.region) 
                        features = ['Заражений','Максимальная температура, С',
                                    'Средняя температура, С','Минимальная температура, С',
                                    'population','latitude_dd','longitude_dd']
                        
                        self.pred_price_max = []
                        self.pred_price_min = []
                        self.pred_price_avg = []
                        self.pred_count = []
                        # теперь сама линейная регрессия и предсказание
                        for par_for_predict in ['max_3','min_3','avg_3','Count_3']:
                            weights = self.weights_filtered[par_for_predict]
                            #print(weights)
                            self.df_cut_region = self.df_cut_region[features]
                            for mounth in array(self.df_cut_region):
                                # mounth в необходимом порядке, т.к. features в правильном порядке
                                if par_for_predict == 'max_3':
                                    self.pred_price_max.append(exp((weights[0]@mounth + weights[1])))
                                elif par_for_predict == 'min_3':
                                    self.pred_price_min.append(exp((weights[0]@mounth + weights[1])))
                                elif par_for_predict == 'avg_3':
                                    self.pred_price_avg.append(exp((weights[0]@mounth + weights[1])))
                                elif par_for_predict == 'Count_3':
                                    self.pred_count.append(exp((weights[0]@mounth + weights[1])))
    
                        self.pred_flag = True
                    except:
                        mb.showwarning('Внимание', 'Вероятно, недостаточно данных для расчета или веса для модели данного региона не были посчитаны.')
                else:
                    mb.showerror('Ошибка', 'Введите МНН. Если у вас нет списка МНН, обратитесь к специалисту.')
            else:
               mb.showerror('Ошибка', 'Выберите регион') 
        else:
            mb.showerror('Ошибка', 'Загрузите данные')
    
    def save_file(self)-> None:
        """На вход ничего не получает, ничего не возращает, работает с переменными класса.
        Пользователь выбирает директорию, вписывает имя файла, расширение дописывается
        автоматически. Можно сохранить только в CSV.
        Записывает файл в формате (pred_price_min, pred_price_avg, pred_price_max, pred_count)"""
        file_name = fd.asksaveasfilename() + '.csv'
        if (file_name[:-4] != ''):
            try:
                self.prediction = column_stack([array(self.pred_price_min),  array(self.pred_price_avg)])
                self.prediction = column_stack([self.prediction, array(self.pred_price_max)])
                self.prediction = column_stack([self.prediction, array(self.pred_count)])
                self.prediction = pd.DataFrame(self.prediction, columns=['pred_price_min',
                                                                         'pred_price_avg',
                                                                         'pred_price_max',
                                                                         'pred_count'])
                self.prediction.to_csv(file_name)
            except:
                mb.showerror('Ошибка', 'Ошибка сохранения файла')


def parse_json(json: dict, mnn: str, region: int) -> dict:
    '''
    json - dict, полученный из json
    mnn - str, e.g. 'МНН №269'
    region - int, e.g. 24
    '''
    dict_mnn = json[mnn]
    region = str(region)
    for key, value in dict_mnn.items():
        if ('_weights' in key) & (region == key.replace('.0_weights', '')):
            dict_region = dict_mnn[key]
            return dict_region


# отдельная функция для 
def _onKeyRelease(event)->None:
    """
    Баг ткинтера- он обрабатывает горячие клавиши: ctrl+c ctrl+v только для англ раскладки.
    Функция для обработки нажатий ctrl+c ctrl+v при русской раскладке - т.е. нужно добавить бинд клавиш.
    Взята отсюда: https://coderoad.ru/40946919/
    /Python-tkinter-copy-paste-не-работает-с-другими-языками
    """
    ctrl  = (event.state & 0x4) != 0
    if event.keycode==88 and  ctrl and event.keysym.lower() != "x": 
        event.widget.event_generate("<<Cut>>")
    if event.keycode==86 and  ctrl and event.keysym.lower() != "v": 
        event.widget.event_generate("<<Paste>>")
    if event.keycode==67 and  ctrl and event.keysym.lower() != "c":
        event.widget.event_generate("<<Copy>>")


main_block = Block(root)
root.resizable(False, False)
root.configure(background = main_block.bgcolor)
root.bind_all("<Key>", _onKeyRelease, "+")
root.title("GPOWER")
root.mainloop()