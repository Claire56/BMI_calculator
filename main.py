from kivy.app import App
from kivy.lang import Builder
from kivy.uix.button import Button
from kivy.properties import ObjectProperty,ListProperty
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput


from os import listdir
kv_path = './kv/'
for kv in listdir(kv_path):
    Builder.load_file(kv_path+kv)



class BmiButton(Button):
    pass


class Container(GridLayout):
    # display = ObjectProperty()
    data_list = ListProperty([])
    bmi=ObjectProperty()

    # def add_one(self):
    #     value = int(self.display.text)
    #     self.display.text = str(value+1)

    # def subtract_one(self):
    #     value = int(self.display.text)
    #     self.display.text = str(value-1)

    def get_bmi(self):
        # height = int(self.height.value)
        # weight = int(self.weight.text)
        bmi =str(self.height * self.weight)
        self.bmi.text= bmi

        for child in reversed(self.children):
            if isinstance(child, TextInput):
                self.data_list.append(child.text)
        print(self.data_list)       
        

class MainApp(App):
    def build(self):
        self.title = 'My First Mobile app!!!'
        return Container()


if __name__ == "__main__":
    app = MainApp()
    app.run()


