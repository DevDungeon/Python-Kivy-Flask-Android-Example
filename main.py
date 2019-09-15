import kivy
kivy.require('1.11.1')  # Set to your Kivy version
from kivy.app import App
from kivy.uix.textinput import TextInput
from flask import Flask, request
from threading import Thread


class MyApp(App):
    
    host = '0.0.0.0'
    port = 5000

    def build(self):
        self.log_text = TextInput(multiline=True, text='Starting\n')
        Thread(target=self.start_flask).start()
        self.log_text.insert_text('Flask listening on %s:%s\n' % (self.host, self.port))
        return self.log_text

    def start_flask(self):
        self.flask_app = Flask(__name__)

        @self.flask_app.route('/')
        def index():
            self.log_text.insert_text('Request: %s %s\n' % (request.remote_addr, request.path))
            return '<html><body>Ok</body></html>\n'

        self.flask_app.run(host=self.host, port=self.port)


if __name__ == '__main__':
    MyApp().run()
        