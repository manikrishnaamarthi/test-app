import anvil
from io import BytesIO
from kivy.core.image import Image as CoreImage
from kivy.graphics import Color,Ellipse
import base64
from kivy.uix.screenmanager import ScreenManager

from anvil import Label
from anvil.tables import app_tables
from kivy.metrics import dp
from kivy.uix.image import Image
from kivymd.uix.card import MDCard
from kivymd.uix.label import MDLabel
from kivy.properties import ObjectProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.popup import Popup
from kivymd.app import MDApp
from kivy.graphics import Color, Rectangle
from kivy.uix.screenmanager import Screen
from kivy.lang import Builder
from kivymd.uix.progressbar import MDProgressBar
import os
from kivy.utils import platform
from fpdf import FPDF
from datetime import datetime
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDRectangleFlatButton
from kivy.metrics import dp
from kivymd.uix.button import MDRaisedButton, MDRectangleFlatButton, MDFillRoundFlatButton
from kivymd.uix.dialog import MDDialog
from kivymd.uix.list import *
from kivy.metrics import dp
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.uix.screenmanager import Screen, SlideTransition, ScreenManager
from kivy.utils import platform
from kivy.clock import mainthread
from kivymd.uix.filemanager import MDFileManager
from kivy.uix.widget import Widget
from kivy.graphics.texture import Texture
from kivy.graphics import Rectangle
import matplotlib.pyplot as plt
from kivy.graphics import Color, Rectangle, Line
from kivy.core.text import Label as CoreLabel
import numpy as np
from matplot_figure import MatplotFigure
from kivy.metrics import dp
from kivy.uix.scrollview import ScrollView
from kivymd.uix.gridlayout import MDGridLayout
from kivymd.uix.progressbar import MDProgressBar
from datetime import datetime
from kivy.clock import Clock  # Import Clock from Kivy

borrower_portfolio = '''
<WindowManager>:
    LenderDetails:
    ViewPortfolio:

<LenderDetails>:
    BoxLayout:
        orientation: 'vertical'
        MDTopAppBar:
            title: "Lender Details"
            elevation: 3
            left_action_items: [['arrow-left', lambda x: root.go_back()]]
            right_action_items: [['refresh', lambda x: root.refresh()]]
            title_align: 'left'
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

<ViewPortfolio>:
    BoxLayout:
        orientation: 'vertical'
        MDTopAppBar:
            title: "Lender Portfolio"
            elevation: 3
            left_action_items: [['arrow-left', lambda x: root.go_back()]]
            right_action_items: [["download", lambda x: root.download_portfolio_as_pdf()]]  # Add download icon

            title_align: 'left'
            md_bg_color: 0.043, 0.145, 0.278, 1

        ScrollView:  # Add ScrollView here
            id: scroll_view
            do_scroll_x: False
            BoxLayout:
                orientation: "vertical"
                padding:dp(10)
                spacing:dp(25)
                size_hint_y: None
                height: self.minimum_height
                MDBoxLayout:
                    orientation: 'vertical'
                    size_hint_y: None
                    height: self.minimum_height
                    padding: dp(20)

                    BoxLayout:
                        id: box1
                        orientation: 'vertical'
                        size_hint_y: None
                        height: dp(800)
                        padding: [10, 0,0,0]
                        canvas.before:
                            Color:
                                rgba: 0, 0, 0, 1
                            Line:
                                width: 0.25
                                rounded_rectangle: (self.x, self.y, self.width, self.height, 15)
                        Image:
                            id: selected_image1
                            size_hint: None, None
                            size: dp(70), dp(70)  # Make sure the size is a perfect square for a circular shape
                            source: ""  # Set the path to your image source if needed
                            pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                            allow_stretch: True
                            keep_ratio: True
                            canvas.before:
                                StencilPush
                                Ellipse:
                                    size: self.width - dp(10), self.height - dp(10)
                                    pos: self.x + dp(5), self.y + dp(5)
                                StencilUse
                            canvas:
                                Rectangle:
                                    texture: self.texture
                                    size: self.width - dp(10), self.height - dp(10)
                                    pos: self.x + dp(5), self.y + dp(5)
                            canvas.after:
                                StencilUnUse
                                Ellipse:
                                    size: self.width - dp(10), self.height - dp(10)
                                    pos: self.x + dp(5), self.y + dp(5)
                                StencilPop

                        MDGridLayout:
                            cols: 2
                            spacing: dp(10)
                            padding: dp(10)
                            MDLabel:
                                text: "Full Name" 
                                size_hint_y:None
                                height:dp(50)
                                bold: True
                                halign: "left"
                            MDLabel:
                                id: full_name      
                                text: "" 
                                size_hint_y:None
                                height:dp(50)
                                halign: "left"                    
                        MDGridLayout:
                            cols: 2
                            spacing: dp(10)
                            padding: dp(10)
                            MDLabel:
                                text: "Mobile Number" 
                                size_hint_y:None
                                height:dp(50)
                                bold: True
                                halign: "left"
                            MDLabel:
                                id: mobile_number      
                                text: "" 
                                size_hint_y:None
                                height:dp(50)
                                halign: "left"
                        MDGridLayout:
                            cols: 2
                            spacing: dp(10)
                            padding: dp(10)
                            MDLabel:
                                text: "Date of Birth" 
                                size_hint_y:None
                                height:dp(50)
                                bold: True
                                halign: "left"
                            MDLabel:
                                id: date_of_birth      
                                text: "" 
                                size_hint_y:None
                                height:dp(50)
                                halign: "left"
                        MDGridLayout:
                            cols: 2
                            spacing: dp(10)
                            padding: dp(10)
                            MDLabel:
                                text: "Gender" 
                                size_hint_y:None
                                height:dp(50)
                                bold: True
                                halign: "left"
                            MDLabel:
                                id: gender      
                                text: "" 
                                size_hint_y:None
                                height:dp(50)
                                halign: "left"
                        MDGridLayout:
                            cols: 2
                            spacing: dp(10)
                            padding: dp(10)
                            MDLabel:
                                text: "Marital Status" 
                                size_hint_y:None
                                height:dp(50)
                                bold: True
                                halign: "left"
                            MDLabel:
                                id: marital_status      
                                text: "" 
                                size_hint_y:None
                                height:dp(50)
                                halign: "left"
                        MDGridLayout:
                            cols: 2
                            spacing: dp(10)
                            padding: dp(10)
                            MDLabel:
                                text: "Type of Address" 
                                size_hint_y:None
                                height:dp(50)
                                bold: True
                                halign: "left"
                            MDLabel:
                                id: type_of_address      
                                text: "" 
                                size_hint_y:None
                                height:dp(50)
                                halign: "left"

                        MDGridLayout:
                            cols: 2
                            spacing: dp(10)
                            padding: dp(10)
                            MDLabel:
                                text: "Qualification" 
                                size_hint_y:None
                                height:dp(50)
                                bold: True
                                halign: "left"
                            MDLabel:
                                id: qualification      
                                text: "" 
                                size_hint_y:None
                                height:dp(50)
                                halign: "left"
                        MDGridLayout:
                            cols: 2
                            spacing: dp(10)
                            padding: dp(10)
                            MDLabel:
                                text: "Profession" 
                                size_hint_y:None
                                height:dp(50)
                                bold: True
                                halign: "left"
                            MDLabel:
                                id: profession      
                                text: "" 
                                size_hint_y:None
                                height:dp(50)
                                halign: "left"

                        MDGridLayout:
                            cols: 2
                            spacing: dp(10)
                            padding: dp(10)
                            MDLabel:
                                text: "Annual Salary" 
                                size_hint_y:None
                                height:dp(50)
                                bold: True
                                halign: "left"
                            MDLabel:
                                id: annual_salary      
                                text: "" 
                                size_hint_y:None
                                height:dp(50)
                                halign: "left"  

                        MDGridLayout:
                            cols: 2
                            spacing: dp(10)
                            padding: dp(10)
                            MDLabel:
                                text: "Membership Type" 
                                size_hint_y:None
                                height:dp(50)
                                bold: True
                                halign: "left"
                            MDLabel:
                                id: membership      
                                text: "" 
                                size_hint_y:None
                                height:dp(50)
                                halign: "left"         
                                color: (0, 0, 0, 1)
                                font_size: dp(19)
                                bold: True

                    # Heading for Chart
                    MDLabel:
                        text: "Financial Status Overview"
                        size_hint_y: None
                        height: dp(60)  # Increased height to add space
                        bold: True
                        font_style: "H6"
                        halign: "center"
                        valign: "middle"
                        padding_y: dp(10)



                    AnchorLayout:
                        size_hint_y: None
                        height: dp(380)  # Decreased height to reduce space
                        padding: dp(10)
                        anchor_x: 'center'
                        anchor_y: 'center'
                        BoxLayout:
                            id: chart_container
                            orientation: "horizontal"
                            padding: dp(10)
                            spacing: dp(40)

                    BoxLayout:
                        orientation: 'horizontal'
                        spacing: dp(20)  # Spacing between the two columns
                        size_hint_y: None
                        height: dp(40)
                        padding: dp(10)

                        # Column 1: Investment
                        BoxLayout:
                            orientation: 'horizontal'
                            spacing: dp(5)  # Space between the widget and label
                            size_hint_y: None
                            height: dp(40)
                            Widget:
                                size_hint_x: None
                                width: dp(13)
                                size_hint_y: None
                                height: dp(13)
                                canvas:
                                    Color:
                                        rgba: 0, 1, 0, 1  # Green color
                                    Rectangle:
                                        pos: self.pos
                                        size: self.size
                            MDLabel:
                                text: "Investment"
                                halign: 'left'
                                valign: 'middle'
                                size_hint_y: None
                                height: dp(13)

                        # Column 2: Returns
                        BoxLayout:
                            orientation: 'horizontal'
                            spacing: dp(5)  # Space between the widget and label
                            size_hint_y: None
                            height: dp(40)
                            Widget:
                                size_hint_x: None
                                width: dp(13)
                                size_hint_y: None
                                height: dp(13)
                                canvas:
                                    Color:
                                        rgba: 1, 0, 0, 1  # Red color
                                    Rectangle:
                                        pos: self.pos
                                        size: self.size
                            MDLabel:
                                text: "Returns"
                                halign: 'left'
                                valign: 'middle'
                                size_hint_y: None
                                height: dp(13)


'''
Builder.load_string(borrower_portfolio)
date = datetime.today()
print(date)


class WindowManager(ScreenManager):
    pass


class LenderDetails(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.lender_details = {}  # Ensure lender_details is initialized
        self.populate_lender_list()

    def populate_lender_list(self, instance=None):
        data = app_tables.fin_loan_details.search()
        profile = app_tables.fin_user_profile.search()

        self.lender_details = {}  # Ensure lender_details is cleared and re-populated

        for loan in data:
            if loan['loan_updated_status'] in ['disbursed', 'foreclosure', 'extension']:
                lender_id = loan['lender_customer_id']
                if lender_id not in self.lender_details:
                    self.lender_details[lender_id] = {
                        'full_name': loan['lender_full_name'],
                        'mobile_number': '',
                        'product_name': loan['product_name'],
                        'loan_amount': loan['loan_amount'],
                        'interest_rate': loan['interest_rate'],
                        'loan_status': loan['loan_updated_status'],
                        'membership_type': loan['membership_type'],
                        'lending_type': '',
                        'photo_texture': None  # Placeholder for the photo texture
                    }

        for prof in profile:
            if prof['customer_id'] in self.lender_details:
                self.lender_details[prof['customer_id']]['mobile_number'] = prof['mobile']
                self.lender_details[prof['customer_id']]['lending_type'] = prof['lending_type']

                # Load profile photo if available
                if prof['user_photo']:
                    image_data = prof['user_photo'].get_bytes()
                    if isinstance(image_data, bytes):
                        try:
                            profile_texture_io = BytesIO(image_data)
                            photo_texture = CoreImage(profile_texture_io, ext='png').texture
                            self.lender_details[prof['customer_id']]['photo_texture'] = photo_texture
                        except Exception as e:
                            print(f"Error processing image for lender {prof['customer_id']}: {e}")
                    else:
                        try:
                            image_data_binary = base64.b64decode(image_data)
                            profile_texture_io = BytesIO(image_data_binary)
                            photo_texture = CoreImage(profile_texture_io, ext='png').texture
                            self.lender_details[prof['customer_id']]['photo_texture'] = photo_texture
                        except base64.binascii.Error as e:
                            print(f"Base64 decoding error for lender {prof['customer_id']}: {e}")
                        except Exception as e:
                            print(f"Error processing image for lender {prof['customer_id']}: {e}")

        for lender_id, details in self.lender_details.items():
            card = MDCard(
                orientation='vertical',
                size_hint=(None, None),
                size=("320dp", "220dp"),
                padding="8dp",
                spacing="5dp",
                elevation=3
            )
            horizontal_layout = BoxLayout(orientation='horizontal')
            photo_texture = details.get('photo_texture')  # Get the photo texture for the current lender
            if photo_texture:
                image = Image(texture=photo_texture, size_hint_x=None, height="30dp", width="60dp")
                horizontal_layout.add_widget(image)
            horizontal_layout.add_widget(Widget(size_hint_x=None, width='10dp'))
            text_layout = BoxLayout(orientation='vertical')
            text_layout.add_widget(MDLabel(
                text=f"[b]Lender Name:[/b] {details['full_name']}",
                theme_text_color='Custom',
                text_color=(0, 0, 0, 1),
                halign='left',
                markup=True,
            ))
            text_layout.add_widget(MDLabel(
                text=f"[b]Mobile No:[/b] {details['mobile_number']}[/b]",
                theme_text_color='Custom',
                text_color=(0, 0, 0, 1),
                halign='left',
                markup=True,
            ))
            text_layout.add_widget(MDLabel(
                text=f"[b]Lending Type:[/b] {details.get('lending_type')}",
                theme_text_color='Custom',
                text_color=(0, 0, 0, 1),
                halign='left',
                markup=True,
            ))
            text_layout.add_widget(MDLabel(
                text=f"[b]Membership Type:[/b] {details['membership_type']}",
                theme_text_color='Custom',
                text_color=(0, 0, 0, 1),
                halign='left',
                markup=True,
            ))
            text_layout.add_widget(MDLabel(
                text=f"[b]Product Name:[/b] {details['product_name']}",
                theme_text_color='Custom',
                text_color=(0, 0, 0, 1),
                halign='left',
                markup=True,
            ))

            horizontal_layout.add_widget(text_layout)
            card.add_widget(horizontal_layout)

            card.add_widget(Widget(size_hint_y=None, height='10dp'))
            button1 = MDFillRoundFlatButton(
                text="            View Details             ",
                height="40dp",
                width="250dp",
                pos_hint={"center_x": 0.5, "center_y": 0.5},
                md_bg_color=(0.043, 0.145, 0.278, 1),
                on_release=lambda x, lender_id=lender_id: self.icon_button_clicked(instance, lender_id)
            )
            card.add_widget(button1)
            self.ids.container2.add_widget(card)
            # item = ThreeLineAvatarIconListItem(
            #     IconLeftWidget(icon="account"),
            #     text=f"Lender Name: {details['full_name']}",
            #     secondary_text=f"Lender Mobile Number: {details['mobile_number']}",
            #     tertiary_text=f"Product Name: {details['product_name']}",
            #     text_color=(0, 0, 0, 1),
            #     theme_text_color='Custom',
            #     secondary_text_color=(0, 0, 0, 1),
            #     secondary_theme_text_color='Custom',
            #     tertiary_text_color=(0, 0, 0, 1),
            #     tertiary_theme_text_color='Custom'
            # )
            # item.bind(on_release=lambda instance, lender_id=lender_id: self.icon_button_clicked(instance, lender_id))
            # self.ids.container.add_widget(item)

    def icon_button_clicked(self, instance, lender_id):
        print(f"icon_button_clicked called with lender_id: {lender_id}")
        print(f"Current lender_details: {self.lender_details}")
        sm = self.manager
        approved = ViewPortfolio(name='ViewPortfolio')
        sm.add_widget(approved)
        sm.current = 'ViewPortfolio'
        details = self.lender_details[lender_id]
        self.manager.get_screen('ViewPortfolio').initialize_with_value(lender_id, details.get('photo_texture'))

    def go_back(self):
        self.manager.current = 'DashboardScreen'

    def on_pre_enter(self):
        Window.bind(on_keyboard=self.on_back_button)

    def on_pre_leave(self):
        Window.unbind(on_keyboard=self.on_back_button)

    def on_back_button(self, instance, key, scancode, codepoint, modifier):
        if key == 27:
            self.go_back()
            return True
        return False

    def refresh(self):
        self.ids.container2.clear_widgets()
        self.__init__()


class HorizontalLinesAndBarsWidget(Widget):
    def __init__(self, investment_percentage, return_percentage, investment_amount, return_amount, bar_width=dp(50),
                 bar_spacing=dp(10), **kwargs):
        super().__init__(**kwargs)
        self.investment_percentage = investment_percentage
        self.return_percentage = return_percentage
        self.investment_amount = investment_amount
        self.return_amount = return_amount
        self.bar_width = bar_width
        self.bar_spacing = bar_spacing
        self.bind(pos=self.update_canvas, size=self.update_canvas)

    def update_canvas(self, *args):
        self.canvas.clear()
        step = 20  # Draw lines every 20%
        margin = dp(10)
        bar_total_width = self.bar_width * 2 + self.bar_spacing  # Total width for two bars and spacing
        bar_start_x = self.center_x - bar_total_width / 2
        with self.canvas:
            Color(0.8, 0.8, 0.8, 1)  # Cement color for lines
            for i in range(0, 101, step):
                line_y = self.y + (i / 100) * self.height
                Line(points=[self.x, line_y, self.right, line_y], width=1)

                # Label for percentage
                line_percentage_text = f"{i}%"
                line_label = CoreLabel(text=line_percentage_text, font_size=dp(12),
                                       color=(0, 0, 0, 1))  # Black color for text
                line_label.refresh()
                line_text_width, line_text_height = line_label.texture.size
                line_text_x = self.x - line_text_width - dp(5)  # Position to the left of the widget
                line_text_y = line_y - line_text_height / 2
                Rectangle(texture=line_label.texture, pos=(line_text_x, line_text_y), size=line_label.texture.size)

            # Draw investment bar
            investment_bar_height = self.height * self.investment_percentage / 100
            Color(0, 1, 0, 1)  # Green color for investment bar
            Rectangle(pos=(bar_start_x, self.y), size=(self.bar_width, investment_bar_height))

            # Draw return bar
            return_bar_height = self.height * self.return_percentage / 100
            Color(1, 0, 0, 1)  # Red color for return bar
            Rectangle(pos=(bar_start_x + self.bar_width + self.bar_spacing, self.y),
                      size=(self.bar_width, return_bar_height))

            # Label for investment amount
            investment_amount_text = f"₹{self.investment_amount}"  # Add label prefix
            investment_label = CoreLabel(text=investment_amount_text, font_size=dp(12),
                                         color=(0, 0, 0, 1))  # Black color for text
            investment_label.refresh()
            investment_text_width, investment_text_height = investment_label.texture.size
            investment_text_x = bar_start_x + (self.bar_width - investment_text_width) / 2
            investment_text_y = self.y + investment_bar_height + dp(5)
            Rectangle(texture=investment_label.texture, pos=(investment_text_x, investment_text_y),
                      size=investment_label.texture.size)

            # Label for return amount
            return_amount_text = f"₹{self.return_amount}"  # Add label prefix
            return_label = CoreLabel(text=return_amount_text, font_size=dp(12),
                                     color=(0, 0, 0, 1))  # Black color for text
            return_label.refresh()
            return_text_width, return_text_height = return_label.texture.size
            return_text_x = bar_start_x + self.bar_width + self.bar_spacing + (self.bar_width - return_text_width) / 2
            return_text_y = self.y + return_bar_height + dp(5)
            Rectangle(texture=return_label.texture, pos=(return_text_x, return_text_y), size=return_label.texture.size)


class ViewPortfolio(Screen):
    def go_back(self):
        self.manager.current = 'LenderDetails'
    def get_email(self):
        # Make a call to the Anvil server function
        # Replace 'YourAnvilFunction' with the actual name of your Anvil server function
        return anvil.server.call('another_method')
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        email = self.get_email()
        data = app_tables.fin_user_profile.search(email_user=email)

        if not data:
            print("No data found for email:", email)
            return
        photo = []
        email1 = []
        for row in data:
            if row['user_photo']:
                image_data = row['user_photo'].get_bytes()
                if isinstance(image_data, bytes):
                    print(f"Image data type: {type(image_data)}, length: {len(image_data)}")
                    # Assuming image_data is already a binary image file
                    try:
                        profile_texture_io = BytesIO(image_data)
                        profile_texture_obj = CoreImage(profile_texture_io, ext='png').texture
                        photo.append(profile_texture_obj)
                    except Exception as e:
                        print(f"Error processing image for email {row['email_user']}: {e}")
                        photo.append(None)
                else:
                    # If image_data is not bytes, assume it's base64 encoded and decode it
                    try:
                        image_data_binary = base64.b64decode(image_data)
                        print(f"Decoded image data length: {len(image_data_binary)}")
                        profile_texture_io = BytesIO(image_data_binary)
                        profile_texture_obj = CoreImage(profile_texture_io, ext='png').texture
                        photo.append(profile_texture_obj)
                    except base64.binascii.Error as e:
                        print(f"Base64 decoding error for email {row['email_user']}: {e}")
                        photo.append(None)
                    except Exception as e:
                        print(f"Error processing image for email {row['email_user']}: {e}")
                        photo.append(None)
            else:
                photo.append(None)
            email1.append(row['email_user'])
            if email in email1:
                index = email1.index(email)

                if photo[index]:
                    self.ids.selected_image1.texture = photo[index]
                else:
                    print("No profile photo found for email:", email)
            else:
                print(f"Email {email} not found in data.")

    def initialize_with_value(self, lender_id, photo_texture=None):
        profile = app_tables.fin_user_profile.get(customer_id=lender_id)

        if profile:
            self.ids.full_name.text = f"{profile['full_name']}"
            self.ids.mobile_number.text = f"{profile['mobile']}"
            self.ids.date_of_birth.text = f"{profile['date_of_birth']}"
            self.ids.gender.text = f"{profile['gender']}"
            self.ids.marital_status.text = f"{profile['marital_status']}"
            self.ids.type_of_address.text = f"{profile['present_address']}"
            self.ids.qualification.text = f"{profile['qualification']}"
            self.ids.profession.text = f"{profile['profession']}"
            self.ids.annual_salary.text = f"{profile['annual_salary']}"

            lender_data = app_tables.fin_lender.get(customer_id=lender_id)
            if lender_data:
                membership = lender_data['membership']
                membership_color = {
                    'silver': (255 / 255, 255 / 255, 0 / 255, 1),   # Yellow
                    'gold': (255 / 255, 165 / 255, 0 / 255, 1),     # Orange
                    'platinum': (0 / 255, 128 / 255, 0 / 255, 1)    # Green
                }.get(membership.lower(), (0, 0, 0, 1))  # Default to black if no match

                self.ids.membership.text = membership.capitalize()
                self.ids.membership.theme_text_color = 'Custom'
                self.ids.membership.text_color = membership_color

                all_lenders = app_tables.fin_lender.search()
                if all_lenders:
                    max_commitments = max(lender['lender_total_commitments'] for lender in all_lenders)

                    total_commitments = lender_data['lender_total_commitments']
                    return_on_investment = lender_data['return_on_investment']

                    if max_commitments > 0:
                        investment_percentage = (total_commitments / max_commitments) * 100
                    else:
                        investment_percentage = 0

                    if total_commitments > 0:
                        return_percentage = (return_on_investment / total_commitments) * 100
                    else:
                        return_percentage = 0

                    investment_amount = lender_data['lender_total_commitments']  # Assuming this is the column name
                    return_amount = lender_data['return_on_investment']  # Assuming this is the column name

                    chart_widget = HorizontalLinesAndBarsWidget(investment_percentage, return_percentage,
                                                                investment_amount, return_amount,
                                                                bar_width=dp(90), bar_spacing=dp(20))

                    self.ids.chart_container.clear_widgets()
                    self.ids.chart_container.add_widget(chart_widget)
            if photo_texture:
                self.ids.selected_image1.texture = photo_texture
            else:
                print("No profile photo texture passed.")
    def download_portfolio_as_pdf(self):
        # Obtain the ScrollView and its content
        scroll_view = self.ids.scroll_view  # Assuming your ScrollView has id 'scroll_view'
        scroll_content = scroll_view.children[0]  # Assuming the content is the first (and only) child

        # Save the original size of the ScrollView and its content
        self.original_size_hint_y = scroll_content.size_hint_y
        self.original_height = scroll_content.height

        # Temporarily resize the ScrollView content to fit all the children
        scroll_content.size_hint_y = None
        scroll_content.height = scroll_content.minimum_height

        # Schedule the screenshot to be taken after the layout update
        Clock.schedule_once(self.capture_screenshot, 0)

    def capture_screenshot(self, dt):
        # Obtain the ScrollView and its content
        scroll_view = self.ids.scroll_view  # Assuming your ScrollView has id 'scroll_view'
        scroll_content = scroll_view.children[0]  # Assuming the content is the first (and only) child

        # Capture the content of the ScrollView as an image
        screenshot_path = 'portfolio_screenshot.png'
        scroll_content.export_to_png(screenshot_path)

        # Restore the original size of the ScrollView content
        scroll_content.size_hint_y = self.original_size_hint_y
        scroll_content.height = self.original_height

        # Check if the screenshot was saved successfully
        if os.path.exists(screenshot_path):
            # Create a unique filename for the PDF
            pdf_filename = f"portfolio_{datetime.now().strftime('%Y%m%d_%H%M%S')}.pdf"
            # Determine the path to the Downloads folder based on the platform
            if platform == 'android':
                pdf_path = os.path.join(os.path.expanduser('~'), 'Download', pdf_filename)
            else:
                downloads_dir = os.path.join(os.path.expanduser('~'), 'Downloads')
                pdf_path = os.path.join(downloads_dir, pdf_filename)

            # Create a PDF
            pdf = FPDF()
            pdf.add_page()

            # Calculate image dimensions to fit the PDF page
            image_width, image_height = scroll_content.size
            pdf_width, pdf_height = pdf.w - 20, pdf.h - 20
            aspect_ratio = image_height / image_width
            img_height = pdf_width * aspect_ratio
            if img_height > pdf_height:
                img_height = pdf_height
                pdf_width = img_height / aspect_ratio

            # Add the image to the PDF
            pdf.image(screenshot_path, x=10, y=10, w=pdf_width, h=img_height)

            # Save the PDF
            pdf.output(pdf_path, 'F')
            print(f"PDF saved as {pdf_path}")

            # Optionally, remove the screenshot file after PDF creation
            os.remove(screenshot_path)

            # Show success dialog
            self.show_success_dialog('Portfolio downloaded successfully!')

        else:
            print("Failed to save the screenshot. Please try again.")

    def show_success_dialog(self, message):
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