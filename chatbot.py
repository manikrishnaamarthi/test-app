import json

from kivy.factory import Factory
from kivy.uix.image import Image
from kivymd.app import MDApp
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.scrollview import ScrollView
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.graphics import Color, RoundedRectangle
from kivymd.uix.button import MDIconButton, MDRaisedButton, MDFlatButton
from kivymd.uix.textfield import MDTextField
from datetime import datetime
import google.generativeai as genai

# Configure the generative AI model
genai.configure(api_key="AIzaSyArcg51sCGVGwX0U_zyo4KeC349s5iyWBI")
model = genai.GenerativeModel('gemini-1.5-pro')

# Predefined FAQs and their answers
FAQS = [
    ("How do I start lending on your platform?",
     "To begin lending, you need to create an account on our platform. Once registered, you can deposit funds into your wallet and start browsing available loan listings. Choose the loans that match your preferences and lend the desired amount to borrowers."),
    ("How can I withdraw my earnings from lending?",
     "You can withdraw your earnings from lending by accessing your account dashboard. From there, navigate to the 'Withdraw Funds' section and follow the instructions to transfer your earnings to your linked bank account or other preferred payment methods."),
    ("Can I cancel a loan that I've already funded?",
     "No, once you have funded a loan, you cannot cancel it. However, you have the flexibility to choose which loans to fund based on your preferences and risk tolerance. We encourage thorough review of loan details before making lending decisions."),
    ("What are the payment methods?", "We accept various payment methods including credit/debit cards, UPI, and more."),
    ("How do I contact customer support?", "You can contact us through the 'Something else' section.", True),  # Added identifier
    ("How do I apply for a loan?", "To apply for a loan, you need to create an account on our platform. Once registered, fill out the loan application form with the necessary details and submit it for review."),
    ("What documents are required for loan approval?", "For loan approval, you need to provide identification proof, address proof, income proof, and bank statements for the last six months.")
]


class ChatBotScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.build_ui()

    def build_ui(self):
        self.layout = BoxLayout(orientation='vertical', padding=10, spacing=10)

        # Create top bar
        top_bar = BoxLayout(size_hint=(1, 0.08))
        with top_bar.canvas.before:
            Color(0.043, 0.145, 0.278, 1)  # Dark blue color
            self.rect = RoundedRectangle(size=top_bar.size, pos=top_bar.pos, radius=[0, 0, 10, 10])
            top_bar.bind(pos=self.update_top_bar, size=self.update_top_bar)

        back_button = MDIconButton(icon='arrow-left', theme_text_color='Custom', text_color=(1, 1, 1, 1),
                                   on_press=self.go_to_LenderDashboard)
        top_bar.add_widget(back_button)
        top_bar.add_widget(Label(text="Chat Support", bold=True, color=(1, 1, 1, 1), size_hint=(1, 1)))

        self.layout.add_widget(top_bar)

        # Create ScrollView for chat messages
        self.scroll_view = ScrollView(size_hint=(1, 0.7))
        self.chat_layout = GridLayout(cols=1, size_hint_y=None, padding=10, spacing=10)
        self.chat_layout.bind(minimum_height=self.chat_layout.setter('height'))
        self.scroll_view.add_widget(self.chat_layout)

        # Create input layout
        input_layout = BoxLayout(size_hint=(1, 0.1), spacing=10)

        # Create profile Image
        self.upload_button = MDIconButton(icon='attachment', size_hint=(0.1, 1))

        # Create rounded TextField
        self.input_text = MDTextField(
            hint_text='  Enter your message',
            size_hint=(0.8, 1),
            mode='rectangle',
            radius=[20, 20, 20, 20],  # Apply rounded corners
        )

        # Create send icon Button
        self.send_button = MDIconButton(icon='send', size_hint=(0.1, 1))
        self.send_button.bind(on_press=self.on_send_button_press)

        input_layout.add_widget(self.upload_button)
        input_layout.add_widget(self.input_text)
        input_layout.add_widget(self.send_button)

        self.layout.add_widget(self.scroll_view)
        self.layout.add_widget(input_layout)

        self.add_widget(self.layout)

        # Display FAQs and Ask Something Else button
        self.display_faqs()

    def go_to_LenderDashboard(self, instance):
        # Load the email.json file
        with open('emails.json', 'r') as file:
            email_data = json.load(file)

        # Get the email of the currently logged-in user
        current_user_email = email_data.get("email_user")

        # Check the user_type of the current user
        if current_user_email and current_user_email in email_data:
            user_info = email_data[current_user_email]
            user_type = user_info.get("user_type")

            # Redirect based on user_type
            if user_type == 'borrower':
                self.manager.add_widget(Factory.DashboardScreen(name='DashboardScreen'))
                self.manager.current = 'DashboardScreen'
                # self.manager.current = 'DashScreen'
            elif user_type == 'lender':
                self.manager.add_widget(Factory.LenderDashboard(name='LenderDashboard'))
                self.manager.current = 'LenderDashboard'
            else:
                print("Error: Unknown user type")
        else:
            print("Error: User email not found in email.json")

    def update_top_bar(self, instance, value):
        self.rect.pos = instance.pos
        self.rect.size = instance.size

    def on_send_button_press(self, instance):
        user_message = self.input_text.text
        if user_message:
            self.add_message(user_message, 'user')
            self.input_text.text = ''

            # Generate response from AI model
            response = model.generate_content(user_message)
            self.add_message(response.text, 'bot')
            self.add_something_else_button()

    def add_message(self, message, sender):
        # Create a box layout to hold the message and the profile image
        message_box = BoxLayout(orientation='vertical', size_hint_y=None, size_hint_x=3, padding=(5, 5))
        message_box.bind(minimum_height=message_box.setter('height'))

        # Create the message label
        message_label = Label(text=message, size_hint_y=None, halign='left', valign='middle',
                              text_size=(self.scroll_view.width - 70, None), padding=(10, 10))
        message_label.bind(texture_size=message_label.setter('size'))

        # Set the background color and rounded corners for the message
        with message_label.canvas.before:
            if sender == 'user':
                Color(0.6, 0.6, 0.6, 1)  # Dark cement color for user messages
            else:
                Color(0.043, 0.145, 0.278, 1)  # Dark blue color for bot messages
            RoundedRectangle(pos=message_label.pos, size=message_label.size, radius=[10, 10, 10, 10])
            message_label.bind(pos=self.update_rect(message_label, sender),
                               size=self.update_rect(message_label, sender))

        # Create a horizontal box layout to hold the profile image and message
        message_layout = BoxLayout(orientation='horizontal', size_hint_y=None)
        message_layout.bind(minimum_height=message_layout.setter('height'))

        # Add profile image and message label based on sender
        if sender == 'user':
            profile_image = Image(source='user.png', size_hint=(None, None), size=(40, 40))
            message_layout.add_widget(profile_image)
            message_layout.add_widget(message_label)
        else:
            message_layout.add_widget(message_label)
            profile_image = Image(source='LOGO.png', size_hint=(None, None), size=(40, 40))
            message_layout.add_widget(profile_image)

        # Add timestamp below the message
        timestamp = datetime.now().strftime('%I:%M %p, %b %d')
        if sender == 'user':
            timestamp_label = Label(text=timestamp, size_hint_y=None, halign='right', valign='middle',
                                    text_size=(self.scroll_view.width - 30, None), color=(0.043, 0.145, 0.278, 1),
                                    font_size=15)
        else:
            timestamp_label = Label(text=timestamp, size_hint_y=None, halign='left', valign='middle',
                                    text_size=(self.scroll_view.width - 30, None), color=(0.043, 0.145, 0.278, 1),
                                    font_size=15)

        timestamp_label.bind(texture_size=timestamp_label.setter('size'))

        message_box.add_widget(message_layout)
        message_box.add_widget(timestamp_label)

        self.chat_layout.add_widget(message_box)
        self.scroll_view.scroll_to(message_box)

    def update_rect(self, instance, sender):
        def update(instance, value):
            instance.canvas.before.clear()
            with instance.canvas.before:
                if sender == 'user':
                    Color(0.9, 0.9, 0.9, 1)  # Dark cement color for user messages
                else:
                    Color(0.043, 0.145, 0.278, 1)  # Dark blue color for bot messages
                RoundedRectangle(pos=instance.pos, size=instance.size, radius=[10, 10, 10, 10])

        return update

    def display_faqs(self, instance=None):  # Added instance parameter
        for question, answer, *has_options in FAQS:
            faq_button = MDFlatButton(text=question, font_name="Roboto", theme_text_color='Custom',
                                      text_color=(0.043, 0.145, 0.278, 1), md_bg_color=(0.9, 0.9, 0.9, 1), size_hint=(None, None),
                                      height=40)
            faq_button.bind(on_press=lambda instance, ans=answer, opt=has_options: self.show_faq_response(ans, opt))
            self.chat_layout.add_widget(faq_button)
        self.add_ask_something_else_button()

    def add_ask_something_else_button(self):
        ask_something_else_button = MDFlatButton(
            text="Ask Something Else",
            font_name="Roboto",
            theme_text_color='Custom',
            text_color=(0, 0, 0, 1),
            md_bg_color=(0.6, 0.6, 0.6, 1),
            size_hint=(None, None),
            height=40,
        )
        ask_something_else_button.bind(on_press=self.show_sure_tell_me_message)
        self.chat_layout.add_widget(ask_something_else_button)

    def show_faq_response(self, answer, has_options):
        if has_options:
            # Display two buttons: Call Support and Chat Support
            self.add_support_options()
        else:
            self.add_message(answer, 'bot')
            self.add_something_else_button()

    def show_sure_tell_me_message(self, instance):
        self.add_message("Sure, tell me", 'bot')

    def add_support_options(self):
        call_support_button = MDFlatButton(
            text="Call Support",
            font_name="Roboto",
            theme_text_color='Custom',
            text_color=(0, 0, 0, 1),
            md_bg_color=(0.6, 0.6, 0.6, 1),
            size_hint=(None, None),
            height=40,
            width=100
        )
        chat_support_button = MDFlatButton(
            text="Chat Support",
            font_name="Roboto",
            theme_text_color='Custom',
            text_color=(0, 0, 0, 1),
            md_bg_color=(0.6, 0.6, 0.6, 1),
            size_hint=(None, None),
            height=40,
            width=100
        )
        call_support_button.bind(on_press=self.show_call_support_message)
        chat_support_button.bind(on_press=self.show_chat_support_message)

        self.chat_layout.add_widget(call_support_button)
        self.chat_layout.add_widget(chat_support_button)

    def show_call_support_message(self, instance):
        self.add_message("You can call this toll-free number for P2P support: 1-800-123-4567", 'bot')
        self.add_something_else_button()

    def show_chat_support_message(self, instance):
        self.add_message("You can mail your issue to this mail id 'gtpltechnologies@gmail.com' this mail id", 'bot')
        self.add_something_else_button()

    def add_something_else_button(self):
        something_else_button = MDFlatButton(
            text="click this for more questions?",
            font_name="Roboto",
            theme_text_color='Custom',
            text_color=(0.043, 0.145, 0.278, 1),
            md_bg_color=(0.9, 0.9, 0.9, 1),
            size_hint=(None, None),
            height=40,
            width=100
        )
        something_else_button.bind(on_press=self.display_faqs)
        self.chat_layout.add_widget(something_else_button)


class LenderDashboardScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.add_widget(Label(text="Lender Dashboard"))
