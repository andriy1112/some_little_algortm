from kivy.uix.floatlayout import FloatLayout
from kivy.lang import Builder
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button

class MainWindow(BoxLayout):

    # We create a dictionary of all our possible methods to call, along with keys
    def command_dict(self):
        return {

        }

    def process_command(self):
        # comand_key save comand
        command_key = self.ids.fetch_key_and_process_command.text
        print(command_key)
        # We then use that key in the command built in 'get_method' because it is a dict
        # then we store it into a variable for later use
        called_command = self.command_dict().get(command_key, 'default')

        try:
            # The variable is a method, so by adding we can call it by simple adding your typical () to the end of it.
            called_command()

        except TypeError:
            # However we use an exception clause to catch in case people enter a key that doesn't exist
            self.ids.fetch_key_and_process_command.text = 'you input: ' + command_key



class MainApp(App):


    def build(self):

        return MainWindow()



if __name__ == '__main__':
    MainApp().run()
