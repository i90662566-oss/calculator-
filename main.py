import kivy

from kivy.app import App

from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout


class CalculatorApp(App):
    def build(self):
        
        self.first = 0
        self.second = 0
        self.flag = False
        self.operation = ""
        self.result = 0
        self.sec = 0
        self.flag2 =False

        layout = GridLayout(cols=4, padding=10, spacing=10)
        self.lbl = Label(text="0")
        layout.add_widget(self.lbl)
        btn_one = Button(text="1")
        btn_one.bind(on_press=self.on_button_one)
        layout.add_widget(btn_one)
        btn_two = Button(text="2")
        btn_two.bind(on_press=self.on_button_two)
        layout.add_widget(btn_two)
        btn_three = Button(text="3")
        btn_three.bind(on_press=self.on_button_three)
        layout.add_widget(btn_three)
        btn_four = Button(text="4")
        layout.add_widget(btn_four)
        btn_four.bind(on_press=self.on_button_four)
        btn_five = Button(text="5")
        layout.add_widget(btn_five)
        btn_five.bind(on_press=self.on_button_five)

        btn_six = Button(text="6")
        layout.add_widget(btn_six)
        btn_six.bind(on_press=self.on_button_dup)

        btn_seven = Button(text="7")
        layout.add_widget(btn_seven)
        btn_seven.bind(on_press=self.on_button_seven)
        btn_eight = Button(text="8")

        layout.add_widget(btn_eight)
        btn_eight.bind(on_press=self.on_button_eight)
        btn_nine = Button(text="9")
        btn_nine.bind(on_press=self.on_button_nine)

        layout.add_widget(btn_nine)
        btn_zero = Button(text="0")
        layout.add_widget(btn_zero)
        btn_zero.bind(on_press=self.on_button_zero)
        btn_plus = Button(text="+")
        btn_plus.bind(on_press=self.on_button_plus)
        layout.add_widget(btn_plus)
        btn_minus = Button(text="-")
        btn_dev = Button(text="*")
        btn_double = Button(text="/")
        btn_square = Button(text="x**2")
        btn_result = Button(text="result")
        btn_result5= Button(text="show result")
        btn_result5.bind(on_press=self.on_button_result5)
        layout.add_widget(btn_result)
        btn_result.bind(on_press=self.on_button_result)
        layout.add_widget(btn_square)
        btn_square.bind(on_press=self.on_button_square)
        layout.add_widget(btn_double)
        btn_dev.bind(on_press=self.on_button_dev)
        btn_double.bind(on_press=self.on_button_double)
        layout.add_widget(btn_dev)

        layout.add_widget(btn_minus)

        btn_minus.bind(on_press=self.on_button_minus)

        btn_equal = Button(text="=")

        btnAC = Button(text="AC")
        layout.add_widget(btnAC)
        btnAC.bind(on_press=self.clear_me)
        layout.add_widget(btn_equal)
        btn_equal.bind(on_press=self.equal_result)


        return layout

    def on_button_one(self, instance):
        if self.flag == False:
            self.first = 1 + (self.first * 10)
            # self.lbl.text = str(self.first)
            self.lbl.text = f"{self.first} {self.operation} {self.second}"
        else:
            self.second = 1 + (self.second * 10)
            self.lbl.text = f"{self.first} {self.operation} {self.second}"
            self.sec += self.second

    def on_button_two(self, instance):
        if self.flag == False:
            self.first = 2 + (self.first * 10)
            self.lbl.text = f"{self.first} {self.operation} {self.second}"
        else:
            self.second = 2 + (self.second * 10)
            self.lbl.text = f"{self.first} {self.operation} {self.second}"
            self.sec += self.second

    def on_button_three(self, instance):
        if self.flag == False:
            self.first = 3 + (self.first * 10)
            self.lbl.text =f"{self.first} {self.operation} {self.second}"
        else:
            self.second = 3 + (self.second * 10)
            self.lbl.text =f"{self.first} {self.operation} {self.second}"
            self.sec += self.second

    def on_button_plus(self, instance):
        self.flag = True
        self.operation = "+"
        self.lbl.text = f"{self.first} {self.operation} {self.second}"

    def clear_me(self, instance):
        self.first = 0
        self.second = 0
        self.flag = False
        self.operation = ""
        self.lbl.text = str(self.first)

    def equal_result(self, instance):
        if self.operation == "+":
            self.result = self.first + self.second
            self.lbl.text = f"{self.first} {self.operation} {self.second}\n{self.result}"





        elif self.operation == "-":
            self.result = self.first - self.second
            self.lbl.text = f"{self.first} {self.operation} {self.second}\n{self.result}"

        elif self.operation == "*":
            self.result = self.first * self.second
            self.lbl.text =f"{self.first} {self.operation} {self.second}\n{self.result}"
        elif self.operation == "/":
            if self.second == 0:
                self.lbl.text = f"{self.first} {self.operation} {self.second}\nНе опредиленно"

                return
            self.result = self.first / self.second
            self.lbl.text = f"{self.first} {self.operation} {self.second}\n{self.result}"

        elif self.operation == "x**2":
            self.result = self.first ** self.second
            self.lbl.text = f"{self.first} {self.operation} {self.second}\n{self.result}"

        self.flag = False


    def on_button_four(self, instance):
        if self.flag == False:
            self.first = 4 + (self.first * 10)
            self.lbl.text =f"{self.first} {self.operation} {self.second}"
            #str((self.first, self.operation, self.second))

        else:
            self.second = 4 + (self.second * 10)
            self.lbl.text = f"{self.first} {self.operation} {self.second}"
            self.sec += self.second

    def on_button_five(self, instance):
        if self.flag == False:
            self.first = 5 + (self.first * 10)
            self.lbl.text =f"{self.first} {self.operation} {self.second}"
        else:
            self.second = 5 + (self.second * 10)
            self.lbl.text = f"{self.first} {self.operation} {self.second}"
            self.sec += self.second

    def on_button_dup(self, instance):
        if self.flag == False:
            self.first = 6 + (self.first * 10)
            self.lbl.text =f"{self.first} {self.operation} {self.second}"
        else:
            self.second = 6 + (self.second * 10)
            self.lbl.text = f"{self.first} {self.operation} {self.second}"
            self.sec += self.second

    def on_button_seven(self, instance):
        if self.flag == False:
            self.first = 7 + (self.first * 10)
            self.lbl.text = f"{self.first} {self.operation} {self.second}"
            self.sec += self.second
        else:
            self.second = 7 + (self.second * 10)
            self.lbl.text = f"{self.first} {self.operation} {self.second}"
            self.sec += self.second

    def on_button_eight(self, instance):
        if self.flag == False:
            self.first = 8 + (self.first * 10)
            self.lbl.text =f"{self.first} {self.operation} {self.second}"
        else:
            self.second = 8 + (self.second * 10)
            self.lbl.text =f"{self.first} {self.operation} {self.second}"
            self.sec += self.second

    def on_button_nine(self, instance):
        if self.flag == False:
            self.first = 9 + (self.first * 10)
            self.lbl.text = f"{self.first} {self.operation} {self.second}"


        else:
            self.second = 9 + (self.second * 10)
            self.lbl.text = f"{self.first} {self.operation} {self.second}"
            self.sec += self.second

    def on_button_zero(self, instance):
        if self.flag == False:
            self.first = 0 + (self.first * 10)
            self.lbl.text =f"{self.first} {self.operation} {self.second}"
            self.sec += self.second
        else:
            self.second = 0 + (self.second * 10)
            self.lbl.text =f"{self.first} {self.operation} {self.second}"
            self.sec += self.second

    def on_button_minus(self, instance):
        self.flag = True
        self.operation = "-"
        self.lbl.text =f"{self.first} {self.operation} {self.second}"

    def on_button_dev(self, instance):
        self.flag = True
        self.operation = "*"
        self.lbl.text =f"{self.first} {self.operation} {self.second}"
    def on_button_double(self, instance):
        self.flag = True
        self.operation = "/"
        self.lbl.text = f"{self.first} {self.operation} {self.second}"



    def on_button_square(self, instance):
        self.flag = True
        self.operation = "x**2"
        self.lbl.text = f"{self.first} {self.operation} {self.second}"

    def on_button_result(self, instance):
        self.lbl.text = str((self.result))

    def on_button_result5(self, instance):
        self.flag2=True
        self.first=0
        self.second=0






if __name__ == "__main__":
    CalculatorApp().run()
