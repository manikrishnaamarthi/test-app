import anvil
from anvil.tables import app_tables
from kivy.core.window import Window
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.filechooser import platform
from kivy.uix.image import Image
from kivy.uix.screenmanager import Screen, ScreenManager
import anvil.server
from kivy.lang import Builder
import anvil.server
from kivy.uix.screenmanager import Screen, SlideTransition
from kivy.uix.widget import Widget
from kivymd.app import MDApp
from kivymd.uix.button import MDFillRoundFlatButton
from kivymd.uix.card import MDCard
from kivymd.uix.label import MDLabel
from kivymd.uix.list import ThreeLineAvatarIconListItem, IconLeftWidget
import base64
from kivy.core.image import Image as CoreImage
from io import BytesIO
from kivymd.uix.boxlayout import MDBoxLayout
from kivy.graphics import Color, Line
from kivy.utils import get_color_from_hex
from kivy.clock import Clock
from kivy.properties import ObjectProperty
from datetime import datetime
import logging
import time
from num2words import num2words  # Library to convert numbers to words

lender_view_transaction_history = '''

<WindowManager>:
    TransactionLH:
    ViewProfileScreenLTH:

<TransactionLH>
    BoxLayout:
        orientation: 'vertical'
        MDTopAppBar:
            title: "Transaction History"
            elevation: 3
            left_action_items: [['arrow-left', lambda x: root.go_back_screen()]]
            right_action_items: [['refresh', lambda x: root.refresh()]]
            md_bg_color: 0.043, 0.145, 0.278, 1
        MDScrollView:
            MDBoxLayout:
                id: container2
                orientation: 'vertical'
                padding: dp(30)
                spacing: dp(10)
                size_hint_y: None
                height: self.minimum_height
                width: self.minimum_width
                adaptive_size: True

                pos_hint: {"center_x": 0, "center_y":  0}


<ViewProfileScreenLTH>:

    MDBoxLayout:
        orientation: 'horizontal'
        md_bg_color: 1, 1, 1, 1

        # Back arrow and status label
        MDIconButton:
            icon: "arrow-left"
            pos_hint: {"center_y": .95, "center_x": .05}
            user_font_size: "30sp"
            theme_text_color: "Custom"
            text_color: 0.102, 0.094, 0.227, 1
            on_release: root.on_back_button_press()

        MDLabel:
            id: status_label  # ID for dynamically changing status label
            text: ''
            halign: 'left'
            theme_text_color: 'Custom'
            text_color: 0, 0, 0, 1
            bold: True
            pos_hint: {"center_y": .95, "center_x": .5}
            size_hint_y: None
            height: dp(30)
            font_size: dp(20)

    # Card with curved edges for full screen height
    MDCard:
        orientation: 'vertical'
        padding: dp(10)
        size_hint: 0.9, 0.70
        elevation: 0.3
        radius: [25, 25, 25, 25]
        md_bg_color: 1, 1, 1, 1
        pos_hint: {"center_x": 0.5, "center_y": 0.45}

        # First part
        MDBoxLayout:
            orientation: 'vertical'
            padding: dp(10)
            spacing: dp(5)
            MDLabel:
                text: 'Amount'
                halign: 'left'
                theme_text_color: 'Custom'
                text_color: 0, 0, 0, 1

            MDBoxLayout:
                orientation: 'horizontal'
                size_hint_y: None
                height: dp(30)
                MDIcon:
                    id: rupee_icon  # ID for rupee icon
                    icon: 'currency-inr'
                    size_hint: None, None
                    size: dp(15), dp(15)
                    pos_hint: {"center_y": 0.5}
                MDLabel:
                    id: money_label  # ID for dynamically changing amount label
                    text: ''
                    halign: 'left'
                    text_color: 0, 0, 0, 1
                    bold: True
                    size_hint_x: None
                    pos_hint: {"center_y": 0.5}
                    font_style:'H6'
                Image:
                    id: selected_image1
                    size_hint: None, None
                    size: dp(30), dp(30)
                    source: "img2.png"  
                    allow_stretch: True
                    keep_ratio: True
                    pos_hint: {"center_y": 0.5}
                    canvas.before:
                        StencilPush
                        Ellipse:
                            size: self.size
                            pos: self.pos
                        StencilUse
                    canvas:
                        Rectangle:
                            texture: self.texture
                            size: self.size
                            pos: self.pos
                    canvas.after:
                        StencilUnUse
                        Ellipse:
                            size: self.size
                            pos: self.pos
                        StencilPop

            MDLabel:
                id: amount_in_words_label
                text: ""
                halign: 'left'
                theme_text_color: 'Custom'
                text_color: 0, 0, 0, 1

            MDSeparator:
                height: dp(1)
                color: 0.5, 0.5, 0.5, 1

        # Second part
        MDBoxLayout:
            orientation: 'horizontal'
            padding: dp(10)
            spacing: dp(5)

            MDBoxLayout:
                orientation: 'vertical'
                spacing: dp(5)
                MDLabel:
                    text: ''
                    id: transaction_type_label
                    halign: 'left'
                    theme_text_color: 'Custom'
                    text_color: 0, 0, 0, 1

                MDLabel:
                    id: user_name
                    text: ''
                    font_style:'H5'
                    bold: True
                    halign: 'left'
                    theme_text_color: 'Custom'
                    text_color: 0, 0, 0, 1

                MDLabel:
                    id: transaction_id
                    text: ''
                    halign: 'left'
                    theme_text_color: 'Custom'
                    text_color: 0, 0, 0, 1

            Image:
                id: selected_image2
                size_hint: None, None
                size: dp(50), dp(50)
                source: ""  # Set the path to your image source if needed
                allow_stretch: True
                keep_ratio: True
                pos_hint: {"center_y": 0.5}
                canvas.before:
                    StencilPush
                    Ellipse:
                        size: self.size
                        pos: self.pos
                    StencilUse
                canvas:
                    Rectangle:
                        texture: self.texture
                        size: self.size
                        pos: self.pos
                canvas.after:
                    StencilUnUse
                    Ellipse:
                        size: self.size
                        pos: self.pos
                    StencilPop

        MDSeparator:
            height: dp(1)
            color: 0.5, 0.5, 0.5, 1

        # Third part
        MDBoxLayout:
            orientation: 'horizontal'
            padding: dp(10)
            spacing: dp(5)

            MDBoxLayout:
                orientation: 'vertical'
                spacing: dp(5)
                MDLabel:
                    text: ''
                    id: to_from_label
                    halign: 'left'
                    theme_text_color: 'Custom'
                    text_color: 0, 0, 0, 1

                MDLabel:
                    id: name_label
                    text: ''
                    font_style:'H5'
                    bold: True
                    halign: 'left'
                    theme_text_color: 'Custom'
                    text_color: 0, 0, 0, 1

                MDLabel:
                    id: timestamp_label
                    text: ''
                    halign: 'left'
                    theme_text_color: 'Custom'
                    text_color: 0, 0, 0, 1

            Image:
                id: selected_image3
                size_hint: None, None
                size: dp(50), dp(50)
                source: ""  # Set the path to your image source if needed
                allow_stretch: True
                keep_ratio: True
                pos_hint: {"center_y": 0.5}
                canvas.before:
                    StencilPush
                    Ellipse:
                        size: self.size
                        pos: self.pos
                    StencilUse
                canvas:
                    Rectangle:
                        texture: self.texture
                        size: self.size
                        pos: self.pos
                canvas.after:
                    StencilUnUse
                    Ellipse:
                        size: self.size
                        pos: self.pos
                    StencilPop



'''
Builder.load_string(lender_view_transaction_history)


class LineSeparator(Widget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.padding_left = 95  # Adjust left padding as needed

        with self.canvas.before:
            Color(0.5, 0.5, 0.5, 1)  # Adjust color as needed (RGBA format)
            self.line = Line(points=[0, 0, 1000, 0], width=1)  # Adjust width as needed

    def on_size(self, *args):
        self.line.points = [self.padding_left, self.y, self.width + self.x, self.y]


class CustomTwoLineListItem(MDBoxLayout):
    def __init__(self, text, secondary_text, amount_text, status_text, transaction_id, **kwargs):
        super().__init__(orientation='vertical', spacing=5, padding=5, **kwargs)
        self.transaction_id = transaction_id
        # Define colors
        transaction_color = get_color_from_hex('#808080')  # Cement color

        # First line with name and amount
        first_line_layout = MDBoxLayout(orientation='horizontal', spacing=10)

        name_label = MDLabel(
            text=text,
            size_hint_x=0.8,
            halign='left',
            valign='middle',
            bold=True,
            font_style='H5'  # Use MDLabel's font style for bold text
        )
        amount_label = MDLabel(
            text=amount_text,
            size_hint_x=0.2,
            halign='right',
            valign='middle',
            bold=True,
            font_size='14sp'
            # Use MDLabel's font style for bold text
        )

        first_line_layout.add_widget(name_label)
        first_line_layout.add_widget(amount_label)

        # Second line with transaction type and status
        second_line_layout = MDBoxLayout(orientation='horizontal', spacing=10)

        transaction_label = MDLabel(
            text=secondary_text,
            size_hint_x=0.8,
            halign='left',
            valign='middle',
            theme_text_color='Custom',
            text_color=transaction_color,
            font_size='13sp'  # Use MDLabel's font style for regular text
        )

        status_label = MDLabel(
            text=status_text,
            size_hint_x=0.2,
            halign='right',
            valign='middle',
            font_style='H6'  # Use MDLabel's font style for regular text
        )

        if status_text.lower() == 'success':
            status_label.theme_text_color = 'Custom'
            status_label.text_color = (0, 1.5, 0, 1)  # Green color for success
        elif status_text.lower() == 'fail':
            status_label.theme_text_color = 'Custom'
            status_label.text_color = (1, 0, 0, 1)  # Red color for fail

        second_line_layout.add_widget(transaction_label)
        second_line_layout.add_widget(status_label)

        self.add_widget(first_line_layout)
        self.add_widget(second_line_layout)


class TransactionLH(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        Clock.schedule_once(lambda dt: self.init_data(), 0)
        self.displayed_transactions_count = 0

    def init_data(self):
        try:
            start_time = time.time()
            print("TransactionLH init_data started")

            email = self.get_email()
            print(f"Email fetched: {email}")

            profile = app_tables.fin_user_profile.search()
            transaction = app_tables.fin_wallet_transactions.search()
            print(f"Profile and transactions fetched. Profiles: {len(profile)}, Transactions: {len(transaction)}")

            transaction_id = []
            wallet_customer_id = []
            status = []
            transaction_type = []
            amount = []
            transaction_time_stamp = []
            user_email = []
            receiver_email = []

            for i in transaction:
                transaction_id.append(i['transaction_id'])
                wallet_customer_id.append(i['customer_id'])
                transaction_type.append(i['transaction_type'])
                transaction_time_stamp.append(i['transaction_time_stamp'])
                status.append(i['status'])
                amount.append(i['amount'])
                user_email.append(i['user_email'])
                receiver_email.append(i['receiver_email'])

            pro_customer_id = []
            pro_mobile_number = []
            pro_email_id = []
            borrower_name = []

            for i in profile:
                pro_customer_id.append(i['customer_id'])
                pro_mobile_number.append(i['mobile'])
                pro_email_id.append(i['email_user'])
                borrower_name.append(i['full_name'])

            index = -1
            if email in pro_email_id:
                index = pro_email_id.index(email)

            print(f"Profile index found: {index}")

            index_list = []

            for idx, val in enumerate(wallet_customer_id):
                if val == pro_customer_id[index]:
                    index_list.append(idx)

            print(f"Index list for matching customer IDs: {index_list}")

            transaction_count_with_email = 0  # Counter for transactions with your email
            transactions_with_email = []  # List to store transactions with the user's email

            for i in reversed(index_list):
                if email == user_email[i]:
                    transaction_count_with_email += 1
                    transactions_with_email.append((transaction_id[i], transaction_type[i]))

            # Print transactions with the user's email
            print(f"Transactions with your email ({email}): {transaction_count_with_email}")
            for tid, ttype in transactions_with_email:
                print(f"Transaction ID: {tid}, Type: {ttype}")

            transaction_item_count = 0  # Counter for transactions fetched into items
            transaction_items = []  # List to store transaction items

            for i in reversed(index_list):
                loop_start_time = time.time()

                # Check if your email is in the user_email column
                if email == user_email[i]:
                    other_email = receiver_email[i]
                else:
                    # Skip this transaction if your email is not in user_email column
                    continue

                if other_email in pro_email_id:
                    number = pro_email_id.index(other_email)
                    other_name = borrower_name[number]
                else:
                    other_name = "Unknown"
                    logging.warning(f"Other email {other_email} not found in pro_email_id")

                main_layout = BoxLayout(orientation='horizontal', size_hint=(None, None), size=("520dp", "80dp"))
                image_layout = BoxLayout(orientation='vertical', size_hint_x=None, width="50dp", padding="5dp")

                image_data_start = time.time()
                image_data = self.get_user_photo(other_email)
                print(f"Image data fetched for {other_email} in {time.time() - image_data_start:.2f} seconds")

                image_widget_start = time.time()
                image = self.get_image_widget(image_data)
                print(f"Image widget created for {other_email} in {time.time() - image_widget_start:.2f} seconds")

                image_layout.add_widget(image)

                info_layout = BoxLayout(orientation='vertical', spacing=10, padding=10)
                transaction_time = transaction_time_stamp[i].strftime("%I:%M %p, %d-%m-%Y")

                if transaction_type[i] == "amount transferred":
                    secondary_text = f"Sent on {transaction_time}"
                    amount_text = f"-{amount[i]}"
                elif transaction_type[i] == "amount received":
                    secondary_text = f"Received on {transaction_time}"
                    amount_text = f"+{amount[i]}"
                else:
                    continue

                item = CustomTwoLineListItem(
                    text=other_name,
                    secondary_text=secondary_text,
                    amount_text=amount_text,
                    status_text=status[i],
                    transaction_id=transaction_id[i]
                )
                item.transaction_type = transaction_type[i]  # Adding transaction type to the item
                item.amount = amount[i]  # Adding amount to the item
                item.bind(on_touch_down=self.on_transaction_click)
                info_layout.add_widget(item)
                main_layout.add_widget(image_layout)
                main_layout.add_widget(info_layout)

                self.ids.container2.add_widget(main_layout)
                self.ids.container2.add_widget(LineSeparator())

                # Print transaction ID and type during display
                transaction_items.append((transaction_id[i], transaction_type[i]))
                print(f"Transaction ID: {transaction_id[i]}, Type: {transaction_type[i]}")
                transaction_item_count += 1
                print(f"Loop for transaction {i} completed in {time.time() - loop_start_time:.2f} seconds")

            # Print transaction items
            print(f"Total transaction items fetched: {transaction_item_count}")
            for tid, ttype in transaction_items:
                print(f"Transaction ID: {tid}, Type: {ttype}")

            self.displayed_transactions_count += 1
            print(f"Transactions displayed: {self.displayed_transactions_count}")
            print(f"Total transactions fetched: {len(index_list)}")  # New print statement

        except Exception as e:
            print(f"Error in init_data: {e}")
            # Handle exceptions gracefully or add more specific error handling

    def get_email(self):
        # Replace with your method to get the current user's email
        return anvil.server.call('another_method')

    def get_user_photo(self, email):
        data = app_tables.fin_user_profile.search(email_user=email)
        if data and len(data) > 0:
            return data[0]['user_photo']
        return None

    def get_image_widget(self, image_data):
        if image_data:
            try:
                image_data = image_data.get_bytes()
                profile_texture_io = BytesIO(image_data)
                photo_texture = CoreImage(profile_texture_io, ext='png').texture
                image = Image(texture=photo_texture, size_hint_x=None, height="50dp", width="50dp")
                return image
            except Exception as e:
                logging.error(f"Error loading image: {e}")
        # If no image data or error loading, return a default image
        default_image = Image(source='img.png', size_hint_x=None, height="50dp", width="50dp")
        return default_image

    def on_transaction_click(self, instance, touch):
        if instance.collide_point(*touch.pos):
            transactions_id = instance.transaction_id
            transaction_type = instance.transaction_type  # Get the transaction type
            amount = instance.amount  # Get the amount
            sm = self.manager

            # Create a new instance of the ViewProfileScreenBTH
            profile = ViewProfileScreenLTH(name='ViewProfileScreenLTH')

            # Add the ViewProfileScreenBTH to the existing ScreenManager
            sm.add_widget(profile)

            # Switch to the ViewProfileScreenBTH
            sm.current = 'ViewProfileScreenLTH'
            self.manager.get_screen('ViewProfileScreenLTH').initialize_with_value(transactions_id, transaction_type,
                                                                                  amount)

    def on_pre_enter(self):
        # Bind the back button event to the on_back_button method
        Window.bind(on_keyboard=self.on_back_button)

    def on_pre_leave(self):
        # Unbind the back button event when leaving the screen
        Window.unbind(on_keyboard=self.on_back_button)

    def on_back_button(self, instance, key, scancode, codepoint, modifier):
        # Handle the back button event
        if key == 27:  # 27 is the keycode for the hardware back button on Android
            self.go_back_screen()
            return True  # Consume the event, preventing further handling
        return False  # Continue handling the event

    def go_back_screen(self):
        self.manager.transition = SlideTransition(direction='right')
        self.manager.current = 'LenderDashboard'

    def refresh(self):
        self.ids.container2.clear_widgets()
        self.__init__()

    def get_table(self):
        # Make a call to the Anvil server function
        # Replace 'YourAnvilFunction' with the actual name of your Anvil server function
        return anvil.server.call('another_method')

    def on_back_button_press(self):
        self.manager.current = 'LenderDashboard'


class ViewProfileScreenLTH(Screen):
    status_label = ObjectProperty(None)
    rupee_icon = ObjectProperty(None)
    money_label = ObjectProperty(None)
    amount_in_words_label = ObjectProperty(None)
    user_name = ObjectProperty(None)
    transaction_id = ObjectProperty(None)
    to_from_label = ObjectProperty(None)
    transaction_type_label = ObjectProperty(None)
    name_label = ObjectProperty(None)
    timestamp_label = ObjectProperty(None)
    selected_image2 = ObjectProperty(None)
    selected_image3 = ObjectProperty(None)

    def initialize_with_value(self, value, transaction_type, amount):
        # Fetch latest data from the database
        data = app_tables.fin_wallet_transactions.search()

        transaction_id = []
        user_email = []
        receiver_email = []
        wallet_id = []
        transaction_type_list = []
        amount_list = []
        date_time = []
        status = []

        # Populate lists with data from the database
        for i in data:
            transaction_id.append(i['transaction_id'])
            user_email.append(i['user_email'])
            receiver_email.append(i['receiver_email'])
            wallet_id.append(i['wallet_id'])
            transaction_type_list.append(i['transaction_type'].strip().lower())
            amount_list.append(i['amount'])
            date_time.append(i['transaction_time_stamp'])
            status.append(i['status'])

        found = False  # Flag to track if the correct transaction is found
        current_user_email = self.get_email()  # Get current user's email

        for idx, trans_id in enumerate(transaction_id):
            if trans_id == value and current_user_email == user_email[idx]:
                # Found the correct transaction for the current user
                transaction_type_value = transaction_type_list[idx]

                print(f"Found transaction for transaction_id {value} and user_email {current_user_email}")
                print(f"Transaction type: {transaction_type_value}")
                print(f"Transaction amount: {amount}")

                # Set amount label and image
                self.ids.money_label.text = str(amount)
                # self.ids.rupee_icon.icon = 'currency-inr'

                # Convert amount to words including paise
                rupees = int(amount)
                paise = round((amount - rupees) * 100)

                amount_in_words_rupees = self.amount_to_words(rupees)
                amount_in_words_paise = self.amount_to_words(paise)

                if paise > 0:
                    self.ids.amount_in_words_label.text = f"Rupees {amount_in_words_rupees} and {amount_in_words_paise} Paise Only"
                else:
                    self.ids.amount_in_words_label.text = f"Rupees {amount_in_words_rupees} only"

                # Get receiver's email and fetch their name
                receiver_email_value = receiver_email[idx]
                self.ids.user_name.text = self.get_full_name(receiver_email_value)

                current_user_photo_texture = self.fetch_profile_photo_texture(current_user_email)
                receiver_photo_texture = self.fetch_profile_photo_texture(receiver_email_value)
                if receiver_photo_texture:
                    self.ids.selected_image2.texture = receiver_photo_texture
                else:
                    print(f"No profile photo found for receiver email: {receiver_email_value}")

                if current_user_photo_texture:
                    self.ids.selected_image3.texture = current_user_photo_texture
                else:
                    print(f"No profile photo found for current user email: {current_user_email}")
                transaction = str(value)
                self.ids.transaction_id.text = f"Transaction Id: {transaction}"
                self.ids.transaction_type_label.text = 'To' if transaction_type == "amount transferred" else 'From'
                self.ids.to_from_label.text = 'From' if transaction_type == "amount transferred" else 'To'
                self.ids.status_label.text = 'Paid Successfully' if transaction_type == "amount transferred" else 'Received Successfully'
                self.ids.name_label.text = self.get_full_name(current_user_email)

                # Format timestamp_label based on transaction type
                timestamp_value = date_time[idx]
                formatted_timestamp = self.format_timestamp(timestamp_value, transaction_type)
                self.ids.timestamp_label.text = formatted_timestamp

                found = True
                break  # Exit loop once the correct transaction is found

        if not found:
            print(f"Transaction {value} not found for user_email {current_user_email}")

    def amount_to_words(self, amount):
        # Dictionary to convert numbers into words
        num_words = {
            0: 'Zero', 1: 'One', 2: 'Two', 3: 'Three', 4: 'Four', 5: 'Five',
            6: 'Six', 7: 'Seven', 8: 'Eight', 9: 'Nine', 10: 'Ten',
            11: 'Eleven', 12: 'Twelve', 13: 'Thirteen', 14: 'Fourteen', 15: 'Fifteen',
            16: 'Sixteen', 17: 'Seventeen', 18: 'Eighteen', 19: 'Nineteen', 20: 'Twenty',
            30: 'Thirty', 40: 'Forty', 50: 'Fifty', 60: 'Sixty', 70: 'Seventy',
            80: 'Eighty', 90: 'Ninety'
        }

        # Add special cases for numbers above twenty
        if amount < 0:
            return "Minus " + self.amount_to_words(-amount)
        elif amount < 21:
            return num_words[amount]
        elif amount < 100:
            return num_words[(amount // 10) * 10] + (" " + num_words[amount % 10] if amount % 10 != 0 else "")
        elif amount < 1000:
            return num_words[amount // 100] + " Hundred" + (
                " " + self.amount_to_words(amount % 100) if amount % 100 != 0 else "")
        elif amount < 100000:
            return self.amount_to_words(amount // 1000) + " Thousand" + (
                " " + self.amount_to_words(amount % 1000) if amount % 1000 != 0 else "")
        elif amount < 10000000:
            return self.amount_to_words(amount // 100000) + " Lakh" + (
                " " + self.amount_to_words(amount % 100000) if amount % 100000 != 0 else "")
        else:
            return "Number too large to convert"

    def get_full_name(self, email):
        profile = app_tables.fin_user_profile.search(email_user=email)
        if profile and len(profile) > 0:
            return profile[0]['full_name']
        return "Unknown"

    def format_timestamp(self, timestamp, transaction_type_value):
        # Format time as hours:minutes AM/PM
        formatted_time = timestamp.strftime('%I:%M %p, %d-%m-%Y')

        # Construct final label based on transaction type
        if transaction_type_value == "amount transferred":
            return f"Paid at {formatted_time}"
        elif transaction_type_value == "amount received":
            return f"Received at {formatted_time}"
        else:
            return "Unknown Time"

    def on_pre_enter(self):
        # Bind the back button event to the on_back_button method
        Window.bind(on_keyboard=self.on_back_button)

    def on_pre_leave(self):
        # Unbind the back button event when leaving the screen
        Window.unbind(on_keyboard=self.on_back_button)

    def on_back_button(self, instance, key, scancode, codepoint, modifier):
        # Handle the back button event
        if key == 27:  # 27 is the keycode for the hardware back button on Android
            self.on_back_button_press()
            return True  # Consume the event, preventing further handling
        return False  # Continue handling the event

    def get_email(self):
        # Replace with your method to get the current user's email
        return anvil.server.call('another_method')

    def on_back_button_press(self):
        self.manager.transition = SlideTransition(direction='right')
        self.manager.current = 'TransactionLH'

    def fetch_profile_photo_texture(self, email):
        # Fetch profile photo from database and return as a CoreImage texture
        data = app_tables.fin_user_profile.search(email_user=email)

        if not data:
            print("No data found for email:", email)
            return self.load_default_image_texture()

        for row in data:
            if row['user_photo']:
                image_data = row['user_photo'].get_bytes()
                if isinstance(image_data, bytes):
                    try:
                        profile_texture_io = BytesIO(image_data)
                        profile_texture_obj = CoreImage(profile_texture_io, ext='png').texture
                        return profile_texture_obj
                    except Exception as e:
                        print(f"Error processing image for email {email}: {e}")
                        return self.load_default_image_texture()
            else:
                print(f"No profile photo found for email {email}")
                return self.load_default_image_texture()

    def load_default_image_texture(self):
        # Load default image texture (img.png)
        try:
            default_texture_obj = CoreImage("img.png").texture
            return default_texture_obj
        except Exception as e:
            print(f"Error loading default image texture: {e}")
            return None


class MyScreenManager(ScreenManager):
    pass



