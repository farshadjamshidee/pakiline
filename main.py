from kivymd.app import MDApp
from kivy.uix.screenmanager import ScreenManager
from kivy.lang import Builder
from kivy.clock import Clock
from arabic_reshaper import reshape
from bidi.algorithm import get_display
from kivy.core.text import LabelBase
from pcalender.datepicker_fa import DatePickerFa
from kivymd.toast import toast
from kivy.garden.mapview import MapView, MapMarker
import requests
import json


url = 'https://api2.ippanel.com/api/v1/sms/pattern/normal/send'

LabelBase.register(name='B Lotus', fn_regular='fonts/B Lotus.ttf', fn_bold='fonts/B Lotus Bold.ttf')
LabelBase.register(name='amin', fn_regular='fonts/amin.ttf', fn_bold='fonts/amin.ttf')


data = {
    'code':'',
    'sender': '+9890000145',
    'recipient':'',
    'variable':{
        'verification-code':'test'
    }
}
headers = {
    'apikey':'UekrGvYRL6ye-xy1lpgPz9VMH5cPpefbkbUUhe6ti9Y=',
    'content-Type':'application/json'
}


class LoginPage(MDApp):
    def __init__(self, **Kwargs):
        super().__init__(**Kwargs)

        self.screen_manager = ScreenManager()
        self.screen_manager.add_widget(Builder.load_file('splash.kv'))
        self.screen_manager.add_widget(Builder.load_file('login.kv'))
        self.screen_manager.add_widget(Builder.load_file('order.kv'))
        self.screen_manager.add_widget(Builder.load_file('order2.kv'))
        self.screen_manager.add_widget(Builder.load_file('order_addr.kv'))

        self.agencies = [self.slogan()['agency_one'], self.slogan()['agency_two']]

    def build(self):
        return self.screen_manager

    def choose(self, me_id,toggle_id):
        if self.screen_manager.current_screen.ids.me_id.active == True:
            self.screen_manager.current_screen.ids.toggle_id.active = False
        else:
            self.screen_manager.current_screen.ids.toggle_id.active = True
    def on_start(self):
        Clock.schedule_once(self.login, 5)

    def login(self, *args):
        self.screen_manager.current = 'login'

    def slogan(self):
        slog_text = reshape('پاکیزگی آنلاین با پاکیلاین')
        slog = get_display(slog_text)
        txt_dict = {
            'slog': get_display(reshape('پاکیزگی آنلاین با پاکیلاین')),
            'user': get_display(reshape("شماره همراه")),
            'welcome': get_display(reshape("به پاکیلاین خوش آمدید")),
            'submit_text' : get_display(reshape("ارسال کد")),
            'choose_lbl': get_display(reshape("انتخاب خشکشویی")),
            'personal': get_display(reshape("نام و نام خانوادگی")),
            'phone' : get_display(reshape("شماره همراه")),
            'time':  get_display(reshape("بازه زمانی")),
            'address': get_display(reshape("ثبت آدرس")),
            'continue': get_display(reshape("ادامه سفارش")),
            'agency_one': get_display(reshape("خشکشویی ماه اکسپرس (اخواس)")),
            'agency_two': get_display(reshape("خشکشویی اکسپرس انصاری")),
            'day': get_display(reshape("روز سفارش")),
        }
        return txt_dict


    def focus(self):
        # print(screen_manager.current_screen.ids.user.text)
        self.screen_manager.current_screen.ids.user.text = ''

    def blur(self):
        self.screen_manager.current_screen.ids.user.text = self.slogan()['user']

    def logger(self):
        # data['recipient'] = screen_manager.current_screen.ids.user.text
        # print(data['recipient'])
        # payload = json.dumps(data)
        # response = requests.request('POST', url, headers=headers, data=payload)
        # if  response.status_code == 200:
        #     screen_manager.current = 'order'
        # print(response.text)
        self.screen_manager.current = 'order'

    def choose_agency(self):
        print('choose!!!')

    def order_continue(self):
        self.screen_manager.current = 'order2'

    def order_addr(self):
        self.screen_manager.current = 'order_addr'

    def choose_date(self):
        self.calender = DatePickerFa(callback=self.calender_callback)
        self.calender.open()

    def calender_callback(self,date):
        self.screen_manager.current_screen.ids.chosen_date.text = date
        return toast(date)

    # def on_start(self):
    #     # self.mapview = self.screen_manager.current_screen.ids.
    #     pass

LoginPage().run()