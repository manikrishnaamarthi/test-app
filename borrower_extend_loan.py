from datetime import datetime, timezone
import anvil.server
from bson import utc
from kivy.config import value
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.metrics import dp
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.image import Image
from kivy.uix.label import Label
from kivy.uix.popup import Popup
from kivy.uix.widget import Widget
from kivymd.uix.button import MDFlatButton, MDRectangleFlatButton, MDFillRoundFlatButton, MDRaisedButton
from kivymd.uix.card import MDCard
from kivymd.uix.dialog import MDDialog
from kivymd.uix.label import MDLabel
from kivy.utils import get_color_from_hex
from kivymd.uix.list import *
from kivy.lang import Builder
from datetime import datetime
from kivy.core.window import Window
import anvil.users
import server
from anvil.tables import app_tables
from kivy.uix.screenmanager import Screen, SlideTransition, ScreenManager
from kivy.uix.label import Label
import base64
from kivy.core.image import Image as CoreImage
from io import BytesIO

extension_loan_request = """
<WindowManager>:
    ExtendLoan:
    ExtendRequestScreen:

<ExtendLoan> 
    BoxLayout:
        orientation: 'vertical'
        MDTopAppBar:
            title: "Extension Loan Request"
            elevation: 3
            left_action_items: [['arrow-left', lambda x: root.on_back_button_press()]]
            right_action_items: [['refresh', lambda x: root.refresh()]]
            md_bg_color: 0.043, 0.145, 0.278, 1
            title_align: 'center'
        MDScrollView:
            MDBoxLayout:
                id: container
                orientation: 'vertical'
                padding: dp(30)
                spacing: dp(10)
                size_hint_y: None
                height: self.minimum_height
                width: self.minimum_width
                adaptive_size: True

                pos_hint: {"center_x": 0, "center_y":  0}


<ExtendRequestScreen>
    GridLayout:
        cols: 1
        MDTopAppBar:
            title: "View Profile"
            elevation: 3
            left_action_items: [['arrow-left', lambda x: root.on_back_button_press()]]
            md_bg_color: 0.043, 0.145, 0.278, 1 
            title_align: 'left'


        BoxLayout:
            orientation: 'vertical'
            spacing: dp(50)
            padding: dp(30)
            size_hint_y: None
            height: self.minimum_height
            canvas.before:
                Color:
                    rgba: 230/255, 245/255, 255/255, 1 
                RoundedRectangle:
                    pos: self.pos
                    size: self.size
                    radius: [1, 1, 1, 1]
                    source: "background.jpg"

            MDGridLayout:
                cols: 2

                MDLabel:
                    text: 'Loan Amount:'
                    halign: 'left'
                    theme_text_color: 'Custom'  
                    text_color: 0, 0, 0, 1
                    bold: True
            MDGridLayout:
                cols: 2
                MDIconButton:
                    icon: 'currency-inr'
                    halign: 'left'
                    size_hint_y: None
                    height: dp(1)
                    bold: True

                MDLabel:
                    id: amount
                    halign: 'left' 
                    theme_text_color: 'Custom'  
                    text_color: 0,0,0,1
                    bold: True
            MDLabel:
                text: ''
                halign: 'left'
                size_hint_y: None
                height: dp(5)
            MDGridLayout:
                cols: 2
                MDLabel:
                    text: 'Borrower Name'
                    halign: 'left' 
                    bold: True

                MDLabel:
                    id: name
                    halign: 'left' 
                    theme_text_color: 'Custom'  
                    text_color: 140/255, 140/255, 140/255, 1   

            MDGridLayout:
                cols: 2
                MDLabel:
                    text: 'Tenure(Months)'
                    halign: 'left'  
                    bold: True

                MDLabel:
                    id: tenure
                    halign: 'left' 
                    theme_text_color: 'Custom'  
                    text_color: 140/255, 140/255, 140/255, 1
            MDGridLayout:
                cols: 2
                MDLabel:
                    text: 'Interest Rate'
                    halign: 'left'
                    theme_text_color: 'Custom'  
                    bold: True

                MDLabel:
                    id: interest
                    halign: 'left'
                    theme_text_color: 'Custom'  
                    text_color: 140/255, 140/255, 140/255, 1
            MDGridLayout:
                cols: 2
                MDLabel:
                    text: "Extension Allowed"
                    halign: 'left' 
                    bold: True
                MDLabel:
                    id: extend_type
                    halign: 'left' 
                    theme_text_color: 'Custom'  
                    text_color: 140/255, 140/255, 140/255, 1
            MDGridLayout:
                cols: 2
                MDLabel:
                    text: "Extension Fee(%)"
                    halign: 'left' 
                    bold: True
                MDLabel:
                    id: ex_fee
                    halign: 'left' 
                    theme_text_color: 'Custom'  
                    text_color: 140/255, 140/255, 140/255, 1
            MDGridLayout:
                cols: 2
                MDLabel:
                    text: "Extension Months"
                    halign: 'left'
                    bold: True

                MDTextField:
                    id: extend_months
                    hint_text: 'Extend Months'
                    multiline: False
                    mode: "rectangle"
                    helper_text_mode: 'on_focus'
                    halign: 'left' 
                    theme_text_color: 'Custom'
                    text_color: 118/255, 134/255, 139/255, 1
                    hint_text_color_normal: 118/255, 134/255, 139/255, 1
                    hint_text_color_focus: 118/255, 134/255, 139/255, 1
                    font_size: "16sp"
                    line_color_focus: 118/255, 134/255, 139/255, 1
                    line_color_normal: 118/255, 134/255, 139/255, 1
                    color_active: 118/255, 134/255, 139/255, 1


            MDLabel:
                text: ''
                halign: 'left'
                size_hint_y: None
                height: dp(25)
        MDLabel:
            text: ''
            halign: 'left'
            size_hint_y: None
            height: dp(25)


        MDBoxLayout:
            orientation: 'horizontal'
            spacing: dp(30)
            padding: dp(30)
            size_hint_y: None
            height: self.minimum_height
            canvas.before:
                Color:
                    rgba: 249/255, 249/255, 247/255, 1 
                RoundedRectangle:
                    pos: self.pos
                    size: self.size
                    radius: [25, 25, 25, 25]   
            MDRaisedButton:
                text: "BACK"
                md_bg_color: 0.043, 0.145, 0.278, 1 
                on_release: root.on_back()
                text_color: 1, 1, 1, 1
                size_hint: 1, None

            MDRaisedButton:
                id: extend_button
                text: "Extension Request"
                md_bg_color: 0.043, 0.145, 0.278, 1 
                on_release: root.on_extension_press()
                size_hint: 1, None

<ExtendRequestScreen1>
    GridLayout:
        cols: 1
        MDTopAppBar:
            title: "View Profile"
            elevation: 3
            left_action_items: [['arrow-left', lambda x: root.on_back_button_press()]]
            md_bg_color: 0.043, 0.145, 0.278, 1 
            title_align: 'left'


        BoxLayout:
            orientation: 'vertical'
            spacing: dp(50)
            padding: dp(30)
            size_hint_y: None
            height: self.minimum_height
            canvas.before:
                Color:
                    rgba: 230/255, 245/255, 255/255, 1 
                RoundedRectangle:
                    pos: self.pos
                    size: self.size
                    radius: [1, 1, 1, 1]
                    source: "background.jpg"

            MDGridLayout:
                cols: 2

                MDLabel:
                    text: 'Loan Amount:'
                    halign: 'left'
                    theme_text_color: 'Custom'  
                    text_color: 0, 0, 0, 1
                    bold: True
            MDGridLayout:
                cols: 2
                MDIconButton:
                    icon: 'currency-inr'
                    halign: 'left'
                    size_hint_y: None
                    height: dp(1)
                    bold: True

                MDLabel:
                    id: amount1
                    halign: 'left' 
                    theme_text_color: 'Custom'  
                    text_color: 0,0,0,1
                    bold: True
            MDLabel:
                text: ''
                halign: 'left'
                size_hint_y: None
                height: dp(5)

            MDGridLayout:
                cols: 2
                MDLabel:
                    text: 'Extension Fee(%)'
                    halign: 'left'
                    theme_text_color: 'Custom'  
                    bold: True

                MDLabel:
                    id: ex_fee
                    halign: 'left'
                    theme_text_color: 'Custom'  
                    text_color: 140/255, 140/255, 140/255, 1
            MDGridLayout:
                cols: 2
                MDLabel:
                    text: "Extension Amount "
                    halign: 'left' 
                    bold: True
                MDLabel:
                    id: extend_amount1
                    halign: 'left' 
                    theme_text_color: 'Custom'  
                    text_color: 140/255, 140/255, 140/255, 1
            MDGridLayout:
                cols: 2
                MDLabel:
                    text: "New EMI "
                    halign: 'left' 
                    bold: True
                MDLabel:
                    id: new_emi
                    halign: 'left' 
                    theme_text_color: 'Custom'  
                    text_color: 140/255, 140/255, 140/255, 1
            MDGridLayout:
                cols: 2
                MDLabel:
                    text: "Final Repayment Amount"
                    halign: 'left'
                    bold: True

                MDLabel:
                    id: repay_amount
                    halign: 'left' 
                    theme_text_color: 'Custom'  
                    text_color: 140/255, 140/255, 140/255, 1

        MDLabel:
            text: ''
            halign: 'left'
            size_hint_y: None
            height: dp(85)

        BoxLayout:
            orientation: 'vertical'
            size_hint_y: None
            height: "75dp"
            spacing:dp(15)
            padding: dp(30)
            pos_hint: {'center_x': 0.5, 'center_y': 0.5}

            MDLabel:
                text: 'Reason for Extending Loan'
                valign: 'top'
                bold: True

            MDTextField:
                id: reason
                hint_text: 'Enter text here'

        BoxLayout:
            orientation: 'horizontal'
            size_hint_y: None
            height: "48dp"
            spacing: dp(15)
            padding: dp(10)
            pos_hint: {'center_x': 0.5, 'center_y': 0.5}
            CheckBox:
                id: check_box
                size_hint: None, None
                size: "30dp", "30dp"
                bold: True
                active: False
                on_active: root.checkbox_callback1(self, self.active)
                color: 0.043, 0.145, 0.278, 1 

            MDLabel:
                text: "I Agree Terms and Conditions"
                multiline: False  
                size: "30dp", "30dp"
                theme_text_color: "Custom"
                text_color: 0, 0, 0, 1
                halign: "left"
                valign: "center" 


        MDBoxLayout:
            orientation: 'horizontal'
            spacing: dp(30)
            padding: dp(30)
            size_hint_y: None
            height: self.minimum_height
            canvas.before:
                Color:
                    rgba: 249/255, 249/255, 247/255, 1 
                RoundedRectangle:
                    pos: self.pos
                    size: self.size
                    radius: [25, 25, 25, 25]   
            MDRaisedButton:
                text: "BACK"
                md_bg_color: 0.043, 0.145, 0.278, 1 
                on_release: root.on_back()
                text_color: 1, 1, 1, 1
                size_hint: 1, None

            MDRaisedButton:
                id: submit_button
                text: "Submit"
                md_bg_color: 0.043, 0.145, 0.278, 1 
                on_release: root.on_extension_press()
                size_hint: 1, None


"""
Builder.load_string(extension_loan_request)
date = datetime.today()
print(date)


class ExtendLoan(Screen):
    def __init__(self, instance=None, **kwargs):
        super().__init__(**kwargs)
        email = self.get_email()
        data = app_tables.fin_user_profile.search(email_user=email)

        if not data:
            print("No data found for email:", email)
            return

        for row in data:
            if row['user_photo']:
                image_data = row['user_photo'].get_bytes()
                if isinstance(image_data, bytes):
                    try:
                        profile_texture_io = BytesIO(image_data)
                        photo_texture = CoreImage(profile_texture_io, ext='png').texture
                    except Exception as e:
                        print(f"Error processing image for email {row['email_user']}: {e}")
                else:
                    try:
                        image_data_binary = base64.b64decode(image_data)
                        profile_texture_io = BytesIO(image_data_binary)
                        photo_texture = CoreImage(profile_texture_io, ext='png').texture
                    except base64.binascii.Error as e:
                        print(f"Base64 decoding error for email {row['email_user']}: {e}")
                    except Exception as e:
                        print(f"Error processing image for email {row['email_user']}: {e}")

        data = app_tables.fin_loan_details.search()
        email = anvil.server.call('another_method')
        profile = app_tables.fin_user_profile.search()
        product = app_tables.fin_product_details.search()
        customer_id = []
        loan_id = []
        loan_amount = []
        borrower_name = []
        loan_status = []
        tenure = []
        product_name = []
        email1 = []
        interest_rate = []
        s = 0
        for i in data:
            s += 1
            customer_id.append(i['borrower_customer_id'])
            loan_id.append(i['loan_id'])
            loan_amount.append(i['loan_amount'])
            borrower_name.append(i['borrower_full_name'])
            loan_status.append(i['loan_updated_status'])
            tenure.append(i['tenure'])
            product_name.append(i['product_name'])
            interest_rate.append(i['interest_rate'])
            email1.append(i['borrower_email_id'])

        extension_allowed = []
        extension_fee = []
        for i in product:
            extension_allowed.append(i['extension_allowed'])
            extension_fee.append(i['extension_fee'])
        profile_customer_id = []
        profile_mobile_number = []
        profile_email_id = []
        ascend_value = []
        for i in profile:
            profile_customer_id.append(i['customer_id'])
            profile_mobile_number.append(i['mobile'])
            profile_email_id.append(i['email_user'])
            ascend_value.append(i['ascend_value'])
        cos_id = None
        index = 0
        if email in profile_email_id:
            index = profile_email_id.index(email)
            cos_id = profile_customer_id[index]
        if cos_id is not None:
            print(cos_id, type(cos_id))
        c = -1
        index_list = []
        print(profile_customer_id[index])
        print(customer_id)
        for i in range(s):
            c += 1
            if loan_status[i] == 'disbursed' and customer_id[i] == cos_id:
                index_list.append(c)
        b = 1
        k = -1
        for i in reversed(index_list):
            b += 1
            k += 1
            number = profile_customer_id.index(customer_id[i])
            card = MDCard(
                orientation='vertical',
                size_hint=(None, None),
                size=("310dp", "200dp"),
                padding="10dp",
                spacing="3dp",
                elevation=3,
            )
            # Horizontal layout to keep the text and image in to the card
            horizontal_layout = BoxLayout(orientation='horizontal')
            if photo_texture:
                image = Image(texture=photo_texture, size_hint_x=None, height="30dp", width="60dp")
                horizontal_layout.add_widget(image)

            # Text Layout to keep the text on card
            horizontal_layout.add_widget(Widget(size_hint_x=None, width='25dp'))
            text_layout = BoxLayout(orientation='vertical')
            text_layout.add_widget(MDLabel(
                text=f" [b]{borrower_name[i]},\n {profile_mobile_number[number]}[/b]",
                theme_text_color='Custom',
                text_color=(0, 0, 0, 1),
                halign='left',
                markup=True,
                font_size='10sp',
                bold=True
            ))
            text_layout.add_widget(MDLabel(
                text=f" [b]Product Name:[/b] {product_name[i]}",
                theme_text_color='Custom',
                text_color=(0, 0, 0, 1),
                halign='left',
                markup=True,
                # font_size='10sp'
            ))
            text_layout.add_widget(MDLabel(
                text=f" [b]Loan Amount:[/b] {loan_amount[i]}",
                theme_text_color='Custom',
                text_color=(0, 0, 0, 1),
                halign='left',
                markup=True,
                # font_size='10sp'
            ))
            text_layout.add_widget(MDLabel(
                text=f" [b]Ascend Score :[/b]{ascend_value[number]}",
                theme_text_color='Custom',
                text_color=(0, 0, 0, 1),
                halign='left',
                markup=True,
                # font_size='10sp'
            ))
            horizontal_layout.add_widget(text_layout)
            card.add_widget(horizontal_layout)

            horizontal_layout1 = BoxLayout(orientation='horizontal', size_hint_y=None, height=dp(45))
            # Button layout to align the Buttons
            button_layout2 = BoxLayout(
                size_hint_y=None,
                height="40dp",
                padding="10dp",
                spacing="30dp"
            )

            # this colors for loan status button colors based on loan status

            status_color = (0.545, 0.765, 0.290, 1)  # default color
            if loan_status[i] == "under process":
                status_color = (253 / 255, 218 / 255, 13 / 255, 1)
            elif loan_status[i] == "disbursed":
                status_color = (0.8588, 0.4392, 0.5765, 1.0)
            elif loan_status[i] == "closed":
                status_color = (0.4235, 0.5569, 0.1373, 1.0)
            elif loan_status[i] == "extension":
                status_color = (1.0, 0.6275, 0.4824, 1.0)
            elif loan_status[i] == "foreclosure":
                status_color = (0.0, 0.749, 1.0, 1.0)
            elif loan_status[i] == "rejected":
                status_color = (0.902, 0.141, 0.141, 1)
            elif loan_status[i] == "approved":
                status_color = (0.2353, 0.7019, 0.4431, 1.0)
            elif loan_status[i] == "lost opportunities":
                status_color = (0.902, 0.141, 0.141, 1)
            button2 = MDFillRoundFlatButton(
                text="  View Details  ",
                # size_hint=(None, None),
                height="40dp",
                width="250dp",
                pos_hint={"center_x": 1},
                md_bg_color=(0.043, 0.145, 0.278, 1),
                on_release=lambda x, loan_id=loan_id[i]: self.icon_button_clicked(instance, loan_id),
                text_color=(1, 1, 1, 1)
            )
            button_layout1 = BoxLayout(
                size_hint_y=None,
                height="40dp",
                padding="10dp",
                spacing=30
            )
            # this status_text for status text to keep button
            status_text = {
                "under process": "  Under Process ",
                "disbursed": "  Disburse Loan ",
                "closed": "    Closed Loan   ",
                "extension": " Extension Loan ",
                "foreclosure": "  Foreclosure  ",
                "accepted": " Accepted Loan ",
                "rejected": "  Rejected Loan ",
                "approved": "  Approved Loan ",
                "lost opportunities": "lost opportunities"
            }
            button1 = MDFillRoundFlatButton(
                text=status_text.get(loan_status[i], loan_status[i]),
                height=dp(40),
                pos_hint={"center_x": 0},
                md_bg_color=status_color,
                text_color=(1, 1, 1, 1),
            )
            button_layout1.add_widget(button1)
            button_layout2.add_widget(button2)

            # Adding the Buttons to the card
            horizontal_layout1.add_widget(button_layout1)
            horizontal_layout1.add_widget(button_layout2)
            card.add_widget(horizontal_layout1)

            self.ids.container.add_widget(card)
            # item = ThreeLineAvatarIconListItem(
            #
            #     IconLeftWidget(
            #         icon="card-account-details-outline"
            #     ),
            #     text=f"Borrower Name : {borrower_name[i]}",
            #     secondary_text=f"Borrower Mobile Number : {profile_mobile_number[number]}",
            #     tertiary_text=f"Product Name : {product_name[i]}",
            #     text_color=(0, 0, 0, 1),  # Black color
            #     theme_text_color='Custom',
            #     secondary_text_color=(0, 0, 0, 1),
            #     secondary_theme_text_color='Custom',
            #     tertiary_text_color=(0, 0, 0, 1),
            #     tertiary_theme_text_color='Custom'
            # )
            # item.bind(on_release=lambda instance, loan_id=loan_id[i]: self.icon_button_clicked(instance, loan_id))
            # self.ids.container1.add_widget(item)

    def get_email(self):
        # Make a call to the Anvil server function
        # Replace 'another_method' with the actual name of your Anvil server function
        return anvil.server.call('another_method')

    def on_back_button_press(self):
        self.manager.current = 'DashboardScreen'

    def refresh(self):
        self.ids.container.clear_widgets()
        self.__init__()

    def icon_button_clicked(self, instance, loan_id1):
        data = app_tables.fin_loan_details.search()

        sm = self.manager
        disbursed = ExtendRequestScreen(name='ExtendRequestScreen')
        sm.add_widget(disbursed)
        sm.current = 'ExtendRequestScreen'
        self.manager.get_screen('ExtendRequestScreen').initialize_with_value(loan_id1, data)

    def on_pre_enter(self):
        # Bind the back button event to the on_back_button method
        Window.bind(on_keyboard=self.on_keyboard)
        Window.bind(on_keyboard=self.on_back_button)

    def on_pre_leave(self):
        # Unbind the back button event when leaving the screen
        Window.bind(on_keyboard=self.on_keyboard)
        Window.bind(on_keyboard=self.on_back_button)

    def on_back_button(self, instance, key, scancode, codepoint, modifier):
        # Handle the back button event
        if key == 27:  # 27 is the keycode for the hardware back button on Android
            self.go_back()
            return True  # Consume the event, preventing further handling
        return False  # Continue handling the event

    def go_back(self):
        # Navigate to the previous screen with a slide transition
        self.manager.transition = SlideTransition(direction='right')
        self.manager.current = 'DashboardScreen'

    def on_keyboard(self, window, key, *args):
        if key == 27:  # Key code for the 'Escape' key
            # Keyboard is closed, move the screen down
            self.screen_manager.y = 0
        return True

    def on_start(self):
        Window.softinput_mode = "below_target"


class ExtendRequestScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.check_box = None

    def initialize_with_value(self, value, data):
        self.loan_id = value
        print(value)
        emi1 = app_tables.fin_emi_table.search()
        pro_details = app_tables.fin_product_details.search()
        data = app_tables.fin_loan_details.search()
        profile = app_tables.fin_user_profile.search()

        customer_id = []
        loan_id = []
        loan_status = []
        borrower_name = []
        tenure = []

        s = 0

        for i in data:
            s += 1
            customer_id.append((i['borrower_customer_id']))
            loan_id.append(i['loan_id'])
            loan_status.append(i['loan_updated_status'])
            borrower_name.append(i['borrower_full_name'])
            tenure.append(i['tenure'])

        emi_loan_id = []
        emi_num = []
        for i in emi1:
            emi_loan_id.append(i['loan_id'])
            emi_num.append(i['emi_number'])
        profile_customer_id = []
        profile_mobile_number = []
        profile_email_id = []

        for i in profile:
            profile_customer_id.append(i['customer_id'])
            profile_mobile_number.append(i['mobile'])
            profile_email_id.append(i['email_user'])

        email = anvil.server.call('another_method')
        index0 = 0
        if email in profile_email_id:
            index0 = profile_email_id.index(email)

        loan_id = []
        loan_amount = []
        email1 = []
        name = []
        tenure = []
        interest = []
        credit = []
        first_payment_date = []

        for i in data:
            loan_id.append(i['loan_id'])
            loan_amount.append(i['loan_amount'])
            email1.append(i['borrower_email_id'])
            name.append(i['borrower_full_name'])
            tenure.append(i['tenure'])
            interest.append(i['interest_rate'])
            credit.append(i['credit_limit'])
            first_payment_date.append(i['first_emi_payment_due_date'])

        product_id1 = []
        for product in data:
            product_id1.append(product['product_id'])
            print(product_id1)
        product_id2 = []
        extend_fee = []
        for product in pro_details:
            product_id2.append(product['product_id'])
            extend_fee.append(product['extension_fee'])

        if value in loan_id:
            index10 = loan_id.index(value)
            print(product_id1[index10])
        index10 = 0
        if product_id1[index10] in product_id2:
            index11 = product_id1.index(product_id1[index10])
            self.ids.ex_fee.text = str(extend_fee[index11])
            ex_fee = self.ids.ex_fee

        if value in loan_id:
            index = loan_id.index(value)
            self.ids.amount.text = str(loan_amount[index])
            self.ids.name.text = str(name[index])
            self.ids.tenure.text = str(tenure[index])
            self.ids.interest.text = str(interest[index])

            emi_loan = [i['emi_number'] for i in emi1 if i['loan_id'] == value]

            if emi_loan:
                highest_number = max(emi_loan)
                total_payment = highest_number
            else:
                total_payment = 0

            minimum_months = [i['min_extension_months'] for i in pro_details if
                              i['product_id'] == data[index]['product_id']]

            if total_payment >= minimum_months[0]:
                self.ids.extend_button.disabled = False
                self.ids.extend_button.opacity = 1
            else:
                self.ids.extend_button.disabled = True
                self.ids.extend_button.opacity = 0
                self.show_success_dialog1(f"Minimum three months of EMI need to paid")

            print(total_payment)
            print(minimum_months[0])

            extension_type = [i['extension_allowed'] for i in pro_details if
                              i['product_id'] == data[index]['product_id']]
            if extension_type:
                extend_value = extension_type[0]
                self.ids.extend_type.text = str(extend_value)

                if extend_value.strip() == 'Yes':
                    self.ids.extend_button.disabled = False
                else:
                    self.ids.extend_button.disabled = True
                    self.show_success_dialog(f"You are not eligible for extension")

    def on_extension_press(self):
        extend_table = app_tables.fin_extends_loan.search()
        data = app_tables.fin_loan_details.search()
        emi1 = app_tables.fin_emi_table.search()
        loan_id2 = self.loan_id
        ex_fee = self.ids.ex_fee

        emi_loan_id = []
        remaining_tenure = []
        for i in emi1:
            emi_loan_id.append(i['loan_id'])
            remaining_tenure.append(i['remaining_tenure'])

        last_index = 0
        if value not in emi_loan_id:
            emi_number = 1
        else:
            last_index = len(emi_loan_id) - 1 - emi_loan_id[::-1].index(value)

        loan_id = []
        tenure = []
        monthly_emi = []

        s = 0
        for i in data:
            s += 1
            loan_id.append(i['loan_id'])
            tenure.append(i['tenure'])
            monthly_emi.append(i['monthly_emi'])
            print(tenure)

        loan_index = 0
        if self.loan_id in loan_id:
            loan_index = loan_id.index(self.loan_id)

        ex_month = int(self.ids.extend_months.text)
        print(ex_month)
        extend_mon = remaining_tenure[last_index] + ex_month

        if ex_month > 1 and ex_month <= 6:
            sm = self.manager

            # Create a new instance of the LoginScreen
            extend = ExtendRequestScreen1(name='ExtendRequestScreen1')

            # Add the LoginScreen to the existing ScreenManager
            sm.add_widget(extend)

            # Switch to the LoginScreen
            sm.current = 'ExtendRequestScreen1'
            self.manager.get_screen('ExtendRequestScreen1').initialize_with_value(self.loan_id, data, ex_month)

        else:
            self.show_validation_errors('Extension number should be between 1 to 6')

    def on_back_button_press(self):
        self.manager.current = 'ExtendLoan'

    def on_back(self):
        self.manager.current = 'ExtendLoan'

    def show_success_dialog(self, text):
        dialog = MDDialog(
            text=text,
            size_hint=(0.8, 0.3),
            buttons=[
                MDRaisedButton(
                    text="OK",
                    on_release=lambda *args: self.open_dashboard_screen(dialog),
                    theme_text_color="Custom",
                    text_color=(0.043, 0.145, 0.278, 1),
                )
            ],
            # Setting the background color to white or any preferred color
            md_bg_color=get_color_from_hex("#FFFFFF")
        )
        dialog.open()

    def show_validation_errors(self, error_message):
        dialog = MDDialog(
            title="Validation Error",
            text=error_message,
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

    def open_dashboard_screen(self, dialog):

        dialog.dismiss()
        self.manager.current = 'DashboardScreen'

    def show_success_dialog1(self, text):
        dialog = MDDialog(
            text=text,
            size_hint=(0.8, 0.3),
            buttons=[
                MDRaisedButton(
                    text="OK",
                    on_release=lambda *args: self.open_dashboard_screen(dialog),
                    theme_text_color="Custom",
                    text_color=(0.043, 0.145, 0.278, 1),
                )
            ],
            # Setting the background color to white or any preferred color
            md_bg_color=get_color_from_hex("#FFFFFF")
        )
        dialog.open()

    def open_dashboard_screen(self, dialog):

        dialog.dismiss()
        self.manager.current = 'DashboardScreen'


class ExtendRequestScreen1(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.check_box = None

    def checkbox_callback1(self, checkbox, value):
        if value:
            self.check_box = True
        else:
            self.check_box = False

    def initialize_with_value(self, value, data, ex_m):
        print(value)
        self.loan_id = value
        self.ex_months = ex_m
        data = app_tables.fin_loan_details.search()
        pro_details = app_tables.fin_product_details.search()
        profile = app_tables.fin_user_profile.search()
        emi1 = app_tables.fin_emi_table.search()

        emi_loan_id = []
        emi_num = []
        remaining_tenure = []
        remain_amount = []

        for i in emi1:
            emi_loan_id.append(i['loan_id'])
            emi_num.append(i['emi_number'])
            remaining_tenure.append(i['remaining_tenure'])
            remain_amount.append(i['total_remaining_amount'])

        last_index = 0
        if value not in emi_loan_id:
            emi_number = 1
        else:
            last_index = len(emi_loan_id) - 1 - emi_loan_id[::-1].index(value)

        loan_id = []
        loan_amount = []
        monthly_emi = []
        tenure = []

        s = 0

        for i in data:
            s += 1
            loan_id.append(i['loan_id'])
            loan_amount.append(i['loan_amount'])
            monthly_emi.append(i['monthly_emi'])
            tenure.append(i['tenure'])

        loan_in1 = 0

        if value in loan_id:
            loan_in1 = loan_id.index(value)
            self.ids.amount1.text = str(loan_amount[loan_in1])

        profile_customer_id = []
        profile_mobile_number = []
        profile_email_id = []

        for i in profile:
            profile_customer_id.append(i['customer_id'])
            profile_mobile_number.append(i['mobile'])
            profile_email_id.append(i['email_user'])

        email = anvil.server.call('another_method')
        index0 = 0
        if email in profile_email_id:
            index0 = profile_email_id.index(email)

        product_id1 = []
        for product in data:
            product_id1.append(product['product_id'])
            print(product_id1)
        product_id2 = []
        extend_fee = []
        for product in pro_details:
            product_id2.append(product['product_id'])
            extend_fee.append(product['extension_fee'])

        if value in loan_id:
            index10 = loan_id.index(value)
            print(product_id1[index10])
        index10 = 0
        index11 = 0
        if product_id1[index10] in product_id2:
            index11 = product_id1.index(product_id1[index10])
            self.ids.ex_fee.text = str(extend_fee[index11])

        emi_loan = [i['emi_number'] for i in emi1 if i['loan_id'] == value]

        if emi_loan:
            highest_number = max(emi_loan)
            total_payments = highest_number
        else:
            total_payments = 0
        extend_mon = remaining_tenure[last_index] + ex_m
        print(remaining_tenure[last_index], ex_m)
        print(ex_m)
        print(remaining_tenure[last_index])
        outstanding_amount = extend_mon
        emi_paid = monthly_emi[loan_in1] * total_payments
        extension_amount = (loan_amount[loan_in1] * extend_fee[index11]) / 100
        self.ids.extend_amount1.text = str(extension_amount)
        final_repay_amount = (loan_amount[loan_in1] - emi_paid) + extension_amount
        self.ids.repay_amount.text = str(final_repay_amount)
        new_emi = remain_amount[last_index] / outstanding_amount
        self.ids.new_emi.text = str(round(new_emi, 2))
        print(outstanding_amount)
        print(tenure[loan_in1])
        print(total_payments)
        print(emi_paid)
        print(monthly_emi[loan_in1])
        print(total_payments)
        print(extension_amount)
        print(loan_amount[loan_in1])
        print(extend_fee[index11])
        print(final_repay_amount)
        print(new_emi)

    def on_extension_press(self):
        loan_id = self.loan_id
        print(loan_id)
        e_m = self.ex_months
        final_repay_amount = self.ids.repay_amount.text
        reason = self.ids.reason.text
        emi = self.ids.new_emi.text
        extend = self.ids.extend_amount1.text
        e_fee = self.ids.ex_fee.text

        if len(self.ids.reason.text) < 3:
            self.show_validation_error('You Must need to enter a reason for extension')
            return
        if self.check_box != True:
            self.show_validation_error2('You need to select Terms and Conditions')
            return
        data = app_tables.fin_loan_details.search()
        data1 = app_tables.fin_emi_table.search()

        loan_id3 = []
        borrower_name1 = []
        loan_amount = []
        lender_name = []
        lender_cos = []
        borrow_cos = []
        borrow_email = []
        lender_email = []
        product_name = []

        for i in data:
            loan_id3.append(i['loan_id'])
            borrower_name1.append(i['borrower_full_name'])
            lender_name.append(i['lender_full_name'])
            loan_amount.append(i['loan_amount'])
            lender_cos.append(i['lender_customer_id'])
            borrow_cos.append(i['borrower_customer_id'])
            borrow_email.append(i['borrower_email_id'])
            lender_email.append(i['lender_email_id'])
            product_name.append(i['product_name'])
        index = 0
        if loan_id in loan_id3:
            index = loan_id3.index(loan_id)
        emi_number = []
        loan_id4 = []
        total_payment = 0
        for i in data1:
            emi_number.append(i['emi_number'])
            loan_id4.append(i['loan_id'])
        if loan_id in loan_id4:
            index3 = loan_id4.index(loan_id)
            highest_number = max(emi_number) if emi_number else 0
            total_payment = highest_number
        app_tables.fin_extends_loan.add_row(loan_id=loan_id,
                                            borrower_full_name=borrower_name1[index],
                                            borrower_email_id=borrow_email[index],
                                            lender_email_id=lender_email[index],
                                            loan_amount=loan_amount[index],
                                            borrower_customer_id=borrow_cos[index],
                                            extension_request_date=datetime.today(),
                                            emi_number=total_payment,
                                            final_repayment_amount=float(final_repay_amount),
                                            extension_amount=float(extend),
                                            status='under process',
                                            total_extension_months=e_m,
                                            extend_fee=float(e_fee),
                                            new_emi=float(emi),
                                            reason=reason
                                            )
        data[index]['loan_updated_status'] = 'extension'
        self.show_success_dialog(
            f"Your extension request has been successfully submitted. You will receive a notification once it is approved.")

    def show_validation_error(self, error_message):
        dialog = MDDialog(
            title="Validation Error",
            text=error_message,
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

    def show_success_dialog(self, text):
        dialog = MDDialog(
            text=text,
            size_hint=(0.8, 0.3),
            buttons=[
                MDRaisedButton(
                    text="OK",
                    on_release=lambda *args: self.open_dashboard_screen(dialog),
                    theme_text_color="Custom",
                    text_color=(0.043, 0.145, 0.278, 1),
                )
            ]
        )
        dialog.open()

    def open_dashboard_screen(self, dialog):
        dialog.dismiss()
        self.manager.current = 'DashboardScreen'

    def show_validation_error2(self, error_message):
        dialog = MDDialog(
            title="Validation Error",
            text=error_message,
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

    def on_back_button_press(self):
        self.manager.current = 'ExtendRequestScreen'

    def on_back(self):
        self.manager.current = 'ExtendRequestScreen'


class MyScreenManager(ScreenManager):
    pass

