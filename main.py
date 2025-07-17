from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from instructions import txt_instruction, txt_test1, txt_test3, txt_sits
from ruffier import test
from seconds import Seconds
from kivy.core.window import Window
from sits import Sits

Window.clearcolor = (0.6, 0.4, 0.7, 1)
btn_color = (0.98, 0.31, 0.8, 1)

age = 7
name = ""
p1, p2, p3 = 0, 0, 0

def check_int(str_num):
    try:
        return int(str_num)
    except:
        return False

class InstrScr(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.instr = Label(text=txt_instruction)
        self.lbl1 = Label(text="Введіть ім'я:", halign="right")
        self.in_name = TextInput(text="Narek", multiline=False)
        self.lbl2 = Label(text="Введіть вік:", halign="right")
        self.in_age = TextInput(text="15", multiline=False)
        self.btn = Button(text="запустити", size_hint=(0.3, 0.2), pos_hint={"center_x": 0.5})
        self.btn.background_color = btn_color
        self.btn.on_press = self.next
        self.line1 = BoxLayout(size_hint=(0.8, None), height="30sp")
        self.line2 = BoxLayout(size_hint=(0.8, None), height="30sp")
        self.line1.add_widget(self.lbl1)
        self.line1.add_widget(self.in_name)
        self.line2.add_widget(self.lbl2)
        self.line2.add_widget(self.in_age)
        self.outer = BoxLayout(orientation="vertical", padding=8, spacing=8)
        self.outer.add_widget(self.instr)
        self.outer.add_widget(self.line1)
        self.outer.add_widget(self.line2)
        self.outer.add_widget(self.btn)
        self.add_widget(self.outer)

    def next(self):
        global name, age
        name = self.in_name.text
        age = check_int(self.in_age.text)
        if age is False or age < 7:
            age = 7
            self.in_age.text = str(age)
        else:
            self.manager.current = "pulse1"

class PulseScr(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.next_screen = False
        self.lbl_sec = Seconds(15)
        self.lbl_sec.bind(done=self.sec_finished)
        self.instr = Label(text=txt_test1)
        self.line = BoxLayout(size_hint=(0.8, None), height="30sp")
        self.lbl_result = Label(text="Введіть результат:", halign="right")
        self.in_result = TextInput(text="0", multiline=False)
        self.in_result.set_disabled(True)
        self.line.add_widget(self.lbl_result)
        self.line.add_widget(self.in_result)
        self.btn = Button(text="Запустити таймер", size_hint=(0.3, 0.2), pos_hint={"center_x": 0.5})
        self.btn.background_color = btn_color
        self.btn.on_press = self.next
        self.outer = BoxLayout(orientation="vertical", padding=8, spacing=8)
        self.outer.add_widget(self.instr)
        self.outer.add_widget(self.lbl_sec)
        self.outer.add_widget(self.line)
        self.outer.add_widget(self.btn)
        self.add_widget(self.outer)

    def sec_finished(self, *args):
        self.next_screen = True
        self.in_result.set_disabled(False)
        self.btn.set_disabled(False)
        self.btn.text = "Продовжити"

    def next(self):
        if not self.next_screen:
            self.btn.set_disabled(True)
            self.lbl_sec.start()
        else:
            global p1
            p1 = check_int(self.in_result.text)
            if p1 is False or p1 <= 0:
                p1 = 0
                self.in_result.text = str(p1)
            else:
                self.manager.current = "sits"

class CheckSits(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.next_screen = False

        self.lbl_timer = Seconds(30)
        self.lbl_timer.bind(done=self.timer_done)

        self.instr = Label(text=txt_sits)

        self.btn = Button(text="Почати", size_hint=(0.3, 0.2), pos_hint={"center_x": 0.5})
        self.btn.background_color = btn_color
        self.btn.on_press = self.next

        self.outer = BoxLayout(orientation="vertical", padding=8, spacing=8)
        self.outer.add_widget(self.instr)         # Инструкция
        self.outer.add_widget(self.btn)           # Кнопка "Почати"
        self.outer.add_widget(self.lbl_timer)     # Таймер — теперь между кнопкой и надписью
        self.add_widget(self.outer)

    def timer_done(self, *args):
        self.btn.set_disabled(False)
        self.btn.text = "Продовжити"
        self.next_screen = True

    def next(self):
        if not self.next_screen:
            self.btn.set_disabled(True)
            self.lbl_timer.start()
        else:
            self.manager.current = "pulse2"


class PulseScr2(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.next_screen = False
        self.stage = 0
        self.instr = Label(text=txt_test3)
        self.lbl_sec = Seconds(15)
        self.lbl_sec.bind(done=self.sec_finished)
        self.lbl1 = Label(text="Рахуйте пульс")
        self.line1 = BoxLayout(size_hint=(0.8, None), height="30sp")
        self.lbl_result1 = Label(text="Результат:", halign="right")
        self.in_result1 = TextInput(text="0", multiline=False)
        self.in_result1.set_disabled(True)
        self.line1.add_widget(self.lbl_result1)
        self.line1.add_widget(self.in_result1)
        self.line2 = BoxLayout(size_hint=(0.8, None), height="30sp")
        self.lbl_result2 = Label(text="Результат після відпочинку:", halign="right")
        self.in_result2 = TextInput(text="0", multiline=False)
        self.in_result2.set_disabled(True)
        self.line2.add_widget(self.lbl_result2)
        self.line2.add_widget(self.in_result2)
        self.btn = Button(text="Завершити", size_hint=(0.3, 0.2), pos_hint={"center_x": 0.5})
        self.btn.background_color = btn_color
        self.btn.on_press = self.next
        self.outer = BoxLayout(orientation="vertical", padding=8, spacing=8)
        self.outer.add_widget(self.instr)
        self.outer.add_widget(self.lbl1)
        self.outer.add_widget(self.lbl_sec)
        self.outer.add_widget(self.line1)
        self.outer.add_widget(self.line2)
        self.outer.add_widget(self.btn)
        self.add_widget(self.outer)

    def sec_finished(self, *args):
        if self.stage == 0:
            self.lbl1.text = "Відпочивайте"
            self.lbl_sec.restart(30)
            self.in_result1.set_disabled(False)
            self.stage = 1
        elif self.stage == 1:
            self.lbl1.text = "Рахуйте пульс"
            self.lbl_sec.restart(15)
            self.stage = 2
        elif self.stage == 2:
            self.in_result2.set_disabled(False)
            self.btn.set_disabled(False)
            self.btn.text = "Завершити"
            self.next_screen = True

    def next(self):
        if not self.next_screen:
            self.btn.set_disabled(True)
            self.lbl_sec.start()
        else:
            global p2, p3
            p2 = check_int(self.in_result1.text)
            p3 = check_int(self.in_result2.text)
            if p2 is False:
                p2 = 0
                self.in_result1.text = str(p2)
            if p3 is False:
                p3 = 0
                self.in_result2.text = str(p3)
            self.manager.current = "result"

class Result(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.outer = BoxLayout(orientation="vertical", padding=8, spacing=8)
        self.instr = Label(text="")
        self.outer.add_widget(self.instr)
        self.add_widget(self.outer)
        self.on_enter = self.before

    def before(self):
        global name
        self.instr.text = name + "\n" + test(p1, p2, p3, age)

class HeartCheck(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(InstrScr(name="instr"))
        sm.add_widget(PulseScr(name="pulse1"))
        sm.add_widget(CheckSits(name="sits"))
        sm.add_widget(PulseScr2(name="pulse2"))
        sm.add_widget(Result(name="result"))
        return sm

app = HeartCheck()
app.run()
