import json
import os
import sqlite3

from kivymd.uix.button import MDFlatButton, MDRectangleFlatButton
from kivymd.uix.dialog import MDDialog

from login import OTPScreen
from anvil.tables import app_tables
from kivy.app import App
from kivy.core.window import Window
from kivy.lang import Builder
from kivy.metrics import dp
from kivy.uix.spinner import SpinnerOption
from kivymd.app import MDApp
from kivy.uix.screenmanager import ScreenManager, SlideTransition
from kivy.uix.screenmanager import Screen
from kivy.properties import BooleanProperty, Clock
from kivy.uix.label import Label
from kivy.uix.popup import Popup
from twilio.rest import Client
import random
import smtplib
from email.message import EmailMessage
from borrower_dashboard import DashboardScreen
from dashboard import DashScreen
from homepage import MainScreen

import anvil.server
from login import OTPScreen
from lender_dashboard import LenderDashboard

anvil.server.connect("server_P54N73TZWZQQLSINFSXUK6X2-OZATT3SDKEEAAR6A")


class MyApp(MDApp):
    otp_screen_visible = BooleanProperty(False)
    client = Client("AC719092795e946e1f96fac9c65257291c", "bce8fed824c0109550dec242afc79130")
    n = random.randint(100000, 999999)
    dialog = None

    def build(self):
        self.sm = ScreenManager(transition=SlideTransition())
        self.load_initial_screen()

        # Add all the screens to the ScreenManager
        main_screen = MainScreen(name='MainScreen')
        otp_screen = OTPScreen(name='otp')
        self.sm.add_widget(main_screen)
        self.sm.add_widget(otp_screen)

        return self.sm

    #### otp code starts from here  ###
    def resend_otp(self):
        login_otp_screen = self.root.get_screen('login')
        user_input = login_otp_screen.ids.user_input.text
        self.send_otp()

    def verify_login(self):
        login_screen = self.root.get_screen('login')
        user_input = login_screen.ids.user_input.text

        if user_input:
            self.send_otp()
        else:
            self.show_dialog("Please enter email ID or phone number")

    def send_otp(self):
        login_otp_screen = self.root.get_screen('login')
        user_input = login_otp_screen.ids.user_input.text
        if user_input:
            self.n = random.randint(100000, 999999)
            if "@" in user_input:
                self.send_email_otp(user_input)
            else:
                self.send_sms_otp(user_input)
            self.show_otp_screen(user_input)
        else:
            self.show_dialog("Please enter a phone number or email ID")

    def send_sms_otp(self, user_input):
        try:
            if not user_input.startswith("+"):
                user_input = "+91" + user_input
            self.client.messages.create(
                to=user_input,
                from_="+12027299166",
                body=f"Your OTP is: {self.n}"
            )
            self.show_dialog("OTP sent via SMS")
        except Exception as e:
            self.show_dialog(f"Failed to send SMS: {e}")

    def send_email_otp(self, email):
        try:
            from_mail = "maniamarthi@gmail.com"
            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.starttls()
            server.login(from_mail, "kulb rdtv kdcq zstt")

            msg = EmailMessage()
            msg['Subject'] = "OTP Verification"
            msg['From'] = from_mail
            msg['To'] = email
            msg.set_content(f"Your OTP is: {self.n}")
            server.send_message(msg)
            server.quit()
            self.show_dialog("OTP sent via Email")
        except Exception as e:
            self.show_dialog(f"Failed to send email: {e}")

    def check_otp(self):
        otp_screen = self.root.get_screen('otp')
        entered_otp = otp_screen.ids.otp_input.text
        login_screen = self.root.get_screen('login')
        user_input = login_screen.ids.user_input.text  # Get user input from login screen

        if str(self.n) == entered_otp:
            self.show_dialog("OTP verified successfully")
            self.perform_database_operations(user_input)
        else:
            self.show_dialog("Invalid OTP. Please try again.")

    def perform_database_operations(self, entered_email):
        conn = sqlite3.connect("fin_user.db")
        cursor = conn.cursor()

        cursor.execute('''
            SELECT * FROM fin_users
            WHERE email = ?
        ''', (entered_email,))

        user_data = cursor.fetchone()
        data = app_tables.users.search()
        profile = app_tables.fin_user_profile.search()
        email_list = []
        registration_approve = []
        user_type = []
        email_user = []

        for i in data:
            email_list.append(i['email'])
        for i in profile:
            registration_approve.append(i['registration_approve'])
            user_type.append(i['usertype'])
            email_user.append(i['email_user'])

        if entered_email in email_list:
            i = email_list.index(entered_email)
            if entered_email in email_user:
                index = email_user.index(entered_email)
            else:
                self.show_dialog('No email found')
                return

            if (email_list[i] == entered_email) and (registration_approve[index] is True):
                self.save_user_info(entered_email, user_type[index])  # Save user info to email.json

                if user_type[index] == 'borrower':
                    Clock.schedule_once(lambda dt: self.show_dashboard('DashboardScreen'), 0)
                elif user_type[index] == 'lender':
                    Clock.schedule_once(lambda dt: self.show_dashboard('LenderDashboard'), 0)
                else:
                    Clock.schedule_once(lambda dt: self.show_dashboard('DashScreen'), 0)

                return
            elif registration_approve[index] is None or user_type[index] == "":
                Clock.schedule_once(lambda dt: self.show_dashboard('DashScreen'), 0)
                return
            else:
                Clock.schedule_once(lambda dt: self.show_error_dialog("Unapproved registration or other issue"), 0)
                return
        else:
            self.show_dialog("Email not found")

    def save_user_info(self, email, user_type):
        user_data = {
            'email': email,
            'logged_status': True,
            'user_type': user_type
        }

        # Check if the emails.json file exists and load data, or initialize as an empty dict
        if os.path.exists("emails.json"):
            with open("emails.json", "r") as file:
                try:
                    data = json.load(file)
                except json.JSONDecodeError:
                    data = {}
        else:
            data = {}

        data[email] = user_data

        # Write back the updated data to emails.json
        with open("emails.json", "w") as file:
            json.dump(data, file, indent=4)

    def show_dashboard(self, screen_name):
        if screen_name == 'DashboardScreen':
            self.sm.add_widget(DashboardScreen(name=screen_name))
        elif screen_name == 'LenderDashboard':
            self.sm.add_widget(LenderDashboard(name=screen_name))
        else:
            self.sm.add_widget(DashScreen(name=screen_name))
        self.sm.current = screen_name

    def show_otp_screen(self, user_input):
        otp_screen = self.root.get_screen('otp')
        otp_screen.ids.user_contact.text = user_input  # Update user contact label
        print(f"user_contact label text set to: {user_input}")  # Debug print
        self.sm.current = 'otp'

    def edit_user_input(self):
        self.root.current = 'login'

    def show_dialog(self, message):
        if self.dialog:
            self.dialog.dismiss()

        dialog = MDDialog(
            title="Success",
            text=message,
            size_hint=(0.8, None),
            height=dp(200),
            buttons=[
                MDRectangleFlatButton(
                    text="OK",
                    text_color=(0.043, 0.145, 0.278, 1),
                    on_release=lambda x: dialog.dismiss()
                )
            ]
        )
        dialog.open()

    def get_otp_call(self):
        login_otp_screen = self.root.get_screen('login')
        user_input = login_otp_screen.ids.user_input.text
        if user_input:
            self.n = random.randint(100000, 999999)
            self.send_voice_otp(user_input)
            self.show_otp_screen(user_input)  # Pass user_input to show_otp_screen
        else:
            self.show_dialog("Please enter a phone number or email ID")

    def send_voice_otp(self, user_input):
        try:
            if not user_input.startswith("+"):
                user_input = "+91" + user_input
            call = self.client.calls.create(
                twiml=f'<Response><Say>Your OTP is {self.n}</Say></Response>',
                to=user_input,
                from_="+14175242099"
            )
            self.show_dialog("OTP call initiated")
        except Exception as e:
            self.show_dialog(f"Failed to send OTP call: {e}")

    #### ended otp code ####

    def load_initial_screen(self):
        # Load initial screen based on logged status and user type
        with open("emails.json", "r") as file:
            user_data = json.load(file)
        print("user_data:", user_data)  # Debug print

        for email, data in user_data.items():
            print("email:", email)  # Debug print
            print("data type:", type(data))  # Debug print
            print("data:", data)  # Debug print
            if isinstance(data, dict) and data.get("logged_status", False):
                user_type = data.get("user_type", "")
                if user_type == "borrower":
                    self.sm.add_widget(DashboardScreen(name='DashboardScreen'))
                    self.sm.current = 'DashboardScreen'
                elif user_type == "lender":
                    self.sm.add_widget(LenderDashboard(name='LenderDashboard'))
                    self.sm.current = 'LenderDashboard'
                else:
                    self.sm.add_widget(DashScreen(name='DashScreen'))
                    self.sm.current = 'DashScreen'
                break
        else:
            self.sm.add_widget(MainScreen(name='MainScreen'))
            self.sm.current = 'MainScreen'

    def on_pre_enter(self):
        Window.bind(on_keyboard=self.on_keyboard)
        Window.bind(on_keyboard=self.on_back_button)

    def on_pre_leave(self):
        Window.unbind(on_keyboard=self.on_keyboard)
        Window.unbind(on_keyboard=self.on_back_button)

    def on_back_button(self, instance, key, scancode, codepoint, modifier):

        if key == 27:
            self.go_back()
            return True
        return False

    def on_keyboard(self, window, key, *args):
        if key == 27:  # Key code for the 'Escape' key
            # Keyboard is closed, move the screen down
            self.screen_manager.y = 0
        return True

    def on_start(self):
        # Preload data when the app starts
        self.fetch_product_groups()

    def fetch_product_groups(self):
        # Call the server function using Anvil Uplink
        product_groups = app_tables.fin_product_details.search()

        # Extract unique product groups
        unique_groups = set(product['product_group'] for product in product_groups)

        # Update the Spinner with unique product groups
        spinner = self.root.get_screen('NewloanScreen').ids.group_id1
        spinner.values = list(unique_groups)
        # Clear other Spinners and labels
        self.clear_spinners_and_labels(['group_id2', 'group_id3'])
        self.clear_label('product_description')

    def fetch_product_categories(self):
        # Clear other Spinners and labels
        self.clear_spinners_and_labels(['group_id3'])
        self.clear_label('product_description')

        # Get the selected product group
        selected_group = self.root.get_screen('NewloanScreen').ids.group_id1.text

        # Call the server function using Anvil Uplink to filter categories based on the selected group
        product_categories = app_tables.fin_product_details.search(product_group=selected_group)

        # Extract unique product categories for the selected group
        unique_categories = set(product['product_categories'] for product in product_categories)

        # Update the Spinner with unique product categories
        spinner = self.root.get_screen('NewloanScreen').ids.group_id2
        spinner.values = list(unique_categories)

    def fetch_product_name(self):
        # Clear other Spinners and labels
        self.clear_label('product_description')

        # Get the selected product category
        selected_category = self.root.get_screen('NewloanScreen').ids.group_id2.text

        # Call the server function using Anvil Uplink to filter product names based on the selected category
        product_names = app_tables.fin_product_details.search(product_categories=selected_category)

        # Extract unique product names for the selected category
        unique_names = set(product['product_name'] for product in product_names)

        # Update the Spinner with unique product names
        spinner = self.root.get_screen('NewloanScreen').ids.group_id3
        spinner.values = list(unique_names)

    def fetch_emi_type(self):
        # Get the selected product category
        selected_category = self.root.get_screen('NewloanScreen').ids.group_id3.text
        # Call the server function using Anvil Uplink to filter product names based on the selected category
        emi_type = app_tables.fin_product_details.search(product_name=selected_category)
        # Extract emi_type from the fetched data
        if emi_type:
            emi_type_list = emi_type[0]['emi_payment'].split(',')  # Split the emi_type string by commas
            # Update the Spinner with filtered product names
            spinner = self.root.get_screen('NewloanScreen1').ids.group_id4
            spinner.values = emi_type_list
        else:
            # Clear the Spinner if no emi_type is found
            self.root.get_screen('NewloanScreen1').ids.group_id4.values = []

    def fetch_product_description(self):
        # Get the selected product name
        selected_product_name = self.root.get_screen('NewloanScreen').ids.group_id3.text

        # Call the server function using Anvil Uplink to fetch the product description based on the selected product name
        product = app_tables.fin_product_details.search(product_name=selected_product_name)

        # Check if product list is not empty before accessing its elements
        if product:
            if len(product) > 0:
                product_description = product[0]['product_description']
                # Check if product_description is not None before updating the label
                if product_description is not None:
                    # Update the product description label with the fetched description
                    self.root.get_screen('NewloanScreen').ids.product_description.text = product_description
                else:
                    # Set a default message when product_description is None
                    self.root.get_screen('NewloanScreen').ids.product_description.text = "No description available"
        else:
            # Clear the product description label if no product is found
            self.root.get_screen('NewloanScreen').ids.product_description.text = ""

    def clear_spinners_and_labels(self, spinner_ids):
        for spinner_id in spinner_ids:
            self.root.get_screen('NewloanScreen').ids[spinner_id].text = "Select"
            self.root.get_screen('NewloanScreen').ids[spinner_id].values = []

    def clear_label(self, label_id):
        self.root.get_screen('NewloanScreen').ids[label_id].text = ""

    def on_start(self):
        Window.softinput_mode = "below_target"


class MyScreenManager(ScreenManager):
    pass


if __name__ == '__main__':
    MyApp().run()
