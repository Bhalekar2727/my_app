from kivymd.uix.screen import MDScreen
from kivymd.app import MDApp
from kivy.uix.image import Image
from kivymd.uix.button import MDFillRoundFlatIconButton, MDFillRoundFlatButton
from kivymd.uix.textfield import MDTextField
from kivymd.uix.label import MDLabel
from kivymd.uix.toolbar import MDTopAppBar

class ConverterApp(MDApp):
    def flip(self):
        if self.state == 0:
            self.state = 1
            self.toolbar.title = "Decimal to Binary"
            self.input.text = "enter a decimal number"
            self.converted.text = ""
            self.label.text = ""
        else:
            self.state = 0
            self.toolbar.title = "Binary to Decimal"
            self.input.text = "enter Binary number"
            self.converted.text = ""
            self.label.text = ""
    def convert(self, args):
        try:
            if "." not in self.input.text:
                if self.state == 0:
                    val = int(self.input.text,2)
                    self.converted.text = str(val)
                    self.label.text = "in decimal is:"
                else:
                    val = bin(int(self.input.text))[2:]
                    self.converted.text = val
                    self.label.text = "in binary is:"
            else:
                whole, fract = self.input.text.split(".")
                #floating point num,ber conversion
                if self.state == 0:
                    #convert Binary to Decimal
                    whole = int(whole, 2)
                    floating = 0
                    for idx, digit in enumerate(fract):
                        floating += int(digit)*2**(-(idx+1))
                    self.converted.text = str(whole + floating)
                    self.label.text = "in Decimal is:"
                else:
                    #Decimal to Binary convart
                    decimal_place = 10
                    whole = bin(int(whole))[2:]
                    fract = float("0."+fract)
                    floating = []
                    for i in range(decimal_place):
                        if fract*2 < 1:
                            floating.append("0")
                            fract *= 2
                        elif fract*2 > 1:
                            floating.append("1")
                            fract *=2 - 1
                        elif fract*2 == 1.0:
                            floating.append("1")
                            break
                    self.converted.text = str(whole+ "." +"".join(floating))
                    self.label.text = "in Binary"
        except ValueError:
            self.converted.text = ""
            if self.state == 0:
                self.label.text = "please enter a valid Binary number"
            else:
                self.label.text = "please enter a valid deimal number"





                
            
    def build(self):
        self.state = 0
        # self.theme_cls.primary_palette = "Green"

        screen = MDScreen()

        self.toolbar = MDTopAppBar(title="Binary to Decimal")
        self.toolbar.pos_hint = {"top": 1}
        self.toolbar.right_action_items = [
            ["rotate-3d-variant", lambda x: self.flip()]]
        screen.add_widget(self.toolbar)

        #Logo
        screen.add_widget(Image(
            source="logo.png",
            pos_hint = {"center_x": 0.5, "center_y": 0.7}))
        
        #collect user input
        self.input = MDTextField(
            text="enter a binary number",
            halign="center",
            size_hint = (0.8,1),
            pos_hint = {"center_x": 0.5, "center_y": 0.5},
            font_size = 22
        )
        screen.add_widget(self.input)

        #secondary + primary labels
        self.label = MDLabel(
            halign = "center",
            pos_hint = {"center_x": 0.5, "center_y": 0.35},
            theme_text_color = "Secondary"
        )

        self.converted = MDLabel(
            text="888",
            halign="center",
            pos_hint = {"center_x": 0.5, "center_y":0.3},
            theme_text_color = "Primary",
            font_style = "H5"
                   

        )
        screen.add_widget(self.label)
        screen.add_widget(self.converted)

        # "CONVERT" button
        screen.add_widget(MDFillRoundFlatButton(
            text="CONVERT",
            font_size = 17,
            pos_hint = {"center_x": 0.5, "center_y": 0.15},
            on_press = self.convert
        ))

        return screen
    
if __name__ == "__main__":
    ConverterApp().run()  