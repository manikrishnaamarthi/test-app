import io
import json
import base64
import os

from anvil import media
from io import BytesIO
from kivy.core.image import Image as CoreImage
from kivy.uix.widget import Widget
from matplotlib import pyplot as plt
from matplotlib.figure import Figure

from chatbot import ChatBotScreen
from lender_portfolio import Lend_Portfolio
from anvil.tables import app_tables
import base64
from kivy.factory import Factory
from kivy.metrics import dp
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.image import Image
from kivy.uix.popup import Popup
from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.uix.screenmanager import Screen, SlideTransition, ScreenManager
import sqlite3
import anvil.server
from kivy.uix.screenmanager import Screen, SlideTransition
from kivy.utils import platform
from kivy.clock import mainthread
from kivymd.uix.button import MDRectangleFlatButton, MDFillRoundFlatButton
from kivymd.uix.card import MDCard
from kivymd.uix.dialog import MDDialog
from kivymd.uix.filemanager import MDFileManager
from kivymd.uix.list import ThreeLineAvatarIconListItem, IconLeftWidget
from kivymd.uix.menu import MDDropdownMenu

from lender_lost_opportunities import LostOpportunitiesScreen
from lender_notification import Lend_NotificationScreen
from lender_view_transaction_history import TransactionLH
from datetime import datetime

from anvil.tables import app_tables
from kivy.core.window import Window
from kivy.metrics import dp
from kivy.uix.button import Button
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.button import MDRaisedButton, MDFlatButton, MDRoundFlatButton, MDRectangleFlatButton
from kivy.uix.screenmanager import Screen, SlideTransition, ScreenManager
import anvil
from kivymd.uix.dialog import MDDialog
from lender_view_loans import ALlLoansScreen, ViewLoansProfileScreens
from lender_view_transaction_history import TransactionLH
from lender_view_loans_request import ViewLoansProfileScreen, ViewLoansProfileScreenLR, ViewLoansProfileScreenRL
from kivy.animation import Animation
from kivymd.uix.label import MDLabel
from kivy.animation import Animation
from kivy.clock import Clock
from kivy.uix.modalview import ModalView
from lender_report_issue import ReportScreenLender

if platform == 'android':
    from kivy.uix.button import Button
    from kivy.uix.modalview import ModalView
    from kivy.clock import Clock
    from android import api_version, mActivity
    from android.permissions import (
        request_permissions, check_permission, Permission)

# anvil.server.connect("server_VRGEXX5AO24374UMBBQ24XN6-ZAWBX57M6ZDN6TBV")

user_helpers1 = """
<WindowManager>:
    LenderDashboard:
    ViewPersonalScreen:
    ViewProfessionalScreen:
    ViewAccountScreen:
    ViewBankScreen:
    ViewBusinessScreen:
    ViewProfileScreen:
    ViewBusinessScreen1:
    ViewEmployeeScreen:
    ViewEditScreen1:
    ReturnsScreen:
    CommitmentScreen:
    ViewEditScreen4:
    ViewEditScreen5:
    ViewEditScreen6:
    ViewEditScreen7:

<LenderDashboard>
    MDBottomNavigation:
        panel_color: '#F5F5F5'
        text_color_active: "#007BFF"
        elevation: 10
        selected_color_background: "#F5F5F5"
        MDBottomNavigationItem:
            name: 'screen 1'
            text: 'Home'
            icon: 'home'
            md_bg_color: "white"
            MDScreen:

                MDNavigationLayout:

                    MDScreenManager:

                        MDScreen:
                            MDBoxLayout:
                                orientation: 'vertical'

                                MDTopAppBar:                                   
                                    elevation: 2
                                    pos_hint: {'top': 1}
                                    left_action_items: [["menu", lambda x: nav_drawer.set_state("open")]]
                                    padding:dp(20)
                                    title_align: 'center'
                                    md_bg_color: 0.043, 0.145, 0.278, 1



                                    BoxLayout:
                                        size_hint_x: None
                                        width: dp(10)
                                        pos_hint: {"center_x": 0.8, "center_y": 1.5}
                                        spacing: dp(-16)


                                        MDIconButton:
                                            icon: "bell"
                                            on_touch_down: root.go_to_lender_notification() if self.collide_point(*args[1].pos) else None    
                                            pos_hint: {"center_y": 1.3}
                                            theme_text_color: 'Custom'
                                            text_color: 1, 1, 1, 1 


                                        MDLabel:
                                            id: notification_label
                                            text: "3"
                                            size_hint_x: None
                                            width: self.texture_size[0]
                                            halign: "center"
                                            size_hint_x: None
                                            width: dp(19)
                                            valign: "center"
                                            theme_text_color: 'Custom'
                                            text_color: 1, 0, 0, 1 
                                            font_name: "Roboto-Bold"
                                            pos_hint: {"center_y": 1.5}
                                    BoxLayout:
                                        size_hint_x: None
                                        width: dp(20)
                                        pos_hint: {"center_x": 0.93, "center_y": 1.5}
                                        spacing: dp(-16)

                                        MDIconButton:
                                            icon: "help-circle-outline"
                                            on_press: root.go_to_chatbot_screen() 
                                            pos_hint: {"center_y": 2.3}
                                            theme_text_color: 'Custom'
                                            text_color: 1, 1, 1, 1
                                ScrollView:
                                    MDBoxLayout:
                                        orientation: 'vertical'
                                        padding: "10dp", "5dp", "10dp", "0dp"
                                        size_hint_y: None
                                        height: dp(1150)
                                        spacing: dp(20)


                                        MDCard:
                                            id: card
                                            orientation: 'vertical'
                                            size_hint: 1, None
                                            height: dp(120)
                                            padding: dp(15)
                                            spacing: dp(3)
                                            elevation: 1
                                            on_release: root.account()

                                            BoxLayout:
                                                orientation: 'horizontal'
                                                spacing: dp(5)

                                                Image:
                                                    id: image
                                                    source: 'img.png'  # Update with the actual path to the image
                                                    size_hint_x: None
                                                    height: dp(60)
                                                    width: dp(90)
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

                                                Widget:
                                                    size_hint_x: None
                                                    width: dp(10)

                                                BoxLayout:
                                                    orientation: 'vertical'

                                                    MDLabel:
                                                        id: details
                                                        text: "[b]Name[/b] : John Doe"
                                                        theme_text_color: 'Custom'
                                                        text_color: 0, 0, 0, 1
                                                        halign: 'left'
                                                        markup: True

                                                    MDLabel:
                                                        id: joined_date
                                                        text: "[b]Joined Date id[/b] : '12-12-2012'"
                                                        theme_text_color: 'Custom'
                                                        text_color: 0, 0, 0, 1
                                                        halign: 'left'
                                                        markup: True

                                                    MDLabel:
                                                        id: member_type
                                                        text: "[b]Membership Type[/b] : Elite"
                                                        theme_text_color: 'Custom'
                                                        text_color: 0, 0, 0, 1
                                                        halign: 'left'
                                                        markup: True


                                        GridLayout:
                                            cols: 2
                                            padding: dp(10)
                                            spacing: dp(10)
                                            MDBoxLayout:
                                                orientation: 'vertical'
                                                size_hint_y: None
                                                height: self.minimum_height
                                                md_bg_color: "#AEDFF7"
                                                canvas.before:
                                                    Color:
                                                        rgba: 0, 0, 0, 1
                                                    Line:
                                                        width: 0.01
                                                        rectangle: (self.x, self.y, self.width, self.height)
                                                MDLabel:
                                                    id: commitment
                                                    text: "Rs. 12903838"
                                                    size_hint_y: None
                                                    height: dp(30)
                                                    halign: 'center'
                                                    theme_text_color: "Custom"
                                                    text_color: "#333333"
                                                    font_name: "Roboto-Bold"
                                                    font_size: dp(20)

                                                MDLabel:
                                                    text: "My Commitments"
                                                    size_hint_y: None
                                                    height: dp(30)
                                                    halign: 'center'
                                                    theme_text_color: "Custom"
                                                    text_color: "#333333"
                                                    font_name: "Roboto-Bold"
                                                MDFlatButton:
                                                    text: "View All"
                                                    size_hint_y: None
                                                    height: dp(30)
                                                    pos_hint: {'center_x': 0.5}
                                                    theme_text_color: "Custom"
                                                    text_color: "#007BFF"
                                                    on_release: root.go_to_commitment_screen()
                                            MDBoxLayout:
                                                orientation: 'vertical'
                                                size_hint_y: None
                                                height: self.minimum_height
                                                md_bg_color: "#AEDFF7"
                                                canvas.before:
                                                    Color:
                                                        rgba: 0, 0, 0, 1
                                                    Line:
                                                        width: 0.1
                                                        rectangle: (self.x, self.y, self.width, self.height)
                                                MDLabel:
                                                    id: total_amount1
                                                    text: "Rs. 50,000"
                                                    size_hint_y: None
                                                    height: dp(30)
                                                    halign: 'center'
                                                    theme_text_color: "Custom"
                                                    text_color: "#333333"
                                                    font_name: "Roboto-Bold"
                                                    font_size: dp(20)

                                                MDLabel:
                                                    text: "Opening Balance"
                                                    size_hint_y: None
                                                    height: dp(30)
                                                    halign: 'center'
                                                    font_name: "Roboto-Bold"
                                                    theme_text_color: "Custom"
                                                    text_color: "#333333"
                                                MDFlatButton:
                                                    text: "View All"
                                                    size_hint_y: None
                                                    height: dp(30)
                                                    pos_hint: {'center_x': 0.5}
                                                    theme_text_color: "Custom"
                                                    text_color: "#007BFF"
                                                    on_release: root.go_to_wallet()
                                            MDBoxLayout:
                                                orientation: 'vertical'
                                                size_hint_y: None
                                                height: self.minimum_height
                                                md_bg_color: "#AEDFF7"
                                                canvas.before:
                                                    Color:
                                                        rgba: 0, 0, 0, 1
                                                    Line:
                                                        width: 0.1
                                                        rectangle: (self.x, self.y, self.width, self.height)
                                                MDLabel:
                                                    id: return_amount
                                                    text: "Rs. 20,000"
                                                    size_hint_y: None
                                                    height: dp(30)
                                                    halign: 'center'
                                                    theme_text_color: "Custom"
                                                    text_color: "#333333"
                                                    font_name: "Roboto-Bold"
                                                    font_size: dp(20)

                                                MDLabel:
                                                    text: "My Returns"
                                                    size_hint_y: None
                                                    height: dp(30)
                                                    halign: 'center'
                                                    font_name: "Roboto-Bold"
                                                    theme_text_color: "Custom"
                                                    text_color: "#333333"
                                                MDFlatButton:
                                                    text: "View All"
                                                    size_hint_y: None
                                                    height: dp(30)
                                                    pos_hint: {'center_x': 0.5}
                                                    theme_text_color: "Custom"
                                                    text_color: "#007BFF" 
                                                    on_release: root.go_to_returns_screen()
                                            MDBoxLayout:
                                                orientation: 'vertical'
                                                size_hint_y: None
                                                height: self.minimum_height
                                                md_bg_color: "#AEDFF7"
                                                canvas.before:
                                                    Color:
                                                        rgba: 0, 0, 0, 1
                                                    Line:
                                                        width: 0.1
                                                        rectangle: (self.x, self.y, self.width, self.height)

                                                MDLabel:
                                                    id: loan
                                                    text: "3"
                                                    size_hint_y: None
                                                    height: dp(30)
                                                    halign: 'center'
                                                    theme_text_color: "Custom"
                                                    text_color: "#333333"
                                                    font_name: "Roboto-Bold"
                                                    font_size: dp(20)

                                                MDLabel:
                                                    text: "New Loan Requests"
                                                    size_hint_y: None
                                                    height: dp(30)
                                                    halign: 'center'
                                                    font_name: "Roboto-Bold"
                                                    theme_text_color: "Custom"
                                                    text_color: "#333333"
                                                MDFlatButton:
                                                    text: "View All"
                                                    size_hint_y: None
                                                    height: dp(30)
                                                    pos_hint: {'center_x': 0.5}
                                                    theme_text_color: "Custom"
                                                    text_color: "#007BFF"
                                                    on_release: root.view_loan_request()

                                        MDLabel:
                                            text: ""
                                        MDLabel:
                                            text: ""
                                        MDLabel:
                                            text: ""
                                            size_hint_y: None
                                            height: dp(30)
                                        Widget:
                                            size_hint_y: None
                                            height: 5
                                            canvas:
                                                Color:
                                                    rgba: 0, 0, 0, 1  # Change color if needed
                                                Line:
                                                    points: self.x, self.y, self.x + self.width, self.y
                                        MDBoxLayout:
                                            orientation: 'vertical'
                                            spacing: dp(10)
                                            BoxLayout:  
                                                orientation: 'vertical'
                                                size_hint_y: None
                                                height: self.minimum_height
                                                MDLabel:
                                                    text: 'Borrower Listing'
                                                    bold: True
                                                    size_hint_y: None
                                                    height: dp(20)
                                                MDFloatLayout:
                                                    MDTextField:
                                                        id: search
                                                        hint_text: "Search"
                                                        pos_hint: {"center_x": 0.5, "top": 1}


                                                    MDIconButton:
                                                        id: button
                                                        icon: 'magnify'
                                                        pos_hint: {"right": 1, "top": 1}
                                                        on_release: app.root.get_screen('LenderDashboard').menu.open()
                                                        on_release: root.setup_menu()

                                        MDLabel:
                                            text: ''
                                            size_hint_y: None
                                            height: dp(30)

                                        GridLayout:
                                            cols: 3
                                            spacing: dp(10)
                                            size_hint_y: None
                                            height: dp(50)
                                            Image:
                                                size_hint: None, None
                                                size: "60dp", "60dp"

                                            MDLabel:
                                                id: borrower_name
                                                text: "Mamidala sai"
                                                font_family: "Arial"
                                                halign: "center"
                                            MDLabel:
                                                id: age
                                                text: "23years"
                                                font_family: "Arial"
                                                font_size: dp(10)

                                        GridLayout:
                                            cols: 3
                                            spacing: dp(10)
                                            MDBoxLayout:
                                                orientation: 'vertical'
                                                height: self.minimum_height
                                                canvas.before:
                                                    Color:
                                                        rgba: 0, 0, 0, 1
                                                    Line:
                                                        width: 1
                                                        rectangle: (self.x, self.y, self.width, self.height)

                                                MDIcon:
                                                    icon: "speedometer"
                                                    pos_hint: {'center_x': 0.5}
                                                    theme_text_color: "Custom"
                                                    text_color: "#23639e"
                                                MDBoxLayout:
                                                    orientation: 'vertical'
                                                    spacing: dp(30)
                                                    padding: dp(20)
                                                    MDLabel:
                                                        text: "Ascend Score"
                                                        font_size: dp(12)
                                                        halign: 'center'
                                                    MDLabel:
                                                        id: score
                                                        text: "170"
                                                        font_size:dp(16)
                                                        halign: 'center'
                                            MDBoxLayout:
                                                orientation: 'vertical'
                                                height: self.minimum_height
                                                canvas.before:
                                                    Color:
                                                        rgba: 0, 0, 0, 1
                                                    Line:
                                                        width: 1
                                                        rectangle: (self.x, self.y, self.width, self.height)

                                                MDIcon:
                                                    icon: "account-tie"
                                                    pos_hint: {'center_x': 0.5}
                                                    theme_text_color: "Custom"
                                                    text_color: "#23639e"
                                                MDBoxLayout:
                                                    orientation: 'vertical'
                                                    spacing: dp(30)
                                                    padding:dp(20)
                                                    MDLabel:
                                                        text: "Profession Type"
                                                        font_size: dp(12)
                                                        halign: 'center'
                                                    MDLabel:
                                                        id: employment
                                                        text: "Full Time"
                                                        font_size:dp(16)
                                                        halign: 'center'
                                            MDBoxLayout:
                                                orientation: 'vertical'
                                                size_hint_y: None
                                                height: dp(100)
                                                canvas.before:
                                                    Color:
                                                        rgba: 0, 0, 0, 1
                                                    Line:
                                                        width: 1
                                                        rectangle: (self.x, self.y, self.width, self.height)
                                                MDIcon:
                                                    icon: "package-variant-plus"
                                                    pos_hint: {'center_x': 0.5}
                                                    theme_text_color: "Custom"
                                                    text_color: "#23639e"
                                                MDBoxLayout:
                                                    orientation: 'vertical'
                                                    spacing: dp(30)
                                                    padding:dp(20)
                                                    MDLabel:
                                                        text: "Product Name"
                                                        font_size: dp(12)
                                                        halign: 'center'
                                                    MDLabel:
                                                        id: product_name
                                                        text: "TVS"
                                                        font_size:dp(16)
                                                        halign: 'center'

                                        MDLabel:
                                            text: ''
                                            size_hint_y: None
                                            height: dp(30)

                                        GridLayout:
                                            cols: 2
                                            padding: dp(10)
                                            spacing: dp(10)
                                            MDBoxLayout:
                                                orientation: 'vertical'
                                                size_hint_y: None
                                                height: dp(70)

                                                canvas.before:
                                                    Color:
                                                        rgba: 0, 0, 0, 1
                                                    Line:
                                                        width: 2
                                                        rectangle: (self.x, self.y, self.width, self.height)

                                                GridLayout:
                                                    cols: 2
                                                    spacing: dp(10)
                                                    padding: dp(5)

                                                    Image:
                                                        source: "icon1.png"
                                                        size_hint: None, None
                                                        size: "60dp", "60dp"
                                                    MDBoxLayout:
                                                        orientation: 'vertical'
                                                        MDLabel:
                                                            text: "Loan Amount"
                                                            font_size: dp(12)
                                                        MDLabel:
                                                            id: amount
                                                            text: "Rs. 1,50,000"
                                                            font_size:dp(15)

                                            MDBoxLayout:
                                                orientation: 'vertical'
                                                size_hint_y: None
                                                height: dp(70)
                                                canvas.before:
                                                    Color:
                                                        rgba: 0, 0, 0, 1
                                                    Line:
                                                        width: 2
                                                        rectangle: (self.x, self.y, self.width, self.height)

                                                GridLayout:
                                                    cols: 2
                                                    spacing: dp(10)
                                                    padding: dp(5)

                                                    Image:
                                                        source: "icon2.png"
                                                        size_hint: None, None
                                                        size: "60dp", "60dp"
                                                    MDBoxLayout:
                                                        orientation: 'vertical'
                                                        MDLabel:
                                                            text: "Left Amount"
                                                            font_size: dp(12)
                                                        MDLabel:
                                                            id:left
                                                            text: "Rs. 1,50,000"
                                                            font_size:dp(15)

                                        MDLabel:
                                            text: ""
                                            size_hint_y: None
                                            height: dp(2)

                                        GridLayout:
                                            cols: 2
                                            padding: dp(10)
                                            spacing: dp(10)
                                            MDBoxLayout:
                                                orientation: 'vertical'
                                                size_hint_y: None
                                                height: dp(70)
                                                canvas.before:
                                                    Color:
                                                        rgba: 0, 0, 0, 1
                                                    Line:
                                                        width: 2
                                                        rectangle: (self.x, self.y, self.width, self.height)

                                                GridLayout:
                                                    cols: 2
                                                    spacing: dp(10)
                                                    padding: dp(5)

                                                    Image:
                                                        source: "icon3.png"
                                                        size_hint: None, None
                                                        size: "50dp", "50dp"
                                                    MDBoxLayout:
                                                        orientation: 'vertical'
                                                        MDLabel:
                                                            text: "Interest Rate"
                                                            font_size: dp(12)
                                                        MDLabel:
                                                            id: interest
                                                            text: "22%"
                                                            font_size:dp(15)

                                            MDBoxLayout:
                                                orientation: 'vertical'
                                                size_hint_y: None
                                                height: dp(70)
                                                canvas.before:
                                                    Color:
                                                        rgba: 0, 0, 0, 1
                                                    Line:
                                                        width: 2
                                                        rectangle: (self.x, self.y, self.width, self.height)

                                                GridLayout:
                                                    cols: 2
                                                    spacing: dp(20)
                                                    padding: dp(5)

                                                    Image:
                                                        source: "icon4.png"
                                                        size_hint: None, None
                                                        size: "30dp", "60dp"
                                                    MDBoxLayout:
                                                        orientation: 'vertical'
                                                        MDLabel:
                                                            text: "Tenure"
                                                            font_size: dp(12)
                                                        MDLabel:
                                                            id: tenure
                                                            text: "24 Months"
                                                            font_size:dp(15)
                                        MDLabel:
                                            text: ""
                                            size_hint_y: None
                                            height: dp(10)
                                        GridLayout:
                                            cols: 2
                                            spacing: dp(20)
                                            padding: dp(20)
                                            pos_hint: {'center_x': 0.55}
                                            MDFillRoundFlatIconButton:
                                                text: "Invest Now"
                                                icon: "currency-rupee"
                                                text_color: "white"
                                                font_name: "Roboto-Bold"
                                                md_bg_color: '#117d2e'
                                                on_release: root.invest()
                                            MDFillRoundFlatIconButton:
                                                text: "View More"
                                                icon: "clipboard-text-outline"
                                                font_name: "Roboto-Bold"
                                                text_color: "white"
                                                md_bg_color: 0.043, 0.145, 0.278, 1
                                                on_release: root.view_loan_request()

                                        Widget:
                                            size_hint_y: None
                                            height: 5
                                            canvas:
                                                Color:
                                                    rgba: 0, 0, 0, 1  # Change color if needed
                                                Line:
                                                    points: self.x, self.y, self.x + self.width, self.y


                                        MDLabel:
                                            text: ""
                                        MDLabel:
                                            text: ""
                    MDNavigationDrawer:
                        id: nav_drawer
                        radius: (0, 16, 16, 0)

                        MDNavigationDrawerMenu:

                            MDNavigationDrawerHeader:
                                id: name
                                title: "Welcome Back"
                                title_color: "#4a4939"
                                text: "Sai Mamidala"
                                spacing: "4dp"
                                padding: "12dp", 0, 0, "56dp"

                            MDNavigationDrawerItem
                                icon: "calendar-check-outline"
                                text: "Today's Dues"
                                icon_color: "#23639e"
                                on_release: root.lender_today_due()
                            MDNavigationDrawerDivider:

                            MDNavigationDrawerItem
                                icon: "bank"
                                text: "View Loans"
                                icon_color: "#23639e"
                                on_release: root.view_loanscreen()
                            MDNavigationDrawerDivider:

                            MDNavigationDrawerItem
                                icon: "file-document"
                                text: "View Loan Requests"
                                icon_color: "#23639e"
                                on_release: root.view_loan_request()
                            MDNavigationDrawerDivider:

                            MDNavigationDrawerItem
                                icon: "plus-circle"
                                text: "View Loans Extensions"
                                icon_color: "#23639e"
                                on_release: root.newloan_extension()
                            MDNavigationDrawerDivider:

                            MDNavigationDrawerItem
                                icon: "home-minus"
                                text: "View Loans Foreclosure"
                                icon_color: "#23639e"
                                on_release: root.view_loan_foreclose()
                            MDNavigationDrawerDivider:

                            MDNavigationDrawerItem
                                icon: "eye-outline"
                                text: "View Lost Opportunities"
                                icon_color: "#23639e"
                                on_release: root.view_lost_opportunities()
                            MDNavigationDrawerDivider:

                            MDNavigationDrawerItem
                                icon: "history"
                                text: "View Transactions History"
                                icon_color: "#23639e"
                                on_release: root.view_transaction_history()
                            MDNavigationDrawerDivider:
                            MDNavigationDrawerItem
                                icon: "report_icon.png"
                                text: "Report Issue!"
                                icon_color: "#23639e"
                                on_release: root.go_to_lender_report_issue()
                            MDNavigationDrawerDivider:
                            MDNavigationDrawerItem
                                icon: "briefcase"
                                text: "View  Portfolio"
                                icon_color: "#23639e"
                                on_release: root.view_Borr_Portfolio()
                            MDNavigationDrawerDivider:
                            MDNavigationDrawerItem
                                icon: "logout"
                                text: "Logout"
                                icon_color: "#23639e"
                                on_release: root.go_to_main_screen()
                            MDNavigationDrawerDivider:

        MDBottomNavigationItem:
            name: 'screen 2'
            text: 'Wallet'
            icon: 'wallet'
            on_tab_press: root.wallet()
            MDTopAppBar:
                title: "Ascends P2P Wallet"
                elevation: 2
                pos_hint: {'top': 1}
                # left_action_items: [['arrow-left',lambda x: root.on_back_button()]]
                right_action_items: [['refresh', lambda x: root.refresh1()]]
                title_align: 'center'
                md_bg_color: 0.043, 0.145, 0.278, 1

            MDBoxLayout:
                id: box1
                orientation: 'vertical'
                spacing: dp(30)
                padding: dp(30)
                MDLabel:
                    text: 'Available Balance'
                    halign: 'center'
                    size_hint_y: None
                    height: dp(30)

                GridLayout:
                    cols: 2
                    spacing: dp(20)
                    pos_hint: {'center_x': 0.7, 'center_y':0.3}
                    size_hint_y: None
                    height: dp(30)
                    MDIcon:
                        icon: 'currency-inr'
                        halign: 'center'
                    MDLabel:
                        id: total_amount
                        halign: 'left'
                        font_size: dp(25)
                        bold: True

                GridLayout:
                    cols: 2
                    spacing: dp(20)
                    size_hint_y: None
                    height: dp(50)
                    pos_hint: {'center_x': 0.6}
                    MDRectangleFlatIconButton:
                        text: "Deposit"
                        id: deposit_button_grid
                        line_color: 0, 0, 0, 0
                        icon: "cash"
                        text_color: 0, 0, 0, 1
                        md_bg_color:1,1,1,1
                        font_name:"Roboto-Bold"
                        on_release: root.highlight_button('deposit')
                    MDRectangleFlatIconButton:
                        id: withdraw_button_grid
                        text: "Withdraw"
                        icon: "cash"
                        line_color: 0, 0, 0, 0
                        text_color: 0, 0, 0, 1
                        md_bg_color: 1,1,1,1
                        font_name:"Roboto-Bold"
                        on_release: root.highlight_button('withdraw')
                MDLabel:
                    text: 'Enter Amount'
                    bold: True
                    size_hint_y: None
                    height: dp(5)
                MDTextField:
                    id: enter_amount
                    multiline: False
                    helper_text: 'Enter valid Amount'
                    helper_text_mode: 'on_focus'
                    size_hint_y:None
                    font_size: "15dp"
                    theme_text_color: "Custom"
                    hint_text_color: 0, 0, 0, 1
                    hint_text_color_normal: "black"
                    text_color_normal: "black"
                    helper_text_color_normal: "black"
                    on_touch_down: root.on_amount_touch_down()

                MDFlatButton:
                    text: "View Transaction History >"
                    theme_text_color: "Custom"
                    text_color: "black"
                    pos_hint: {'center_x': 0.5}
                    padding: dp(10)
                    md_bg_color: 140/255, 140/255, 140/255, 1
                    on_release: root.view_transaction_history()
                GridLayout:
                    id: box
                    cols: 1
                    spacing: dp(20)
                    size_hint_y: None
                    height: dp(50)
                    pos_hint: {'center_x': 0.65}


                MDRoundFlatButton:
                    text: "Submit"
                    md_bg_color: 0.043, 0.145, 0.278, 1
                    theme_text_color: 'Custom'
                    font_name: "Roboto-Bold" 
                    text_color: 1, 1, 1, 1
                    size_hint: 0.7, None
                    height: "40dp"
                    pos_hint: {'center_x': 0.5}
                    on_release: root.submit()
                MDLabel:
                    text:''
                    size_hint_y:None
                    height:dp(20)


        MDBottomNavigationItem:
            name: 'screen 4'
            text: 'Loans'
            icon: 'cash'
            text_color_normal: '#4c594f'
            text_color_active: 1, 0, 0, 1
            on_tab_press: root.refresh5()
            BoxLayout:
                orientation: 'vertical'

                MDTopAppBar:
                    title: "View All Loans"
                    elevation: 3
                    # left_action_items: [['arrow-left', lambda x: root.on_back_button()]]
                    right_action_items: [['refresh', lambda x: root.refresh5()]]
                    md_bg_color: 0.043, 0.145, 0.278, 1

                MDScrollView:
                    MDBoxLayout:
                        id: container
                        orientation: 'vertical'
                        padding: dp(25)
                        spacing: dp(10)
                        size_hint_y: None
                        height: self.minimum_height
                        width: self.minimum_width
                        adaptive_size: True
                        pos_hint: {"center_x": 0, "center_y":  0}

                    # MDList:
                    #     
                    #     id: container

        MDBottomNavigationItem:
            name: 'screen 3'
            text: 'Account'
            icon: 'account'
            icon_color: '#4c594f'
            font_name: "Roboto-Bold"
            BoxLayout:
                orientation: 'vertical'
                size_hint: 1, 1
                pos_hint: {'center_x':0.5, 'center_y':0.5}
                MDTopAppBar:
                    title: "Account Profile"
                    elevation: 2
                    pos_hint: {'top': 1}
                    # left_action_items: [['arrow-left', lambda x: root.on_back_button()]]
                    right_action_items: [['refresh', lambda x: root.refresh6()]]
                    title_align: 'center'
                    md_bg_color: 0.043, 0.145, 0.278, 1

                MDBoxLayout:
                    size_hint: 1, 1
                    orientation: "vertical"
                    spacing: dp(5)
                    padding: dp(5)

                    MDBoxLayout:
                        orientation: "horizontal"
                        pos_hint: {"top": 1}
                        size_hint_y: 0.15
                        padding:dp(10)
                        canvas.before:
                            Color:
                                rgba: 0, 0, 0, 1
                            Line:
                                width: 0.25
                                rounded_rectangle: (self.x, self.y, self.width, self.height, 15)


                        text_size: self.width - dp(20), None

                        Image:
                            id: image1
                            source: 'icon8.png'
                            size_hint_x: None
                            height: dp(60)
                            width: dp(90)
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

                        MDBoxLayout:
                            orientation: "vertical"
                            size_hint_y: None
                            height: self.minimum_height
                            pos_hint: {"center_y": 0.5}
                            padding: dp(5)
                            spacing: dp(5)

                            MDLabel:
                                id: username
                                text: "Welcome"
                                bold: True
                                font_size: dp(20)
                                size_hint_y: None
                                height: self.texture_size[1]

                            MDLabel:
                                id: date
                                text: "Joined Date:"
                                font_size: dp(15)
                                size_hint_y: None
                                height: self.texture_size[1]

                            MDLabel:
                                id: balance
                                text: "Available Balance:"
                                font_size: dp(15)
                                size_hint_y: None
                                height: self.texture_size[1]

                    MDBoxLayout:
                        orientation: "vertical"
                        size_hint_y:0.47

                        MDCard:
                            pos_hint:{"top": 1}

                            MDGridLayout:
                                cols: 2
                                spacing: dp(20)  # Equal gap between cards
                                padding: dp(20)  # Proper padding around the grid
                                MDBoxLayout:
                                    orientation: 'vertical'
                                    size_hint_y: None
                                    height: dp(70)
                                    md_bg_color: "#ffffff"
                                    canvas.before:
                                        Color:
                                            rgba: 0, 0, 0, 1
                                        Line:
                                            width: 1.5
                                            rectangle: (self.x, self.y, self.width,self.height)
                                    # Card 1
                                    MDCard:
                                        md_bg_color: "#ffffff"  # Customize background color
                                        orientation: "vertical"
                                        padding:dp(9), dp(3)
                                        on_release: root.profile()

                                        Image:
                                            source: "icon7.png"
                                            size_hint: (0.4, 1)
                                            pos_hint:{"center_x":0.5,"center_y":0.2}
                                            pos_hint: {'center_x': 0.5, 'center_y': 0.5}

                                        MDLabel:
                                            text: "Profile Info"
                                            font_size:dp(12)
                                            bold: True
                                            theme_text_color: "Custom"
                                            text_color: 0, 0, 0, 1
                                            halign: "center"  # Center-align the label text
                                MDBoxLayout:
                                    orientation: 'vertical'
                                    size_hint_y: None
                                    height: dp(70)
                                    md_bg_color: "#ffffff"
                                    canvas.before:
                                        Color:
                                            rgba: 0, 0, 0, 1
                                        Line:
                                            width: 1.5
                                            rectangle: (self.x, self.y, self.width,self.height)
                                    MDCard:
                                        md_bg_color: "#ffffff"  # Customize background color
                                        orientation: "vertical"
                                        padding:dp(9), dp(3)
                                        on_release:root.personal()
                                        Image:
                                            source: "icon6.png"
                                            size_hint: (0.4, 1)
                                            pos_hint:{"center_x":0.5,"center_y":0.2}
                                            pos_hint: {'center_x': 0.5, 'center_y': 0.5}

                                        MDLabel:
                                            text: "Personal Info"
                                            font_size:dp(12)
                                            bold: True
                                            theme_text_color: "Custom"
                                            text_color: 0, 0, 0, 1
                                            halign: "center"
                                MDBoxLayout:
                                    orientation: 'vertical'
                                    size_hint_y: None
                                    height: dp(70)
                                    md_bg_color: "#ffffff"
                                    canvas.before:
                                        Color:
                                            rgba: 0, 0, 0, 1
                                        Line:
                                            width: 1.5
                                            rectangle: (self.x, self.y, self.width,self.height)
                                    MDCard:
                                        md_bg_color: "#ffffff"  # Customize background color
                                        orientation: "vertical"
                                        padding:dp(9), dp(3)
                                        on_release: root.navigate_based_on_touch1()
                                        Image:
                                            source: "icon12.png"
                                            size_hint: (0.4, 1)
                                            pos_hint:{"center_x":0.5,"center_y":0.2}
                                            pos_hint: {'center_x': 0.5, 'center_y': 0.5}


                                        MDLabel:
                                            text: "Professional Info"
                                            font_size:dp(12)
                                            bold: True
                                            theme_text_color: "Custom"
                                            text_color: 0, 0, 0, 1
                                            halign: "center"
                                MDBoxLayout:
                                    orientation: 'vertical'
                                    size_hint_y: None
                                    height: dp(70)
                                    md_bg_color: "#ffffff"
                                    canvas.before:
                                        Color:
                                            rgba: 0, 0, 0, 1
                                        Line:
                                            width: 1.5
                                            rectangle: (self.x, self.y, self.width,self.height)
                                    MDCard:
                                        md_bg_color: "#ffffff"  # Customize background color
                                        orientation: "vertical"
                                        padding:dp(9), dp(3)
                                        on_release:root.go_to_business1()

                                        Image:
                                            source: "icon9.png"
                                            size_hint: (0.4, 1)
                                            pos_hint:{"center_x":0.5,"center_y":0.2}
                                            pos_hint: {'center_x': 0.5, 'center_y': 0.5}


                                        MDLabel:
                                            text: "Business Info"
                                            font_size:dp(12)
                                            bold: True
                                            theme_text_color: "Custom"
                                            text_color: 0, 0, 0, 1
                                            halign: "center"

                                MDBoxLayout:
                                    orientation: 'vertical'
                                    size_hint_y: None
                                    height: dp(70)
                                    md_bg_color: "#ffffff"
                                    canvas.before:
                                        Color:
                                            rgba: 0, 0, 0, 1
                                        Line:
                                            width: 1.5
                                            rectangle: (self.x, self.y, self.width,self.height)
                                    MDCard:
                                        md_bg_color: "#ffffff"  # Customize background color
                                        orientation: "vertical"
                                        padding:dp(9), dp(3)
                                        on_release: root.bank()
                                        Image:
                                            source: "icon10.png"
                                            size_hint: (0.4, 1)
                                            pos_hint:{"center_x":0.5,"center_y":0.2}
                                            pos_hint: {'center_x': 0.5, 'center_y': 0.5}


                                        MDLabel:
                                            text: "Bank Details"
                                            font_size:dp(12)
                                            bold: True
                                            theme_text_color: "Custom"
                                            text_color: 0, 0, 0, 1
                                            halign: "center"

                                MDBoxLayout:
                                    orientation: 'vertical'
                                    size_hint_y: None
                                    height: dp(70)
                                    md_bg_color: "#ffffff"
                                    canvas.before:
                                        Color:
                                            rgba: 0, 0, 0, 1
                                        Line:
                                            width: 1.5
                                            rectangle: (self.x, self.y, self.width,self.height)
                                    MDCard:
                                        md_bg_color: "#ffffff"  # Customize background color
                                        orientation: "vertical"
                                        padding:dp(9), dp(3)
                                        on_release:root.Edit_email()

                                        Image:
                                            source: "icon11.png"
                                            size_hint: (0.4, 1)
                                            pos_hint:{"center_x":0.5,"center_y":0.2}
                                            pos_hint: {'center_x': 0.5, 'center_y': 0.5}


                                        MDLabel:
                                            text: "Change User Email"
                                            font_size:dp(12)
                                            bold: True
                                            theme_text_color: "Custom"
                                            text_color: 0, 0, 0, 1
                                            halign: "center"   

<ViewAccountScreen>
    MDBoxLayout:
        orientation: 'vertical'
        MDTopAppBar:
            title: "Account Information"
            elevation: 2
            pos_hint: {'top': 1}
            left_action_items: [['arrow-left', lambda x: root.on_back_button_press()]]
            right_action_items: [['refresh', lambda x: root.refresh()]]
            title_align: 'center'  # Center-align the title
            md_bg_color: 0.043, 0.145, 0.278, 1

        MDBoxLayout:
            size_hint: 1, 1
            orientation: "vertical"
            spacing: dp(5)
            padding: dp(5)

            MDBoxLayout:
                orientation: "horizontal"
                pos_hint: {"top": 1}
                size_hint_y: 0.15
                spacing: dp(10)
                padding:dp(10)
                spacing:
                canvas.before:
                    Color:
                        rgba: 0, 0, 0, 1
                    Line:
                        width: 0.25
                        rounded_rectangle: (self.x, self.y, self.width, self.height, 15)


                text_size: self.width - dp(20), None

                Image:
                    id: selected_image1
                    source: 'icon8.png'
                    size_hint_x: None
                    height: dp(60)
                    width: dp(90)
                    size_hint: None, None
                    size: dp(80), dp(80)  # Make sure the size is a perfect square for a circular shape
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

                MDBoxLayout:
                    orientation: "vertical"
                    size_hint_y: None
                    height: self.minimum_height
                    pos_hint: {"center_y": 0.5}
                    padding: dp(5)

                    MDLabel:
                        id: username
                        text: "Welcome"
                        bold: True
                        font_size: dp(20)
                        size_hint_y: None
                        height: self.texture_size[1]

                    MDLabel:
                        id: date
                        text: "Joined Date:"
                        font_size: dp(15)
                        size_hint_y: None
                        height: self.texture_size[1]

                    MDLabel:
                        id: balance
                        text: "Available Balance:"
                        font_size: dp(15)
                        size_hint_y: None
                        height: self.texture_size[1]

            MDBoxLayout:
                orientation: "vertical"
                size_hint_y:0.47

                MDCard:
                    pos_hint:{"top": 1}

                    MDGridLayout:
                        cols: 2
                        spacing: dp(20)  # Equal gap between cards
                        padding: dp(20)  # Proper padding around the grid
                        MDBoxLayout:
                            orientation: 'vertical'
                            size_hint_y: None
                            height: dp(70)
                            md_bg_color: "#ffffff"
                            canvas.before:
                                Color:
                                    rgba: 0, 0, 0, 1
                                Line:
                                    width: 1.5
                                    rectangle: (self.x, self.y, self.width,self.height)
                            # Card 1
                            MDCard:
                                md_bg_color: "#ffffff"  # Customize background color
                                orientation: "vertical"
                                padding:dp(9), dp(3)
                                on_release:root.profile()
                                Image:
                                    source: "icon7.png"
                                    size_hint: (0.4, 1)
                                    pos_hint:{"center_x":0.5,"center_y":0.2}
                                    pos_hint: {'center_x': 0.5, 'center_y': 0.5}

                                MDLabel:
                                    text: "Profile Info"
                                    font_size:dp(12)
                                    bold: True
                                    theme_text_color: "Custom"
                                    text_color: 0, 0, 0, 1
                                    halign: "center"  # Center-align the label text
                        MDBoxLayout:
                            orientation: 'vertical'
                            size_hint_y: None
                            height: dp(70)
                            md_bg_color: "#ffffff"
                            canvas.before:
                                Color:
                                    rgba: 0, 0, 0, 1
                                Line:
                                    width: 1.5
                                    rectangle: (self.x, self.y, self.width,self.height)
                            MDCard:
                                md_bg_color: "#ffffff"  # Customize background color
                                orientation: "vertical"
                                padding:dp(9), dp(3)
                                on_release:root.personal()
                                Image:
                                    source: "icon6.png"
                                    size_hint: (0.4, 1)
                                    pos_hint:{"center_x":0.5,"center_y":0.2}
                                    pos_hint: {'center_x': 0.5, 'center_y': 0.5}

                                MDLabel:
                                    text: "Personal Info"
                                    font_size:dp(12)
                                    bold: True
                                    theme_text_color: "Custom"
                                    text_color: 0, 0, 0, 1
                                    halign: "center"
                        MDBoxLayout:
                            orientation: 'vertical'
                            size_hint_y: None
                            height: dp(70)
                            md_bg_color: "#ffffff"
                            canvas.before:
                                Color:
                                    rgba: 0, 0, 0, 1
                                Line:
                                    width: 1.5
                                    rectangle: (self.x, self.y, self.width,self.height)
                            MDCard:
                                md_bg_color: "#ffffff"  # Customize background color
                                orientation: "vertical"
                                padding:dp(9), dp(3)
                                on_release: root.navigate_based_on_touch1()
                                Image:
                                    source: "icon12.png"
                                    size_hint: (0.4, 1)
                                    pos_hint:{"center_x":0.5,"center_y":0.2}
                                    pos_hint: {'center_x': 0.5, 'center_y': 0.5}

                                MDLabel:
                                    text: "Professional Info"
                                    font_size:dp(12)
                                    bold: True
                                    theme_text_color: "Custom"
                                    text_color: 0, 0, 0, 1
                                    halign: "center"
                        MDBoxLayout:
                            orientation: 'vertical'
                            size_hint_y: None
                            height: dp(70)
                            md_bg_color: "#ffffff"
                            canvas.before:
                                Color:
                                    rgba: 0, 0, 0, 1
                                Line:
                                    width: 1.5
                                    rectangle: (self.x, self.y, self.width,self.height)
                            MDCard:
                                md_bg_color: "#ffffff"  # Customize background color
                                orientation: "vertical"
                                padding:dp(9), dp(3)
                                on_release: root.go_to_business1()

                                Image:
                                    source: "icon9.png"
                                    size_hint: (0.4, 1)
                                    pos_hint:{"center_x":0.5,"center_y":0.2}
                                    pos_hint: {'center_x': 0.5, 'center_y': 0.5}


                                MDLabel:
                                    text: "Business Info"
                                    font_size:dp(12)
                                    bold: True
                                    theme_text_color: "Custom"
                                    text_color: 0, 0, 0, 1
                                    halign: "center"

                        MDBoxLayout:
                            orientation: 'vertical'
                            size_hint_y: None
                            height: dp(70)
                            md_bg_color: "#ffffff"
                            canvas.before:
                                Color:
                                    rgba: 0, 0, 0, 1
                                Line:
                                    width: 1.5
                                    rectangle: (self.x, self.y, self.width,self.height)
                            MDCard:
                                md_bg_color: "#ffffff"  # Customize background color
                                orientation: "vertical"
                                padding:dp(9), dp(3)
                                on_release: root.bank()
                                Image:
                                    source: "icon10.png"
                                    size_hint: (0.4, 1)
                                    pos_hint:{"center_x":0.5,"center_y":0.2}
                                    pos_hint: {'center_x': 0.5, 'center_y': 0.5}


                                MDLabel:
                                    text: "Bank Details"
                                    font_size:dp(12)
                                    bold: True
                                    theme_text_color: "Custom"
                                    text_color: 0, 0, 0, 1
                                    halign: "center"

                        MDBoxLayout:
                            orientation: 'vertical'
                            size_hint_y: None
                            height: dp(70)
                            md_bg_color: "#ffffff"
                            canvas.before:
                                Color:
                                    rgba: 0, 0, 0, 1
                                Line:
                                    width: 1.5
                                    rectangle: (self.x, self.y, self.width,self.height)
                            MDCard:
                                md_bg_color: "#ffffff"  # Customize background color
                                orientation: "vertical"
                                padding:dp(9), dp(3)
                                on_release:root.Edit_email()


                                Image:
                                    source: "icon11.png"
                                    size_hint: (0.4, 1)
                                    pos_hint:{"center_x":0.5,"center_y":0.2}
                                    pos_hint: {'center_x': 0.5, 'center_y': 0.5}


                                MDLabel:
                                    text: "Change User Email"
                                    font_size:dp(12)
                                    bold: True
                                    theme_text_color: "Custom"
                                    text_color: 0, 0, 0, 1
                                    halign: "center"

<ViewEmployeeScreen>:
    canvas.before:
        Color:
            rgba: 1, 1, 1, 1
        Rectangle:
            size: self.size
            pos: self.pos

    BoxLayout:
        orientation: 'vertical'
        size_hint: 1, 1
        pos_hint: {'center_x':0.5, 'center_y':0.5}
        MDTopAppBar:
            title: "Professional Information"
            elevation: 2
            pos_hint: {'top': 1}
            left_action_items: [['arrow-left', lambda x: root.on_back_button_press()]]
            right_action_items: [['refresh', lambda x: root.refresh()]]
            title_align: 'center'
            md_bg_color: 0.043, 0.145, 0.278, 1
        ScrollView:
            BoxLayout:
                orientation: "vertical"
                padding: dp(10)
                spacing: dp(10)
                size_hint_y: None
                height: self.minimum_height
                BoxLayout:
                    orientation: "vertical"
                    size_hint_y: None
                    height: self.minimum_height
                    padding: dp(0)
                    spacing: dp(10)
                    MDLabel:
                        text: ' '
                    MDLabel:
                        text: ' '
                    MDLabel:
                        text: ' '
                    BoxLayout:
                        orientation: "horizontal"
                        size_hint_y: None
                        height: dp(10)
                        spacing: dp(10)
                        padding:dp(7)

                        MDLabel:
                            text: ' Company name '
                            color: 0, 0, 0, 1
                            halign: 'left'
                            font_size: dp(13)
                            size_hint_x: 0.4
                            pos_hint: {'center_y': 0.5}
                            bold: True
                            multiline: False

                        MDLabel:
                            id: company_name
                            font_size: dp(13)
                            text:'Add company name'
                            size_hint: None, None
                            size_hint_x: 0.6
                            multiline: False
                            halign: 'left'
                            pos_hint: {'center_y': 0.5}

                Widget:
                    size_hint_y: None
                    height: dp(1)
                    canvas:
                        Color:
                            rgba: 0, 0, 0, 1
                        Line:
                            points: self.x, self.y, self.x + self.width, self.y

                BoxLayout:
                    orientation: "horizontal"
                    size_hint_y: None
                    height: dp(10)
                    spacing: dp(10)
                    padding:dp(7)

                    MDLabel:
                        text: ' Occupation type  '
                        color: 0, 0, 0, 1
                        font_size: dp(13)
                        halign: 'left'
                        size_hint_x: 0.4
                        pos_hint: {'center_y': 0.5}
                        bold: True
                        multiline: False

                    MDLabel:
                        id: occupation_type 
                        text:'Add occupation type '
                        size_hint: None, None
                        size_hint_x: 0.6
                        multiline: False
                        halign: 'left'
                        font_size: dp(13)
                        pos_hint: {'center_y': 0.5}

                Widget:
                    size_hint_y: None
                    height: dp(1)
                    canvas:
                        Color:
                            rgba: 0, 0, 0, 1
                        Line:
                            points: self.x, self.y, self.x + self.width, self.y

                BoxLayout:
                    orientation: "horizontal"
                    size_hint_y: None
                    height: dp(10)
                    spacing: dp(10)
                    padding:dp(7)

                    MDLabel:
                        text: ' Employment type '
                        color: 0, 0, 0, 1
                        font_size: dp(13)
                        halign: 'left'
                        size_hint_x: 0.4
                        pos_hint: {'center_y': 0.5}
                        bold: True
                        multiline: False

                    MDLabel:
                        id: employment_type
                        text:'Add employment type'
                        size_hint: None, None
                        size_hint_x: 0.6
                        multiline: False
                        halign: 'left'
                        font_size: dp(13)
                        pos_hint: {'center_y': 0.5}

                Widget:
                    size_hint_y: None
                    height: dp(1)
                    canvas:
                        Color:
                            rgba: 0, 0, 0, 1
                        Line:
                            points: self.x, self.y, self.x + self.width, self.y

                BoxLayout:
                    orientation: "horizontal"
                    size_hint_y: None
                    height: dp(10)
                    spacing: dp(10)
                    padding:dp(7)

                    MDLabel:
                        text: ' Organization type  '
                        color: 0, 0, 0, 1
                        halign: 'left'
                        font_size: dp(13)
                        size_hint_x: 0.4
                        pos_hint: {'center_y': 0.5}
                        bold: True
                        multiline: False

                    MDLabel:
                        id: organization_type 
                        text:'Add organization type '
                        size_hint: None, None
                        size_hint_x: 0.6
                        multiline: False
                        font_size: dp(13)
                        halign: 'left'
                        pos_hint: {'center_y': 0.5}

                Widget:
                    size_hint_y: None
                    height: dp(1)
                    canvas:
                        Color:
                            rgba: 0, 0, 0, 1
                        Line:
                            points: self.x, self.y, self.x + self.width, self.y


                BoxLayout:
                    orientation: "horizontal"
                    size_hint_y: None
                    height: dp(10)
                    spacing: dp(10)
                    padding:dp(7)

                    MDLabel:
                        text: ' Company address '
                        color: 0, 0, 0, 1
                        halign: 'left'
                        font_size: dp(13)
                        size_hint_x: 0.4
                        pos_hint: {'center_y': 0.5}
                        bold: True
                        multiline: False

                    MDLabel:
                        id: company_address
                        font_size: dp(13)
                        text:'Add company address'
                        size_hint: None, None
                        size_hint_x: 0.6
                        multiline: False
                        halign: 'left'
                        pos_hint: {'center_y': 0.5}

                Widget:
                    size_hint_y: None
                    height: dp(1)
                    canvas:
                        Color:
                            rgba: 0, 0, 0, 1
                        Line:
                            points: self.x, self.y, self.x + self.width, self.y

                BoxLayout:
                    orientation: "horizontal"
                    size_hint_y: None
                    height: dp(10)
                    spacing: dp(10)
                    padding:dp(7)

                    MDLabel:
                        text: ' Landmark '
                        color: 0, 0, 0, 1
                        halign: 'left'
                        font_size: dp(13)
                        size_hint_x: 0.4
                        pos_hint: {'center_y': 0.5}
                        bold: True
                        multiline: False

                    MDLabel:
                        id: landmark
                        font_size: dp(13)
                        text:'Add landmark'
                        size_hint: None, None
                        size_hint_x: 0.6
                        multiline: False
                        halign: 'left'
                        pos_hint: {'center_y': 0.5}

                Widget:
                    size_hint_y: None
                    height: dp(1)
                    canvas:
                        Color:
                            rgba: 0, 0, 0, 1
                        Line:
                            points: self.x, self.y, self.x + self.width, self.y

                BoxLayout:
                    orientation: "horizontal"
                    size_hint_y: None
                    height: dp(20)
                    spacing: dp(10)
                    padding:dp(7)

                    MDLabel:
                        text: ' Company phone \\n number '
                        color: 0, 0, 0, 1
                        halign: 'left'
                        font_size: dp(13)
                        size_hint_x: 0.4
                        pos_hint: {'center_y': 0.5}
                        bold: True
                        multiline: False

                    MDLabel:
                        id: company_phone_number
                        text:'Add company phone number'
                        size_hint: None, None
                        size_hint_x: 0.6
                        multiline: False
                        font_size: dp(13)
                        halign: 'left'
                        pos_hint: {'center_y': 0.5}

                Widget:
                    size_hint_y: None
                    height: dp(1)
                    canvas:
                        Color:
                            rgba: 0, 0, 0, 1
                        Line:
                            points: self.x, self.y, self.x + self.width, self.y


                BoxLayout:
                    orientation: "horizontal"
                    size_hint_y: None
                    height: dp(10)
                    spacing: dp(10)
                    padding:dp(7)

                    MDLabel:
                        text: " Annual salary "
                        color: 0, 0, 0, 1
                        halign: 'left'
                        font_size: dp(13)
                        size_hint_x: 0.4
                        pos_hint: {'center_y': 0.5}
                        bold: True
                        multiline: False

                    MDLabel:
                        id: annual_salary
                        font_size: dp(13)
                        text:"Add annual salary"
                        size_hint: None, None
                        size_hint_x: 0.6
                        multiline: False
                        halign: 'left'
                        pos_hint: {'center_y': 0.5}

                Widget:
                    size_hint_y: None
                    height: dp(1)
                    canvas:
                        Color:
                            rgba: 0, 0, 0, 1
                        Line:
                            points: self.x, self.y, self.x + self.width, self.y

                BoxLayout:
                    orientation: "horizontal"
                    size_hint_y: None
                    height: dp(10)
                    spacing: dp(10)
                    padding:dp(7)

                    MDLabel:
                        text: ' Salary type '
                        color: 0, 0, 0, 1
                        halign: 'left'
                        font_size: dp(13)
                        size_hint_x: 0.4
                        pos_hint: {'center_y': 0.5}
                        bold: True
                        multiline: False

                    MDLabel:
                        id: salary_type
                        font_size: dp(13)
                        text:'Add salary type'
                        size_hint: None, None
                        size_hint_x: 0.6
                        multiline: False
                        halign: 'left'
                        pos_hint: {'center_y': 0.5}

                Widget:
                    size_hint_y: None
                    height: dp(1)
                    canvas:
                        Color:
                            rgba: 0, 0, 0, 1
                        Line:
                            points: self.x, self.y, self.x + self.width, self.y

                BoxLayout:
                    orientation: "horizontal"
                    size_hint_y: None
                    height: dp(10)
                    spacing: dp(10)
                    padding:dp(7)

                    MDLabel:
                        text: ' Designation '
                        color: 0, 0, 0, 1
                        halign: 'left'
                        font_size: dp(13)
                        size_hint_x: 0.4
                        pos_hint: {'center_y': 0.5}
                        bold: True
                        multiline: False

                    MDLabel:
                        id: designation
                        text:'Add designation'
                        size_hint: None, None
                        size_hint_x: 0.6
                        multiline: False
                        font_size: dp(13)
                        halign: 'left'
                        pos_hint: {'center_y': 0.5}

                Widget:
                    size_hint_y: None
                    height: dp(1)
                    canvas:
                        Color:
                            rgba: 0, 0, 0, 1
                        Line:
                            points: self.x, self.y, self.x + self.width, self.y

                BoxLayout:
                    orientation: "horizontal"
                    size_hint_y: None
                    height: dp(60)
                    spacing: dp(10)
                    padding:dp(7)

                    MDLabel:
                        text: ' Employee id '
                        color: 0, 0, 0, 1
                        font_size: dp(13)
                        halign: 'left'
                        size_hint_x: 0.4
                        pos_hint: {'center_y': 0.5}
                        bold: True
                        multiline: False

                    Image:
                        id: employee_id
                        size: dp(50), dp(50)
                        source: ''


                Widget:
                    size_hint_y: None
                    height: dp(1)
                    canvas:
                        Color:
                            rgba: 0, 0, 0, 1
                        Line:
                            points: self.x, self.y, self.x + self.width, self.y

                BoxLayout:
                    orientation: "horizontal"
                    size_hint_y: None
                    height: dp(60)
                    spacing: dp(10)
                    padding:dp(7)

                    MDLabel:
                        text: ' Last six months \\n bank statement '
                        color: 0, 0, 0, 1
                        halign: 'left'
                        font_size: dp(13)
                        size_hint_x: 0.4
                        pos_hint: {'center_y': 0.5}
                        bold: True
                        multiline: False

                    Image:
                        id: last_six_months_bank_statement
                        size: dp(50), dp(50)
                        source: ''

                Widget:
                    size_hint_y: None
                    height: dp(1)
                    canvas:
                        Color:
                            rgba: 0, 0, 0, 1
                        Line:
                            points: self.x, self.y, self.x + self.width, self.y
                MDLabel:
                    text: ' '
                MDLabel:
                    text: ' '
                MDLabel:
                    text: ' '
                MDLabel:
                    text: ' '
                MDLabel:
                    text: ' '
                MDLabel:
                    text: ' '
                MDLabel:
                    text: ' '

                MDLabel:
                    text: ' '

                MDFloatLayout:
                    MDRaisedButton:
                        text: "Edit Profile"
                        md_bg_color: 0.043, 0.145, 0.278, 1
                        font_name: "Roboto-Bold"
                        size_hint: 0.4, None
                        height: dp(50)
                        on_release: root.on_employee_edit()
                        pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                        font_size: dp(15)
                MDLabel:
                    text: '  '
                MDLabel:
                    text: '  '

<ViewBusinessScreen1>:
    BoxLayout:
        orientation: 'vertical'
        MDTopAppBar:
            title: "Business Information"
            elevation: 2
            pos_hint: {'top': 1}
            left_action_items: [['arrow-left', lambda x: root.on_back_button_press()]]
            right_action_items: [['refresh', lambda x: root.refresh()]]
            title_align: 'center'
            md_bg_color: 0.043, 0.145, 0.278, 1
        BoxLayout:
            orientation: 'vertical'
            spacing: dp(10)
            padding: dp(20)
            height:dp(5)
            Image:
                source: 'icon9.png'
                size_hint: (None, None)
                size: dp(100), dp(100)
                pos_hint: {'center_x': 0.5}

            MDLabel:
                text: "Business details are not available."
                halign: "center"
                bold: True
                theme_text_color: "Custom"
                text_color: 0, 0, 0, 1
                font_size: dp(16)
                size_hint_y: None
                height: self.texture_size[1]

        MDLabel:
            text: ' '

<ViewProfessionalScreen>
    BoxLayout:
        orientation: 'vertical'
        MDTopAppBar:
            title: "Professional Information"
            elevation: 2
            pos_hint: {'top': 1}
            left_action_items: [['arrow-left', lambda x: root.on_back_button_press()]]
            right_action_items: [['refresh', lambda x: root.refresh()]]
            title_align: 'center'
            md_bg_color: 0.043, 0.145, 0.278, 1


        BoxLayout:
            orientation: 'vertical'
            spacing: dp(10)
            padding: dp(20)
            height:dp(5)
            Image:
                source: 'icon12.png'
                size_hint: (None, None)
                size: dp(100), dp(100)
                pos_hint: {'center_x': 0.5}

            MDLabel:
                text: "Professional details are not available."
                halign: "center"
                bold: True
                theme_text_color: "Custom"
                text_color: 0, 0, 0, 1
                font_size: dp(16)
                size_hint_y: None
                height: self.texture_size[1]
        MDLabel:
            text: ' '

<ViewBusinessScreen>
    canvas.before:
        Color:
            rgba: 1, 1, 1, 1
        Rectangle:
            size: self.size
            pos: self.pos

    BoxLayout:
        orientation: 'vertical'
        size_hint: 1, 1
        pos_hint: {'center_x':0.5, 'center_y':0.5}
        MDTopAppBar:
            title: "Business Information"
            elevation: 2
            pos_hint: {'top': 1}
            left_action_items: [['arrow-left', lambda x: root.on_back_button_press()]]
            right_action_items: [['refresh', lambda x: root.refresh()]]
            title_align: 'center'
            md_bg_color: 0.043, 0.145, 0.278, 1
        ScrollView:
            BoxLayout:
                orientation: "vertical"
                padding: dp(10)
                spacing: dp(10)
                size_hint_y: None
                height: self.minimum_height
                BoxLayout:
                    orientation: "vertical"
                    size_hint_y: None
                    height: self.minimum_height
                    padding: dp(0)
                    spacing: dp(10)
                    MDLabel:
                        text: ' '
                    MDLabel:
                        text: ' '
                    MDLabel:
                        text: ' '
                    BoxLayout:
                        orientation: "horizontal"
                        size_hint_y: None
                        height: dp(10)
                        spacing: dp(10)
                        padding:dp(7)

                        MDLabel:
                            text: ' Business name '
                            color: 0, 0, 0, 1
                            halign: 'left'
                            font_size: dp(13)
                            size_hint_x: 0.4
                            pos_hint: {'center_y': 0.5}
                            bold: True
                            multiline: False

                        MDLabel:
                            id: business_name
                            font_size: dp(13)
                            text:'Add business name'
                            size_hint: None, None
                            size_hint_x: 0.6
                            multiline: False
                            halign: 'left'
                            pos_hint: {'center_y': 0.5}

                Widget:
                    size_hint_y: None
                    height: dp(1)
                    canvas:
                        Color:
                            rgba: 0, 0, 0, 1
                        Line:
                            points: self.x, self.y, self.x + self.width, self.y

                BoxLayout:
                    orientation: "horizontal"
                    size_hint_y: None
                    height: dp(10)
                    spacing: dp(10)
                    padding:dp(7)

                    MDLabel:
                        text: ' Business address '
                        color: 0, 0, 0, 1
                        font_size: dp(13)
                        halign: 'left'
                        size_hint_x: 0.4
                        pos_hint: {'center_y': 0.5}
                        bold: True
                        multiline: False

                    MDLabel:
                        id: business_address
                        text:'Add business address'
                        size_hint: None, None
                        size_hint_x: 0.6
                        multiline: False
                        halign: 'left'
                        font_size: dp(13)
                        pos_hint: {'center_y': 0.5}

                Widget:
                    size_hint_y: None
                    height: dp(1)
                    canvas:
                        Color:
                            rgba: 0, 0, 0, 1
                        Line:
                            points: self.x, self.y, self.x + self.width, self.y

                BoxLayout:
                    orientation: "horizontal"
                    size_hint_y: None
                    height: dp(10)
                    spacing: dp(10)
                    padding:dp(7)

                    MDLabel:
                        text: ' Business type '
                        color: 0, 0, 0, 1
                        font_size: dp(13)
                        halign: 'left'
                        size_hint_x: 0.4
                        pos_hint: {'center_y': 0.5}
                        bold: True
                        multiline: False

                    MDLabel:
                        id: business_type
                        text:'Add business type'
                        size_hint: None, None
                        size_hint_x: 0.6
                        multiline: False
                        halign: 'left'
                        font_size: dp(13)
                        pos_hint: {'center_y': 0.5}

                Widget:
                    size_hint_y: None
                    height: dp(1)
                    canvas:
                        Color:
                            rgba: 0, 0, 0, 1
                        Line:
                            points: self.x, self.y, self.x + self.width, self.y

                BoxLayout:
                    orientation: "horizontal"
                    size_hint_y: None
                    height: dp(20)
                    spacing: dp(10)
                    padding:dp(7)

                    MDLabel:
                        text: ' No of Employees \\n Working '
                        color: 0, 0, 0, 1
                        halign: 'left'
                        font_size: dp(13)
                        size_hint_x: 0.4
                        pos_hint: {'center_y': 0.5}
                        bold: True
                        multiline: False

                    MDLabel:
                        id: no_working
                        text:'Add no of employees working'
                        size_hint: None, None
                        size_hint_x: 0.6
                        multiline: False
                        font_size: dp(13)
                        halign: 'left'
                        pos_hint: {'center_y': 0.5}

                Widget:
                    size_hint_y: None
                    height: dp(1)
                    canvas:
                        Color:
                            rgba: 0, 0, 0, 1
                        Line:
                            points: self.x, self.y, self.x + self.width, self.y


                BoxLayout:
                    orientation: "horizontal"
                    size_hint_y: None
                    height: dp(20)
                    spacing: dp(10)
                    padding:dp(7)

                    MDLabel:
                        text: ' Year of \\n Establishment '
                        color: 0, 0, 0, 1
                        halign: 'left'
                        font_size: dp(13)
                        size_hint_x: 0.4
                        pos_hint: {'center_y': 0.5}
                        bold: True
                        multiline: False

                    MDLabel:
                        id: year
                        font_size: dp(13)
                        text:'Add year of establishment'
                        size_hint: None, None
                        size_hint_x: 0.6
                        multiline: False
                        halign: 'left'
                        pos_hint: {'center_y': 0.5}

                Widget:
                    size_hint_y: None
                    height: dp(1)
                    canvas:
                        Color:
                            rgba: 0, 0, 0, 1
                        Line:
                            points: self.x, self.y, self.x + self.width, self.y

                BoxLayout:
                    orientation: "horizontal"
                    size_hint_y: None
                    height: dp(10)
                    spacing: dp(10)
                    padding:dp(7)

                    MDLabel:
                        text: ' Industry Type '
                        color: 0, 0, 0, 1
                        halign: 'left'
                        font_size: dp(13)
                        size_hint_x: 0.4
                        pos_hint: {'center_y': 0.5}
                        bold: True
                        multiline: False

                    MDLabel:
                        id: industry_type
                        font_size: dp(13)
                        text:'Add industry type'
                        size_hint: None, None
                        size_hint_x: 0.6
                        multiline: False
                        halign: 'left'
                        pos_hint: {'center_y': 0.5}

                Widget:
                    size_hint_y: None
                    height: dp(1)
                    canvas:
                        Color:
                            rgba: 0, 0, 0, 1
                        Line:
                            points: self.x, self.y, self.x + self.width, self.y

                BoxLayout:
                    orientation: "horizontal"
                    size_hint_y: None
                    height: dp(20)
                    spacing: dp(10)
                    padding:dp(7)

                    MDLabel:
                        text: ' Last six months \\n turnover '
                        color: 0, 0, 0, 1
                        halign: 'left'
                        font_size: dp(13)
                        size_hint_x: 0.4
                        pos_hint: {'center_y': 0.5}
                        bold: True
                        multiline: False

                    MDLabel:
                        id: last_six
                        text:'Add last six months turnover'
                        size_hint: None, None
                        size_hint_x: 0.6
                        multiline: False
                        font_size: dp(13)
                        halign: 'left'
                        pos_hint: {'center_y': 0.5}

                Widget:
                    size_hint_y: None
                    height: dp(1)
                    canvas:
                        Color:
                            rgba: 0, 0, 0, 1
                        Line:
                            points: self.x, self.y, self.x + self.width, self.y

                BoxLayout:
                    orientation: "horizontal"
                    size_hint_y: None
                    height: dp(60)
                    spacing: dp(10)
                    padding:dp(7)

                    MDLabel:
                        text: " last six month's \\n bank statements "
                        color: 0, 0, 0, 1
                        halign: 'left'
                        font_size: dp(13)
                        size_hint_x: 0.4
                        pos_hint: {'center_y': 0.5}
                        bold: True
                        multiline: False

                    Image:
                        id: six_bank
                        size: dp(50), dp(50)
                        source: ''

                Widget:
                    size_hint_y: None
                    height: dp(1)
                    canvas:
                        Color:
                            rgba: 0, 0, 0, 1
                        Line:
                            points: self.x, self.y, self.x + self.width, self.y

                BoxLayout:
                    orientation: "horizontal"
                    size_hint_y: None
                    height: dp(10)
                    spacing: dp(10)
                    padding:dp(7)

                    MDLabel:
                        text: ' DIN '
                        color: 0, 0, 0, 1
                        halign: 'left'
                        font_size: dp(13)
                        size_hint_x: 0.4
                        pos_hint: {'center_y': 0.5}
                        bold: True
                        multiline: False

                    MDLabel:
                        id: din
                        font_size: dp(13)
                        text:'Add din'
                        size_hint: None, None
                        size_hint_x: 0.6
                        multiline: False
                        halign: 'left'
                        pos_hint: {'center_y': 0.5}

                Widget:
                    size_hint_y: None
                    height: dp(1)
                    canvas:
                        Color:
                            rgba: 0, 0, 0, 1
                        Line:
                            points: self.x, self.y, self.x + self.width, self.y

                BoxLayout:
                    orientation: "horizontal"
                    size_hint_y: None
                    height: dp(10)
                    spacing: dp(10)
                    padding:dp(7)

                    MDLabel:
                        text: ' CIN '
                        color: 0, 0, 0, 1
                        halign: 'left'
                        font_size: dp(13)
                        size_hint_x: 0.4
                        pos_hint: {'center_y': 0.5}
                        bold: True
                        multiline: False

                    MDLabel:
                        id: cin
                        text:'Add cin'
                        size_hint: None, None
                        size_hint_x: 0.6
                        multiline: False
                        font_size: dp(13)
                        halign: 'left'
                        pos_hint: {'center_y': 0.5}

                Widget:
                    size_hint_y: None
                    height: dp(1)
                    canvas:
                        Color:
                            rgba: 0, 0, 0, 1
                        Line:
                            points: self.x, self.y, self.x + self.width, self.y

                BoxLayout:
                    orientation: "horizontal"
                    size_hint_y: None
                    height: dp(10)
                    spacing: dp(10)
                    padding:dp(7)

                    MDLabel:
                        text: ' Office address '
                        color: 0, 0, 0, 1
                        font_size: dp(13)
                        halign: 'left'
                        size_hint_x: 0.4
                        pos_hint: {'center_y': 0.5}
                        bold: True
                        multiline: False

                    MDLabel:
                        id: office_address
                        text:'Add office address'
                        size_hint: None, None
                        size_hint_x: 0.6
                        multiline: False
                        halign: 'left'
                        font_size: dp(13)
                        pos_hint: {'center_y': 0.5}

                Widget:
                    size_hint_y: None
                    height: dp(1)
                    canvas:
                        Color:
                            rgba: 0, 0, 0, 1
                        Line:
                            points: self.x, self.y, self.x + self.width, self.y

                BoxLayout:
                    orientation: "horizontal"
                    size_hint_y: None
                    height: dp(60)
                    spacing: dp(10)
                    padding:dp(7)

                    MDLabel:
                        text: ' Proof verification '
                        color: 0, 0, 0, 1
                        halign: 'left'
                        font_size: dp(13)
                        size_hint_x: 0.4
                        pos_hint: {'center_y': 0.5}
                        bold: True
                        multiline: False

                    Image:
                        id: proof
                        size: dp(50), dp(50)
                        source: ''

                Widget:
                    size_hint_y: None
                    height: dp(1)
                    canvas:
                        Color:
                            rgba: 0, 0, 0, 1
                        Line:
                            points: self.x, self.y, self.x + self.width, self.y


                MDLabel:
                    text: ' '
                MDLabel:
                    text: ' '
                MDLabel:
                    text: ' '
                MDLabel:
                    text: ' '
                MDLabel:
                    text: ' '
                MDLabel:
                    text: ' '

                MDFloatLayout:
                    MDRaisedButton:
                        text: "Edit Profile"
                        md_bg_color: 0.043, 0.145, 0.278, 1
                        font_name: "Roboto-Bold"
                        size_hint: 0.4, None
                        height: dp(50)
                        on_release: root.on_business_edit()
                        pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                        font_size: dp(15)
                MDLabel:
                    text: '  '
                MDLabel:
                    text: '  '

<ViewEditScreen5>
    canvas.before:
        Color:
            rgba: 1, 1, 1, 1
        Rectangle:
            size: self.size
            pos: self.pos

    BoxLayout:
        orientation: 'vertical'
        size_hint: 1, 1
        pos_hint: {'center_x':0.5, 'center_y':0.5}
        MDTopAppBar:
            title: "Business Information"
            elevation: 2
            pos_hint: {'top': 1}
            left_action_items: [['arrow-left', lambda x: root.on_back_button_press()]]
            right_action_items: [['refresh', lambda x: root.refresh()]]
            title_align: 'center'
            md_bg_color: 0.043, 0.145, 0.278, 1
        ScrollView:
            BoxLayout:
                orientation: "vertical"
                padding: dp(10)
                spacing: dp(10)
                size_hint_y: None
                height: self.minimum_height
                BoxLayout:
                    orientation: "vertical"
                    size_hint_y: None
                    height: self.minimum_height
                    padding: dp(0)
                    spacing: dp(10)
                    MDLabel:
                        text: ' '
                    MDLabel:
                        text: ' '
                    MDLabel:
                        text: ' '
                    BoxLayout:
                        orientation: "horizontal"
                        size_hint_y: None
                        height: dp(20)
                        spacing: dp(10)
                        padding:dp(7)

                        MDLabel:
                            text: ' Business name '
                            color: 0, 0, 0, 1
                            halign: 'left'
                            font_size: dp(13)
                            size_hint_x: 0.4
                            pos_hint: {'center_y': 0.5}
                            bold: True
                            multiline: False

                        MDTextField:
                            id: business_name
                            font_size: dp(13)
                            text:'Add business name'
                            size_hint: None, None
                            size_hint_x: 0.6
                            multiline: False
                            halign: 'left'
                            pos_hint: {'center_y': 0.5}


                BoxLayout:
                    orientation: "horizontal"
                    size_hint_y: None
                    height: dp(20)
                    spacing: dp(10)
                    padding:dp(7)

                    MDLabel:
                        text: ' Business address '
                        color: 0, 0, 0, 1
                        font_size: dp(13)
                        halign: 'left'
                        size_hint_x: 0.4
                        pos_hint: {'center_y': 0.5}
                        bold: True
                        multiline: False

                    MDTextField:
                        id: business_address
                        text:'Add business address'
                        size_hint: None, None
                        size_hint_x: 0.6
                        multiline: False
                        halign: 'left'
                        font_size: dp(13)
                        pos_hint: {'center_y': 0.5}


                BoxLayout:
                    orientation: "horizontal"
                    size_hint_y: None
                    height: dp(40)
                    spacing: dp(10)
                    padding:dp(7)

                    MDLabel:
                        text: ' Business type '
                        color: 0, 0, 0, 1
                        font_size: dp(13)
                        halign: 'left'
                        size_hint_x: 0.4
                        pos_hint: {'center_y': 0.5}
                        bold: True
                        multiline: False

                    Spinner:
                        id: business_type
                        text:'Add business type'
                        size_hint: None, None
                        size_hint_x: 0.6
                        multiline: False
                        width: dp(200)
                        text_size: self.width - dp(20), None
                        height:"30dp"
                        font_size: dp(13)
                        pos_hint: {'center_y': 0.5}
                        halign: "center"
                        background_color: 1, 1, 1, 0
                        color: 0, 0, 0, 1
                        canvas.before:
                            Color:
                                rgba: 0, 0, 0, 1  
                            Line:
                                width: 0.7
                                rounded_rectangle: (self.x, self.y, self.width, self.height, 15)


                BoxLayout:
                    orientation: "horizontal"
                    size_hint_y: None
                    height: dp(40)
                    spacing: dp(10)
                    padding:dp(7)

                    MDLabel:
                        text: ' No of Employees \\n Working '
                        color: 0, 0, 0, 1
                        halign: 'left'
                        font_size: dp(13)
                        size_hint_x: 0.4
                        pos_hint: {'center_y': 0.5}
                        bold: True
                        multiline: False

                    Spinner:
                        id: no_working
                        text:'Add no of employees working'
                        size_hint: None, None
                        size_hint_x: 0.6
                        multiline: False
                        width: dp(200)
                        text_size: self.width - dp(20), None
                        height:"30dp"
                        font_size: dp(13)
                        pos_hint: {'center_y': 0.5}
                        halign: "center"
                        background_color: 1, 1, 1, 0
                        color: 0, 0, 0, 1
                        canvas.before:
                            Color:
                                rgba: 0, 0, 0, 1  
                            Line:
                                width: 0.7
                                rounded_rectangle: (self.x, self.y, self.width, self.height, 15)



                BoxLayout:
                    orientation: "horizontal"
                    size_hint_y: None
                    height: dp(30)
                    spacing: dp(10)
                    padding:dp(7)

                    MDLabel:
                        text: ' Year of \\n Establishment '
                        color: 0, 0, 0, 1
                        halign: 'left'
                        font_size: dp(13)
                        size_hint_x: 0.4
                        pos_hint: {'center_y': 0.5}
                        bold: True
                        multiline: False

                    MDTextField:
                        id: year
                        font_size: dp(13)
                        text:'Add year of establishment'
                        size_hint: None, None
                        size_hint_x: 0.6
                        multiline: False
                        halign: 'left'
                        pos_hint: {'center_y': 0.5}


                BoxLayout:
                    orientation: "horizontal"
                    size_hint_y: None
                    height: dp(20)
                    spacing: dp(10)
                    padding:dp(7)

                    MDLabel:
                        text: ' Industry Type '
                        color: 0, 0, 0, 1
                        halign: 'left'
                        font_size: dp(13)
                        size_hint_x: 0.4
                        pos_hint: {'center_y': 0.5}
                        bold: True
                        multiline: False

                    MDTextField:
                        id: industry_type
                        font_size: dp(13)
                        text:'Add industry type'
                        size_hint: None, None
                        size_hint_x: 0.6
                        multiline: False
                        halign: 'left'
                        pos_hint: {'center_y': 0.5}


                BoxLayout:
                    orientation: "horizontal"
                    size_hint_y: None
                    height: dp(30)
                    spacing: dp(10)
                    padding:dp(7)

                    MDLabel:
                        text: ' Last six months \\n turnover '
                        color: 0, 0, 0, 1
                        halign: 'left'
                        font_size: dp(13)
                        size_hint_x: 0.4
                        pos_hint: {'center_y': 0.5}
                        bold: True
                        multiline: False

                    MDTextField:
                        id: last_six
                        text:'Add last six months turnover'
                        size_hint: None, None
                        size_hint_x: 0.6
                        multiline: False
                        font_size: dp(13)
                        halign: 'left'
                        pos_hint: {'center_y': 0.5}

                BoxLayout:
                    orientation: "horizontal"
                    size_hint_y: None
                    height: dp(60)
                    spacing: dp(10)
                    padding:dp(7)

                    MDLabel:
                        text: " last six month's \\n bank statements "
                        color: 0, 0, 0, 1
                        halign: 'left'
                        font_size: dp(13)
                        size_hint_x: 0.4
                        pos_hint: {'center_y': 0.5}
                        bold: True
                        multiline: False

                    Image:
                        id: six_bank
                        size: dp(50), dp(50)
                        source: ''

                    MDIconButton:
                        icon: 'upload'
                        on_release: app.root.get_screen('ViewEditScreen5').check_and_open_file_manager1()

                BoxLayout:
                    orientation: "horizontal"
                    size_hint_y: None
                    height: dp(20)
                    spacing: dp(10)
                    padding:dp(7)

                    MDLabel:
                        text: ' DIN '
                        color: 0, 0, 0, 1
                        halign: 'left'
                        font_size: dp(13)
                        size_hint_x: 0.4
                        pos_hint: {'center_y': 0.5}
                        bold: True
                        multiline: False

                    MDTextField:
                        id: din
                        font_size: dp(13)
                        text:'Add din'
                        size_hint: None, None
                        size_hint_x: 0.6
                        multiline: False
                        halign: 'left'
                        pos_hint: {'center_y': 0.5}

                BoxLayout:
                    orientation: "horizontal"
                    size_hint_y: None
                    height: dp(20)
                    spacing: dp(10)
                    padding:dp(7)

                    MDLabel:
                        text: ' CIN '
                        color: 0, 0, 0, 1
                        halign: 'left'
                        font_size: dp(13)
                        size_hint_x: 0.4
                        pos_hint: {'center_y': 0.5}
                        bold: True
                        multiline: False

                    MDTextField:
                        id: cin
                        text:'Add cin'
                        size_hint: None, None
                        size_hint_x: 0.6
                        multiline: False
                        font_size: dp(13)
                        halign: 'left'
                        pos_hint: {'center_y': 0.5}

                BoxLayout:
                    orientation: "horizontal"
                    size_hint_y: None
                    height: dp(20)
                    spacing: dp(10)
                    padding:dp(7)

                    MDLabel:
                        text: ' Office address '
                        color: 0, 0, 0, 1
                        font_size: dp(13)
                        halign: 'left'
                        size_hint_x: 0.4
                        pos_hint: {'center_y': 0.5}
                        bold: True
                        multiline: False

                    MDTextField:
                        id: office_address
                        text:'Add office address'
                        size_hint: None, None
                        size_hint_x: 0.6
                        multiline: False
                        halign: 'left'
                        font_size: dp(13)
                        pos_hint: {'center_y': 0.5}

                BoxLayout:
                    orientation: "horizontal"
                    size_hint_y: None
                    height: dp(60)
                    spacing: dp(10)
                    padding:dp(7)

                    MDLabel:
                        text: ' Proof verification '
                        color: 0, 0, 0, 1
                        halign: 'left'
                        font_size: dp(13)
                        size_hint_x: 0.4
                        pos_hint: {'center_y': 0.5}
                        bold: True
                        multiline: False

                    Image:
                        id: proof
                        size: dp(50), dp(50)
                        source: ''

                    MDIconButton:
                        icon: 'upload'
                        on_release:app.root.get_screen('ViewEditScreen5').check_and_open_file_manager2()

                MDLabel:
                    text: ' '
                MDLabel:
                    text: ' '
                MDLabel:
                    text: ' '

                MDFloatLayout:
                    MDRaisedButton:
                        text: "Save Profile"
                        md_bg_color: 0.043, 0.145, 0.278, 1
                        font_name: "Roboto-Bold"
                        size_hint: 0.4, None
                        height: dp(50)
                        on_release: root.on_business_save()
                        pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                        font_size: dp(15)
                MDLabel:
                    text: '  '
                MDLabel:
                    text: '  '

<ViewProfileScreen>
    canvas.before:
        Color:
            rgba: 1, 1, 1, 1
        Rectangle:
            size: self.size
            pos: self.pos

    BoxLayout:
        orientation: 'vertical'
        size_hint: 1, 1
        pos_hint: {'center_x':0.5, 'center_y':0.5}
        MDTopAppBar:
            title: "Profile Information"
            elevation: 2
            pos_hint: {'top': 1}
            left_action_items: [['arrow-left', lambda x: root.on_back_button_press()]]
            right_action_items: [['refresh', lambda x: root.refresh()]]
            title_align: 'center'
            md_bg_color: 0.043, 0.145, 0.278, 1

        ScrollView:  # Add ScrollView here
            do_scroll_x: False
            BoxLayout:
                orientation: "vertical"
                padding: dp(0)
                spacing: dp(10)
                size_hint_y: None
                height: self.minimum_height

                BoxLayout:
                    orientation: "vertical"
                    size_hint_y: None
                    height: self.minimum_height
                    padding: dp(0)
                    spacing: dp(10)
                    MDLabel:
                        text: ' '
                    MDLabel:
                        text: ' '
                    MDLabel:
                        text: ' '
                    BoxLayout:
                        orientation: "horizontal"
                        size_hint_y: None
                        height: dp(10)
                        spacing: dp(5)
                        padding:dp(7)

                        MDLabel:
                            text: ' Investment '
                            color: 0, 0, 0, 1
                            halign: 'left'
                            font_size: dp(13)
                            size_hint_x: 0.4
                            pos_hint: {'center_y': 0.5}
                            bold: True
                            multiline: False

                        MDLabel:
                            id: investment
                            font_size: dp(13)
                            text:'Add investment'
                            size_hint: None, None
                            size_hint_x: 0.6
                            multiline: False
                            halign: 'left'
                            pos_hint: {'center_y': 0.5}

                Widget:
                    size_hint_y: None
                    height: dp(1)
                    canvas:
                        Color:
                            rgba: 0, 0, 0, 1
                        Line:
                            points: self.x, self.y, self.x + self.width, self.y

                BoxLayout:
                    orientation: "vertical"
                    size_hint_y: None
                    height: self.minimum_height
                    padding: dp(0)
                    spacing: dp(10)

                    BoxLayout:
                        orientation: "horizontal"
                        size_hint_y: None
                        height: dp(10)
                        spacing: dp(5)
                        padding:dp(7)

                        MDLabel:
                            text: ' Membership type '
                            color: 0, 0, 0, 1
                            halign: 'left'
                            font_size: dp(13)
                            size_hint_x: 0.4
                            pos_hint: {'center_y': 0.5}
                            bold: True
                            multiline: False

                        MDLabel:
                            id: membership_type
                            font_size: dp(13)
                            text:'Add membership type'
                            size_hint: None, None
                            size_hint_x: 0.6
                            multiline: False
                            halign: 'left'
                            pos_hint: {'center_y': 0.5}

                Widget:
                    size_hint_y: None
                    height: dp(1)
                    canvas:
                        Color:
                            rgba: 0, 0, 0, 1
                        Line:
                            points: self.x, self.y, self.x + self.width, self.y

                BoxLayout:
                    orientation: "vertical"
                    size_hint_y: None
                    height: self.minimum_height
                    padding: dp(0)
                    spacing: dp(10)

                    BoxLayout:
                        orientation: "horizontal"
                        size_hint_y: None
                        height: dp(10)
                        spacing: dp(5)
                        padding:dp(7)

                        MDLabel:
                            text: ' Lender returns '
                            color: 0, 0, 0, 1
                            halign: 'left'
                            font_size: dp(13)
                            size_hint_x: 0.4
                            pos_hint: {'center_y': 0.5}
                            bold: True
                            multiline: False

                        MDLabel:
                            id: return_on_investment
                            font_size: dp(13)
                            text:'Add lender returns'
                            size_hint: None, None
                            size_hint_x: 0.6
                            multiline: False
                            halign: 'left'
                            pos_hint: {'center_y': 0.5}

                Widget:
                    size_hint_y: None
                    height: dp(1)
                    canvas:
                        Color:
                            rgba: 0, 0, 0, 1
                        Line:
                            points: self.x, self.y, self.x + self.width, self.y

                BoxLayout:
                    orientation: "vertical"
                    size_hint_y: None
                    height: self.minimum_height
                    padding: dp(0)
                    spacing: dp(10)

                    BoxLayout:
                        orientation: "horizontal"
                        size_hint_y: None
                        height: dp(10)
                        spacing: dp(5)
                        padding:dp(7)

                        MDLabel:
                            text: ' Lending period '
                            color: 0, 0, 0, 1
                            halign: 'left'
                            font_size: dp(13)
                            size_hint_x: 0.4
                            pos_hint: {'center_y': 0.5}
                            bold: True
                            multiline: False

                        MDLabel:
                            id: lending_period
                            font_size: dp(13)
                            text:'Add lending period'
                            size_hint: None, None
                            size_hint_x: 0.6
                            multiline: False
                            halign: 'left'
                            pos_hint: {'center_y': 0.5}

                Widget:
                    size_hint_y: None
                    height: dp(1)
                    canvas:
                        Color:
                            rgba: 0, 0, 0, 1
                        Line:
                            points: self.x, self.y, self.x + self.width, self.y


<ViewBankScreen>
    canvas.before:
        Color:
            rgba: 1, 1, 1, 1
        Rectangle:
            size: self.size
            pos: self.pos

    BoxLayout:
        orientation: 'vertical'
        size_hint: 1, 1
        pos_hint: {'center_x':0.5, 'center_y':0.5}
        MDTopAppBar:
            title: "Bank Information"
            elevation: 2
            pos_hint: {'top': 1}
            left_action_items: [['arrow-left', lambda x: root.on_back_button_press()]]
            right_action_items: [['refresh', lambda x: root.refresh()]]
            title_align: 'center'
            md_bg_color: 0.043, 0.145, 0.278, 1

        ScrollView:  # Add ScrollView here
            do_scroll_x: False
            BoxLayout:
                orientation: "vertical"
                padding: dp(10)
                spacing: dp(10)
                size_hint_y: None
                height: self.minimum_height

                BoxLayout:
                    orientation: "vertical"
                    size_hint_y: None
                    height: self.minimum_height
                    padding: dp(0)
                    spacing: dp(10)
                    MDLabel:
                        text: ' '
                    MDLabel:
                        text: ' '
                    MDLabel:
                        text: ' '
                    BoxLayout:
                        orientation: "horizontal"
                        size_hint_y: None
                        height: dp(20)
                        spacing: dp(10)
                        padding:dp(7)

                        MDLabel:
                            text: ' Account holder \\n name '
                            color: 0, 0, 0, 1
                            halign: 'left'
                            font_size: dp(13)
                            size_hint_x: 0.4
                            pos_hint: {'center_y': 0.5}
                            bold: True
                            multiline: False

                        MDLabel:
                            id: holder
                            font_size: dp(13)
                            text:'Add Account holder name'
                            size_hint: None, None
                            size_hint_x: 0.6
                            multiline: False
                            halign: 'left'
                            pos_hint: {'center_y': 0.5}

                Widget:
                    size_hint_y: None
                    height: dp(1)
                    canvas:
                        Color:
                            rgba: 0, 0, 0, 1
                        Line:
                            points: self.x, self.y, self.x + self.width, self.y

                BoxLayout:
                    orientation: "vertical"
                    size_hint_y: None
                    height: self.minimum_height
                    padding: dp(0)
                    spacing: dp(10)

                    BoxLayout:
                        orientation: "horizontal"
                        size_hint_y: None
                        height: dp(10)
                        spacing: dp(10)
                        padding:dp(7)

                        MDLabel:
                            text: ' Account type '
                            color: 0, 0, 0, 1
                            halign: 'left'
                            font_size: dp(13)
                            size_hint_x: 0.4
                            pos_hint: {'center_y': 0.5}
                            bold: True
                            multiline: False

                        MDLabel:
                            id: account_type
                            font_size: dp(13)
                            text:'Add account type'
                            size_hint: None, None
                            size_hint_x: 0.6
                            multiline: False
                            halign: 'left'
                            pos_hint: {'center_y': 0.5}

                Widget:
                    size_hint_y: None
                    height: dp(1)
                    canvas:
                        Color:
                            rgba: 0, 0, 0, 1
                        Line:
                            points: self.x, self.y, self.x + self.width, self.y

                BoxLayout:
                    orientation: "vertical"
                    size_hint_y: None
                    height: self.minimum_height
                    padding: dp(0)
                    spacing: dp(10)

                    BoxLayout:
                        orientation: "horizontal"
                        size_hint_y: None
                        height: dp(10)
                        spacing: dp(10)
                        padding:dp(7)

                        MDLabel:
                            text: ' Account number '
                            color: 0, 0, 0, 1
                            halign: 'left'
                            font_size: dp(13)
                            size_hint_x: 0.4
                            pos_hint: {'center_y': 0.5}
                            bold: True
                            multiline: False

                        MDLabel:
                            id: account_number
                            font_size: dp(13)
                            text:'Add account number'
                            size_hint: None, None
                            size_hint_x: 0.6
                            multiline: False
                            halign: 'left'
                            pos_hint: {'center_y': 0.5}

                Widget:
                    size_hint_y: None
                    height: dp(1)
                    canvas:
                        Color:
                            rgba: 0, 0, 0, 1
                        Line:
                            points: self.x, self.y, self.x + self.width, self.y

                BoxLayout:
                    orientation: "vertical"
                    size_hint_y: None
                    height: self.minimum_height
                    padding: dp(0)
                    spacing: dp(10)

                    BoxLayout:
                        orientation: "horizontal"
                        size_hint_y: None
                        height: dp(10)
                        spacing: dp(10)
                        padding:dp(7)

                        MDLabel:
                            text: ' Bank name '
                            color: 0, 0, 0, 1
                            halign: 'left'
                            font_size: dp(13)
                            size_hint_x: 0.4
                            pos_hint: {'center_y': 0.5}
                            bold: True
                            multiline: False

                        MDLabel:
                            id: bank_name
                            font_size: dp(13)
                            text:'Add bank name'
                            size_hint: None, None
                            size_hint_x: 0.6
                            multiline: False
                            halign: 'left'
                            pos_hint: {'center_y': 0.5}

                Widget:
                    size_hint_y: None
                    height: dp(1)
                    canvas:
                        Color:
                            rgba: 0, 0, 0, 1
                        Line:
                            points: self.x, self.y, self.x + self.width, self.y

                BoxLayout:
                    orientation: "vertical"
                    size_hint_y: None
                    height: self.minimum_height
                    padding: dp(0)
                    spacing: dp(10)

                    BoxLayout:
                        orientation: "horizontal"
                        size_hint_y: None
                        height: dp(10)
                        spacing: dp(10)
                        padding:dp(7)

                        MDLabel:
                            text: ' Bank id '
                            color: 0, 0, 0, 1
                            halign: 'left'
                            font_size: dp(13)
                            size_hint_x: 0.4
                            pos_hint: {'center_y': 0.5}
                            bold: True
                            multiline: False

                        MDLabel:
                            id: bank_id
                            font_size: dp(13)
                            text:'Add bank id'
                            size_hint: None, None
                            size_hint_x: 0.6
                            multiline: False
                            halign: 'left'
                            pos_hint: {'center_y': 0.5}

                Widget:
                    size_hint_y: None
                    height: dp(1)
                    canvas:
                        Color:
                            rgba: 0, 0, 0, 1
                        Line:
                            points: self.x, self.y, self.x + self.width, self.y

                BoxLayout:
                    orientation: "vertical"
                    size_hint_y: None
                    height: self.minimum_height
                    padding: dp(0)
                    spacing: dp(10)

                    BoxLayout:
                        orientation: "horizontal"
                        size_hint_y: None
                        height: dp(10)
                        spacing: dp(10)
                        padding:dp(7)

                        MDLabel:
                            text: ' Branch name '
                            color: 0, 0, 0, 1
                            halign: 'left'
                            font_size: dp(13)
                            size_hint_x: 0.4
                            pos_hint: {'center_y': 0.5}
                            bold: True
                            multiline: False

                        MDLabel:
                            id: branch_name
                            font_size: dp(13)
                            text:'Add branch name'
                            size_hint: None, None
                            size_hint_x: 0.6
                            multiline: False
                            halign: 'left'
                            pos_hint: {'center_y': 0.5}

                Widget:
                    size_hint_y: None
                    height: dp(1)
                    canvas:
                        Color:
                            rgba: 0, 0, 0, 1
                        Line:
                            points: self.x, self.y, self.x + self.width, self.y
                MDLabel:
                    text: ' '
                MDLabel:
                    text: ' '
                MDLabel:
                    text: ' '
                MDLabel:
                    text: ' '
                MDLabel:
                    text: ' '
                MDLabel:
                    text: ' '
                MDLabel:
                    text: ' '
                MDLabel:
                    text: ' '
                MDLabel:
                    text: ' '
                MDLabel:
                    text: ' '
                MDLabel:
                    text: ' '
                MDLabel:
                    text: ' '
                MDLabel:
                    text: ' '
                MDLabel:
                    text: ' '
                MDLabel:
                    text: ' '
                MDLabel:
                    text: ' '
                MDLabel:
                    text: ' '
                MDLabel:
                    text: ' '
                MDLabel:
                    text: ' '
                MDLabel:
                    text: ' '
                MDLabel:
                    text: ' '
                MDLabel:
                    text: ' '
                MDLabel:
                    text: ' '
                MDLabel:
                    text: ' '
                MDLabel:
                    text: ' '
                MDLabel:
                    text: ' '
                MDLabel:
                    text: ' '

                MDFloatLayout:
                    MDRaisedButton:
                        text: "Edit Profile"
                        md_bg_color: 0.043, 0.145, 0.278, 1
                        font_name: "Roboto-Bold"
                        size_hint: 0.4, None
                        height: dp(50)
                        on_release: root.on_bank_edit()
                        pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                        font_size: dp(15)
                MDLabel:
                    text: '  '
                MDLabel:
                    text: '  '

<ViewEditScreen6>
    canvas.before:
        Color:
            rgba: 1, 1, 1, 1
        Rectangle:
            size: self.size
            pos: self.pos

    BoxLayout:
        orientation: 'vertical'
        size_hint: 1, 1
        pos_hint: {'center_x':0.5, 'center_y':0.5}
        MDTopAppBar:
            title: "Bank Information"
            elevation: 2
            pos_hint: {'top': 1}
            left_action_items: [['arrow-left', lambda x: root.on_back_button_press()]]
            right_action_items: [['refresh', lambda x: root.refresh()]]
            title_align: 'center'
            md_bg_color: 0.043, 0.145, 0.278, 1

        ScrollView:  # Add ScrollView here
            do_scroll_x: False
            BoxLayout:
                orientation: "vertical"
                padding: dp(10)
                spacing: dp(10)
                size_hint_y: None
                height: self.minimum_height

                BoxLayout:
                    orientation: "vertical"
                    size_hint_y: None
                    height: self.minimum_height
                    padding: dp(0)
                    spacing: dp(10)
                    MDLabel:
                        text: ' '
                    MDLabel:
                        text: ' '
                    MDLabel:
                        text: ' '
                    BoxLayout:
                        orientation: "horizontal"
                        size_hint_y: None
                        height: dp(30)
                        spacing: dp(10)
                        padding:dp(7)

                        MDLabel:
                            text: ' Account holder \\n name '
                            color: 0, 0, 0, 1
                            halign: 'left'
                            font_size: dp(13)
                            size_hint_x: 0.4
                            pos_hint: {'center_y': 0.5}
                            bold: True
                            multiline: False

                        MDTextField:
                            id: holder
                            font_size: dp(13)
                            text:'Add Account holder name'
                            size_hint: None, None
                            size_hint_x: 0.6
                            multiline: False
                            halign: 'left'
                            pos_hint: {'center_y': 0.5}
                MDLabel:
                    text: ' '
                BoxLayout:
                    orientation: "vertical"
                    size_hint_y: None
                    height: self.minimum_height
                    padding: dp(0)
                    spacing: dp(10)

                    BoxLayout:
                        orientation: "horizontal"
                        size_hint_y: None
                        height: dp(20)
                        spacing: dp(10)
                        padding:dp(7)

                        MDLabel:
                            text: ' Account type '
                            color: 0, 0, 0, 1
                            halign: 'left'
                            font_size: dp(13)
                            size_hint_x: 0.4
                            pos_hint: {'center_y': 0.5}
                            bold: True
                            multiline: False

                        Spinner:
                            id: account_type
                            text:'Add account type'
                            size_hint: None, None
                            size_hint_x: 0.6
                            multiline: False
                            width: dp(200)
                            text_size: self.width - dp(20), None
                            height:"30dp"
                            font_size: dp(13)
                            pos_hint: {'center_y': 0.5}
                            halign: "center"
                            background_color: 1, 1, 1, 0
                            color: 0, 0, 0, 1
                            canvas.before:
                                Color:
                                    rgba: 0, 0, 0, 1  
                                Line:
                                    width: 0.7
                                    rounded_rectangle: (self.x, self.y, self.width, self.height, 15)

                BoxLayout:
                    orientation: "vertical"
                    size_hint_y: None
                    height: self.minimum_height
                    padding: dp(0)
                    spacing: dp(10)

                    BoxLayout:
                        orientation: "horizontal"
                        size_hint_y: None
                        height: dp(20)
                        spacing: dp(10)
                        padding:dp(7)

                        MDLabel:
                            text: ' Account number '
                            color: 0, 0, 0, 1
                            halign: 'left'
                            font_size: dp(13)
                            size_hint_x: 0.4
                            pos_hint: {'center_y': 0.5}
                            bold: True
                            multiline: False

                        MDTextField:
                            id: account_number
                            font_size: dp(13)
                            text:'Add account number'
                            size_hint: None, None
                            size_hint_x: 0.6
                            multiline: False
                            halign: 'left'
                            pos_hint: {'center_y': 0.5}

                BoxLayout:
                    orientation: "vertical"
                    size_hint_y: None
                    height: self.minimum_height
                    padding: dp(0)
                    spacing: dp(10)

                    BoxLayout:
                        orientation: "horizontal"
                        size_hint_y: None
                        height: dp(20)
                        spacing: dp(10)
                        padding:dp(7)

                        MDLabel:
                            text: ' Bank name '
                            color: 0, 0, 0, 1
                            halign: 'left'
                            font_size: dp(13)
                            size_hint_x: 0.4
                            pos_hint: {'center_y': 0.5}
                            bold: True
                            multiline: False

                        MDTextField:
                            id: bank_name
                            font_size: dp(13)
                            text:'Add bank name'
                            size_hint: None, None
                            size_hint_x: 0.6
                            multiline: False
                            halign: 'left'
                            pos_hint: {'center_y': 0.5}

                BoxLayout:
                    orientation: "vertical"
                    size_hint_y: None
                    height: self.minimum_height
                    padding: dp(0)
                    spacing: dp(10)

                    BoxLayout:
                        orientation: "horizontal"
                        size_hint_y: None
                        height: dp(20)
                        spacing: dp(10)
                        padding:dp(7)

                        MDLabel:
                            text: ' Bank id '
                            color: 0, 0, 0, 1
                            halign: 'left'
                            font_size: dp(13)
                            size_hint_x: 0.4
                            pos_hint: {'center_y': 0.5}
                            bold: True
                            multiline: False

                        MDTextField:
                            id: bank_id
                            font_size: dp(13)
                            text:'Add bank id'
                            size_hint: None, None
                            size_hint_x: 0.6
                            multiline: False
                            halign: 'left'
                            pos_hint: {'center_y': 0.5}

                BoxLayout:
                    orientation: "vertical"
                    size_hint_y: None
                    height: self.minimum_height
                    padding: dp(0)
                    spacing: dp(10)

                    BoxLayout:
                        orientation: "horizontal"
                        size_hint_y: None
                        height: dp(20)
                        spacing: dp(10)
                        padding:dp(7)

                        MDLabel:
                            text: ' Branch name '
                            color: 0, 0, 0, 1
                            halign: 'left'
                            font_size: dp(13)
                            size_hint_x: 0.4
                            pos_hint: {'center_y': 0.5}
                            bold: True
                            multiline: False

                        MDTextField:
                            id: branch_name
                            font_size: dp(13)
                            text:'Add branch name'
                            size_hint: None, None
                            size_hint_x: 0.6
                            multiline: False
                            halign: 'left'
                            pos_hint: {'center_y': 0.5}

                MDLabel:
                    text: ' '
                MDLabel:
                    text: ' '
                MDLabel:
                    text: ' '
                MDLabel:
                    text: ' '
                MDLabel:
                    text: ' '

                MDLabel:
                    text: ' '
                MDLabel:
                    text: ' '
                MDLabel:
                    text: ' '
                MDLabel:
                    text: ' '
                MDLabel:
                    text: ' '
                MDLabel:
                    text: ' '
                MDLabel:
                    text: ' '
                MDLabel:
                    text: ' '
                MDLabel:
                    text: ' '
                MDLabel:
                    text: ' '
                MDLabel:
                    text: ' '
                MDLabel:
                    text: ' '
                MDLabel:
                    text: ' '
                MDLabel:
                    text: ' '
                MDLabel:
                    text: ' '
                MDLabel:
                    text: ' '
                MDLabel:
                    text: ' '
                MDFloatLayout:
                    MDRaisedButton:
                        text: "Save Profile"
                        md_bg_color: 0.043, 0.145, 0.278, 1
                        font_name: "Roboto-Bold"
                        size_hint: 0.4, None
                        height: dp(50)
                        on_release: root.on_bank_save()
                        pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                        font_size: dp(15)
                MDLabel:
                    text: '  '
                MDLabel:
                    text: '  '

<ViewPersonalScreen>
    canvas.before:
        Color:
            rgba: 1, 1, 1, 1
        Rectangle:
            size: self.size
            pos: self.pos

    BoxLayout:
        orientation: 'vertical'
        size_hint: 1, 1
        pos_hint: {'center_x':0.5, 'center_y':0.5}
        MDTopAppBar:
            title: "Personal Information"
            elevation: 2
            pos_hint: {'top': 1}
            left_action_items: [['arrow-left', lambda x: root.on_back_button_press()]]
            right_action_items: [['refresh', lambda x: root.refresh()]]
            title_align: 'center'
            md_bg_color: 0.043, 0.145, 0.278, 1

        ScrollView:  # Add ScrollView here
            do_scroll_x: False
            BoxLayout:
                orientation: "vertical"
                padding: dp(10)
                spacing: dp(10)
                size_hint_y: None
                height: self.minimum_height

                MDFloatLayout:
                    size_hint_y: None
                    height: dp(120)
                    padding: dp(20)
                    spacing: dp(10)


                    MDFloatLayout:
                        size_hint: None, None
                        size: dp(70), dp(70)
                        pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                        radius: 70
                        canvas.before:
                            Color:
                                rgba: 1, 1, 1, 1
                            Ellipse:
                                size: self.size
                                pos: self.pos
                        Image:
                            id: selected_image1
                            size_hint: None, None
                            size: dp(80), dp(80)  # Make sure the size is a perfect square for a circular shape
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

                        MDIconButton:
                            icon: 'camera'
                            source: ""
                            pos_hint: {'center_x': 1.1, 'center_y': 0.}
                            on_release: app.root.get_screen('ViewPersonalScreen').check_and_open_file_manager1()

                Label:
                    id: selected_file_label
                    color: 0, 0, 0, 1
                    text: 'Upload Photo'
                    size_hint_y: None
                    height: dp(10)

                Widget:
                    size_hint_y: None
                    height: dp(1)
                    canvas:
                        Color:
                            rgba: 0, 0, 0, 1
                        Line:
                            points: self.x, self.y, self.x + self.width, self.y


                BoxLayout:
                    orientation: "vertical"
                    size_hint_y: None
                    height: self.minimum_height
                    padding: dp(0)
                    spacing: dp(10)

                    BoxLayout:
                        orientation: "horizontal"
                        size_hint_y: None
                        height: dp(10)
                        spacing: dp(10)
                        padding:dp(7)

                        MDLabel:
                            text: ' Full Name '
                            color: 0, 0, 0, 1
                            halign: 'left'
                            font_size: dp(13)
                            size_hint_x: 0.4
                            pos_hint: {'center_y': 0.5}
                            bold: True
                            multiline: False

                        MDLabel:
                            id: name
                            font_size: dp(13)
                            text:'Add full name'
                            size_hint: None, None
                            size_hint_x: 0.6
                            multiline: False
                            halign: 'left'
                            pos_hint: {'center_y': 0.5}

                Widget:
                    size_hint_y: None
                    height: dp(1)
                    canvas:
                        Color:
                            rgba: 0, 0, 0, 1
                        Line:
                            points: self.x, self.y, self.x + self.width, self.y

                BoxLayout:
                    orientation: "horizontal"
                    size_hint_y: None
                    height: dp(10)
                    spacing: dp(10)
                    padding:dp(7)

                    MDLabel:
                        text: ' Gender '
                        color: 0, 0, 0, 1
                        font_size: dp(13)
                        halign: 'left'
                        size_hint_x: 0.4
                        pos_hint: {'center_y': 0.5}
                        bold: True
                        multiline: False

                    MDLabel:
                        id: gender
                        text:'Add gender'
                        size_hint: None, None
                        size_hint_x: 0.6
                        multiline: False
                        halign: 'left'
                        font_size: dp(13)
                        pos_hint: {'center_y': 0.5}

                Widget:
                    size_hint_y: None
                    height: dp(1)
                    canvas:
                        Color:
                            rgba: 0, 0, 0, 1
                        Line:
                            points: self.x, self.y, self.x + self.width, self.y

                BoxLayout:
                    orientation: "horizontal"
                    size_hint_y: None
                    height: dp(10)
                    spacing: dp(10)
                    padding:dp(7)

                    MDLabel:
                        text: ' Date Of Birth '
                        color: 0, 0, 0, 1
                        font_size: dp(13)
                        halign: 'left'
                        size_hint_x: 0.4
                        pos_hint: {'center_y': 0.5}
                        bold: True
                        multiline: False

                    MDLabel:
                        id: dob
                        text:'Add dob'
                        size_hint: None, None
                        size_hint_x: 0.6
                        multiline: False
                        halign: 'left'
                        font_size: dp(13)
                        pos_hint: {'center_y': 0.5}

                Widget:
                    size_hint_y: None
                    height: dp(1)
                    canvas:
                        Color:
                            rgba: 0, 0, 0, 1
                        Line:
                            points: self.x, self.y, self.x + self.width, self.y

                BoxLayout:
                    orientation: "horizontal"
                    size_hint_y: None
                    height: dp(10)
                    spacing: dp(10)
                    padding:dp(7)

                    MDLabel:
                        text: ' Mobile No '
                        color: 0, 0, 0, 1
                        halign: 'left'
                        font_size: dp(13)
                        size_hint_x: 0.4
                        pos_hint: {'center_y': 0.5}
                        bold: True
                        multiline: False

                    MDLabel:
                        id: mobile_no
                        text:'Add mobile no'
                        size_hint: None, None
                        size_hint_x: 0.6
                        multiline: False
                        font_size: dp(13)
                        halign: 'left'
                        pos_hint: {'center_y': 0.5}

                Widget:
                    size_hint_y: None
                    height: dp(1)
                    canvas:
                        Color:
                            rgba: 0, 0, 0, 1
                        Line:
                            points: self.x, self.y, self.x + self.width, self.y


                BoxLayout:
                    orientation: "horizontal"
                    size_hint_y: None
                    height: dp(10)
                    spacing: dp(10)
                    padding:dp(7)

                    MDLabel:
                        text: ' Email '
                        color: 0, 0, 0, 1
                        halign: 'left'
                        font_size: dp(13)
                        size_hint_x: 0.4
                        pos_hint: {'center_y': 0.5}
                        bold: True
                        multiline: False

                    MDLabel:
                        id: email
                        font_size: dp(13)
                        text:'Add email'
                        size_hint: None, None
                        size_hint_x: 0.6
                        multiline: False
                        halign: 'left'
                        pos_hint: {'center_y': 0.5}

                Widget:
                    size_hint_y: None
                    height: dp(1)
                    canvas:
                        Color:
                            rgba: 0, 0, 0, 1
                        Line:
                            points: self.x, self.y, self.x + self.width, self.y

                BoxLayout:
                    orientation: "horizontal"
                    size_hint_y: None
                    height: dp(10)
                    spacing: dp(10)
                    padding:dp(7)

                    MDLabel:
                        text: ' Alternate Email '
                        color: 0, 0, 0, 1
                        halign: 'left'
                        font_size: dp(13)
                        size_hint_x: 0.4
                        pos_hint: {'center_y': 0.5}
                        bold: True
                        multiline: False

                    MDLabel:
                        id: email_id
                        font_size: dp(13)
                        text:'Add email'
                        size_hint: None, None
                        size_hint_x: 0.6
                        multiline: False
                        halign: 'left'
                        pos_hint: {'center_y': 0.5}

                Widget:
                    size_hint_y: None
                    height: dp(1)
                    canvas:
                        Color:
                            rgba: 0, 0, 0, 1
                        Line:
                            points: self.x, self.y, self.x + self.width, self.y

                BoxLayout:
                    orientation: "horizontal"
                    size_hint_y: None
                    height: dp(10)
                    spacing: dp(10)
                    padding:dp(7)

                    MDLabel:
                        text: ' Gov ID1 '
                        color: 0, 0, 0, 1
                        halign: 'left'
                        font_size: dp(13)
                        size_hint_x: 0.4
                        pos_hint: {'center_y': 0.5}
                        bold: True
                        multiline: False

                    MDLabel:
                        id: gov_id1
                        text:'Add mobile no'
                        size_hint: None, None
                        size_hint_x: 0.6
                        multiline: False
                        font_size: dp(13)
                        halign: 'left'
                        pos_hint: {'center_y': 0.5}

                Widget:
                    size_hint_y: None
                    height: dp(1)
                    canvas:
                        Color:
                            rgba: 0, 0, 0, 1
                        Line:
                            points: self.x, self.y, self.x + self.width, self.y

                BoxLayout:
                    orientation: "horizontal"
                    size_hint_y: None
                    height: dp(60)
                    spacing: dp(10)
                    padding:dp(7)

                    MDLabel:
                        text: ' Upload Gov ID1 '
                        color: 0, 0, 0, 1
                        halign: 'left'
                        font_size: dp(13)
                        size_hint_x: 0.4
                        pos_hint: {'center_y': 0.5}
                        bold: True
                        multiline: False

                    Image:
                        id: upload_gov_id1_img

                        size: dp(50), dp(50)
                        source: ''
                    MDIconButton:
                        icon: ''
                        halign: 'left'

                Widget:
                    size_hint_y: None
                    height: dp(1)
                    canvas:
                        Color:
                            rgba: 0, 0, 0, 1
                        Line:
                            points: self.x, self.y, self.x + self.width, self.y

                BoxLayout:
                    orientation: "horizontal"
                    size_hint_y: None
                    height: dp(10)
                    spacing: dp(10)
                    padding:dp(7)

                    MDLabel:
                        text: ' Gov ID2 '
                        color: 0, 0, 0, 1
                        halign: 'left'
                        font_size: dp(13)
                        size_hint_x: 0.4
                        pos_hint: {'center_y': 0.5}
                        bold: True
                        multiline: False

                    MDLabel:
                        id: gov_id2
                        font_size: dp(13)
                        text:'Add email'
                        size_hint: None, None
                        size_hint_x: 0.6
                        multiline: False
                        halign: 'left'
                        pos_hint: {'center_y': 0.5}

                Widget:
                    size_hint_y: None
                    height: dp(1)
                    canvas:
                        Color:
                            rgba: 0, 0, 0, 1
                        Line:
                            points: self.x, self.y, self.x + self.width, self.y

                BoxLayout:
                    orientation: "horizontal"
                    size_hint_y: None
                    height: dp(60)
                    spacing: dp(10)
                    padding:dp(7)

                    MDLabel:
                        text: ' Upload Gov ID2 '
                        color: 0, 0, 0, 1
                        halign: 'left'
                        font_size: dp(13)
                        size_hint_x: 0.4
                        pos_hint: {'center_y': 0.5}
                        bold: True
                        multiline: False

                    Image:
                        id: upload_gov_id2_img
                        size: dp(50), dp(50)
                        source: ''
                    MDIconButton:
                        icon: ''
                        halign: 'left'
                Widget:
                    size_hint_y: None
                    height: dp(1)
                    canvas:
                        Color:
                            rgba: 0, 0, 0, 1
                        Line:
                            points: self.x, self.y, self.x + self.width, self.y

                BoxLayout:
                    orientation: "horizontal"
                    size_hint_y: None
                    height: dp(10)
                    spacing: dp(10)
                    padding:dp(7)

                    MDLabel:
                        text: ' Type of address '
                        color: 0, 0, 0, 1
                        font_size: dp(13)
                        halign: 'left'
                        size_hint_x: 0.4
                        pos_hint: {'center_y': 0.5}
                        bold: True
                        multiline: False

                    MDLabel:
                        id: type
                        text:'Add dob'
                        size_hint: None, None
                        size_hint_x: 0.6
                        multiline: False
                        halign: 'left'
                        font_size: dp(13)
                        pos_hint: {'center_y': 0.5}

                Widget:
                    size_hint_y: None
                    height: dp(1)
                    canvas:
                        Color:
                            rgba: 0, 0, 0, 1
                        Line:
                            points: self.x, self.y, self.x + self.width, self.y

                BoxLayout:
                    orientation: "horizontal"
                    size_hint_y: None
                    height: dp(10)
                    spacing: dp(10)
                    padding:dp(7)

                    MDLabel:
                        text: ' Address1 '
                        color: 0, 0, 0, 1
                        halign: 'left'
                        font_size: dp(13)
                        size_hint_x: 0.4
                        pos_hint: {'center_y': 0.5}
                        bold: True
                        multiline: False

                    MDLabel:
                        id: address1
                        font_size: dp(13)
                        text:'Add address1'
                        size_hint: None, None
                        size_hint_x: 0.6
                        multiline: False
                        halign: 'left'
                        pos_hint: {'center_y': 0.5}

                Widget:
                    size_hint_y: None
                    height: dp(1)
                    canvas:
                        Color:
                            rgba: 0, 0, 0, 1
                        Line:
                            points: self.x, self.y, self.x + self.width, self.y

                BoxLayout:
                    orientation: "horizontal"
                    size_hint_y: None
                    height: dp(10)
                    spacing: dp(10)
                    padding:dp(7)

                    MDLabel:
                        text: ' Address2 '
                        color: 0, 0, 0, 1
                        halign: 'left'
                        font_size: dp(13)
                        size_hint_x: 0.4
                        pos_hint: {'center_y': 0.5}
                        bold: True
                        multiline: False

                    MDLabel:
                        id: address2
                        text:'Add address2'
                        size_hint: None, None
                        size_hint_x: 0.6
                        multiline: False
                        font_size: dp(13)
                        halign: 'left'
                        pos_hint: {'center_y': 0.5}

                Widget:
                    size_hint_y: None
                    height: dp(1)
                    canvas:
                        Color:
                            rgba: 0, 0, 0, 1
                        Line:
                            points: self.x, self.y, self.x + self.width, self.y

                BoxLayout:
                    orientation: "horizontal"
                    size_hint_y: None
                    height: dp(20)
                    spacing: dp(10)
                    padding:dp(7)

                    MDLabel:
                        text: ' How long living \\n here '
                        color: 0, 0, 0, 1
                        halign: 'left'
                        font_size: dp(13)
                        size_hint_x: 0.4
                        pos_hint: {'center_y': 0.5}
                        bold: True
                        multiline: False

                    MDLabel:
                        id: stay
                        text:'Add mobile no'
                        size_hint: None, None
                        size_hint_x: 0.6
                        multiline: False
                        font_size: dp(13)
                        halign: 'left'
                        pos_hint: {'center_y': 0.5}

                Widget:
                    size_hint_y: None
                    height: dp(1)
                    canvas:
                        Color:
                            rgba: 0, 0, 0, 1
                        Line:
                            points: self.x, self.y, self.x + self.width, self.y


                BoxLayout:
                    orientation: "horizontal"
                    size_hint_y: None
                    height: dp(10)
                    spacing: dp(10)
                    padding:dp(7)

                    MDLabel:
                        text: ' Zipcode '
                        color: 0, 0, 0, 1
                        font_size: dp(13)
                        halign: 'left'
                        size_hint_x: 0.4
                        pos_hint: {'center_y': 0.5}
                        bold: True
                        multiline: False

                    MDLabel:
                        id: zip_code
                        text:'Add pin code'
                        size_hint: None, None
                        size_hint_x: 0.6
                        multiline: False
                        halign: 'left'
                        font_size: dp(13)
                        pos_hint: {'center_y': 0.5}

                Widget:
                    size_hint_y: None
                    height: dp(1)
                    canvas:
                        Color:
                            rgba: 0, 0, 0, 1
                        Line:
                            points: self.x, self.y, self.x + self.width, self.y

                BoxLayout:
                    orientation: "horizontal"
                    size_hint_y: None
                    height: dp(10)
                    spacing: dp(10)
                    padding:dp(7)

                    MDLabel:
                        text: ' State '
                        color: 0, 0, 0, 1
                        font_size: dp(13)
                        halign: 'left'
                        size_hint_x: 0.4
                        pos_hint: {'center_y': 0.5}
                        bold: True
                        multiline: False

                    MDLabel:
                        id: state
                        text:'Add state'
                        size_hint: None, None
                        size_hint_x: 0.6
                        multiline: False
                        halign: 'left'
                        font_size: dp(13)
                        pos_hint: {'center_y': 0.5}

                Widget:
                    size_hint_y: None
                    height: dp(1)
                    canvas:
                        Color:
                            rgba: 0, 0, 0, 1
                        Line:
                            points: self.x, self.y, self.x + self.width, self.y

                BoxLayout:
                    orientation: "horizontal"
                    size_hint_y: None
                    height: dp(10)
                    spacing: dp(10)
                    padding:dp(7)

                    MDLabel:
                        text: ' Country '
                        color: 0, 0, 0, 1
                        font_size: dp(13)
                        halign: 'left'
                        size_hint_x: 0.4
                        pos_hint: {'center_y': 0.5}
                        bold: True
                        multiline: False

                    MDLabel:
                        id: country
                        text:'Add country'
                        size_hint: None, None
                        size_hint_x: 0.6
                        multiline: False
                        halign: 'left'
                        font_size: dp(13)
                        pos_hint: {'center_y': 0.5}

                Widget:
                    size_hint_y: None
                    height: dp(1)
                    canvas:
                        Color:
                            rgba: 0, 0, 0, 1
                        Line:
                            points: self.x, self.y, self.x + self.width, self.y

                BoxLayout:
                    orientation: "horizontal"
                    size_hint_y: None
                    height: dp(10)
                    spacing: dp(10)
                    padding:dp(7)

                    MDLabel:
                        text: ' Qualification '
                        color: 0, 0, 0, 1
                        font_size: dp(13)
                        halign: 'left'
                        size_hint_x: 0.4
                        pos_hint: {'center_y': 0.5}
                        bold: True
                        multiline: False

                    MDLabel:
                        id: qualification
                        text:'Add qualification'
                        size_hint: None, None
                        size_hint_x: 0.6
                        multiline: False
                        halign: 'left'
                        font_size: dp(13)
                        pos_hint: {'center_y': 0.5}

                Widget:
                    size_hint_y: None
                    height: dp(1)
                    canvas:
                        Color:
                            rgba: 0, 0, 0, 1
                        Line:
                            points: self.x, self.y, self.x + self.width, self.y

                BoxLayout:
                    orientation: "horizontal"
                    size_hint_y: None
                    height: dp(10)
                    spacing: dp(10)
                    padding:dp(7)

                    MDLabel:
                        text: ' Marrital Status '
                        color: 0, 0, 0, 1
                        halign: 'left'
                        size_hint_x: 0.4
                        font_size: dp(13)
                        multiline: False
                        pos_hint: {'center_y': 0.5}
                        bold: True

                    MDLabel:
                        id: marrital_status
                        size_hint: None, None
                        size_hint_x: 0.6
                        font_size: dp(13)
                        halign: 'left'
                        text:'Add marrital status'
                        multiline: False
                        pos_hint: {'center_y': 0.5}

                Widget:
                    size_hint_y: None
                    height: dp(1)
                    canvas:
                        Color:
                            rgba: 0, 0, 0, 1
                        Line:
                            points: self.x, self.y, self.x + self.width, self.y

                MDLabel:
                    text: ' '

                MDLabel:
                    text: ' '

                MDLabel:
                    text: ' '

                MDFloatLayout:
                    MDRaisedButton:
                        text: "Edit Profile"
                        md_bg_color: 0.043, 0.145, 0.278, 1
                        font_name: "Roboto-Bold"
                        size_hint: 0.4, None
                        height: dp(50)
                        on_release: root.on_edit()
                        pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                        font_size: dp(15)
                MDLabel:
                    text: '  '
                MDLabel:
                    text: '  '

<ViewEditScreen1>                            
    BoxLayout:
        orientation: 'vertical'
        size_hint: 1, 1
        pos_hint: {'center_x':0.5, 'center_y':0.5}
        MDTopAppBar:
            title: "Personal Information"
            elevation: 2
            pos_hint: {'top': 1}
            left_action_items: [['arrow-left', lambda x: root.on_back_button_press()]]
            title_align: 'center'
            md_bg_color: 0.043, 0.145, 0.278, 1

        ScrollView:  # Add ScrollView here
            do_scroll_x: False
            BoxLayout:
                orientation: "vertical"
                padding: dp(10)
                spacing: dp(10)
                size_hint_y: None
                height: self.minimum_height

                MDFloatLayout:
                    size_hint_y: None
                    height: dp(120)
                    padding: dp(20)
                    spacing: dp(10)


                    MDFloatLayout:
                        size_hint: None, None
                        size: dp(80), dp(80)
                        pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                        radius: 70
                        canvas.before:
                            Color:
                                rgba: 1, 1, 1, 1
                            Ellipse:
                                size: self.size
                                pos: self.pos
                        Image:
                            id: selected_image1
                            source: 'icon8.png'
                            size_hint_x: None
                            height: dp(60)
                            width: dp(90)
                            size_hint: None, None
                            size: dp(80), dp(80)  # Make sure the size is a perfect square for a circular shape
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

                        MDIconButton:
                            icon: 'camera'
                            source: ""
                            pos_hint: {'center_x': 1.1, 'center_y': 0.}
                            on_release: app.root.get_screen('ViewEditScreen1').check_and_open_file_manager1()

                Label:
                    id: selected_file_label
                    color: 0, 0, 0, 1
                    text: 'Upload Photo'
                    size_hint_y: None
                    height: dp(10)


                BoxLayout:
                    orientation: "vertical"
                    size_hint_y: None
                    height: self.minimum_height
                    padding: dp(0)
                    spacing: dp(10)

                    BoxLayout:
                        orientation: "horizontal"
                        size_hint_y: None
                        height: dp(20)
                        spacing: dp(10)
                        padding:dp(7)

                        MDLabel:
                            text: ' Full Name '
                            color: 0, 0, 0, 1
                            halign: 'left'
                            font_size: dp(13)
                            size_hint_x: 0.4
                            pos_hint: {'center_y': 0.5}
                            bold: True
                            multiline: False

                        MDTextField:
                            id: name
                            font_size: dp(13)
                            text:'Add full name'
                            size_hint: None, None
                            size_hint_x: 0.6
                            multiline: False
                            halign: 'left'
                            pos_hint: {'center_y': 0.5}

                BoxLayout:
                    orientation: "horizontal"
                    size_hint_y: None
                    height: dp(40)
                    spacing: dp(10)
                    padding:dp(7)

                    MDLabel:
                        text: ' Gender '
                        color: 0, 0, 0, 1
                        font_size: dp(13)
                        halign: 'left'
                        size_hint_x: 0.4
                        pos_hint: {'center_y': 0.5}
                        bold: True
                        multiline: False

                    Spinner:
                        id: gender
                        text: "Select Gender"
                        size_hint: None, None
                        size_hint_x: 0.6
                        multiline: False
                        width: dp(200)
                        text_size: self.width - dp(20), None
                        height:"30dp"
                        font_size: dp(13)
                        pos_hint: {'center_y': 0.5}
                        halign: "center"
                        background_color: 1, 1, 1, 0
                        color: 0, 0, 0, 1
                        canvas.before:
                            Color:
                                rgba: 0, 0, 0, 1  
                            Line:
                                width: 0.7
                                rounded_rectangle: (self.x, self.y, self.width, self.height, 15)

                BoxLayout:
                    orientation: "horizontal"
                    size_hint_y: None
                    height: dp(20)
                    spacing: dp(10)
                    padding:dp(7)

                    MDLabel:
                        text: ' Date Of Birth '
                        color: 0, 0, 0, 1
                        font_size: dp(13)
                        halign: 'left'
                        size_hint_x: 0.4
                        pos_hint: {'center_y': 0.5}
                        bold: True
                        multiline: False

                    MDLabel:
                        id: dob
                        text:'Add dob'
                        size_hint: None, None
                        size_hint_x: 0.6
                        multiline: False
                        halign: 'left'
                        font_size: dp(13)
                        pos_hint: {'center_y': 0.5}

                BoxLayout:
                    orientation: "horizontal"
                    size_hint_y: None
                    height: dp(20)
                    spacing: dp(10)
                    padding:dp(7)

                    MDLabel:
                        text: ' Mobile No '
                        color: 0, 0, 0, 1
                        halign: 'left'
                        font_size: dp(13)
                        size_hint_x: 0.4
                        pos_hint: {'center_y': 0.5}
                        bold: True
                        multiline: False

                    MDTextField:
                        id: mobile_no
                        text:'Add mobile no'
                        size_hint: None, None
                        size_hint_x: 0.6
                        multiline: False
                        font_size: dp(13)
                        halign: 'left'
                        pos_hint: {'center_y': 0.5}


                BoxLayout:
                    orientation: "horizontal"
                    size_hint_y: None
                    height: dp(20)
                    spacing: dp(10)
                    padding:dp(7)

                    MDLabel:
                        text: ' Email '
                        color: 0, 0, 0, 1
                        halign: 'left'
                        font_size: dp(13)
                        size_hint_x: 0.4
                        pos_hint: {'center_y': 0.5}
                        bold: True
                        multiline: False

                    MDLabel:
                        id: email
                        font_size: dp(13)
                        text:'Add email'
                        size_hint: None, None
                        size_hint_x: 0.6
                        multiline: False
                        halign: 'left'
                        pos_hint: {'center_y': 0.5}

                BoxLayout:
                    orientation: "horizontal"
                    size_hint_y: None
                    height: dp(20)
                    spacing: dp(10)
                    padding:dp(7)

                    MDLabel:
                        text: ' Alternate Email '
                        color: 0, 0, 0, 1
                        halign: 'left'
                        font_size: dp(13)
                        size_hint_x: 0.4
                        pos_hint: {'center_y': 0.5}
                        bold: True
                        multiline: False

                    MDTextField:
                        id: email_id
                        font_size: dp(13)
                        text:'Add email'
                        size_hint: None, None
                        size_hint_x: 0.6
                        multiline: False
                        halign: 'left'
                        pos_hint: {'center_y': 0.5}

                BoxLayout:
                    orientation: "horizontal"
                    size_hint_y: None
                    height: dp(20)
                    spacing: dp(10)
                    padding:dp(7)

                    MDLabel:
                        text: ' Gov ID1 '
                        color: 0, 0, 0, 1
                        halign: 'left'
                        font_size: dp(13)
                        size_hint_x: 0.4
                        pos_hint: {'center_y': 0.5}
                        bold: True
                        multiline: False

                    MDLabel:
                        id: gov_id1
                        text:'Add mobile no'
                        size_hint: None, None
                        size_hint_x: 0.6
                        multiline: False
                        font_size: dp(13)
                        halign: 'left'
                        pos_hint: {'center_y': 0.5}

                BoxLayout:
                    orientation: "horizontal"
                    size_hint_y: None
                    height: dp(60)
                    spacing: dp(10)
                    padding:dp(7)

                    MDLabel:
                        text: ' Upload Gov ID1 '
                        color: 0, 0, 0, 1
                        halign: 'left'
                        font_size: dp(13)
                        size_hint_x: 0.4
                        pos_hint: {'center_y': 0.5}
                        bold: True
                        multiline: False

                    Image:
                        id: upload_gov_id1_img
                        size: dp(50), dp(50)
                        source: ''

                    MDIconButton:
                        icon: 'upload'
                        on_release: app.root.get_screen('ViewEditScreen1').check_and_open_file_manager2()  

                BoxLayout:
                    orientation: "horizontal"
                    size_hint_y: None
                    height: dp(20)
                    spacing: dp(10)
                    padding:dp(7)

                    MDLabel:
                        text: ' Gov ID2 '
                        color: 0, 0, 0, 1
                        halign: 'left'
                        font_size: dp(13)
                        size_hint_x: 0.4
                        pos_hint: {'center_y': 0.5}
                        bold: True
                        multiline: False

                    MDLabel:
                        id: gov_id2
                        font_size: dp(13)
                        text:'Add email'
                        size_hint: None, None
                        size_hint_x: 0.6
                        multiline: False
                        halign: 'left'
                        pos_hint: {'center_y': 0.5}

                BoxLayout:
                    orientation: "horizontal"
                    size_hint_y: None
                    height: dp(60)
                    spacing: dp(10)
                    padding:dp(7)

                    MDLabel:
                        text: ' Upload Gov ID2 '
                        color: 0, 0, 0, 1
                        halign: 'left'
                        font_size: dp(13)
                        size_hint_x: 0.4
                        pos_hint: {'center_y': 0.5}
                        bold: True
                        multiline: False

                    Image:
                        id: upload_gov_id2_img
                        size: dp(50), dp(50)
                        source: ''

                    MDIconButton:
                        icon: 'upload'
                        on_release: app.root.get_screen('ViewEditScreen1').check_and_open_file_manager3()

                BoxLayout:
                    orientation: "horizontal"
                    size_hint_y: None
                    height: dp(40)
                    spacing: dp(10)
                    padding:dp(7)

                    MDLabel:
                        text: ' Type of address '
                        color: 0, 0, 0, 1
                        font_size: dp(13)
                        halign: 'left'
                        size_hint_x: 0.4
                        pos_hint: {'center_y': 0.5}
                        bold: True
                        multiline: False

                    Spinner:
                        id: type
                        text:'Add dob'
                        size_hint: None, None
                        size_hint_x: 0.6
                        multiline: False
                        width: dp(200)
                        text_size: self.width - dp(20), None
                        height:"30dp"
                        font_size: dp(13)
                        pos_hint: {'center_y': 0.5}
                        halign: "center"
                        background_color: 1, 1, 1, 0
                        color: 0, 0, 0, 1
                        canvas.before:
                            Color:
                                rgba: 0, 0, 0, 1  
                            Line:
                                width: 0.7
                                rounded_rectangle: (self.x, self.y, self.width, self.height, 15)

                BoxLayout:
                    orientation: "horizontal"
                    size_hint_y: None
                    height: dp(20)
                    spacing: dp(10)
                    padding:dp(7)

                    MDLabel:
                        text: ' Address1 '
                        color: 0, 0, 0, 1
                        halign: 'left'
                        font_size: dp(13)
                        size_hint_x: 0.4
                        pos_hint: {'center_y': 0.5}
                        bold: True
                        multiline: False

                    MDTextField:
                        id: address1
                        font_size: dp(13)
                        text:'Add email'
                        size_hint: None, None
                        size_hint_x: 0.6
                        multiline: False
                        halign: 'left'
                        pos_hint: {'center_y': 0.5}


                BoxLayout:
                    orientation: "horizontal"
                    size_hint_y: None
                    height: dp(20)
                    spacing: dp(10)
                    padding:dp(7)

                    MDLabel:
                        text: ' Address2 '
                        color: 0, 0, 0, 1
                        halign: 'left'
                        font_size: dp(13)
                        size_hint_x: 0.4
                        pos_hint: {'center_y': 0.5}
                        bold: True
                        multiline: False

                    MDTextField:
                        id: address2
                        text:'Add mobile no'
                        size_hint: None, None
                        size_hint_x: 0.6
                        multiline: False
                        font_size: dp(13)
                        halign: 'left'
                        pos_hint: {'center_y': 0.5}



                BoxLayout:
                    orientation: "horizontal"
                    size_hint_y: None
                    height: dp(40)
                    spacing: dp(10)
                    padding:dp(7)

                    MDLabel:
                        text: ' How long living \\n here '
                        color: 0, 0, 0, 1
                        halign: 'left'
                        font_size: dp(13)
                        size_hint_x: 0.4
                        pos_hint: {'center_y': 0.5}
                        bold: True
                        multiline: True

                    Spinner:
                        id: stay
                        text:'Select present address'
                        size_hint: None, None
                        size_hint_x: 0.6
                        multiline: False
                        width: dp(200)
                        text_size: self.width - dp(20), None
                        height:"30dp"
                        font_size: dp(13)
                        pos_hint: {'center_y': 0.5}
                        halign: "center"
                        background_color: 1, 1, 1, 0
                        color: 0, 0, 0, 1
                        canvas.before:
                            Color:
                                rgba: 0, 0, 0, 1  
                            Line:
                                width: 0.7
                                rounded_rectangle: (self.x, self.y, self.width, self.height, 15)

                BoxLayout:
                    orientation: "horizontal"
                    size_hint_y: None
                    height: dp(20)
                    spacing: dp(10)
                    padding:dp(7)

                    MDLabel:
                        text: ' Zipcode '
                        color: 0, 0, 0, 1
                        font_size: dp(13)
                        halign: 'left'
                        size_hint_x: 0.4
                        pos_hint: {'center_y': 0.5}
                        bold: True
                        multiline: False

                    MDTextField:
                        id: zip_code
                        text:'Add gender'
                        size_hint: None, None
                        size_hint_x: 0.6
                        multiline: False
                        halign: 'left'
                        font_size: dp(13)
                        pos_hint: {'center_y': 0.5}

                BoxLayout:
                    orientation: "horizontal"
                    size_hint_y: None
                    height: dp(20)
                    spacing: dp(10)
                    padding:dp(7)

                    MDLabel:
                        text: ' State '
                        color: 0, 0, 0, 1
                        font_size: dp(13)
                        halign: 'left'
                        size_hint_x: 0.4
                        pos_hint: {'center_y': 0.5}
                        bold: True
                        multiline: False

                    MDTextField:
                        id: state
                        text:'Add gender'
                        size_hint: None, None
                        size_hint_x: 0.6
                        multiline: False
                        halign: 'left'
                        font_size: dp(13)
                        pos_hint: {'center_y': 0.5}

                BoxLayout:
                    orientation: "horizontal"
                    size_hint_y: None
                    height: dp(20)
                    spacing: dp(10)
                    padding:dp(7)

                    MDLabel:
                        text: ' Country '
                        color: 0, 0, 0, 1
                        font_size: dp(13)
                        halign: 'left'
                        size_hint_x: 0.4
                        pos_hint: {'center_y': 0.5}
                        bold: True
                        multiline: False

                    MDTextField:
                        id: country
                        text:'Add gender'
                        size_hint: None, None
                        size_hint_x: 0.6
                        multiline: False
                        halign: 'left'
                        font_size: dp(13)
                        pos_hint: {'center_y': 0.5}

                BoxLayout:
                    orientation: "horizontal"
                    size_hint_y: None
                    height: dp(40)
                    spacing: dp(10)
                    padding:dp(7)

                    MDLabel:
                        text: ' Qualification '
                        color: 0, 0, 0, 1
                        font_size: dp(13)
                        halign: 'left'
                        size_hint_x: 0.4
                        pos_hint: {'center_y': 0.5}
                        bold: True
                        multiline: False

                    Spinner:
                        id: qualification
                        text:'Add gender'
                        size_hint: None, None
                        size_hint_x: 0.6
                        multiline: False
                        width: dp(200)
                        text_size: self.width - dp(20), None
                        height:"30dp"
                        font_size: dp(13)
                        pos_hint: {'center_y': 0.5}
                        halign: "center"
                        background_color: 1, 1, 1, 0
                        color: 0, 0, 0, 1
                        canvas.before:
                            Color:
                                rgba: 0, 0, 0, 1  
                            Line:
                                width: 0.7
                                rounded_rectangle: (self.x, self.y, self.width, self.height, 15)
                BoxLayout:
                    orientation: "horizontal"
                    size_hint_y: None
                    height: dp(40)
                    spacing: dp(10)
                    padding:dp(7)

                    MDLabel:
                        text: ' Marrital Status '
                        color: 0, 0, 0, 1
                        halign: 'left'
                        size_hint_x: 0.4
                        font_size: dp(13)
                        multiline: False
                        pos_hint: {'center_y': 0.5}
                        bold: True

                    Spinner:
                        id: marrital_status
                        size_hint: None, None
                        size_hint_x: 0.6
                        text:"Select marrital status"
                        multiline: False
                        width: dp(200)
                        text_size: self.width - dp(20), None
                        height:"30dp"
                        font_size: dp(13)
                        pos_hint: {'center_y': 0.5}
                        halign: "center"
                        background_color: 1, 1, 1, 0
                        color: 0, 0, 0, 1
                        canvas.before:
                            Color:
                                rgba: 0, 0, 0, 1  
                            Line:
                                width: 0.7
                                rounded_rectangle: (self.x, self.y, self.width, self.height, 15)

                MDLabel:
                    text: ' '

                MDLabel:
                    text: ' '

                MDLabel:
                    text: ' '

                MDFloatLayout:
                    MDRaisedButton:
                        text: "Save"
                        md_bg_color: 0.043, 0.145, 0.278, 1
                        font_name: "Roboto-Bold"
                        size_hint: 0.4, None
                        height: dp(50)
                        on_release:root.save_edited_data()
                        pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                        font_size:dp(15)
                MDLabel:
                    text: '  '
                MDLabel:
                    text: '  '

<ReturnsScreen>
    MDBoxLayout:
        orientation: 'vertical'
        MDTopAppBar:                                   
            elevation: 2
            pos_hint: {'top': 1}
            left_action_items: [['arrow-left', lambda x: setattr(app.root, 'current', 'LenderDashboard')]]
            right_action_items: [['refresh', lambda x: root.return_refresh()]]
            title_align: 'center'
            title: "My Returns"
            md_bg_color: 0.043, 0.145, 0.278, 1
        MDBoxLayout:
            orientation: 'vertical'
            size_hint_y: None
            heigt: dp(70)
            MDLabel:
                text: ''
                size_hint_y: None
                height: dp(50)
            MDGridLayout:
                cols: 2
                spacing: dp(20)
                padding: dp(20)
                MDRaisedButton:
                    id: total_returns
                    text: "Total Returns"
                    md_bg_color: 0.043, 0.145, 0.278, 1
                    font_name: "Roboto-Bold"
                    size_hint: 0.4, None
                    height: dp(50)
                    pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                    font_size:dp(15)
                    on_release: root.total_return_screeen()
                MDRaisedButton:
                    id: user_returns
                    text: "Users Returns"
                    md_bg_color: 0.043, 0.145, 0.278, 1
                    font_name: "Roboto-Bold"
                    size_hint: 0.4, None
                    height: dp(50)
                    pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                    font_size:dp(15)
                    on_release: root.user_return_screeen()

        MDBoxLayout:
            id: box
            Image:
                id: image
                size_hint: (1, None)
                height: dp(420)

<CommitmentScreen>
    MDBoxLayout:
        orientation: 'vertical'
        MDTopAppBar:                                   
            elevation: 2
            pos_hint: {'top': 1}
            left_action_items: [['arrow-left', lambda x: setattr(app.root, 'current', 'LenderDashboard')]]
            title_align: 'center'
            title: "My Commitments"
            md_bg_color: 0.043, 0.145, 0.278, 1
        MDBoxLayout:
            id: box
            Image:
                id: image
                size_hint: (1, None)
                height: dp(450)
        MDLabel:
            text: ''
            size_hint_y: None
            height: dp(100)

<ViewEditScreen4>
    canvas.before:
        Color:
            rgba: 1, 1, 1, 1
        Rectangle:
            size: self.size
            pos: self.pos

    BoxLayout:
        orientation: 'vertical'
        size_hint: 1, 1
        pos_hint: {'center_x':0.5, 'center_y':0.5}
        MDTopAppBar:
            title: "Professional Information"
            elevation: 2
            pos_hint: {'top': 1}
            left_action_items: [['arrow-left', lambda x: root.on_back_button_press()]]
            right_action_items: [['refresh', lambda x: root.refresh()]]
            title_align: 'center'
            md_bg_color: 0.043, 0.145, 0.278, 1
        ScrollView:
            BoxLayout:
                orientation: "vertical"
                padding: dp(10)
                spacing: dp(10)
                size_hint_y: None
                height: self.minimum_height
                BoxLayout:
                    orientation: "vertical"
                    size_hint_y: None
                    height: self.minimum_height
                    padding: dp(0)
                    spacing: dp(10)
                    MDLabel:
                        text: ' '
                    MDLabel:
                        text: ' '
                    MDLabel:
                        text: ' '
                    BoxLayout:
                        orientation: "horizontal"
                        size_hint_y: None
                        height: dp(10)
                        spacing: dp(10)
                        padding:dp(7)

                        MDLabel:
                            text: ' Company name '
                            color: 0, 0, 0, 1
                            halign: 'left'
                            font_size: dp(13)
                            size_hint_x: 0.4
                            pos_hint: {'center_y': 0.5}
                            bold: True
                            multiline: False

                        MDTextField:
                            id: company_name
                            font_size: dp(13)
                            text:'Add company name'
                            size_hint: None, None
                            size_hint_x: 0.6
                            multiline: False
                            halign: 'left'
                            pos_hint: {'center_y': 0.5}

                BoxLayout:
                    orientation: "horizontal"
                    size_hint_y: None
                    height: dp(40)
                    spacing: dp(10)
                    padding:dp(7)

                    MDLabel:
                        text: ' Occupation type  '
                        color: 0, 0, 0, 1
                        font_size: dp(13)
                        halign: 'left'
                        size_hint_x: 0.4
                        pos_hint: {'center_y': 0.5}
                        bold: True
                        multiline: False

                    Spinner:
                        id: occupation_type 
                        text:'Add occupation type '
                        size_hint: None, None
                        size_hint_x: 0.6
                        multiline: False
                        width: dp(200)
                        text_size: self.width - dp(20), None
                        height:"30dp"
                        font_size: dp(13)
                        pos_hint: {'center_y': 0.5}
                        halign: "center"
                        background_color: 1, 1, 1, 0
                        color: 0, 0, 0, 1
                        canvas.before:
                            Color:
                                rgba: 0, 0, 0, 1  
                            Line:
                                width: 0.7
                                rounded_rectangle: (self.x, self.y, self.width, self.height, 15)

                BoxLayout:
                    orientation: "horizontal"
                    size_hint_y: None
                    height: dp(40)
                    spacing: dp(10)
                    padding:dp(7)

                    MDLabel:
                        text: ' Employment type '
                        color: 0, 0, 0, 1
                        font_size: dp(13)
                        halign: 'left'
                        size_hint_x: 0.4
                        pos_hint: {'center_y': 0.5}
                        bold: True
                        multiline: False

                    Spinner:
                        id: employment_type
                        text:'Add employment type'
                        size_hint: None, None
                        size_hint_x: 0.6
                        multiline: False
                        width: dp(200)
                        text_size: self.width - dp(20), None
                        height:"30dp"
                        font_size: dp(13)
                        pos_hint: {'center_y': 0.5}
                        halign: "center"
                        background_color: 1, 1, 1, 0
                        color: 0, 0, 0, 1
                        canvas.before:
                            Color:
                                rgba: 0, 0, 0, 1  
                            Line:
                                width: 0.7
                                rounded_rectangle: (self.x, self.y, self.width, self.height, 15)

                BoxLayout:
                    orientation: "horizontal"
                    size_hint_y: None
                    height: dp(40)
                    spacing: dp(10)
                    padding:dp(7)

                    MDLabel:
                        text: ' Organization type  '
                        color: 0, 0, 0, 1
                        halign: 'left'
                        font_size: dp(13)
                        size_hint_x: 0.4
                        pos_hint: {'center_y': 0.5}
                        bold: True
                        multiline: False

                    Spinner:
                        id: organization_type 
                        text:'Add organization type '
                        size_hint: None, None
                        size_hint_x: 0.6
                        multiline: False
                        width: dp(200)
                        text_size: self.width - dp(20), None
                        height:"30dp"
                        font_size: dp(13)
                        pos_hint: {'center_y': 0.5}
                        halign: "center"
                        background_color: 1, 1, 1, 0
                        color: 0, 0, 0, 1
                        canvas.before:
                            Color:
                                rgba: 0, 0, 0, 1  
                            Line:
                                width: 0.7
                                rounded_rectangle: (self.x, self.y, self.width, self.height, 15)

                BoxLayout:
                    orientation: "horizontal"
                    size_hint_y: None
                    height: dp(20)
                    spacing: dp(10)
                    padding:dp(7)

                    MDLabel:
                        text: ' Company address '
                        color: 0, 0, 0, 1
                        halign: 'left'
                        font_size: dp(13)
                        size_hint_x: 0.4
                        pos_hint: {'center_y': 0.5}
                        bold: True
                        multiline: False

                    MDTextField:
                        id: company_address
                        font_size: dp(13)
                        text:'Add company address'
                        size_hint: None, None
                        size_hint_x: 0.6
                        multiline: False
                        halign: 'left'
                        pos_hint: {'center_y': 0.5}

                BoxLayout:
                    orientation: "horizontal"
                    size_hint_y: None
                    height: dp(20)
                    spacing: dp(10)
                    padding:dp(7)

                    MDLabel:
                        text: ' Landmark '
                        color: 0, 0, 0, 1
                        halign: 'left'
                        font_size: dp(13)
                        size_hint_x: 0.4
                        pos_hint: {'center_y': 0.5}
                        bold: True
                        multiline: False

                    MDTextField:
                        id: landmark
                        font_size: dp(13)
                        text:'Add landmark'
                        size_hint: None, None
                        size_hint_x: 0.6
                        multiline: False
                        halign: 'left'
                        pos_hint: {'center_y': 0.5}

                BoxLayout:
                    orientation: "horizontal"
                    size_hint_y: None
                    height: dp(30)
                    spacing: dp(10)
                    padding:dp(7)

                    MDLabel:
                        text: ' Company phone \\n number '
                        color: 0, 0, 0, 1
                        halign: 'left'
                        font_size: dp(13)
                        size_hint_x: 0.4
                        pos_hint: {'center_y': 0.5}
                        bold: True
                        multiline: False

                    MDTextField:
                        id: company_phone_number
                        text:'Add company phone number'
                        size_hint: None, None
                        size_hint_x: 0.6
                        multiline: False
                        font_size: dp(13)
                        halign: 'left'
                        pos_hint: {'center_y': 0.5}

                BoxLayout:
                    orientation: "horizontal"
                    size_hint_y: None
                    height: dp(20)
                    spacing: dp(10)
                    padding:dp(7)

                    MDLabel:
                        text: " Annual salary "
                        color: 0, 0, 0, 1
                        halign: 'left'
                        font_size: dp(13)
                        size_hint_x: 0.4
                        pos_hint: {'center_y': 0.5}
                        bold: True
                        multiline: False

                    MDTextField:
                        id: annual_salary
                        font_size: dp(13)
                        text:"Add annual salary"
                        size_hint: None, None
                        size_hint_x: 0.6
                        multiline: False
                        halign: 'left'
                        pos_hint: {'center_y': 0.5}

                BoxLayout:
                    orientation: "horizontal"
                    size_hint_y: None
                    height: dp(40)
                    spacing: dp(10)
                    padding:dp(7)

                    MDLabel:
                        text: ' Salary type '
                        color: 0, 0, 0, 1
                        halign: 'left'
                        font_size: dp(13)
                        size_hint_x: 0.4
                        pos_hint: {'center_y': 0.5}
                        bold: True
                        multiline: False

                    Spinner:
                        id: salary_type
                        text:'Add salary type'
                        size_hint: None, None
                        size_hint_x: 0.6
                        multiline: False
                        width: dp(200)
                        text_size: self.width - dp(20), None
                        height:"30dp"
                        font_size: dp(13)
                        pos_hint: {'center_y': 0.5}
                        halign: "center"
                        background_color: 1, 1, 1, 0
                        color: 0, 0, 0, 1
                        canvas.before:
                            Color:
                                rgba: 0, 0, 0, 1  
                            Line:
                                width: 0.7
                                rounded_rectangle: (self.x, self.y, self.width, self.height, 15)

                BoxLayout:
                    orientation: "horizontal"
                    size_hint_y: None
                    height: dp(20)
                    spacing: dp(10)
                    padding:dp(7)

                    MDLabel:
                        text: ' Designation '
                        color: 0, 0, 0, 1
                        halign: 'left'
                        font_size: dp(13)
                        size_hint_x: 0.4
                        pos_hint: {'center_y': 0.5}
                        bold: True
                        multiline: False

                    MDTextField:
                        id: designation
                        text:'Add designation'
                        size_hint: None, None
                        size_hint_x: 0.6
                        multiline: False
                        font_size: dp(13)
                        halign: 'left'
                        pos_hint: {'center_y': 0.5}

                BoxLayout:
                    orientation: "horizontal"
                    size_hint_y: None
                    height: dp(60)
                    spacing: dp(10)
                    padding:dp(7)

                    MDLabel:
                        text: ' Employee id '
                        color: 0, 0, 0, 1
                        font_size: dp(13)
                        halign: 'left'
                        size_hint_x: 0.4
                        pos_hint: {'center_y': 0.5}
                        bold: True
                        multiline: False

                    Image:
                        id: employee_id
                        size: dp(50), dp(50)
                        source: ''

                    MDIconButton:
                        icon: 'upload'
                        on_release: app.root.get_screen('ViewEditScreen4').check_and_open_file_manager1()

                BoxLayout:
                    orientation: "horizontal"
                    size_hint_y: None
                    height: dp(60)
                    spacing: dp(10)
                    padding:dp(7)

                    MDLabel:
                        text: ' Last six months \\n bank statement '
                        color: 0, 0, 0, 1
                        halign: 'left'
                        font_size: dp(13)
                        size_hint_x: 0.4
                        pos_hint: {'center_y': 0.5}
                        bold: True
                        multiline: False

                    Image:
                        id: last_six_months_bank_statement
                        size: dp(50), dp(50)
                        source: ''

                    MDIconButton:
                        icon: 'upload'
                        on_release: app.root.get_screen('ViewEditScreen4').check_and_open_file_manager2()

                MDLabel:
                    text: ' '
                MDLabel:
                    text: ' '
                MDLabel:
                    text: ' '
                MDLabel:
                    text: ' '
                MDLabel:
                    text: ' '
                MDFloatLayout:
                    MDRaisedButton:
                        text: "Save Profile"
                        md_bg_color: 0.043, 0.145, 0.278, 1
                        font_name: "Roboto-Bold"
                        size_hint: 0.4, None
                        height: dp(50)
                        on_release: root.on_employee_save()
                        pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                        font_size: dp(15)
                MDLabel:
                    text: '  '
                MDLabel:
                    text: '  '
<ViewEditScreen7>                            
    BoxLayout:
        orientation: 'vertical'
        size_hint: 1, 1
        pos_hint: {'center_x':0.5, 'center_y':0.5}
        MDTopAppBar:
            title: "User Email Info"
            elevation: 2
            pos_hint: {'top': 1}
            left_action_items: [['arrow-left', lambda x: root.on_back_button_press()]]
            right_action_items: [['refresh', lambda x: root.refresh()]]
            title_align: 'center'
            md_bg_color: 0.043, 0.145, 0.278, 1

        ScrollView:
            do_scroll_x: False
            BoxLayout:
                orientation: "vertical"
                padding: dp(10)
                spacing: dp(10)
                size_hint_y: None
                height: self.minimum_height

                MDFloatLayout:
                    size_hint_y: None
                    height: dp(120)
                    padding: dp(20)
                    spacing: dp(10)

                    MDFloatLayout:
                        size_hint: None, None
                        size: dp(80), dp(80)
                        pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                        radius: 70
                        canvas.before:
                            Color:
                                rgba: 1, 1, 1, 1
                            Ellipse:
                                size: self.size
                                pos: self.pos
                        Image:
                            id: selected_image1
                            source: 'icon8.png'
                            size_hint_x: None
                            height: dp(60)
                            width: dp(90)
                            size_hint: None, None
                            size: dp(80), dp(80)
                            source: ""
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


                BoxLayout:
                    orientation: "vertical"
                    size_hint_y: None
                    height: self.minimum_height
                    padding: dp(0)
                    spacing: dp(10)

                    BoxLayout:
                        orientation: "horizontal"
                        size_hint_y: None
                        height: dp(20)
                        spacing: dp(10)
                        padding:dp(7)

                        MDLabel:
                            text: ' Email '
                            color: 0, 0, 0, 1
                            halign: 'left'
                            font_size: dp(13)
                            size_hint_x: 0.4
                            pos_hint: {'center_y': 0.5}
                            bold: True
                            multiline: False

                        MDTextField:
                            id: email
                            font_size: dp(13)
                            text: 'Add email'
                            size_hint: None, None
                            size_hint_x: 0.6
                            multiline: False
                            halign: 'left'
                            pos_hint: {'center_y': 0.5}

                MDLabel:
                    text: ' '

                MDLabel:
                    text: ' '

                MDLabel:
                    text: ' '

                MDFloatLayout:
                    MDRaisedButton:
                        text: "Save"
                        md_bg_color: 0.043, 0.145, 0.278, 1
                        font_name: "Roboto-Bold"
                        size_hint: 0.4, None
                        height: dp(50)
                        on_release: root.save_edited_data1()
                        pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                        font_size: dp(15)

                MDLabel:
                    text: '  '

                MDLabel:
                    text: '  '
"""

conn = sqlite3.connect('fin_user.db')
cursor = conn.cursor()


class LenderDashboard(Screen):
    Builder.load_string(user_helpers1)

    def go_to_returns_screen(self):
        sm = self.manager

        # Create a new instance of the LoginScreen
        returns_screen = ReturnsScreen(name='ReturnsScreen')

        # Add the LoginScreen to the existing ScreenManager
        sm.add_widget(returns_screen)

        # Switch to the LoginScreen
        sm.current = 'ReturnsScreen'

    def go_to_commitment_screen(self):
        sm = self.manager

        # Create a new instance of the LoginScreen
        commitment_screen = CommitmentScreen(name='CommitmentScreen')

        # Add the LoginScreen to the existing ScreenManager
        sm.add_widget(commitment_screen)

        # Switch to the LoginScreen
        sm.current = 'CommitmentScreen'

    def update_notification_count(self, count):
        self.ids.notification_label.text = str(count)

    def go_to_lender_notification(self):
        # Create a modal view for the loading animation
        modal_view = ModalView(size_hint=(None, None), size=(300, 150), background_color=[0, 0, 0, 0])

        # Create a BoxLayout to hold the loading text
        box_layout = BoxLayout(orientation='vertical')

        # Create a label for the loading text
        loading_label = MDLabel(
            text="Loading...",
            halign="center",
            valign="center",
            theme_text_color="Custom",
            text_color=[1, 1, 1, 1],
            font_size="20sp",
            bold=True
        )

        # Add the label to the box layout
        box_layout.add_widget(loading_label)

        # Add the box layout to the modal view
        modal_view.add_widget(box_layout)

        # Open the modal view
        modal_view.open()

        # Perform the actual action (e.g., checking account details and navigating)
        Clock.schedule_once(lambda dt: self.show_transfer_screen(modal_view), 1)

    def show_transfer_screen(self, modal_view):
        # Dismiss the loading animation modal view
        modal_view.dismiss()
        notification_screen = Lend_NotificationScreen(name='Lend_NotificationScreen')
        notification_screen.lender_dashboard = self  # Pass reference to LenderDashBoard screen
        self.manager.add_widget(notification_screen)
        self.manager.current = 'Lend_NotificationScreen'

    def go_to_chatbot_screen(self):
        # Create a modal view for the loading animation
        modal_view = ModalView(size_hint=(None, None), size=(300, 150), background_color=[0, 0, 0, 0])

        # Create a BoxLayout to hold the loading text
        box_layout = BoxLayout(orientation='vertical')

        # Create a label for the loading text
        loading_label = MDLabel(
            text="Loading...",
            halign="center",
            valign="center",
            theme_text_color="Custom",
            text_color=[1, 1, 1, 1],
            font_size="20sp",
            bold=True
        )

        # Add the label to the box layout
        box_layout.add_widget(loading_label)

        # Add the box layout to the modal view
        modal_view.add_widget(box_layout)

        # Open the modal view
        modal_view.open()

        # Perform the actual action (e.g., checking account details and navigating)
        Clock.schedule_once(lambda dt: self.show_chatbot_screen(modal_view), 1)

    def show_chatbot_screen(self, modal_view):
        # Close the modal view after performing the action
        modal_view.dismiss()
        self.manager.add_widget(Factory.ChatBotScreen(name='ChatBotScreen'))
        self.manager.current = 'ChatBotScreen'

    def view_Borr_Portfolio(self):
        modal_view = ModalView(size_hint=(None, None), size=(1000, 600), background_color=[0, 0, 0, 0])

        # Create MDLabel with white text color, increased font size, and bold text
        loading_label = MDLabel(text="Loading...", halign="center", valign="bottom",
                                theme_text_color="Custom", text_color=[1, 1, 1, 1],
                                font_size="50sp", bold=True)

        # Set initial y-position off-screen
        loading_label.y = -loading_label.height

        modal_view.add_widget(loading_label)
        modal_view.open()

        # Perform the animation
        self.animate_loading_text(loading_label, modal_view.height)

        # Perform the actual action (e.g., fetching loan requests)
        # You can replace the sleep with your actual logic
        Clock.schedule_once(lambda dt: self.perform_view_Borr_Portfolio(modal_view), 2)

    def perform_view_Borr_Portfolio(self, modal_view):
        # Close the modal view after performing the action
        modal_view.dismiss()
        self.manager.add_widget(Factory.Lend_Portfolio(name='Lend_Portfolio'))
        self.manager.current = 'Lend_Portfolio'

    def notification(self):
        pass

    def refresh6(self):
        self.on_pre_enter()

    def on_pre_leave(self):
        # Unbind the back button event when leaving the screen
        Window.unbind(on_keyboard=self.on_back_button)

    def on_back_button(self, instance, key, scancode, codepoint, modifier):
        # Handle the back button event
        if key == 27:  # 27 is the keycode for the hardware back button on Android
            self.go_back()
            return True  # Consume the event, preventing further handling
        return False  # Continue handling the event

    def go_back(self):
        # Navigate to the previous screen with a slide transition
        self.manager.transition = SlideTransition(direction='right')
        self.manager.current = 'LenderDashboard'

    def on_back_button_press(self):
        self.manager.current = 'LenderDashboard'

    def animate_loading_text(self, loading_label, modal_height):
        # Define the animation to move the label vertically
        anim = Animation(y=modal_height - loading_label.height, duration=1) + \
               Animation(y=0, duration=5)
        anim.bind(on_complete=lambda *args: self.animate_loading_text(loading_label,
                                                                      modal_height))  # Bind to the completion event to repeat the animation
        anim.start(loading_label)

    def refresh2(self):
        self.__init__()

    def wallet(self):
        self.type = None
        data = app_tables.fin_wallet.search()
        email = self.email()
        w_email = []
        w_id = []
        w_amount = []
        for i in data:
            w_email.append(i['user_email'])
            w_id.append(i['wallet_id'])
            w_amount.append(i['wallet_amount'])

        index = 0
        if email in w_email:
            index = w_email.index(email)
            self.ids.total_amount.text = str(round(w_amount[index], 2))
        else:
            print("no email found")

    def on_amount_touch_down(self):
        self.ids.enter_amount.input_type = 'number'

    def view_transaction_history(self):
        sm = self.manager
        # Create a new instance of the LenderWalletScreen
        wallet_screen = TransactionLH(name='TransactionLH')
        # Add the LenderWalletScreen to the existing ScreenManager
        sm.add_widget(wallet_screen)
        # Switch to the LenderWalletScreen
        sm.current = 'TransactionLH'

    def disbrsed_loan(self, instance):
        print("amount paid")
        view_loan_text = anvil.server.call("view_loan_text")
        if view_loan_text == "view_loan_text":
            self.manager.get_screen('ViewUnderScreenLR').paynow()
        else:
            self.manager.get_screen('ViewLoansProfileScreenLR').paynow()

    def highlight_button(self, button_type):
        if button_type == 'deposit':
            self.ids.deposit_button_grid.md_bg_color = 0, 0, 0, 1
            self.ids.withdraw_button_grid.md_bg_color = 1, 1, 1, 1
            self.ids.deposit_button_grid.text_color = 1, 1, 1, 1
            self.ids.withdraw_button_grid.text_color = 0, 0, 0, 1
            self.type = 'deposit'
        elif button_type == 'withdraw':
            self.ids.deposit_button_grid.md_bg_color = 1, 1, 1, 1
            self.ids.withdraw_button_grid.md_bg_color = 0, 0, 0, 1
            self.ids.withdraw_button_grid.text_color = 1, 1, 1, 1
            self.ids.deposit_button_grid.text_color = 0, 0, 0, 1
            self.type = 'withdraw'

    def on_pre_leave(self):
        Window.unbind(on_keyboard=self.on_back_button)

    def on_back_button(self, instance, key, *args):
        if key == 27:  # 27 is the keycode for the hardware back button on Android
            self.go_back()
            return True  # Consume the event, preventing further handling
        return False  # Continue handling the event

    def go_back(self):
        # Navigate to the previous screen with a slide transition
        self.manager.transition = SlideTransition(direction='right')
        self.manager.current = 'LenderDashboard'

    def on_back_button_press(self):
        self.go_back()
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
        self.manager.current = 'LenderWalletScreen'

    def submit(self):
        enter_amount = self.ids.enter_amount.text
        if self.type == None:
            self.show_validation_error3('Please Select Transaction Type')
        elif self.ids.enter_amount.text == '' and not self.ids.enter_amount.text.isdigit():
            self.show_validation_error3('Enter Valid Amount')
        elif self.type == 'deposit':
            data = app_tables.fin_wallet.search()
            transaction = app_tables.fin_wallet_transactions.search()
            email = self.email()
            w_email = []
            w_id = []
            w_amount = []
            w_customer_id = []
            for i in data:
                w_email.append(i['user_email'])
                w_id.append(i['wallet_id'])
                w_amount.append(i['wallet_amount'])
                w_customer_id.append(i['customer_id'])

            t_id = []
            for i in transaction:
                t_id.append(i['transaction_id'])

            if len(t_id) >= 1:
                transaction_id = 'TA' + str(int(t_id[-1][2:]) + 1).zfill(4)
            else:
                transaction_id = 'TA0001'

            transaction_date_time = datetime.today()
            if email in w_email:
                index = w_email.index(email)
                data[index]['wallet_amount'] = int(enter_amount) + w_amount[index]
                self.show_validation_error(f'Amount {enter_amount} Deposited Successfully')
                self.ids.enter_amount.text = ''
                app_tables.fin_wallet_transactions.add_row(transaction_id=transaction_id,
                                                           customer_id=w_customer_id[index], user_email=email,
                                                           transaction_type=self.type, amount=int(enter_amount),
                                                           status='success', wallet_id=w_id[index],
                                                           transaction_time_stamp=transaction_date_time)
            else:
                print("no email found")
            self.refresh1()

        elif self.type == 'withdraw':
            data = app_tables.fin_wallet.search()
            transaction = app_tables.fin_wallet_transactions.search()
            email = self.email()
            w_email = []
            w_id = []
            w_amount = []
            w_customer_id = []
            for i in data:
                w_email.append(i['user_email'])
                w_id.append(i['wallet_id'])
                w_amount.append(i['wallet_amount'])
                w_customer_id.append(i['customer_id'])

            t_id = []
            for i in transaction:
                t_id.append(i['transaction_id'])

            if len(t_id) >= 1:
                transaction_id = 'TA' + str(int(t_id[-1][2:]) + 1).zfill(4)
            else:
                transaction_id = 'TA0001'

            transaction_date_time = datetime.today()

            if email in w_email:
                index = w_email.index(email)
                if w_amount[index] >= int(self.ids.enter_amount.text):
                    data[index]['wallet_amount'] = w_amount[index] - int(self.ids.enter_amount.text)
                    self.show_validation_error(
                        f'Amount {self.ids.enter_amount.text} Withdraw Successfully')
                    self.ids.enter_amount.text = ''
                    app_tables.fin_wallet_transactions.add_row(transaction_id=transaction_id,
                                                               customer_id=w_customer_id[index], user_email=email,
                                                               transaction_type=self.type, amount=int(enter_amount),
                                                               status='success', wallet_id=w_id[index],
                                                               transaction_time_stamp=transaction_date_time)
                else:
                    self.show_validation_error2(
                        f'Insufficient Amount {self.ids.enter_amount.text} Please Deposit Required Money')
                    app_tables.fin_wallet_transactions.add_row(transaction_id=transaction_id,
                                                               customer_id=w_customer_id[index], user_email=email,
                                                               transaction_type=self.type, amount=int(enter_amount),
                                                               status='fail', wallet_id=w_id[index],
                                                               transaction_time_stamp=transaction_date_time)
                    self.ids.enter_amount.text = ''
            else:
                print("no email found")
        self.refresh1()

    def refresh1(self):
        self.wallet()

    def show_validation_error(self, error_message):
        dialog = MDDialog(
            title="Transaction Success",
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

    def show_validation_error2(self, error_message):
        dialog = MDDialog(
            title="Transaction Failure",
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

    def show_validation_error3(self, error_message):
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

    def email(self):
        return anvil.server.call('another_method')

    def build(self):
        self.update_notification_count(0)  # Initially set count to 0
        return super().build()

    def on_pre_enter(self):
        notification_screen = Factory.Lend_NotificationScreen(name='Lend_NotificationScreen')
        self.manager.add_widget(notification_screen)
        notification_screen.lender_dashboard = self  # Pass reference to LenderDashBoard screen
        notification_count = sum([len(screen.ids.container1.children) for screen in self.manager.screens if
                                  isinstance(screen, Lend_NotificationScreen)])
        self.update_notification_count(notification_count)
        Window.bind(on_keyboard=self.on_back_button)

        log_email = anvil.server.call('another_method')
        profile = app_tables.fin_user_profile.search()
        print(log_email)

        email_user = []
        name_list = []
        investment = []
        user_age = []
        p_customer_id = []
        ascend_score = []
        emp_type = []
        profile_list = []

        for i in profile:
            email_user.append(i['email_user'])
            name_list.append(i['full_name'])
            investment.append(i['investment'])
            user_age.append(i['user_age'])
            p_customer_id.append(i['customer_id'])
            ascend_score.append(i['ascend_value'])
            emp_type.append(i['profession'])
            profile_list.append(i['user_photo'])

        # Check if 'logged' is in the status list
        log_index = 0
        if log_email in email_user:
            log_index = email_user.index(log_email)
            self.ids.details.text = "Welcome " + name_list[log_index]
            self.ids.details.font_style = 'H6'
            self.ids.name.text = name_list[log_index]
            self.ids.username.text = name_list[log_index]
        else:
            # Handle the case when 'logged' is not in the status list
            self.ids.details.text = "User welcome to P2P"
            self.ids.username.text = ""

        data = app_tables.fin_loan_details.search()

        loan_id = []
        loan_status = []
        borrower_name = []
        product_name = []
        customer_id = []
        loan_amount = []
        left_amount = []
        interest_rate = []
        tenure = []
        s = 0
        for i in data:
            s += 1
            loan_id.append(i['loan_id'])
            loan_status.append(i['loan_updated_status'])
            borrower_name.append(i['borrower_full_name'])
            product_name.append(i['product_name'])
            customer_id.append(i['borrower_customer_id'])
            loan_amount.append(i['loan_amount'])
            left_amount.append(i['remaining_amount'])
            interest_rate.append(i['interest_rate'])
            tenure.append(i['tenure'])

        c = -1
        index_list = []
        for i in range(s):
            c += 1
            if loan_status[c] == 'under process' or loan_status[c] == 'approved':
                index_list.append(c)

        self.ids.loan.text = str(len(index_list))

        if len(loan_id) < 1:
            self.ids.borrower_name.text = ""
            self.ids.age.text = ''
            self.ids.product_name = ''
            self.ids.amount.text = ''
            self.ids.interest.text = ''
            self.ids.tenure.text = ''
            self.ids.age.text = ''
            self.ids.employment.text = ''
            self.ids.score.text = ''
            self.ids.left.text = ''

        else:
            a = 0
            b = -1
            for i in loan_status:
                b += 1
                if i == 'under process':
                    a = b
            print(a)
            self.ids.borrower_name.text = str(borrower_name[a])
            self.ids.product_name.text = str(product_name[a])
            self.ids.amount.text = "Rs. " + str(loan_amount[a])
            self.ids.interest.text = str(interest_rate[a]) + "%"
            self.ids.tenure.text = str(int(tenure[a])) + ' Months'
            self.ids.left.text = "Rs. " + str(left_amount[a])
            if customer_id[a] in p_customer_id:
                index1 = p_customer_id.index(customer_id[a])
                self.ids.age.text = str(user_age[index1]) + " Years"
                self.ids.employment.text = str(emp_type[index1])
                self.ids.score.text = str(ascend_score[index1])
            else:
                print("customer_id is not there")

        data = app_tables.fin_wallet.search()
        w_email = []
        w_id = []
        w_amount = []
        for i in data:
            w_email.append(i['user_email'])
            w_id.append(i['wallet_id'])
            w_amount.append(i['wallet_amount'])

        index = 0
        if log_email in w_email:
            index = w_email.index(log_email)
            self.ids.total_amount1.text = "Rs. " + str(round(w_amount[index], 2))
            self.ids.balance.text = "Available Balance: Rs. " + str(round(w_amount[index], 2))
        else:
            self.ids.balance.text = "Available Balance: "
            print("no email found")

        member = app_tables.fin_membership.search()

        a = 0
        membership_type = []
        max_amount = []
        min_amount = []
        for i in member:
            a += 1
            membership_type.append(i['membership_type'])
            min_amount.append(i['min_amount'])
            max_amount.append(i['max_amount'])
        print(log_index)
        print(investment)

        if investment[log_index] != None:
            try:
                investment_value = float(investment[log_index])
                for i in range(a):
                    if min_amount[i] <= investment_value < max_amount[i]:
                        self.ids.member_type.text = f"Membership Type: {membership_type[i]}"
                    break
            except ValueError:
                self.ids.member_type.text = f"Membership Type: None"

        else:
            self.ids.member_type.text = f"Membership Type: None"
            print("Investment Amount Not There or Invalid")

        lender_data = app_tables.fin_lender.search()
        lender_cus_id = []
        create_date = []
        returns = []
        membership_type = []
        present_commitment = []
        for i in lender_data:
            lender_cus_id.append(i['customer_id'])
            create_date.append(i['member_since'])
            returns.append(i['return_on_investment'])
            membership_type.append(i['membership'])
            present_commitment.append(i['present_commitments'])
        #
        if p_customer_id[log_index] in lender_cus_id:
            index1 = lender_cus_id.index(p_customer_id[log_index])
            self.ids.joined_date.text = "[b]Joined Date[/b]: " + str(create_date[index1])
            self.ids.return_amount.text = "Rs. " + str(returns[index1])
            self.ids.member_type.text = "[b]Membership Type[/b]: " + str(membership_type[index1])
            self.ids.commitment.text = "Rs. " + str(present_commitment[index1])
            self.ids.date.text = "Joined Date: " + str(create_date[index1])
        else:
            self.ids.joined_date.text = "[b]Joined Date[/b]: "
            self.ids.return_amount.text = "Rs. "
            self.ids.member_type.text = "[b]Membership Type[/b]: "
            self.ids.commitment.text = "Rs. "
            self.ids.date.text = "Joined Date: "

        if profile_list[log_index] != None:
            image_data = profile_list[log_index].get_bytes()
            if isinstance(image_data, bytes):
                try:
                    profile_texture_io = BytesIO(image_data)
                    photo_texture = CoreImage(profile_texture_io, ext='png').texture
                    self.ids.image.texture = photo_texture
                    self.ids.image1.texture = photo_texture
                except Exception as e:
                    print(f"Error processing image for customer {p_customer_id[log_index]}: {e}")
            else:
                try:
                    image_data_binary = base64.b64decode(image_data)
                    profile_texture_io = BytesIO(image_data_binary)
                    photo_texture = CoreImage(profile_texture_io, ext='png').texture
                    self.ids.image.texture = photo_texture
                    self.ids.image1.texture = photo_texture
                except base64.binascii.Error as e:
                    print(f"Base64 decoding error for customer {p_customer_id[log_index]}: {e}")
                except Exception as e:
                    print(f"Error processing image for customer {i['customer_id']}: {e}")
        else:
            print('photo is not there')

    def on_kv_post(self, base_widget):
        self.setup_menu()

    def setup_menu(self):
        data = app_tables.fin_loan_details.search()

        enter_data = self.ids.search.text

        loan_id = []
        borrower_name = []
        loan_status_list = []
        s = 0
        for i in data:
            s += 1
            loan_id.append(i['loan_id'])
            borrower_name.append(i['borrower_full_name'])
            loan_status_list.append(i['loan_updated_status'])

        menu_items = [

        ]
        a = -1
        index_list = []
        for i in range(s):
            a += 1
            print(enter_data.lower(), borrower_name[i].lower())
            print(enter_data.lower() in borrower_name[i].lower())
            if enter_data.lower() in borrower_name[i].lower() and loan_status_list[i] in ['under process', 'approved',
                                                                                          'rejected']:
                index_list.append(a)

        for i in index_list:
            item = {
                "text": f"{borrower_name[i]}",
                "viewclass": "OneLineListItem",
                "on_release": lambda x=i: self.menu_callback(x),
            }
            menu_items.append(item)

        self.menu = MDDropdownMenu(
            caller=self.ids.button,
            items=menu_items,
            ver_growth="down",
            max_height=dp(224),
            position="center",
            width_mult=4,
        )

    def menu_callback(self, text_item):
        print(text_item)
        self.menu.dismiss()
        data = app_tables.fin_loan_details.search()

        loan_id = []
        loan_status_list = []
        s = 0
        for i in data:
            s += 1
            loan_id.append(i['loan_id'])
            loan_status_list.append(i['loan_updated_status'])

        loan_status = loan_status_list[text_item]
        if loan_status == 'approved':
            # Open the screen for approved loans

            sm = self.manager

            # Create a new instance of the LoginScreen
            approved = ViewLoansProfileScreenLR(name='ViewLoansProfileScreenLR')

            # Add the LoginScreen to the existing ScreenManager
            sm.add_widget(approved)

            # Switch to the LoginScreen
            sm.current = 'ViewLoansProfileScreenLR'
            self.manager.get_screen('ViewLoansProfileScreenLR').initialize_with_value(loan_id[text_item], data)

        elif loan_status == 'under process':
            # Open the screen for pending loans
            sm = self.manager

            # Create a new instance of the LoginScreen
            under_process = ViewLoansProfileScreen(name='ViewLoansProfileScreen')

            # Add the LoginScreen to the existing ScreenManager
            sm.add_widget(under_process)

            # Switch to the LoginScreen
            sm.current = 'ViewLoansProfileScreen'
            self.manager.get_screen('ViewLoansProfileScreen').initialize_with_value(loan_id[text_item], data)
        elif loan_status == 'rejected':
            # Open the screen for pending loans
            sm = self.manager

            # Create a new instance of the LoginScreen
            rejected = ViewLoansProfileScreenRL(name='ViewLoansProfileScreenRL')

            # Add the LoginScreen to the existing ScreenManager
            sm.add_widget(rejected)

            # Switch to the LoginScreen
            sm.current = 'ViewLoansProfileScreenRL'
            self.manager.get_screen('ViewLoansProfileScreenRL').initialize_with_value(loan_id[text_item], data)
        else:
            # Handle other loan statuses or show an error message
            pass

    def show_validation_error5(self, error_message):
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

    def invest(self):
        data = app_tables.fin_loan_details.search()

        loan_id = []
        loan_status = []
        borrower_name = []
        product_name = []
        customer_id = []
        loan_amount = []
        left_amount = []
        interest_rate = []
        tenure = []
        s = 0
        for i in data:
            s += 1
            loan_id.append(i['loan_id'])
            loan_status.append(i['loan_updated_status'])
            borrower_name.append(i['borrower_full_name'])
            product_name.append(i['product_name'])
            customer_id.append(i['borrower_customer_id'])
            loan_amount.append(i['loan_amount'])
            left_amount.append(i['remaining_amount'])
            interest_rate.append(i['interest_rate'])
            tenure.append(i['tenure'])
        if len(loan_id) < 1:
            pass
        else:
            a = 0
            b = -1
            for i in loan_status:
                b += 1
                if i == 'under process':
                    a = b
            # Open the screen for pending loans
            sm = self.manager

            # Create a new instance of the LoginScreen
            under_process = ViewLoansProfileScreen(name='ViewLoansProfileScreen')

            # Add the LoginScreen to the existing ScreenManager
            sm.add_widget(under_process)

            # Switch to the LoginScreen
            sm.current = 'ViewLoansProfileScreen'
            self.manager.get_screen('ViewLoansProfileScreen').initialize_with_value(loan_id[a], data)

    def on_pre_leave(self):
        # Unbind the back button event when leaving the screen
        Window.unbind(on_keyboard=self.on_back_button)

    def on_back_button(self, instance, key, *args):
        if key == 27:  # 27 is the keycode for the hardware back button on Android
            self.go_back()
            return True  # Consume the event, preventing further handling
        return False  # Continue handling the event

    def go_back(self):
        # Navigate to the previous screen with a slide transition
        self.manager.transition = SlideTransition(direction='right')
        self.manager.current = 'LenderDashboard'

    def on_back_button_press(self):
        self.go_back()

        # Replace with the actual name of your previous screen

    def homepage(self):
        self.manager.current = 'MainScreen'

    def loans(self):
        self.selected_item = None  # Track the selected item
        data = app_tables.fin_loan_details.search()
        email = anvil.server.call('another_method')
        profile = app_tables.fin_user_profile.search()
        customer_id = []
        loan_id = []
        borrower_name = []
        loan_status = []
        product_name = []
        email1 = []
        loan_amount = []
        tenure = []
        interest_rate = []
        ascend_score = []
        s = 0
        for i in data:
            s += 1
            customer_id.append(i['borrower_customer_id'])
            loan_id.append(i['loan_id'])
            borrower_name.append(i['borrower_full_name'])
            loan_status.append(i['loan_updated_status'])
            product_name.append(i['product_name'])
            email1.append(i['borrower_email_id'])
            loan_amount.append(i['loan_amount'])
            tenure.append(i['tenure'])
            interest_rate.append(i['interest_rate'])

        profile_customer_id = []
        profile_mobile_number = []
        profile_phote_list = []
        profile_photo = {}
        for i in profile:
            profile_customer_id.append(i['customer_id'])
            profile_mobile_number.append(i['mobile'])
            ascend_score.append(i['ascend_value'])
            profile_phote_list.append(i['user_photo'])
            print(i['user_photo'])

            if i['user_photo']:
                image_data = i['user_photo'].get_bytes()
                if isinstance(image_data, bytes):
                    try:
                        profile_texture_io = BytesIO(image_data)
                        photo_texture = CoreImage(profile_texture_io, ext='png').texture
                        profile_photo[i['customer_id']] = photo_texture
                    except Exception as e:
                        print(f"Error processing image for customer {i['customer_id']}: {e}")
                else:
                    try:
                        image_data_binary = base64.b64decode(image_data)
                        profile_texture_io = BytesIO(image_data_binary)
                        photo_texture = CoreImage(profile_texture_io, ext='png').texture
                        profile_photo[i['customer_id']] = photo_texture
                    except base64.binascii.Error as e:
                        print(f"Base64 decoding error for customer {i['customer_id']}: {e}")
                    except Exception as e:
                        print(f"Error processing image for customer {i['customer_id']}: {e}")
        print(profile_photo)
        if email in email1:
            index = email1.index(email)

        c = -1
        index_list = []
        for i in range(s):
            c += 1
            index_list.append(c)

        b = 1
        k = -1
        for i in reversed(index_list):
            b += 1
            k += 1
            if customer_id[i] in profile_customer_id:
                number = profile_customer_id.index(customer_id[i])
            else:
                number = 0
            # Card to display the list of details
            card = MDCard(
                orientation='vertical',
                size_hint=(None, None),
                size=("310dp", "200dp"),
                padding="8dp",
                spacing="5dp",
                elevation=3
            )
            horizontal_layout = BoxLayout(orientation='horizontal')
            if customer_id[i] in profile_photo:
                image = Image(
                    texture=profile_photo[customer_id[i]],  # Get the profile photo texture
                    size_hint_x=None,
                    height="30dp",
                    width="60dp"
                )
            else:
                image = Image(
                    source='img.png',  # Update with the actual path to the image
                    size_hint_x=None,
                    height="60dp",
                    width="70dp"
                )
            horizontal_layout.add_widget(image)

            horizontal_layout.add_widget(Widget(size_hint_x=None, width='10dp'))
            text_layout = BoxLayout(orientation='vertical')
            text_layout.add_widget(MDLabel(
                text=f"[b]{borrower_name[i]}[/b],\n[b]{profile_mobile_number[number]}[/b]",
                theme_text_color='Custom',
                text_color=(0, 0, 0, 1),
                halign='left',
                markup=True,
            ))
            text_layout.add_widget(MDLabel(
                text=f"[b]Product name:[/b] {product_name[i]}",
                theme_text_color='Custom',
                text_color=(0, 0, 0, 1),
                halign='left',
                markup=True,
            ))
            text_layout.add_widget(MDLabel(
                text=f"[b]Loan Amount:[/b] {loan_amount[i]}",
                theme_text_color='Custom',
                text_color=(0, 0, 0, 1),
                halign='left',
                markup=True,
            ))
            text_layout.add_widget(MDLabel(
                text=f"[b]Ascend Score:[/b] {ascend_score[number]}",
                theme_text_color='Custom',
                text_color=(0, 0, 0, 1),
                halign='left',
                markup=True,
            ))

            horizontal_layout.add_widget(text_layout)
            card.add_widget(horizontal_layout)

            card.add_widget(Widget(size_hint_y=None, height='10dp'))
            button_layout = BoxLayout(
                size_hint_y=None,
                height="40dp",
                padding="10dp",
                spacing="20dp"
            )
            status_color = (0.545, 0.765, 0.290, 1)  # default color
            if loan_status[i] in ["under process"]:
                status_color = (253 / 255, 218 / 255, 13 / 255, 1)  # yellow
            elif loan_status[i] in ["disbursed"]:
                status_color = (255 / 255, 88 / 255, 93 / 255, 1)  # pink
            elif loan_status[i] in ["closed"]:
                status_color = (0 / 255, 100 / 255, 0 / 255, 1)  # bottle-green
            elif loan_status[i] in ["extension"]:
                status_color = (255 / 255, 165 / 255, 0 / 255, 1)  # orange
            elif loan_status[i] in ["foreclosure"]:
                status_color = (0.424, 0.663, 0.859, 1.0)  # sky blue
            elif loan_status[i] in ["rejected"]:
                status_color = (210 / 255, 4 / 255, 45 / 255, 1)  # cherry
            elif loan_status[i] in ["approved"]:
                status_color = (0 / 255, 128 / 255, 0 / 255, 1)  # light green
            elif loan_status[i] == "lost opportunities":
                status_color = (0.902, 0.141, 0.141, 1)

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
                size_hint=(None, None),
                height="40dp",
                width="250dp",
                pos_hint={"center_x": 0},
                md_bg_color=status_color,
                # on_release=lambda x, i=i: self.close_loan(i)
            )
            button2 = MDFillRoundFlatButton(
                text=" View Details ",
                size_hint=(None, None),
                height="40dp",
                width="250dp",
                pos_hint={"center_x": 1},
                md_bg_color=(0.043, 0.145, 0.278, 1),
                on_release=lambda instance, loan_id=loan_id[i]: self.icon_button_clicked(instance, loan_id)
            )

            button_layout.add_widget(button1)
            button_layout.add_widget(button2)
            card.add_widget(button_layout)

            # card.bind(on_release=lambda instance, loan_id=loan_id[i]: self.icon_button_clicked(instance, loan_id))
            self.ids.container.add_widget(card)

    def icon_button_clicked(self, instance, loan_id):
        data = app_tables.fin_loan_details.search()
        # Deselect all other items
        self.deselect_items()

        # Change the background color of the clicked item to indicate selection
        instance.bg_color = (0.5, 0.5, 0.5, 1)  # Change color as desired
        self.selected_item = instance

        sm = self.manager

        # Create a new instance of the LoginScreen
        under_process = ViewLoansProfileScreens(name='ViewLoansProfileScreens')

        # Add the LoginScreen to the existing ScreenManager
        sm.add_widget(under_process)

        # Switch to the LoginScreen
        sm.current = 'ViewLoansProfileScreens'
        self.manager.get_screen('ViewLoansProfileScreens').initialize_with_value(loan_id, data)

    def deselect_items(self):
        # Deselect all items in the list
        for item in self.ids.container.children:
            if isinstance(item, ThreeLineAvatarIconListItem):
                item.bg_color = (1, 1, 1, 1)  # Reset background color for all items

    def go_to_lender_report_issue(self):
        modal_view = ModalView(size_hint=(None, None), size=(1000, 500), background_color=[0, 0, 0, 0])

        # Create MDLabel with white text color, increased font size, and bold text
        loading_label = MDLabel(text="Loading...", halign="center", valign="bottom",
                                theme_text_color="Custom", text_color=[1, 1, 1, 1],
                                font_size=dp(50), bold=True)

        # Set initial y-position off-screen
        loading_label.y = -loading_label.height

        modal_view.add_widget(loading_label)
        modal_view.open()

        # Perform the animation
        self.animate_loading_text(loading_label, modal_view.height)

        # Perform the actual action (e.g., fetching transaction history)
        # You can replace the sleep with your actual logic
        Clock.schedule_once(lambda dt: self.perform_lender_report_issue_action(modal_view), 2)

    def perform_lender_report_issue_action(self, modal_view):
        # Dismiss the modal view
        modal_view.dismiss()

        # Get the ScreenManager
        sm = self.manager

        # Create a new instance of the TransactionBH screen
        Report_Issue_screen = ReportScreenLender(name='ReportScreenLender')

        # Add the TransactionBH screen to the existing ScreenManager
        sm.add_widget(Report_Issue_screen)

        # Switch to the TransactionBH screen
        sm.current = 'ReportScreenLender'

    def refresh_profile_data(self):
        email = self.get_email()
        data = app_tables.fin_user_profile.search(email_user=email)
        name = []
        email1 = []
        mobile_no = []
        dob = []
        city = []
        gender = []
        marrital_status = []
        for row in data:
            name.append(row['full_name'])
            email1.append(row['email_user'])
            mobile_no.append(row['mobile'])
            dob.append(row['date_of_birth'])
            city.append(row['city'])
            gender.append(row['gender'])
            marrital_status.append(row['marital_status'])
        if email in email1:
            index = email1.index(email)
            self.ids.name.text = str(name[index])
            self.ids.email.text = str(email1[index])
            self.ids.mobile_no.text = str(mobile_no[index])
            self.ids.dob.text = str(dob[index])
            self.ids.city.text = str(city[index])
            self.ids.gender.text = str(gender[index])
            self.ids.marrital_status.text = str(marrital_status[index])

    def get_email(self):
        # Make a call to the Anvil server function
        # Replace 'YourAnvilFunction' with the actual name of your Anvil server function
        return anvil.server.call('another_method')

    def get_table(self):
        # Make a call to the Anvil server function
        # Replace 'YourAnvilFunction' with the actual name of your Anvil server function
        return anvil.server.call('profile')

    def refresh5(self):
        self.ids.container.clear_widgets()
        self.loans()

    def check_and_open_file_manager1(self):
        self.check_and_open_file_manager("upload_icon1", "upload_label1", "selected_file_label1", "selected_image1")

    def check_and_open_file_manager(self, icon_id, label_id, file_label_id, image_id):
        if platform == 'android':
            if check_permission(Permission.READ_MEDIA_IMAGES):
                self.file_manager_open(icon_id, label_id, file_label_id, image_id)
            else:
                self.request_media_images_permission()
        else:
            # For non-Android platforms, directly open the file manager
            self.file_manager_open(icon_id, label_id, file_label_id, image_id)

    def on_edit(self):
        self.manager.add_widget(Factory.EditScreen1(name='ViewEditScreen1'))
        self.manager.current = 'ViewEditScreen1'

    def file_manager_open(self, icon_id, label_id, file_label_id, image_id):
        self.file_manager = MDFileManager(
            exit_manager=self.exit_manager,
            select_path=lambda path: self.select_path1(path, icon_id, label_id, file_label_id, image_id),
        )
        if platform == 'android':
            primary_external_storage = "/storage/emulated/0"
            self.file_manager.show(primary_external_storage)
        else:
            # For other platforms, show the file manager from the root directory
            self.file_manager.show('/')

    def select_path1(self, path, icon_id, label_id, file_label_id, image_id):
        self.ids[image_id].source = path  # Set the source of the Image widget
        self.file_manager.close()

    def exit_manager(self, *args):
        self.file_manager.close()

    def request_media_images_permission(self):
        request_permissions([Permission.READ_MEDIA_IMAGES], self.permission_callback)

    def permission_callback(self, permissions, grants):
        if all(grants.values()):
            # Permission granted, open the file manager
            self.file_manager_open()
        else:
            # Permission denied, show a modal view
            self.show_permission_denied()

    def show_permission_denied(self):
        view = ModalView()
        view.add_widget(Button(
            text='Permission NOT granted.\n\n' +
                 'Tap to quit app.\n\n\n' +
                 'If you selected "Don\'t Allow",\n' +
                 'enable permission with App Settings.',
            on_press=self.bye)
        )
        view.open()

    def on_pre_leave(self):
        # Unbind the back button event when leaving the screen
        Window.unbind(on_keyboard=self.on_back_button)

    def on_back_button(self, instance, key, *args):
        if key == 27:  # 27 is the keycode for the hardware back button on Android
            self.go_back()
            return True  # Consume the event, preventing further handling
        return False  # Continue handling the event

    def go_back(self):
        # Navigate to the previous screen with a slide transition
        self.manager.transition = SlideTransition(direction='right')
        self.manager.current = 'LenderDashboard'

    def on_back_button_press(self):
        self.go_back()

    def go_to_main_screen(self):
        # Clear user data
        with open("emails.json", "r+") as file:
            user_data = json.load(file)
            # Check if user_data is a dictionary
            if isinstance(user_data, dict):
                for email, data in user_data.items():
                    if isinstance(data, dict) and data.get("logged_status", False):
                        data["logged_status"] = False
                        data["user_type"] = ""
                        break
                # Move the cursor to the beginning of the file
                file.seek(0)
                # Write the updated data back to the file
                json.dump(user_data, file, indent=4)
                # Truncate any remaining data in the file
                file.truncate()

        # Switch to MainScreen
        self.manager.current = 'MainScreen'

    def account(self):
        modal_view = ModalView(size_hint=(None, None), size=(1000, 600), background_color=[0, 0, 0, 0])

        # Create MDLabel with white text color, increased font size, and bold text
        loading_label = MDLabel(text="Loading...", halign="center", valign="bottom",
                                theme_text_color="Custom", text_color=[1, 1, 1, 1],
                                font_size="50sp", bold=True)

        # Set initial y-position off-screen
        loading_label.y = -loading_label.height

        modal_view.add_widget(loading_label)
        modal_view.open()

        # Perform the animation
        self.animate_loading_text(loading_label, modal_view.height)

        # Perform the actual action (e.g., fetching loan requests)
        # You can replace the sleep with your actual logic
        Clock.schedule_once(lambda dt: self.permformance_account(modal_view), 2)

    def permformance_account(self, modal_view):
        # self.manager.current = 'ViewProfileScreen'
        modal_view.dismiss()
        self.manager.add_widget(Factory.ViewAccountScreen(name='ViewAccountScreen'))
        self.manager.current = 'ViewAccountScreen'

    def lender_today_due(self):
        modal_view = ModalView(size_hint=(None, None), size=(1000, 600), background_color=[0, 0, 0, 0])

        # Create MDLabel with white text color, increased font size, and bold text
        loading_label = MDLabel(text="Loading...", halign="center", valign="bottom",
                                theme_text_color="Custom", text_color=[1, 1, 1, 1],
                                font_size="50sp", bold=True)

        # Set initial y-position off-screen
        loading_label.y = -loading_label.height

        modal_view.add_widget(loading_label)
        modal_view.open()

        # Perform the animation
        self.animate_loading_text(loading_label, modal_view.height)

        # Perform the actual action (e.g., fetching loan requests)
        # You can replace the sleep with your actual logic
        Clock.schedule_once(lambda dt: self.performance_lender_today_due(modal_view), 2)

    def view_lost_opportunities(self):
        modal_view = ModalView(size_hint=(None, None), size=(1000, 600), background_color=[0, 0, 0, 0])

        # Create MDLabel with white text color, increased font size, and bold text
        loading_label = MDLabel(text="Loading...", halign="center", valign="bottom",
                                theme_text_color="Custom", text_color=[1, 1, 1, 1],
                                font_size="50sp", bold=True)

        # Set initial y-position off-screen
        loading_label.y = -loading_label.height

        modal_view.add_widget(loading_label)
        modal_view.open()

        # Perform the animation
        self.animate_loading_text(loading_label, modal_view.height)

        # Perform the actual action (e.g., fetching loan requests)
        # You can replace the sleep with your actual logic
        Clock.schedule_once(lambda dt: self.perform_view_lost_opportunities(modal_view), 2)

    def perform_view_lost_opportunities(self, modal_view):
        # Close the modal view after performing the action
        modal_view.dismiss()
        self.manager.add_widget(Factory.LostOpportunitiesScreen(name='LostOpportunitiesScreen'))
        self.manager.current = 'LostOpportunitiesScreen'

    def performance_lender_today_due(self, modal_view):
        modal_view.dismiss()
        self.manager.add_widget(Factory.TodayDuesTD(name='TodayDuesTD'))
        self.manager.current = 'TodayDuesTD'

    def view_loan_request(self):
        modal_view = ModalView(size_hint=(None, None), size=(1000, 600), background_color=[0, 0, 0, 0])

        # Create MDLabel with white text color, increased font size, and bold text
        loading_label = MDLabel(text="Loading...", halign="center", valign="bottom",
                                theme_text_color="Custom", text_color=[1, 1, 1, 1],
                                font_size="50sp", bold=True)

        # Set initial y-position off-screen
        loading_label.y = -loading_label.height

        modal_view.add_widget(loading_label)
        modal_view.open()

        # Perform the animation
        self.animate_loading_text(loading_label, modal_view.height)

        # Perform the actual action (e.g., fetching loan requests)
        # You can replace the sleep with your actual logic
        Clock.schedule_once(lambda dt: self.perform_loan_request_action(modal_view), 2)

    def animate_loading_text(self, loading_label, modal_height):
        # Define the animation to move the label vertically
        anim = Animation(y=modal_height - loading_label.height, duration=1) + \
               Animation(y=0, duration=1)
        anim.bind(on_complete=lambda *args: self.animate_loading_text(loading_label,
                                                                      modal_height))  # Bind to the completion event to repeat the animation
        anim.start(loading_label)

    def perform_loan_request_action(self, modal_view):
        # Close the modal view after performing the action
        modal_view.dismiss()
        self.manager.add_widget(Factory.ViewLoansRequest(name='ViewLoansRequest'))
        self.manager.current = 'ViewLoansRequest'

    def view_loanscreen(self):
        modal_view = ModalView(size_hint=(None, None), size=(1000, 600), background_color=[0, 0, 0, 0])

        # Create MDLabel with white text color, increased font size, and bold text
        loading_label = MDLabel(text="Loading...", halign="center", valign="bottom",
                                theme_text_color="Custom", text_color=[1, 1, 1, 1],
                                font_size="50sp", bold=True)

        # Set initial y-position off-screen
        loading_label.y = -loading_label.height

        modal_view.add_widget(loading_label)
        modal_view.open()

        # Perform the animation
        self.animate_loading_text(loading_label, modal_view.height)

        # Perform the actual action (e.g., fetching loan requests)
        # You can replace the sleep with your actual logic
        Clock.schedule_once(lambda dt: self.perform_view_loanscreen(modal_view), 2)

    def perform_view_loanscreen(self, modal_view):
        # Close the modal view after performing the action
        modal_view.dismiss()
        self.manager.add_widget(Factory.ALlLoansScreen(name='ALlLoansScreen'))
        self.manager.current = 'ALlLoansScreen'

    def newloan_extension(self):
        modal_view = ModalView(size_hint=(None, None), size=(1000, 600), background_color=[0, 0, 0, 0])

        # Create MDLabel with white text color, increased font size, and bold text
        loading_label = MDLabel(text="Loading...", halign="center", valign="bottom",
                                theme_text_color="Custom", text_color=[1, 1, 1, 1],
                                font_size="50sp", bold=True)

        # Set initial y-position off-screen
        loading_label.y = -loading_label.height

        modal_view.add_widget(loading_label)
        modal_view.open()

        # Perform the animation
        self.animate_loading_text(loading_label, modal_view.height)

        # Perform the actual action (e.g., fetching loan requests)
        # You can replace the sleep with your actual logic
        Clock.schedule_once(lambda dt: self.perform_newloan_extension(modal_view), 2)

    def perform_newloan_extension(self, modal_view):
        # self.manager.current = 'ViewProfileScreen'
        modal_view.dismiss()

        self.manager.add_widget(Factory.ALLLoansEX(name='ALLLoansEX'))
        self.manager.current = 'ALLLoansEX'

    def view_transaction_history(self):
        modal_view = ModalView(size_hint=(None, None), size=(1000, 600), background_color=[0, 0, 0, 0])

        # Create MDLabel with white text color, increased font size, and bold text
        loading_label = MDLabel(text="Loading...", halign="center", valign="bottom",
                                theme_text_color="Custom", text_color=[1, 1, 1, 1],
                                font_size="50sp", bold=True)

        # Set initial y-position off-screen
        loading_label.y = -loading_label.height

        modal_view.add_widget(loading_label)
        modal_view.open()

        # Perform the animation
        self.animate_loading_text(loading_label, modal_view.height)

        # Perform the actual action (e.g., fetching loan requests)
        # You can replace the sleep with your actual logic
        Clock.schedule_once(lambda dt: self.performance_view_transaction_history(modal_view), 2)

    def performance_view_transaction_history(self, modal_view):
        modal_view.dismiss()

        self.manager.add_widget(Factory.TransactionLH(name='TransactionLH'))
        self.manager.current = 'TransactionLH'

    def view_loan_foreclose(self):
        modal_view = ModalView(size_hint=(None, None), size=(1000, 600), background_color=[0, 0, 0, 0])

        # Create MDLabel with white text color, increased font size, and bold text
        loading_label = MDLabel(text="Loading...", halign="center", valign="bottom",
                                theme_text_color="Custom", text_color=[1, 1, 1, 1],
                                font_size="50sp", bold=True)

        # Set initial y-position off-screen
        loading_label.y = -loading_label.height

        modal_view.add_widget(loading_label)
        modal_view.open()

        # Perform the animation
        self.animate_loading_text(loading_label, modal_view.height)

        # Perform the actual action (e.g., fetching loan requests)
        # You can replace the sleep with your actual logic
        Clock.schedule_once(lambda dt: self.performance_view_loan_foreclose(modal_view), 2)

    def performance_view_loan_foreclose(self, modal_view):
        modal_view.dismiss()
        self.manager.add_widget(Factory.ViewAllLoansLF(name='ViewAllLoansLF'))
        self.manager.current = 'ViewAllLoansLF'

    def go_to_wallet(self):
        modal_view = ModalView(size_hint=(None, None), size=(1000, 600), background_color=[0, 0, 0, 0])

        # Create MDLabel with white text color, increased font size, and bold text
        loading_label = MDLabel(text="Loading...", halign="center", valign="bottom",
                                theme_text_color="Custom", text_color=[1, 1, 1, 1],
                                font_size="50sp", bold=True)

        # Set initial y-position off-screen
        loading_label.y = -loading_label.height

        modal_view.add_widget(loading_label)
        modal_view.open()

        # Perform the animation
        self.animate_loading_text(loading_label, modal_view.height)

        # Perform the actual action (e.g., fetching loan requests)
        # You can replace the sleep with your actual logic
        Clock.schedule_once(lambda dt: self.perform_wallet(modal_view), 2)

    def perform_wallet(self, modal_view):
        from lender_wallet import LenderWalletScreen

        modal_view.dismiss()
        self.manager.add_widget(Factory.LenderWalletScreen(name='LenderWalletScreen'))
        self.manager.current = 'LenderWalletScreen'
        # Get the existing ScreenManager

    def bank(self):
        self.manager.add_widget(Factory.ViewBankScreen(name='ViewBankScreen1'))
        self.manager.current = 'ViewBankScreen1'

    def profile(self):
        self.manager.add_widget(Factory.ViewProfileScreen(name='ViewProfileScreen1'))
        self.manager.current = 'ViewProfileScreen1'

    def personal(self):
        self.manager.add_widget(Factory.ViewPersonalScreen(name='ViewPersonalScreen1'))
        self.manager.current = 'ViewPersonalScreen1'

    def go_to_business1(self):
        employee = self.get_business1()
        if employee is None:
            if not self.manager.has_screen('None'):
                self.manager.add_widget(Factory.ViewBusinessScreen1(name='ViewBusinessScreen1'))
            self.manager.current = 'ViewBusinessScreen1'

            print("Business is not available for the user.")
            # Handle this case as per your application's logic
        elif employee == 'Individual' or employee == 'individual':
            if not self.manager.has_screen('Individual'):
                self.manager.add_widget(Factory.ViewBusinessScreen(name='ViewBusinessScreen'))
            self.manager.current = 'ViewBusinessScreen'
        else:
            if not self.manager.has_screen('None'):
                self.manager.add_widget(Factory.ViewBusinessScreen1(name='ViewBusinessScreen1'))
            self.manager.current = 'ViewBusinessScreen1'

    def get_business1(self):
        email = self.get_email()
        profession_records = app_tables.fin_user_profile.search(email_user=email)

        if profession_records:
            # Assuming the profession is stored in the first record if found
            employee = profession_records[0]['lendor_lending_type']
            return employee
        else:
            # Handle case where profession is not found
            return None

    def navigate_based_on_touch1(self):
        profession = self.get_profession()
        if profession is None:
            if not self.manager.has_screen('None'):
                self.manager.add_widget(Factory.ViewProfessionalScreen(name='ViewProfessionalScreen'))
            self.manager.current = 'ViewProfessionalScreen'

            print("Professional is not available for the user.")
            # Handle this case as per your application's logic
        elif profession == 'institutional' or profession == 'Institutional':
            if not self.manager.has_screen('institutional'):
                self.manager.add_widget(Factory.ViewEmployeeScreen(name='ViewEmployeeScreen'))
            self.manager.current = 'ViewEmployeeScreen'
        else:
            if not self.manager.has_screen('None'):
                self.manager.add_widget(Factory.ViewProfessionalScreen(name='ViewProfessionalScreen'))
            self.manager.current = 'ViewProfessionalScreen'

    def get_profession(self):
        email = self.get_email()
        profession_records = app_tables.fin_user_profile.search(email_user=email)

        if profession_records:
            # Assuming the profession is stored in the first record if found
            profession_emp = profession_records[0]['lendor_lending_type']
            return profession_emp
        else:
            # Handle case where profession is not found
            return None

    def Edit_email(self):
        self.manager.add_widget(Factory.ViewEditScreen7(name='ViewEditScreen7'))
        self.manager.current = 'ViewEditScreen7'

    def help_module(self):
        from help_module import HelpScreen
        self.manager.add_widget(Factory.HelpScreen(name='HelpScreen'))
        self.manager.current = 'HelpScreen'


class ViewAccountScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        log_email = anvil.server.call('another_method')
        profile = app_tables.fin_user_profile.search()
        email_user = []
        name_list = []
        p_customer_id = []
        for i in profile:
            email_user.append(i['email_user'])
            name_list.append(i['full_name'])
            p_customer_id.append(i['customer_id'])
        log_index = 0
        if log_email in email_user:
            log_index = email_user.index(log_email)
            self.ids.username.text = name_list[log_index]
            self.ids.username.font_style = 'H6'

        else:
            # Handle the case when 'logged' is not in the status list
            self.ids.username.text = "User welcome to P2P"

        lender_data = app_tables.fin_lender.search()
        lender_cus_id = []
        create_date = []
        for i in lender_data:
            lender_cus_id.append(i['customer_id'])
            create_date.append(i['member_since'])
        #
        if p_customer_id[log_index] in lender_cus_id:
            index1 = lender_cus_id.index(p_customer_id[log_index])
            self.ids.date.text = "[b]Joined Date[/b]: " + str(create_date[index1])
            self.ids.date.text = "Joined Date: " + str(create_date[index1])
        else:
            self.ids.date.text = "[b]Joined Date[/b]: "
            self.ids.date.text = "Joined Date: "

        data = app_tables.fin_wallet.search()
        w_email = []
        w_id = []
        w_amount = []
        for i in data:
            w_email.append(i['user_email'])
            w_id.append(i['wallet_id'])
            w_amount.append(i['wallet_amount'])

        index = 0
        if log_email in w_email:
            index = w_email.index(log_email)
            self.ids.balance.text = "Available Balance: " + "Rs. " + str(round(w_amount[index], 2))
        else:
            print("no email found")

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

    def get_email(self):
        return anvil.server.call('another_method')

    def on_back_button_press(self):
        self.manager.transition = SlideTransition(direction='right')
        self.manager.current = 'LenderDashboard'

    def bank(self):
        self.manager.add_widget(Factory.ViewBankScreen(name='ViewBankScreen1'))
        self.manager.current = 'ViewBankScreen1'

    def profile(self):
        self.manager.add_widget(Factory.ViewProfileScreen(name='ViewProfileScreen1'))
        self.manager.current = 'ViewProfileScreen1'

    def personal(self):
        self.manager.add_widget(Factory.ViewPersonalScreen(name='ViewPersonalScreen1'))
        self.manager.current = 'ViewPersonalScreen1'

    def go_to_business1(self):
        employee = self.get_business1()
        if employee is None:
            if not self.manager.has_screen('None'):
                self.manager.add_widget(Factory.ViewBusinessScreen1(name='ViewBusinessScreen1'))
            self.manager.current = 'ViewBusinessScreen1'

            print("Business is not available for the user.")
            # Handle this case as per your application's logic
        elif employee == 'Individual' or employee == 'individual':
            if not self.manager.has_screen('Individual'):
                self.manager.add_widget(Factory.ViewBusinessScreen(name='ViewBusinessScreen'))
            self.manager.current = 'ViewBusinessScreen'
        else:
            if not self.manager.has_screen('None'):
                self.manager.add_widget(Factory.ViewBusinessScreen1(name='ViewBusinessScreen1'))
            self.manager.current = 'ViewBusinessScreen1'

    def get_business1(self):
        email = self.get_email()
        profession_records = app_tables.fin_user_profile.search(email_user=email)

        if profession_records:
            # Assuming the profession is stored in the first record if found
            employee = profession_records[0]['lendor_lending_type']
            return employee
        else:
            # Handle case where profession is not found
            return None

    def navigate_based_on_touch1(self):
        profession = self.get_profession()
        if profession is None:
            if not self.manager.has_screen('None'):
                self.manager.add_widget(Factory.ViewProfessionalScreen(name='ViewProfessionalScreen'))
            self.manager.current = 'ViewProfessionalScreen'

            print("Professional is not available for the user.")
            # Handle this case as per your application's logic
        elif profession == 'institutional' or profession == 'Institutional':
            if not self.manager.has_screen('institutional'):
                self.manager.add_widget(Factory.ViewEmployeeScreen(name='ViewEmployeeScreen'))
            self.manager.current = 'ViewEmployeeScreen'
        else:
            if not self.manager.has_screen('None'):
                self.manager.add_widget(Factory.ViewProfessionalScreen(name='ViewProfessionalScreen'))
            self.manager.current = 'ViewProfessionalScreen'

    def get_profession(self):
        email = self.get_email()
        profession_records = app_tables.fin_user_profile.search(email_user=email)

        if profession_records:
            # Assuming the profession is stored in the first record if found
            profession_emp = profession_records[0]['lendor_lending_type']
            return profession_emp
        else:
            # Handle case where profession is not found
            return None

    def Edit_email(self):
        self.manager.add_widget(Factory.ViewEditScreen7(name='ViewEditScreen7'))
        self.manager.current = 'ViewEditScreen7'


class ViewProfileScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        email = self.get_email()
        data = app_tables.fin_lender.search(email_id=email)
        investment = []
        email1 = []
        membership = []
        returns = []
        lending = []
        for row in data:
            email1.append(row['email_id'])
            investment.append(row['investment'])
            membership.append(row['membership_type'])
            returns.append(row['return_on_investment'])
            lending.append(row['lending_period'])

        if email in email1:
            index = email1.index(email)
            self.ids.investment.text = str(investment[index])
            self.ids.membership_type.text = str(membership[index])
            self.ids.return_on_investment.text = str(returns[index])
            self.ids.lending_period.text = str(lending[index])

    def refresh(self):
        pass

    def on_back_button_press(self):
        self.manager.current = 'ViewAccountScreen'

    def get_email(self):
        # Make a call to the Anvil server function
        # Replace 'YourAnvilFunction' with the actual name of your Anvil server function
        return anvil.server.call('another_method')

    def on_pre_enter(self):
        Window.bind(on_keyboard=self.on_back_button)

    def on_pre_leave(self):
        Window.unbind(on_keyboard=self.on_back_button)

    def on_back_button(self, instance, key, scancode, codepoint, modifier):
        if key == 27:
            self.on_back_button_press()
            return True
        return False


class ViewEmployeeScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.employee_screen()

    def employee_screen(self):
        email = self.get_email()
        data = app_tables.fin_user_profile.search(email_user=email)
        company_name = []
        email1 = []
        occupation_type = []
        employment_type = []
        organization_type = []
        company_address = []
        landmark = []
        company_ph_no = []
        annual_salary = []
        salary_type = []
        designation = []
        employee_id = []
        last_six_months = []

        for row in data:
            if row['emp_id_proof']:
                image_data = row['emp_id_proof'].get_bytes()
                if isinstance(image_data, bytes):
                    print(f"Image data type: {type(image_data)}, length: {len(image_data)}")
                    # Assuming image_data is already a binary image file
                    try:
                        profile_texture_io = BytesIO(image_data)
                        profile_texture_obj = CoreImage(profile_texture_io, ext='png').texture
                        employee_id.append(profile_texture_obj)
                    except Exception as e:
                        print(f"Error processing image for email {row['email_user']}: {e}")
                        employee_id.append(None)
                else:
                    # If image_data is not bytes, assume it's base64 encoded and decode it
                    try:
                        image_data_binary = base64.b64decode(image_data)
                        print(f"Decoded image data length: {len(image_data_binary)}")
                        profile_texture_io = BytesIO(image_data_binary)
                        profile_texture_obj = CoreImage(profile_texture_io, ext='png').texture
                        employee_id.append(profile_texture_obj)
                    except base64.binascii.Error as e:
                        print(f"Base64 decoding error for email {row['email_user']}: {e}")
                        employee_id.append(None)
                    except Exception as e:
                        print(f"Error processing image for email {row['email_user']}: {e}")
                        employee_id.append(None)
            else:
                employee_id.append(None)

            if row['last_six_month_bank_proof']:
                image_data = row['last_six_month_bank_proof'].get_bytes()
                if isinstance(image_data, bytes):
                    print(f"Image data type: {type(image_data)}, length: {len(image_data)}")
                    # Assuming image_data is already a binary image file
                    try:
                        profile_texture_io = BytesIO(image_data)
                        profile_texture_obj = CoreImage(profile_texture_io, ext='png').texture
                        last_six_months.append(profile_texture_obj)
                    except Exception as e:
                        print(f"Error processing image for email {row['email_user']}: {e}")
                        last_six_months.append(None)
                else:
                    # If image_data is not bytes, assume it's base64 encoded and decode it
                    try:
                        image_data_binary = base64.b64decode(image_data)
                        print(f"Decoded image data length: {len(image_data_binary)}")
                        profile_texture_io = BytesIO(image_data_binary)
                        profile_texture_obj = CoreImage(profile_texture_io, ext='png').texture
                        last_six_months.append(profile_texture_obj)
                    except base64.binascii.Error as e:
                        print(f"Base64 decoding error for email {row['email_user']}: {e}")
                        last_six_months.append(None)
                    except Exception as e:
                        print(f"Error processing image for email {row['email_user']}: {e}")
                        last_six_months.append(None)
            else:
                last_six_months.append(None)

            email1.append(row['email_user'])
            company_name.append(row['company_name'])
            occupation_type.append(row['occupation_type'])
            employment_type.append(row['employment_type'])
            organization_type.append(row['organization_type'])
            company_address.append(row['company_address'])
            landmark.append(row['company_landmark'])
            company_ph_no.append(row['business_no'])
            annual_salary.append(row['annual_salary'])
            salary_type.append(row['salary_type'])
            designation.append(row['designation'])
            employee_id.append(row['emp_id_proof'])
            last_six_months.append(row['last_six_month_bank_proof'])
        if email in email1:
            index = email1.index(email)
            self.ids.employee_id.text = str(employee_id[index])
            self.ids.designation.text = str(designation[index])
            self.ids.salary_type.text = str(salary_type[index])
            self.ids.annual_salary.text = str(annual_salary[index])
            self.ids.company_phone_number.text = str(company_ph_no[index])
            self.ids.company_name.text = str(company_name[index])
            self.ids.occupation_type.text = str(occupation_type[index])
            self.ids.employment_type.text = str(employment_type[index])
            self.ids.landmark.text = str(landmark[index])
            self.ids.last_six_months_bank_statement.text = str(last_six_months[index])
            self.ids.organization_type.text = str(organization_type[index])
            self.ids.company_address.text = str(company_address[index])
            if last_six_months[index]:
                self.ids.last_six_months_bank_statement.texture = last_six_months[index]
            else:
                print("No profile photo found for email:", email)
            if employee_id[index]:
                self.ids.employee_id.texture = employee_id[index]
            else:
                print("No profile photo found for email:", email)
        else:
            print(f"Email {email} not found in data.")

    def refresh(self):
        self.employee_screen()

    def on_employee_edit(self):
        self.manager.add_widget(Factory.ViewEditScreen4(name='ViewEditScreen4'))
        self.manager.current = 'ViewEditScreen4'

    def on_back_button_press(self):
        self.manager.current = 'ViewAccountScreen'

    def get_email(self):
        # Make a call to the Anvil server function
        # Replace 'YourAnvilFunction' with the actual name of your Anvil server function
        return anvil.server.call('another_method')

    def on_pre_enter(self):
        self.employee_screen()
        Window.bind(on_keyboard=self.on_back_button)

    def on_pre_leave(self):
        Window.unbind(on_keyboard=self.on_back_button)

    def on_back_button(self, instance, key, scancode, codepoint, modifier):
        if key == 27:
            self.on_back_button_press()
            return True
        return False


class ViewEditScreen4(Screen):
    MAX_IMAGE_SIZE_MB = 2
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        gender_data = app_tables.fin_occupation_type.search()
        gender_list = []
        for i in gender_data:
            gender_list.append(i['occupation_type'])
        self.unique_gender = []
        for i in gender_list:
            if i not in self.unique_gender:
                self.unique_gender.append(i)
        print(self.unique_gender)
        if len(self.unique_gender) >= 1:
            self.ids.occupation_type.values = ['Select occupation type'] + self.unique_gender
        else:
            self.ids.occupation_type.values = ['Select occupation type']

        present_address = app_tables.fin_lendor_employee_type.search()
        present = []
        for i in present_address:
            present.append(i['lendor_employee_type'])
        self.unique_present = []
        for i in present:
            if i not in self.unique_present:
                self.unique_present.append(i)
        print(self.unique_present)
        if len(self.unique_present) >= 1:
            self.ids.employment_type.values = ['Select employment type'] + self.unique_present
        else:
            self.ids.employment_type.values = ['Select employment type']

        gender_data = app_tables.fin_lendor_organization_type.search()
        gender_list = []
        for i in gender_data:
            gender_list.append(i['lendor_organization_type'])
        self.unique_gender = []
        for i in gender_list:
            if i not in self.unique_gender:
                self.unique_gender.append(i)
        print(self.unique_gender)
        if len(self.unique_gender) >= 1:
            self.ids.organization_type.values = ['Select organization type'] + self.unique_gender
        else:
            self.ids.organization_type.values = ['Select organization type']

        gender_data = app_tables.fin_lendor_salary_type.search()
        gender_list = []
        for i in gender_data:
            gender_list.append(i['lendor_salary_type'])
        self.unique_gender = []
        for i in gender_list:
            if i not in self.unique_gender:
                self.unique_gender.append(i)
        print(self.unique_gender)
        if len(self.unique_gender) >= 1:
            self.ids.salary_type.values = ['Select salary type'] + self.unique_gender
        else:
            self.ids.salary_type.values = ['Select salary type']

        email = self.get_email()
        data = app_tables.fin_user_profile.search(email_user=email)
        company_name = []
        email1 = []
        occupation_type = []
        employment_type = []
        organization_type = []
        company_address = []
        landmark = []
        company_ph_no = []
        annual_salary = []
        salary_type = []
        designation = []
        employee_id = []
        last_six_months = []

        for row in data:
            if row['emp_id_proof']:
                image_data = row['emp_id_proof'].get_bytes()
                if isinstance(image_data, bytes):
                    print(f"Image data type: {type(image_data)}, length: {len(image_data)}")
                    # Assuming image_data is already a binary image file
                    try:
                        profile_texture_io = BytesIO(image_data)
                        profile_texture_obj = CoreImage(profile_texture_io, ext='png').texture
                        employee_id.append(profile_texture_obj)
                    except Exception as e:
                        print(f"Error processing image for email {row['email_user']}: {e}")
                        employee_id.append(None)
                else:
                    # If image_data is not bytes, assume it's base64 encoded and decode it
                    try:
                        image_data_binary = base64.b64decode(image_data)
                        print(f"Decoded image data length: {len(image_data_binary)}")
                        profile_texture_io = BytesIO(image_data_binary)
                        profile_texture_obj = CoreImage(profile_texture_io, ext='png').texture
                        employee_id.append(profile_texture_obj)
                    except base64.binascii.Error as e:
                        print(f"Base64 decoding error for email {row['email_user']}: {e}")
                        employee_id.append(None)
                    except Exception as e:
                        print(f"Error processing image for email {row['email_user']}: {e}")
                        employee_id.append(None)
            else:
                employee_id.append(None)

            if row['last_six_month_bank_proof']:
                image_data = row['last_six_month_bank_proof'].get_bytes()
                if isinstance(image_data, bytes):
                    print(f"Image data type: {type(image_data)}, length: {len(image_data)}")
                    # Assuming image_data is already a binary image file
                    try:
                        profile_texture_io = BytesIO(image_data)
                        profile_texture_obj = CoreImage(profile_texture_io, ext='png').texture
                        last_six_months.append(profile_texture_obj)
                    except Exception as e:
                        print(f"Error processing image for email {row['email_user']}: {e}")
                        last_six_months.append(None)
                else:
                    # If image_data is not bytes, assume it's base64 encoded and decode it
                    try:
                        image_data_binary = base64.b64decode(image_data)
                        print(f"Decoded image data length: {len(image_data_binary)}")
                        profile_texture_io = BytesIO(image_data_binary)
                        profile_texture_obj = CoreImage(profile_texture_io, ext='png').texture
                        last_six_months.append(profile_texture_obj)
                    except base64.binascii.Error as e:
                        print(f"Base64 decoding error for email {row['email_user']}: {e}")
                        last_six_months.append(None)
                    except Exception as e:
                        print(f"Error processing image for email {row['email_user']}: {e}")
                        last_six_months.append(None)
            else:
                last_six_months.append(None)

            email1.append(row['email_user'])
            company_name.append(row['company_name'])
            occupation_type.append(row['occupation_type'])
            employment_type.append(row['employment_type'])
            organization_type.append(row['organization_type'])
            company_address.append(row['company_address'])
            landmark.append(row['company_landmark'])
            company_ph_no.append(row['business_no'])
            annual_salary.append(row['annual_salary'])
            salary_type.append(row['salary_type'])
            designation.append(row['designation'])
            employee_id.append(row['emp_id_proof'])
            last_six_months.append(row['last_six_month_bank_proof'])
        if email in email1:
            index = email1.index(email)
            self.ids.employee_id.text = str(employee_id[index])
            self.ids.designation.text = str(designation[index])
            self.ids.salary_type.text = str(salary_type[index])
            self.ids.annual_salary.text = str(annual_salary[index])
            self.ids.company_phone_number.text = str(company_ph_no[index])
            self.ids.company_name.text = str(company_name[index])
            self.ids.occupation_type.text = str(occupation_type[index])
            self.ids.employment_type.text = str(employment_type[index])
            self.ids.landmark.text = str(landmark[index])
            self.ids.last_six_months_bank_statement.text = str(last_six_months[index])
            self.ids.organization_type.text = str(organization_type[index])
            self.ids.company_address.text = str(company_address[index])
            if last_six_months[index]:
                self.ids.last_six_months_bank_statement.texture = last_six_months[index]
            else:
                print("No profile photo found for email:", email)
            if employee_id[index]:
                self.ids.employee_id.texture = employee_id[index]
            else:
                print("No profile photo found for email:", email)
        else:
            print(f"Email {email} not found in data.")

    def check_and_open_file_manager1(self):
        self.check_and_open_file_manager("upload_icon1", "upload_label1", "selected_file_label1", "employee_id", self.upload_image)

    def check_and_open_file_manager2(self):
        self.check_and_open_file_manager("upload_icon1", "upload_label1", "selected_file_label1",
                                         "last_six_months_bank_statement", self.upload_image1)

    def check_and_open_file_manager(self, icon_id, label_id, file_label_id, image_id,upload_function):
        if platform == 'android':
            if check_permission(Permission.READ_MEDIA_IMAGES):
                self.file_manager_open(icon_id, label_id, file_label_id, image_id,upload_function)
            else:
                self.request_media_images_permission()
        else:
            self.file_manager_open(icon_id, label_id, file_label_id, image_id,upload_function)

    def file_manager_open(self, icon_id, label_id, file_label_id, image_id,upload_function):
        self.file_manager = MDFileManager(
            exit_manager=self.exit_manager,
            select_path=lambda path: self.select_path1(path, icon_id, label_id, file_label_id, image_id,upload_function),
        )
        if platform == 'android':
            primary_external_storage = "/storage/emulated/0"
            self.file_manager.show(primary_external_storage)
        else:
            self.file_manager.show('/')

    # def file_manager_open(self, icon_id, label_id, file_label_id, image_id):
    #     self.file_manager = MDFileManager(
    #         exit_manager=self.exit_manager,
    #         select_path=lambda path: self.select_path2(path, icon_id, label_id, file_label_id, image_id),
    #     )
    #     if platform == 'android':
    #         primary_external_storage = "/storage/emulated/0"
    #         self.file_manager.show(primary_external_storage)
    #     else:
    #         self.file_manager.show('/')

    def select_path1(self, path, icon_id, label_id, file_label_id, image_id,upload_function):
        upload_function(path)  # Upload the selected image using the provided function
        self.ids[image_id].source = path if os.path.getsize(path) <= self.MAX_IMAGE_SIZE_MB * 1024 * 1024 else ''
        self.file_manager.close()


    # def select_path2(self, path, icon_id, label_id, file_label_id, image_id):
    #     self.upload_image1(path)  # Upload the selected image
    #     self.ids[image_id].source = path
    #     self.file_manager.close()

    def upload_image(self, file_path):
        try:
            if os.path.getsize(file_path) > self.MAX_IMAGE_SIZE_MB * 1024 * 1024:
                self.show_validation_error(f"File size should be less than {self.MAX_IMAGE_SIZE_MB}MB")
                return
            user_photo_media = media.from_file(file_path, mime_type='image/png')

            email = self.get_email()
            data = app_tables.fin_user_profile.search(email_user=email)

            if not data:
                print("No data found for email:", email)
                return

            user_data = data[0]

            # Update user_photo column with the media object
            user_data['emp_id_proof'] = user_photo_media
            print("Image uploaded successfully.")
            self.ids['employee_id'].source = ''
        except Exception as e:
            print(f"Error uploading image: {e}")

    def upload_image1(self, file_path):
        try:
            if os.path.getsize(file_path) > self.MAX_IMAGE_SIZE_MB * 1024 * 1024:
                self.show_validation_error(f"File size should be less than {self.MAX_IMAGE_SIZE_MB}MB")
                return
            user_photo_media = media.from_file(file_path, mime_type='image/png')

            email = self.get_email()
            data = app_tables.fin_user_profile.search(email_user=email)

            if not data:
                print("No data found for email:", email)
                return

            user_data = data[0]

            # Update user_photo column with the media object
            user_data['last_six_month_bank_proof'] = user_photo_media

            print("Image uploaded successfully.")
            self.ids['last_six_months_bank_statement'].source = ''
        except Exception as e:
            print(f"Error uploading image: {e}")

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
    def refresh(self):
        pass

    def on_employee_save(self):
        designation = self.ids.designation.text
        salary_type = self.ids.salary_type.text
        annual_salary = self.ids.annual_salary.text
        company_ph_no = self.ids.company_phone_number.text
        company_name = self.ids.company_name.text
        occupation_type = self.ids.occupation_type.text
        employment_type = self.ids.employment_type.text
        landmark = self.ids.landmark.text
        last_six_months = self.ids.last_six_months_bank_statement.text
        organization_type = self.ids.organization_type.text
        company_address = self.ids.company_address.text
        success = self.update_profile_data(designation, salary_type, annual_salary, company_ph_no,
                                           company_name, occupation_type, employment_type, landmark, last_six_months,
                                           organization_type, company_address)
        if success:
            # self.show_validation_error("Database Update Sucessfully.")
            # If the update was successful, navigate back to the dashboard screen
            self.manager.add_widget(Factory.ViewAccountScreen(name='ViewAccountScreen'))
            self.manager.current = 'ViewAccountScreen'

        else:
            # Handle the case where the update failed (e.g., display an error message)
            self.on_back_button_press()

    def update_profile_data(self, designation, salary_type, annual_salary, company_ph_no, company_name,
                            occupation_type, employment_type, landmark, last_six_months, organization_type,
                            company_address):
        email = self.get_email()
        user_profiles = app_tables.fin_user_profile.search(email_user=email)

        # Check if any user profile exists
        if user_profiles:
            # Assuming there should be only one row per unique email address,
            # we retrieve the first matching row
            user_profile = user_profiles[0]

            # Update the user's profile data
            user_profile.update(company_name=company_name,
                                occupation_type=occupation_type,
                                employment_type=employment_type,
                                organization_type=organization_type,
                                company_address=company_address,
                                company_landmark=landmark,
                                business_no=company_ph_no,
                                annual_salary=annual_salary,
                                salary_type=salary_type,
                                designation=designation

                                )
            return True
        else:
            # Handle the case where the user's profile does not exist
            return False

    def exit_manager(self, *args):
        self.file_manager.close()

    def request_media_images_permission(self):
        request_permissions([Permission.READ_MEDIA_IMAGES], self.permission_callback)

    def permission_callback(self, permissions, grants):
        if all(grants.values()):
            self.file_manager_open()
        else:
            self.show_permission_denied()

    def show_permission_denied(self):
        view = ModalView()
        view.add_widget(Button(
            text='Permission NOT granted.\n\n' +
                 'Tap to quit app.\n\n\n' +
                 'If you selected "Don\'t Allow",\n' +
                 'enable permission with App Settings.',
            on_press=self.bye)
        )
        view.open()

    def on_back_button_press(self):
        self.manager.current = 'ViewEmployeeScreen'

    def get_email(self):
        # Make a call to the Anvil server function
        # Replace 'YourAnvilFunction' with the actual name of your Anvil server function
        return anvil.server.call('another_method')

    def on_pre_enter(self):
        Window.bind(on_keyboard=self.on_back_button)

    def on_pre_leave(self):
        Window.unbind(on_keyboard=self.on_back_button)

    def on_back_button(self, instance, key, scancode, codepoint, modifier):
        if key == 27:
            self.on_back_button_press()
            return True
        return False


class ViewBusinessScreen1(Screen):
    def on_back_button_press(self):
        self.manager.current = 'ViewAccountScreen'

    def on_pre_enter(self):
        Window.bind(on_keyboard=self.on_back_button)

    def on_pre_leave(self):
        Window.unbind(on_keyboard=self.on_back_button)

    def on_back_button(self, instance, key, scancode, codepoint, modifier):
        if key == 27:
            self.on_back_button_press()
            return True
        return False


class ViewProfessionalScreen(Screen):
    def on_back_button_press(self):
        self.manager.current = 'ViewAccountScreen'

    def on_pre_enter(self):
        Window.bind(on_keyboard=self.on_back_button)

    def on_pre_leave(self):
        Window.unbind(on_keyboard=self.on_back_button)

    def on_back_button(self, instance, key, scancode, codepoint, modifier):
        if key == 27:
            self.on_back_button_press()
            return True
        return False


class ViewBusinessScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.business_screen()

    def business_screen(self):
        email = self.get_email()
        data = app_tables.fin_user_profile.search(email_user=email)
        business_name = []
        email1 = []
        business_address = []
        business_type = []
        employee_working = []
        year_of_establish = []
        industry_type = []
        last_six_months = []
        upload_last_six_months = []
        din = []
        cin = []
        office_address = []
        office_proof = []
        for row in data:
            if row['last_six_month_bank_proof']:
                image_data = row['last_six_month_bank_proof'].get_bytes()
                if isinstance(image_data, bytes):
                    print(f"Image data type: {type(image_data)}, length: {len(image_data)}")
                    # Assuming image_data is already a binary image file
                    try:
                        profile_texture_io = BytesIO(image_data)
                        profile_texture_obj = CoreImage(profile_texture_io, ext='png').texture
                        upload_last_six_months.append(profile_texture_obj)
                    except Exception as e:
                        print(f"Error processing image for email {row['email_user']}: {e}")
                        upload_last_six_months.append(None)
                else:
                    # If image_data is not bytes, assume it's base64 encoded and decode it
                    try:
                        image_data_binary = base64.b64decode(image_data)
                        print(f"Decoded image data length: {len(image_data_binary)}")
                        profile_texture_io = BytesIO(image_data_binary)
                        profile_texture_obj = CoreImage(profile_texture_io, ext='png').texture
                        upload_last_six_months.append(profile_texture_obj)
                    except base64.binascii.Error as e:
                        print(f"Base64 decoding error for email {row['email_user']}: {e}")
                        upload_last_six_months.append(None)
                    except Exception as e:
                        print(f"Error processing image for email {row['email_user']}: {e}")
                        upload_last_six_months.append(None)
            else:
                upload_last_six_months.append(None)

            if row['proof_verification']:
                image_data = row['proof_verification'].get_bytes()
                if isinstance(image_data, bytes):
                    print(f"Image data type: {type(image_data)}, length: {len(image_data)}")
                    # Assuming image_data is already a binary image file
                    try:
                        profile_texture_io = BytesIO(image_data)
                        profile_texture_obj = CoreImage(profile_texture_io, ext='png').texture
                        office_proof.append(profile_texture_obj)
                    except Exception as e:
                        print(f"Error processing image for email {row['email_user']}: {e}")
                        office_proof.append(None)
                else:
                    # If image_data is not bytes, assume it's base64 encoded and decode it
                    try:
                        image_data_binary = base64.b64decode(image_data)
                        print(f"Decoded image data length: {len(image_data_binary)}")
                        profile_texture_io = BytesIO(image_data_binary)
                        profile_texture_obj = CoreImage(profile_texture_io, ext='png').texture
                        office_proof.append(profile_texture_obj)
                    except base64.binascii.Error as e:
                        print(f"Base64 decoding error for email {row['email_user']}: {e}")
                        office_proof.append(None)
                    except Exception as e:
                        print(f"Error processing image for email {row['email_user']}: {e}")
                        office_proof.append(None)
            else:
                office_proof.append(None)

            email1.append(row['email_user'])
            business_name.append(row['business_name'])
            business_address.append(row['business_add'])
            business_type.append(row['business_type'])
            employee_working.append(row['employees_working'])
            year_of_establish.append(row['year_estd'])
            industry_type.append(row['industry_type'])
            din.append(row['din'])
            cin.append(row['cin'])
            office_address.append(row['registered_off_add'])
            last_six_months.append(row['six_month_turnover'])
            upload_last_six_months.append(row['last_six_month_bank_proof'])
            office_proof.append(row['proof_verification'])

        if email in email1:
            index = email1.index(email)
            self.ids.din.text = str(din[index])
            self.ids.cin.text = str(cin[index])
            self.ids.last_six.text = str(last_six_months[index])
            self.ids.industry_type.text = str(industry_type[index])
            self.ids.business_name.text = str(business_name[index])
            self.ids.business_address.text = str(business_address[index])
            self.ids.business_type.text = str(business_type[index])
            self.ids.year.text = str(year_of_establish[index])
            self.ids.no_working.text = str(employee_working[index])
            self.ids.office_address.text = str(office_address[index])
            if upload_last_six_months[index]:
                self.ids.six_bank.texture = upload_last_six_months[index]
            else:
                print("No profile photo found for email:", email)
            if office_proof[index]:
                self.ids.proof.texture = office_proof[index]
            else:
                print("No profile photo found for email:", email)
        else:
            print(f"Email {email} not found in data.")

    def refresh(self):
        self.business_screen()

    def on_business_edit(self):
        self.manager.add_widget(Factory.ViewEditScreen5(name='ViewEditScreen5'))
        self.manager.current = 'ViewEditScreen5'

    def get_email(self):
        # Make a call to the Anvil server function
        # Replace 'YourAnvilFunction' with the actual name of your Anvil server function
        return anvil.server.call('another_method')

    def on_back_button_press(self):
        self.manager.current = 'ViewAccountScreen'

    def on_pre_enter(self):
        self.business_screen()
        Window.bind(on_keyboard=self.on_back_button)

    def on_pre_leave(self):
        Window.unbind(on_keyboard=self.on_back_button)

    def on_back_button(self, instance, key, scancode, codepoint, modifier):
        if key == 27:
            self.on_back_button_press()
            return True
        return False


class ViewEditScreen5(Screen):
    MAX_IMAGE_SIZE_MB = 2
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        gender_data = app_tables.fin_borrower_no_of_employees.search()
        gender_list = []
        for i in gender_data:
            gender_list.append(i['borrower_no_of_employees'])
        self.unique_gender = []
        for i in gender_list:
            if i not in self.unique_gender:
                self.unique_gender.append(i)
        print(self.unique_gender)
        if len(self.unique_gender) >= 1:
            self.ids.no_working.values = ['Select no of employees'] + self.unique_gender
        else:
            self.ids.no_working.values = ['Select no of employees']

        present_address = app_tables.fin_borrower_business_type.search()
        present = []
        for i in present_address:
            present.append(i['borrower_business_type'])
        self.unique_present = []
        for i in present:
            if i not in self.unique_present:
                self.unique_present.append(i)
        print(self.unique_present)
        if len(self.unique_present) >= 1:
            self.ids.business_type.values = ['Select business type'] + self.unique_present
        else:
            self.ids.business_type.values = ['Select business type']

        email = self.get_email()
        data = app_tables.fin_user_profile.search(email_user=email)
        business_name = []
        email1 = []
        business_address = []
        business_type = []
        employee_working = []
        year_of_establish = []
        industry_type = []
        last_six_months = []
        upload_last_six_months = []
        din = []
        cin = []
        office_address = []
        office_proof = []
        for row in data:
            if row['last_six_month_bank_proof']:
                image_data = row['last_six_month_bank_proof'].get_bytes()
                if isinstance(image_data, bytes):
                    print(f"Image data type: {type(image_data)}, length: {len(image_data)}")
                    # Assuming image_data is already a binary image file
                    try:
                        profile_texture_io = BytesIO(image_data)
                        profile_texture_obj = CoreImage(profile_texture_io, ext='png').texture
                        upload_last_six_months.append(profile_texture_obj)
                    except Exception as e:
                        print(f"Error processing image for email {row['email_user']}: {e}")
                        upload_last_six_months.append(None)
                else:
                    # If image_data is not bytes, assume it's base64 encoded and decode it
                    try:
                        image_data_binary = base64.b64decode(image_data)
                        print(f"Decoded image data length: {len(image_data_binary)}")
                        profile_texture_io = BytesIO(image_data_binary)
                        profile_texture_obj = CoreImage(profile_texture_io, ext='png').texture
                        upload_last_six_months.append(profile_texture_obj)
                    except base64.binascii.Error as e:
                        print(f"Base64 decoding error for email {row['email_user']}: {e}")
                        upload_last_six_months.append(None)
                    except Exception as e:
                        print(f"Error processing image for email {row['email_user']}: {e}")
                        upload_last_six_months.append(None)
            else:
                upload_last_six_months.append(None)

            if row['proof_verification']:
                image_data = row['proof_verification'].get_bytes()
                if isinstance(image_data, bytes):
                    print(f"Image data type: {type(image_data)}, length: {len(image_data)}")
                    # Assuming image_data is already a binary image file
                    try:
                        profile_texture_io = BytesIO(image_data)
                        profile_texture_obj = CoreImage(profile_texture_io, ext='png').texture
                        office_proof.append(profile_texture_obj)
                    except Exception as e:
                        print(f"Error processing image for email {row['email_user']}: {e}")
                        office_proof.append(None)
                else:
                    # If image_data is not bytes, assume it's base64 encoded and decode it
                    try:
                        image_data_binary = base64.b64decode(image_data)
                        print(f"Decoded image data length: {len(image_data_binary)}")
                        profile_texture_io = BytesIO(image_data_binary)
                        profile_texture_obj = CoreImage(profile_texture_io, ext='png').texture
                        office_proof.append(profile_texture_obj)
                    except base64.binascii.Error as e:
                        print(f"Base64 decoding error for email {row['email_user']}: {e}")
                        office_proof.append(None)
                    except Exception as e:
                        print(f"Error processing image for email {row['email_user']}: {e}")
                        office_proof.append(None)
            else:
                office_proof.append(None)

            email1.append(row['email_user'])
            business_name.append(row['business_name'])
            business_address.append(row['business_add'])
            business_type.append(row['business_type'])
            employee_working.append(row['employees_working'])
            year_of_establish.append(row['year_estd'])
            industry_type.append(row['industry_type'])
            din.append(row['din'])
            cin.append(row['cin'])
            office_address.append(row['registered_off_add'])
            last_six_months.append(row['six_month_turnover'])
            upload_last_six_months.append(row['last_six_month_bank_proof'])
            office_proof.append(row['proof_verification'])
        if email in email1:
            index = email1.index(email)
            self.ids.din.text = str(din[index])
            self.ids.cin.text = str(cin[index])
            self.ids.last_six.text = str(last_six_months[index])
            self.ids.industry_type.text = str(industry_type[index])
            self.ids.business_name.text = str(business_name[index])
            self.ids.business_address.text = str(business_address[index])
            self.ids.business_type.text = str(business_type[index])
            self.ids.year.text = str(year_of_establish[index])
            self.ids.no_working.text = str(employee_working[index])
            self.ids.office_address.text = str(office_address[index])
            if upload_last_six_months[index]:
                self.ids.six_bank.texture = upload_last_six_months[index]
            else:
                print("No profile photo found for email:", email)
            if office_proof[index]:
                self.ids.proof.texture = office_proof[index]
            else:
                print("No profile photo found for email:", email)
        else:
            print(f"Email {email} not found in data.")

    def check_and_open_file_manager1(self):
        self.check_and_open_file_manager("upload_icon1", "upload_label1", "selected_file_label1", "six_bank", self.upload_image)

    def check_and_open_file_manager2(self):
        self.check_and_open_file_manager("upload_icon1", "upload_label1", "selected_file_label1",
                                         "proof", self.upload_image1)

    def check_and_open_file_manager(self, icon_id, label_id, file_label_id, image_id,upload_function):
        if platform == 'android':
            if check_permission(Permission.READ_MEDIA_IMAGES):
                self.file_manager_open(icon_id, label_id, file_label_id, image_id,upload_function)
            else:
                self.request_media_images_permission()
        else:
            self.file_manager_open(icon_id, label_id, file_label_id, image_id,upload_function)

    def file_manager_open(self, icon_id, label_id, file_label_id, image_id,upload_function):
        self.file_manager = MDFileManager(
            exit_manager=self.exit_manager,
            select_path=lambda path: self.select_path1(path, icon_id, label_id, file_label_id, image_id,upload_function),
        )
        if platform == 'android':
            primary_external_storage = "/storage/emulated/0"
            self.file_manager.show(primary_external_storage)
        else:
            self.file_manager.show('/')

    # def file_manager_open(self, icon_id, label_id, file_label_id, image_id):
    #     self.file_manager = MDFileManager(
    #         exit_manager=self.exit_manager,
    #         select_path=lambda path: self.select_path2(path, icon_id, label_id, file_label_id, image_id),
    #     )
    #     if platform == 'android':
    #         primary_external_storage = "/storage/emulated/0"
    #         self.file_manager.show(primary_external_storage)
    #     else:
    #         self.file_manager.show('/')

    def exit_manager(self, *args):
        self.file_manager.close()

    def request_media_images_permission(self):
        request_permissions([Permission.READ_MEDIA_IMAGES], self.permission_callback)

    def permission_callback(self, permissions, grants):
        if all(grants.values()):
            self.file_manager_open()
        else:
            self.show_permission_denied()

    def show_permission_denied(self):
        view = ModalView()
        view.add_widget(Button(
            text='Permission NOT granted.\n\n' +
                 'Tap to quit app.\n\n\n' +
                 'If you selected "Don\'t Allow",\n' +
                 'enable permission with App Settings.',
            on_press=self.bye)
        )
        view.open()

    def select_path1(self, path, icon_id, label_id, file_label_id, image_id,upload_function):
        upload_function(path)  # Upload the selected image using the provided function
        self.ids[image_id].source = path if os.path.getsize(path) <= self.MAX_IMAGE_SIZE_MB * 1024 * 1024 else ''
        self.file_manager.close()

    # def select_path2(self, path, icon_id, label_id, file_label_id, image_id,upload_function):
    #     upload_function(path)  # Upload the selected image using the provided function
    #     self.ids[image_id].source = path if os.path.getsize(path) <= self.MAX_IMAGE_SIZE_MB * 1024 * 1024 else ''
    #     self.file_manager.close()

    def upload_image(self, file_path):
        try:
            if os.path.getsize(file_path) > self.MAX_IMAGE_SIZE_MB * 1024 * 1024:
                self.show_validation_error(f"File size should be less than {self.MAX_IMAGE_SIZE_MB}MB")
                return
            user_photo_media = media.from_file(file_path, mime_type='image/png')

            email = self.get_email()
            data = app_tables.fin_user_profile.search(email_user=email)

            if not data:
                print("No data found for email:", email)
                return

            user_data = data[0]

            # Update user_photo column with the media object
            user_data['last_six_month_bank_proof'] = user_photo_media

            print("Image uploaded successfully.")
            self.ids['six_bank'].source = ''
        except Exception as e:
            print(f"Error uploading image: {e}")

    def upload_image1(self, file_path):
        try:
            if os.path.getsize(file_path) > self.MAX_IMAGE_SIZE_MB * 1024 * 1024:
                self.show_validation_error(f"File size should be less than {self.MAX_IMAGE_SIZE_MB}MB")
                return
            user_photo_media = media.from_file(file_path, mime_type='image/png')

            email = self.get_email()
            data = app_tables.fin_user_profile.search(email_user=email)

            if not data:
                print("No data found for email:", email)
                return

            user_data = data[0]

            # Update user_photo column with the media object
            # user_data['last_six_month_bank_proof'] = user_photo_media
            user_data['proof_verification'] = user_photo_media

            print("Image uploaded successfully.")
            self.ids['proof'].source = ''
        except Exception as e:
            print(f"Error uploading image: {e}")

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

    def on_business_save(self):
        business_name = self.ids.business_name.text
        business_address = self.ids.business_address.text
        business_type = self.ids.business_type.text
        employee_working = self.ids.no_working.text
        year_of_establish = self.ids.year.text
        industry_type = self.ids.industry_type.text
        last_six_months = self.ids.last_six.text
        upload_last_six_months = []
        din = self.ids.din.text
        cin = self.ids.cin.text
        office_address = self.ids.office_address.text
        office_proof = []
        success = self.update_profile_data(business_name, business_address, business_type, employee_working,
                                           year_of_establish, industry_type, last_six_months, din, cin, office_address)
        if success:

            # If the update was successful, navigate back to the dashboard screen
            self.manager.add_widget(Factory.ViewAccountScreen(name='ViewAccountScreen'))
            self.manager.current = 'ViewAccountScreen'

        else:
            # Handle the case where the update failed (e.g., display an error message)
            self.on_back_button_press()

    def update_profile_data(self, business_name, business_address, business_type, employee_working, year_of_establish,
                            industry_type, last_six_months, din, cin, office_address):
        email = self.get_email()
        user_profiles = app_tables.fin_user_profile.search(email_user=email)
        try:
            year_of_establish = datetime.strptime(year_of_establish, '%Y-%m-%d').date()
        except ValueError:
            print(f"Invalid date format for borrower_since: {year_of_establish}. Expected format: YYYY-MM-DD")
            return False
        # Check if any user profile exists
        if user_profiles:
            # Assuming there should be only one row per unique email address,
            # we retrieve the first matching row
            user_profile = user_profiles[0]

            # Update the user's profile data
            user_profile.update(business_name=business_name,
                                business_add=business_address,
                                business_type=business_type,
                                employees_working=employee_working,
                                year_estd=year_of_establish,
                                industry_type=industry_type,
                                din=din,
                                cin=cin,
                                registered_off_add=office_address,
                                six_month_turnover=last_six_months
                                )
            return True
        else:
            # Handle the case where the user's profile does not exist
            return False

    def refresh(self):
        pass

    def get_email(self):
        # Make a call to the Anvil server function
        # Replace 'YourAnvilFunction' with the actual name of your Anvil server function
        return anvil.server.call('another_method')

    def on_back_button_press(self):
        self.manager.current = 'ViewBusinessScreen'

    def on_pre_enter(self):
        Window.bind(on_keyboard=self.on_back_button)

    def on_pre_leave(self):
        Window.unbind(on_keyboard=self.on_back_button)

    def on_back_button(self, instance, key, scancode, codepoint, modifier):
        if key == 27:
            self.on_back_button_press()
            return True
        return False


class ViewEditScreen6(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        gender_data = app_tables.fin_lendor_account_type.search()
        gender_list = []
        for i in gender_data:
            gender_list.append(i['lendor_account_type'])
        self.unique_gender = []
        for i in gender_list:
            if i not in self.unique_gender:
                self.unique_gender.append(i)
        print(self.unique_gender)
        if len(self.unique_gender) >= 1:
            self.ids.account_type.values = ['Select account type'] + self.unique_gender
        else:
            self.ids.account_type.values = ['Select account type']
        email = self.get_email()
        data = app_tables.fin_user_profile.search(email_user=email)
        account_holder = []
        email1 = []
        account_type = []
        account_number = []
        bank_name = []
        bank_id = []
        branch_name = []
        for row in data:
            email1.append(row['email_user'])
            account_holder.append(row['account_name'])
            account_type.append(row['account_type'])
            account_number.append(row['account_number'])
            bank_name.append(row['bank_name'])
            bank_id.append(row['bank_id'])
            branch_name.append(row['account_bank_branch'])
        if email in email1:
            index = email1.index(email)
            self.ids.branch_name.text = str(branch_name[index])
            self.ids.holder.text = str(account_holder[index])
            self.ids.account_type.text = str(account_type[index])
            self.ids.bank_id.text = str(bank_id[index])
            self.ids.bank_name.text = str(bank_name[index])
            self.ids.account_number.text = str(account_number[index])

    def refresh(self):
        pass

    def on_bank_save(self):
        account_holder = self.ids.holder.text
        account_type = self.ids.account_type.text
        account_number = self.ids.account_number.text
        bank_name = self.ids.bank_name.text
        bank_id = self.ids.bank_id.text
        branch_name = self.ids.branch_name.text
        success = self.update_profile_data(account_holder, account_type, account_number, branch_name, bank_name,
                                           bank_id)
        if not account_holder or account_holder.isdigit() or not account_holder[0].isupper():
            self.show_validation_errors('Please Enter Valid Full Name')
            return

        success = self.update_profile_data(account_holder, account_type, account_number, branch_name, bank_name,
                                           bank_id)
        if success:
            # self.show_validation_error("Database Update Sucessfully.")
            # If the update was successful, navigate back to the dashboard screen
            self.manager.add_widget(Factory.ViewAccountScreen(name='ViewAccountScreen'))
            self.manager.current = 'ViewAccountScreen'

        else:
            # Handle the case where the update failed (e.g., display an error message)
            self.on_back_button_press()

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
    def update_profile_data(self, account_holder, account_type, account_number, branch_name, bank_name, bank_id):
        email = self.get_email()
        user_profiles = app_tables.fin_user_profile.search(email_user=email)

        # Check if any user profile exists
        if user_profiles:
            # Assuming there should be only one row per unique email address,
            # we retrieve the first matching row
            user_profile = user_profiles[0]

            # Update the user's profile data
            user_profile.update(account_name=account_holder,
                                account_type=account_type,
                                account_number=account_number,
                                bank_name=bank_name,
                                bank_id=bank_id,
                                account_bank_branch=branch_name
                                )
            return True
        else:
            # Handle the case where the user's profile does not exist
            return False

    def on_back_button_press(self):
        self.manager.current = 'ViewBankScreen'

    def get_email(self):
        # Make a call to the Anvil server function
        # Replace 'YourAnvilFunction' with the actual name of your Anvil server function
        return anvil.server.call('another_method')

    def on_pre_enter(self):
        Window.bind(on_keyboard=self.on_back_button)

    def on_pre_leave(self):
        Window.unbind(on_keyboard=self.on_back_button)

    def on_back_button(self, instance, key, scancode, codepoint, modifier):
        if key == 27:
            self.on_back_button_press()
            return True
        return False


class ViewBankScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.bank_screen()

    def bank_screen(self):
        email = self.get_email()
        data = app_tables.fin_user_profile.search(email_user=email)
        account_holder = []
        email1 = []
        account_type = []
        account_number = []
        bank_name = []
        bank_id = []
        branch_name = []
        for row in data:
            email1.append(row['email_user'])
            account_holder.append(row['account_name'])
            account_type.append(row['account_type'])
            account_number.append(row['account_number'])
            bank_name.append(row['bank_name'])
            bank_id.append(row['bank_id'])
            branch_name.append(row['account_bank_branch'])
        if email in email1:
            index = email1.index(email)
            self.ids.branch_name.text = str(branch_name[index])
            self.ids.holder.text = str(account_holder[index])
            self.ids.account_type.text = str(account_type[index])
            self.ids.bank_id.text = str(bank_id[index])
            self.ids.bank_name.text = str(bank_name[index])
            self.ids.account_number.text = str(account_number[index])

    def refresh(self):
        self.bank_screen()

    def on_back_button_press(self):
        self.manager.current = 'ViewAccountScreen'

    def get_email(self):
        # Make a call to the Anvil server function
        # Replace 'YourAnvilFunction' with the actual name of your Anvil server function
        return anvil.server.call('another_method')

    def on_bank_edit(self):
        self.manager.add_widget(Factory.ViewEditScreen6(name='ViewEditScreen6'))
        self.manager.current = 'ViewEditScreen6'

    def on_pre_enter(self):
        self.bank_screen()
        Window.bind(on_keyboard=self.on_back_button)

    def on_pre_leave(self):
        Window.unbind(on_keyboard=self.on_back_button)

    def on_back_button(self, instance, key, scancode, codepoint, modifier):
        if key == 27:
            self.on_back_button_press()
            return True
        return False


class ViewPersonalScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.refresh_profile_data()

    def refresh_profile_data(self, dt=None):
        email = self.get_email()
        data = app_tables.fin_user_profile.search(email_user=email)

        if not data:
            print("No data found for email:", email)
            return

        name = []
        email1 = []
        mobile_no = []
        dob = []
        gender = []
        marrital_status = []
        alternate_email = []
        gov_id1 = []
        gov_id2 = []
        address1 = []
        address2 = []
        type_of_address = []
        staying_address = []
        zip_code = []
        state = []
        country = []
        qualification = []
        upload_gov_id1 = []
        upload_gov_id2 = []
        photo = []

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

            if row['aadhaar_photo']:
                image_data = row['aadhaar_photo'].get_bytes()
                if isinstance(image_data, bytes):
                    print(f"Image data type: {type(image_data)}, length: {len(image_data)}")
                    # Assuming image_data is already a binary image file
                    try:
                        profile_texture_io = BytesIO(image_data)
                        profile_texture_obj = CoreImage(profile_texture_io, ext='png').texture
                        upload_gov_id1.append(profile_texture_obj)
                    except Exception as e:
                        print(f"Error processing image for email {row['email_user']}: {e}")
                        upload_gov_id1.append(None)
                else:
                    # If image_data is not bytes, assume it's base64 encoded and decode it
                    try:
                        image_data_binary = base64.b64decode(image_data)
                        print(f"Decoded image data length: {len(image_data_binary)}")
                        profile_texture_io = BytesIO(image_data_binary)
                        profile_texture_obj = CoreImage(profile_texture_io, ext='png').texture
                        upload_gov_id1.append(profile_texture_obj)
                    except base64.binascii.Error as e:
                        print(f"Base64 decoding error for email {row['email_user']}: {e}")
                        upload_gov_id1.append(None)
                    except Exception as e:
                        print(f"Error processing image for email {row['email_user']}: {e}")
                        upload_gov_id1.append(None)
            else:
                upload_gov_id1.append(None)

            if row['pan_photo']:
                image_data = row['pan_photo'].get_bytes()
                if isinstance(image_data, bytes):
                    print(f"Image data type: {type(image_data)}, length: {len(image_data)}")
                    # Assuming image_data is already a binary image file
                    try:
                        profile_texture_io = BytesIO(image_data)
                        profile_texture_obj = CoreImage(profile_texture_io, ext='png').texture
                        upload_gov_id2.append(profile_texture_obj)
                    except Exception as e:
                        print(f"Error processing image for email {row['email_user']}: {e}")
                        upload_gov_id2.append(None)
                else:
                    # If image_data is not bytes, assume it's base64 encoded and decode it
                    try:
                        image_data_binary = base64.b64decode(image_data)
                        print(f"Decoded image data length: {len(image_data_binary)}")
                        profile_texture_io = BytesIO(image_data_binary)
                        profile_texture_obj = CoreImage(profile_texture_io, ext='png').texture
                        upload_gov_id2.append(profile_texture_obj)
                    except base64.binascii.Error as e:
                        print(f"Base64 decoding error for email {row['email_user']}: {e}")
                        upload_gov_id2.append(None)
                    except Exception as e:
                        print(f"Error processing image for email {row['email_user']}: {e}")
                        upload_gov_id2.append(None)
            else:
                upload_gov_id2.append(None)

            name.append(row['full_name'])
            alternate_email.append(row['mail_id'])
            email1.append(row['email_user'])
            mobile_no.append(row['mobile'])
            dob.append(row['date_of_birth'])
            staying_address.append(row['duration_at_address'])
            gov_id1.append(row['aadhaar_no'])
            gov_id2.append(row['pan_number'])
            address1.append(row['street_adress_1'])
            address2.append(row['street_address_2'])
            type_of_address.append(row['present_address'])
            gender.append(row['gender'])
            marrital_status.append(row['marital_status'])
            zip_code.append(row['pincode'])
            state.append(row['state'])
            country.append(row['city'])
            qualification.append(row['qualification'])
            upload_gov_id1.append(row['aadhaar_photo'])
            upload_gov_id2.append(row['pan_photo'])

        if email in email1:
            index = email1.index(email)
            self.ids.name.text = str(name[index])
            self.ids.email_id.text = str(alternate_email[index])
            self.ids.email.text = str(email1[index])
            self.ids.mobile_no.text = str(mobile_no[index])
            self.ids.dob.text = str(dob[index])
            self.ids.address1.text = str(address1[index])
            self.ids.address2.text = str(address2[index])
            self.ids.type.text = str(type_of_address[index])
            self.ids.gov_id1.text = str(gov_id1[index])
            self.ids.gov_id2.text = str(gov_id2[index])
            self.ids.zip_code.text = str(zip_code[index])
            self.ids.state.text = str(state[index])
            self.ids.country.text = str(country[index])
            self.ids.qualification.text = str(qualification[index])
            self.ids.stay.text = str(staying_address[index])
            self.ids.gender.text = str(gender[index])
            self.ids.marrital_status.text = str(marrital_status[index])

            if photo[index]:
                self.ids.selected_image1.texture = photo[index]
            else:
                print("No profile photo found for email:", email)
            if upload_gov_id1[index]:
                self.ids.upload_gov_id1_img.texture = upload_gov_id1[index]
            else:
                print("No profile photo found for email:", email)
            if upload_gov_id2[index]:
                self.ids.upload_gov_id2_img.texture = upload_gov_id2[index]
            else:
                print("No profile photo found for email:", email)
        else:
            print(f"Email {email} not found in data.")

    def upload_image1(self, file_path):
        try:
            user_photo_media = media.from_file(file_path, mime_type='image/png')

            email = self.get_email()
            data = app_tables.fin_user_profile.search(email_user=email)

            if not data:
                print("No data found for email:", email)
                return

            user_data = data[0]

            # Update user_photo column with the media object
            user_data['user_photo'] = user_photo_media

            print("Image uploaded successfully.")
        except Exception as e:
            print(f"Error uploading image: {e}")

    def get_email(self):
        # Make a call to the Anvil server function
        # Replace 'YourAnvilFunction' with the actual name of your Anvil server function
        return anvil.server.call('another_method')

    def refresh(self):
        self.refresh_profile_data()

    def get_table(self):
        # Make a call to the Anvil server function
        # Replace 'YourAnvilFunction' with the actual name of your Anvil server function
        return anvil.server.call('profile')

    def check_and_open_file_manager1(self):
        self.check_and_open_file_manager("upload_icon1", "upload_label1", "selected_file_label1", "selected_image1")

    def check_and_open_file_manager(self, icon_id, label_id, file_label_id, image_id):
        if platform == 'android':
            if check_permission(Permission.READ_MEDIA_IMAGES):
                self.file_manager_open(icon_id, label_id, file_label_id, image_id)
            else:
                self.request_media_images_permission()
        else:
            self.file_manager_open(icon_id, label_id, file_label_id, image_id)

    def file_manager_open(self, icon_id, label_id, file_label_id, image_id):
        self.file_manager = MDFileManager(
            exit_manager=self.exit_manager,
            select_path=lambda path: self.select_path1(path, icon_id, label_id, file_label_id, image_id),
        )
        if platform == 'android':
            primary_external_storage = "/storage/emulated/0"
            self.file_manager.show(primary_external_storage)
        else:
            self.file_manager.show('/')

    def select_path1(self, path, icon_id, label_id, file_label_id, image_id):
        self.upload_image1(path)  # Upload the selected image
        self.ids[image_id].source = path
        self.file_manager.close()

    def exit_manager(self, *args):
        self.file_manager.close()

    def request_media_images_permission(self):
        request_permissions([Permission.READ_MEDIA_IMAGES], self.permission_callback)

    def permission_callback(self, permissions, grants):
        if all(grants.values()):
            self.file_manager_open()
        else:
            self.show_permission_denied()

    def show_permission_denied(self):
        view = ModalView()
        view.add_widget(Button(
            text='Permission NOT granted.\n\n' +
                 'Tap to quit app.\n\n\n' +
                 'If you selected "Don\'t Allow",\n' +
                 'enable permission with App Settings.',
            on_press=self.bye)
        )
        view.open()

    def on_pre_enter(self):
        self.refresh_profile_data()
        Window.bind(on_keyboard=self.on_back_button)

    def on_pre_leave(self):
        Window.unbind(on_keyboard=self.on_back_button)

    def on_back_button(self, instance, key, scancode, codepoint, modifier):
        if key == 27:
            self.on_back_button_press()
            return True
        return False

    def on_edit(self):
        self.manager.add_widget(Factory.ViewEditScreen1(name='ViewEditScreen1'))
        self.manager.current = 'ViewEditScreen1'

    def go_back(self):
        self.manager.transition = SlideTransition(direction='right')
        self.manager.current = 'ViewAccountScreen'

    def on_back_button_press(self):
        self.manager.current = 'ViewAccountScreen'


class ViewEditScreen7(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        email = self.get_email()
        data = app_tables.fin_user_profile.search()
        email1 = []
        photo = []

        for row in data:
            if row['user_photo']:
                image_data = row['user_photo'].get_bytes()
                if isinstance(image_data, bytes):
                    print(f"Image data type: {type(image_data)}, length: {len(image_data)}")
                    try:
                        profile_texture_io = BytesIO(image_data)
                        profile_texture_obj = CoreImage(profile_texture_io, ext='png').texture
                        photo.append(profile_texture_obj)
                    except Exception as e:
                        print(f"Error processing image for email {row['email_user']}: {e}")
                        photo.append(None)
                else:
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
            self.ids.email.text = str(email1[index])

            if photo[index]:
                self.ids.selected_image1.texture = photo[index]
            else:
                print("No profile photo found for email:", email)
        else:
            print(f"Email {email} not found in data.")

    def save_edited_data1(self):
        email1 = self.ids.email.text

        success = self.update_profile_data(email1)

        if success:
            # Show a success message and wait for user confirmation to log out
            self.show_success_message(self.logout_and_go_to_main_screen)
        else:
            # Handle the case where the update failed (e.g., display an error message)
            self.on_back_button_press()

    def show_success_message(self, on_ok_press):
        dialog = MDDialog(
            title="Success",
            text="Email updated successfully \n Please re-login",
            size_hint=(0.8, None),
            height=dp(200),
            buttons=[
                MDRectangleFlatButton(
                    text="OK",
                    text_color=(0.043, 0.145, 0.278, 1),
                    on_release=lambda x: self._on_ok_press(dialog, on_ok_press)
                )
            ]
        )
        dialog.open()

    def _on_ok_press(self, dialog, on_ok_press):
        dialog.dismiss()
        on_ok_press()

    def logout_and_go_to_main_screen(self):
        # Update user status in 'emails.json'
        with open("emails.json", "r+") as file:
            try:
                user_data = json.load(file)
            except json.JSONDecodeError:
                user_data = {}  # Initialize as empty dictionary if file is empty or invalid JSON

            if isinstance(user_data, dict):
                for email, data in user_data.items():
                    if isinstance(data, dict) and data.get("logged_status", False):
                        # Update user's logged_status and user_type
                        data["logged_status"] = False
                        data["user_type"] = ""
                        break
                # Move the cursor to the beginning of the file
                file.seek(0)
                # Write the updated data back to the file
                json.dump(user_data, file, indent=4)
                # Truncate any remaining data in the file
                file.truncate()
        self.manager.current = 'MainScreen'

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

    def update_profile_data(self, email1):
        email = self.get_email()
        data = app_tables.fin_user_profile.search(email_user=email)
        if data:
            # Assuming there should be only one row per unique email address,
            # we retrieve the first matching row
            user_profile = data[0]
            user_profile.update(
                email_user=email1,
            )

            # Update all related tables
            self.update_all_related_tables(email, email1)
            return True
        else:
            print("No data found for email:", email)
            return False

    def update_all_related_tables(self, old_email, new_email):
        try:
            # Users
            user_table = app_tables.users.search(email=old_email)
            for user in user_table:
                user['email'] = new_email
                user.update()

            # Wallet Transactions
            wallet_transactions = app_tables.fin_wallet_transactions.search(user_email=old_email)
            for loans in wallet_transactions:
                loans['user_email'] = new_email
                loans.update()

            # Wallet Bank Account
            wallet_bank_account_table = app_tables.fin_wallet_bank_account_table.search(user_email=old_email)
            for account in wallet_bank_account_table:
                account['user_email'] = new_email
                account.update()

            # Wallet
            wallet = app_tables.fin_wallet.search(user_email=old_email)
            for account in wallet:
                account['user_email'] = new_email
                account.update()

            # EMI Details
            emi_details = app_tables.fin_emi_table.search(lender_email=old_email)
            for loans in emi_details:
                loans['lender_email'] = new_email
                loans.update()

            # Extends Table
            extends_table = app_tables.fin_extends_loan.search(lender_email_id=old_email)
            for loans in extends_table:
                loans['lender_email_id'] = new_email
                loans.update()

            # Foreclosure
            foreclosure = app_tables.fin_foreclosure.search(lender_email_id=old_email)
            for loans in foreclosure:
                loans['lender_email_id'] = new_email
                loans.update()

            # Lender
            fin_lender = app_tables.fin_lender.search(email_id=old_email)
            for lender in fin_lender:
                lender['email_id'] = new_email
                lender.update()

            # Loan Details
            loan_details = app_tables.fin_loan_details.search(lender_email_id=old_email)
            for loans in loan_details:
                loans['lender_email_id'] = new_email
                loans.update()

            # Report Problem
            report_problem = app_tables.fin_reported_problems.search(email=old_email)
            for problem in report_problem:
                problem['email'] = new_email
                problem.update()

        except Exception as e:
            print(f"An error occurred while updating related tables: {e}")

    def get_email(self):
        return anvil.server.call('another_method')

    def on_pre_enter(self):
        Window.bind(on_keyboard=self.on_back_button)

    def on_pre_leave(self):
        Window.unbind(on_keyboard=self.on_back_button)

    def on_back_button(self, instance, key, scancode, codepoint, modifier):
        if key == 27:
            self.on_back_button_press()
            return True
        return False

    def go_back(self):
        self.manager.transition = SlideTransition(direction='right')
        self.manager.current = 'ViewAccountScreen'

    def on_back_button_press(self):
        self.manager.current = 'ViewAccountScreen'

    def refresh(self):
        self.__init__()


class ViewEditScreen1(Screen):
    MAX_IMAGE_SIZE_MB = 2
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        gender_data = app_tables.fin_gender.search()
        gender_list = []
        for i in gender_data:
            gender_list.append(i['gender'])
        self.unique_gender = []
        for i in gender_list:
            if i not in self.unique_gender:
                self.unique_gender.append(i)
        print(self.unique_gender)
        if len(self.unique_gender) >= 1:
            self.ids.gender.values = ['Select a Gender'] + self.unique_gender
        else:
            self.ids.gender.values = ['Select a Gender']

        present_address = app_tables.fin_present_address.search()
        present = []
        for i in present_address:
            present.append(i['present_address'])
        self.unique_present = []
        for i in present:
            if i not in self.unique_present:
                self.unique_present.append(i)
        print(self.unique_present)
        if len(self.unique_present) >= 1:
            self.ids.type.values = ['Select present address'] + self.unique_present
        else:
            self.ids.type.values = ['Select present address']

        gender_data = app_tables.fin_duration_at_address.search()
        gender_list = []
        for i in gender_data:
            gender_list.append(i['duration_at_address'])
        self.unique_gender = []
        for i in gender_list:
            if i not in self.unique_gender:
                self.unique_gender.append(i)
        print(self.unique_gender)
        if len(self.unique_gender) >= 1:
            self.ids.stay.values = ['Select staying address'] + self.unique_gender
        else:
            self.ids.stay.values = ['Select staying address']

        gender_data = app_tables.fin_lendor_marrital_status.search()
        gender_list = []
        for i in gender_data:
            gender_list.append(i['lendor_marrital_status'])
        self.unique_gender = []
        for i in gender_list:
            if i not in self.unique_gender:
                self.unique_gender.append(i)
        print(self.unique_gender)
        if len(self.unique_gender) >= 1:
            self.ids.marrital_status.values = ['Select marrital status'] + self.unique_gender
        else:
            self.ids.marrital_status.values = ['Select marrital status']

        gender_data = app_tables.fin_lendor_qualification.search()
        gender_list = []
        for i in gender_data:
            gender_list.append(i['lendor_qualification'])
        self.unique_gender = []
        for i in gender_list:
            if i not in self.unique_gender:
                self.unique_gender.append(i)
        print(self.unique_gender)
        if len(self.unique_gender) >= 1:
            self.ids.marrital_status.values = ['Select qualification'] + self.unique_gender
        else:
            self.ids.marrital_status.values = ['Select qualification']

        email = self.get_email()
        data = app_tables.fin_user_profile.search()
        name = []
        email1 = []
        mobile_no = []
        dob = []
        gender = []
        marrital_status = []
        alternate_email = []
        gov_id1 = []
        gov_id2 = []
        address1 = []
        address2 = []
        type_of_address = []
        staying_address = []
        zip_code = []
        state = []
        country = []
        qualification = []
        upload_gov_id1 = []
        upload_gov_id2 = []
        photo = []

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

            if row['aadhaar_photo']:
                image_data = row['aadhaar_photo'].get_bytes()
                if isinstance(image_data, bytes):
                    print(f"Image data type: {type(image_data)}, length: {len(image_data)}")
                    # Assuming image_data is already a binary image file
                    try:
                        profile_texture_io = BytesIO(image_data)
                        profile_texture_obj = CoreImage(profile_texture_io, ext='png').texture
                        upload_gov_id1.append(profile_texture_obj)
                    except Exception as e:
                        print(f"Error processing image for email {row['email_user']}: {e}")
                        upload_gov_id1.append(None)
                else:
                    # If image_data is not bytes, assume it's base64 encoded and decode it
                    try:
                        image_data_binary = base64.b64decode(image_data)
                        print(f"Decoded image data length: {len(image_data_binary)}")
                        profile_texture_io = BytesIO(image_data_binary)
                        profile_texture_obj = CoreImage(profile_texture_io, ext='png').texture
                        upload_gov_id1.append(profile_texture_obj)
                    except base64.binascii.Error as e:
                        print(f"Base64 decoding error for email {row['email_user']}: {e}")
                        upload_gov_id1.append(None)
                    except Exception as e:
                        print(f"Error processing image for email {row['email_user']}: {e}")
                        upload_gov_id1.append(None)
            else:
                upload_gov_id1.append(None)

            if row['pan_photo']:
                image_data = row['pan_photo'].get_bytes()
                if isinstance(image_data, bytes):
                    print(f"Image data type: {type(image_data)}, length: {len(image_data)}")
                    # Assuming image_data is already a binary image file
                    try:
                        profile_texture_io = BytesIO(image_data)
                        profile_texture_obj = CoreImage(profile_texture_io, ext='png').texture
                        upload_gov_id2.append(profile_texture_obj)
                    except Exception as e:
                        print(f"Error processing image for email {row['email_user']}: {e}")
                        upload_gov_id2.append(None)
                else:
                    # If image_data is not bytes, assume it's base64 encoded and decode it
                    try:
                        image_data_binary = base64.b64decode(image_data)
                        print(f"Decoded image data length: {len(image_data_binary)}")
                        profile_texture_io = BytesIO(image_data_binary)
                        profile_texture_obj = CoreImage(profile_texture_io, ext='png').texture
                        upload_gov_id2.append(profile_texture_obj)
                    except base64.binascii.Error as e:
                        print(f"Base64 decoding error for email {row['email_user']}: {e}")
                        upload_gov_id2.append(None)
                    except Exception as e:
                        print(f"Error processing image for email {row['email_user']}: {e}")
                        upload_gov_id2.append(None)
            else:
                upload_gov_id2.append(None)

            name.append(row['full_name'])
            alternate_email.append(row['mail_id'])
            email1.append(row['email_user'])
            mobile_no.append(row['mobile'])
            dob.append(row['date_of_birth'])
            staying_address.append(row['duration_at_address'])
            gov_id1.append(row['aadhaar_no'])
            gov_id2.append(row['pan_number'])
            address1.append(row['street_adress_1'])
            address2.append(row['street_address_2'])
            type_of_address.append(row['present_address'])
            gender.append(row['gender'])
            marrital_status.append(row['marital_status'])
            zip_code.append(row['pincode'])
            state.append(row['state'])
            country.append(row['city'])
            qualification.append(row['qualification'])

        if email in email1:
            index = email1.index(email)
            self.ids.name.text = str(name[index])
            self.ids.email_id.text = str(alternate_email[index])
            self.ids.email.text = str(email1[index])
            self.ids.mobile_no.text = str(mobile_no[index])
            self.ids.dob.text = str(dob[index])
            self.ids.address1.text = str(address1[index])
            self.ids.address2.text = str(address2[index])
            self.ids.type.text = str(type_of_address[index])
            self.ids.gov_id1.text = str(gov_id1[index])
            self.ids.gov_id2.text = str(gov_id2[index])
            self.ids.zip_code.text = str(zip_code[index])
            self.ids.state.text = str(state[index])
            self.ids.country.text = str(country[index])
            self.ids.qualification.text = str(qualification[index])
            self.ids.gender.text = str(gender[index])
            self.ids.marrital_status.text = str(marrital_status[index])

            if photo[index]:
                self.ids.selected_image1.texture = photo[index]
            else:
                print("No profile photo found for email:", email)
            if upload_gov_id1[index]:
                self.ids.upload_gov_id1_img.texture = upload_gov_id1[index]
            else:
                print("No profile photo found for email:", email)
            if upload_gov_id2[index]:
                self.ids.upload_gov_id2_img.texture = upload_gov_id2[index]
            else:
                print("No profile photo found for email:", email)
        else:
            print(f"Email {email} not found in data.")

    def upload_image1(self, file_path):
        try:
            if os.path.getsize(file_path) > self.MAX_IMAGE_SIZE_MB * 1024 * 1024:
                self.show_validation_error(f"File size should be less than {self.MAX_IMAGE_SIZE_MB}MB")
                return
            user_photo_media = media.from_file(file_path, mime_type='image/png')

            email = self.get_email()
            data = app_tables.fin_user_profile.search(email_user=email)

            if not data:
                print("No data found for email:", email)
                return

            user_data = data[0]

            # Update user_photo column with the media object
            user_data['user_photo'] = user_photo_media

            print("Image uploaded successfully.")
            self.ids['selected_image1'].source = ''
        except Exception as e:
            print(f"Error uploading image: {e}")

    def upload_image2(self, file_path):
        try:
            if os.path.getsize(file_path) > self.MAX_IMAGE_SIZE_MB * 1024 * 1024:
                self.show_validation_error(f"File size should be less than {self.MAX_IMAGE_SIZE_MB}MB")
                return
            user_photo_media = media.from_file(file_path, mime_type='image/png')

            email = self.get_email()
            data = app_tables.fin_user_profile.search(email_user=email)

            if not data:
                print("No data found for email:", email)
                return

            user_data = data[0]
            user_data['aadhaar_photo'] = user_photo_media
            print("Image uploaded successfully.")
            self.ids['upload_gov_id1_img'].source = ''
        except Exception as e:
            print(f"Error uploading image: {e}")

    def upload_image3(self, file_path):
        try:
            user_photo_media = media.from_file(file_path, mime_type='image/png')

            email = self.get_email()
            data = app_tables.fin_user_profile.search(email_user=email)

            if not data:
                print("No data found for email:", email)
                return

            user_data = data[0]

            # Update user_photo column with the media object
            user_data['pan_photo'] = user_photo_media

            print("Image uploaded successfully.")
            self.ids['upload_gov_id2_img'].source = ''
        except Exception as e:
            print(f"Error uploading image: {e}")

    def save_edited_data(self):
        # Retrieve the edited data from the UI
        name = self.ids.name.text
        email1 = self.ids.email.text
        mobile_no = self.ids.mobile_no.text
        dob = self.ids.dob.text
        gender = self.ids.gender.text
        marrital_status = self.ids.marrital_status.text
        alternate_email = self.ids.email_id.text
        gov_id1 = self.ids.gov_id1.text
        gov_id2 = self.ids.gov_id2.text
        address1 = self.ids.address1.text
        address2 = self.ids.address2.text
        type_of_address = self.ids.type.text
        staying_address = self.ids.stay.text
        zip_code = self.ids.zip_code.text
        state = self.ids.state.text
        country = self.ids.country.text
        qualification = self.ids.qualification.text

        if not name or len(name.split()) < 2 or name.isdigit() or not name[0].isupper():
            self.show_validation_error('Please Enter Full Name and First letter as capital ')
            return
        # Update the database with the edited data
        # Replace 'update_profile_data' with your actual database update function
        success = self.update_profile_data(qualification, country, state, zip_code, staying_address, type_of_address,
                                           address1, address2, gov_id1, gov_id2, alternate_email, marrital_status, name,
                                           email1, mobile_no, dob, gender)

        if success:
            # self.show_validation_error("Database Update Sucessfully.")
            # If the update was successful, navigate back to the dashboard screen
            self.manager.add_widget(Factory.ViewAccountScreen(name='ViewAccountScreen'))
            self.manager.current = 'ViewAccountScreen'

        else:
            # Handle the case where the update failed (e.g., display an error message)
            self.on_back_button_press()

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

    def update_profile_data(self, qualification, country, state, zip_code, staying_address, type_of_address, address1,
                            address2, gov_id1, gov_id2, alternate_email, marrital_status, name, email1, mobile_no, dob,
                            gender):
        email = self.get_email()
        data = app_tables.fin_user_profile.search(email_user=email)
        if data:
            # Assuming there should be only one row per unique email address,
            # we retrieve the first matching row
            user_profile = data[0]
            user_profile.update(full_name=name,
                                mail_id=alternate_email,
                                email_user=email1,
                                mobile=mobile_no,
                                gender=gender,
                                duration_at_address=staying_address,
                                aadhaar_no=gov_id1,
                                pan_number=gov_id2,
                                street_adress_1=address1,
                                street_address_2=address2,
                                present_address=type_of_address,
                                marital_status=marrital_status,
                                date_of_birth=dob,
                                pincode=zip_code,
                                state=state,
                                city=country,
                                qualification=qualification)

            # Update all related tables
            self.update_all_related_tables(email, email1, name, mobile_no)
            return True
        else:
            print("No data found for email:", email)
            return False

    def update_all_related_tables(self, old_email, new_email, name, mobile_no):
        try:
            # Users
            user_table = app_tables.users.search(email=old_email)
            for user in user_table:
                user['email'] = new_email
                user.update()

            # Wallet Transactions
            wallet_transactions = app_tables.fin_wallet_transactions.search(user_email=old_email)
            for loans in wallet_transactions:
                loans['user_email'] = new_email
                loans.update()

            # Wallet Bank Account
            wallet_bank_account_table = app_tables.fin_wallet_bank_account_table.search(user_email=old_email)
            for account in wallet_bank_account_table:
                account['user_email'] = new_email
                account.update()

            # Wallet
            wallet = app_tables.fin_wallet.search(user_email=old_email)
            for account in wallet:
                account['user_email'] = new_email
                account['user_name'] = name
                account.update()

            # EMI Details
            emi_details = app_tables.fin_emi_table.search(lender_email=old_email)
            for loans in emi_details:
                loans['lender_email'] = new_email
                loans.update()

            # Extends Table
            extends_table = app_tables.fin_extends_loan.search(lender_email_id=old_email)
            for loans in extends_table:
                loans['lender_email_id'] = new_email
                loans['lender_full_name'] = name
                loans.update()

            # Foreclosure
            foreclosure = app_tables.fin_foreclosure.search(lender_email_id=old_email)
            for loans in foreclosure:
                loans['lender_email_id'] = new_email
                loans['lender_full_name'] = name
                loans.update()

            # Lender
            fin_lender = app_tables.fin_lender.search(email_id=old_email)
            for lender in fin_lender:
                lender['email_id'] = new_email
                lender['user_name'] = name
                lender.update()

            # Loan Details
            loan_details = app_tables.fin_loan_details.search(lender_email_id=old_email)
            for loans in loan_details:
                loans['lender_email_id'] = new_email
                loans['lender_full_name'] = name
                loans.update()

            # Report Problem
            report_problem = app_tables.fin_reported_problems.search(email=old_email)
            for problem in report_problem:
                problem['email'] = new_email
                problem['name'] = name
                problem['mobile_number'] = mobile_no
                problem.update()

        except Exception as e:
            print(f"An error occurred while updating related tables: {e}")

    def get_email(self):
        # Make a call to the Anvil server function
        # Replace 'YourAnvilFunction' with the actual name of your Anvil server function
        return anvil.server.call('another_method')

    def refresh(self):
        pass

    def get_table(self):
        # Make a call to the Anvil server function
        # Replace 'YourAnvilFunction' with the actual name of your Anvil server function
        return anvil.server.call('profile')

    def check_and_open_file_manager1(self):
        self.check_and_open_file_manager("upload_icon1", "upload_label1", "selected_file_label1", "selected_image1", self.upload_image1)

    def check_and_open_file_manager2(self):
        self.check_and_open_file_manager("upload_icon1", "upload_label1", "selected_file_label1", "upload_gov_id1_img", self.upload_image2)

    def check_and_open_file_manager3(self):
        self.check_and_open_file_manager("upload_icon1", "upload_label1", "selected_file_label1", "upload_gov_id2_img", self.upload_image3)
    def check_and_open_file_manager(self, icon_id, label_id, file_label_id, image_id,upload_function):
        if platform == 'android':
            if check_permission(Permission.READ_MEDIA_IMAGES):
                self.file_manager_open(icon_id, label_id, file_label_id, image_id,upload_function)
            else:
                self.request_media_images_permission()
        else:
            self.file_manager_open(icon_id, label_id, file_label_id, image_id,upload_function)

    def file_manager_open(self, icon_id, label_id, file_label_id, image_id,upload_function):
        self.file_manager = MDFileManager(
            exit_manager=self.exit_manager,
            select_path=lambda path: self.select_path1(path, icon_id, label_id, file_label_id, image_id,upload_function),
        )
        if platform == 'android':
            primary_external_storage = "/storage/emulated/0"
            self.file_manager.show(primary_external_storage)
        else:
            self.file_manager.show('/')

    def select_path1(self, path, icon_id, label_id, file_label_id, image_id,upload_function):
        upload_function(path)  # Upload the selected image using the provided function
        self.ids[image_id].source = path if os.path.getsize(path) <= self.MAX_IMAGE_SIZE_MB * 1024 * 1024 else ''
        self.file_manager.close()

    def exit_manager(self, *args):
        self.file_manager.close()

    def request_media_images_permission(self):
        request_permissions([Permission.READ_MEDIA_IMAGES], self.permission_callback)

    def permission_callback(self, permissions, grants):
        if all(grants.values()):
            self.file_manager_open()
        else:
            self.show_permission_denied()

    def show_permission_denied(self):
        view = ModalView()
        view.add_widget(Button(
            text='Permission NOT granted.\n\n' +
                 'Tap to quit app.\n\n\n' +
                 'If you selected "Don\'t Allow",\n' +
                 'enable permission with App Settings.',
            on_press=self.bye)
        )
        view.open()

    def on_pre_enter(self):
        Window.bind(on_keyboard=self.on_back_button)

    def on_pre_leave(self):
        Window.unbind(on_keyboard=self.on_back_button)

    def on_back_button(self, instance, key, scancode, codepoint, modifier):
        if key == 27:
            self.on_back_button_press()
            return True
        return False

    def go_back(self):
        self.manager.transition = SlideTransition(direction='right')
        self.manager.current = 'ViewPersonalScreen'

    def on_back_button_press(self):
        self.manager.current = 'ViewPersonalScreen'


class ReturnsScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.returns_screen = None

    def user_return_screeen(self):
        self.returns_screen = 'user'
        self.ids.total_returns.md_bg_color = '#8f9691'
        self.ids.user_returns.md_bg_color = 0.043, 0.145, 0.278, 1
        data1 = app_tables.fin_loan_details.search()
        profile = app_tables.fin_user_profile.search()
        email = anvil.server.call('another_method')
        loan_id = []
        borrower_name = []
        cos_id1 = []
        loan_amount = []
        loan_amount_1 = []
        loan_status = []
        tenure = []
        interest = []
        monthly_emi = []
        emi_pay_type = []
        total_int_amount = []
        total_pro_fee_amount = []
        total_repay = []
        shedule_payment = []
        loan_product = []
        lender_customer_id = []
        lender_returns = []
        product_name = []
        s = 0
        for i in data1:
            s += 1
            loan_id.append(i['loan_id'])
            borrower_name.append(i['borrower_full_name'])
            cos_id1.append(i['borrower_customer_id'])
            loan_amount.append(i['loan_amount'])
            loan_status.append(i['loan_updated_status'])
            tenure.append(i['tenure'])
            interest.append(i['interest_rate'])
            monthly_emi.append(i['monthly_emi'])
            emi_pay_type.append(i['emi_payment_type'])
            total_int_amount.append(i['total_interest_amount'])
            total_pro_fee_amount.append(i['total_processing_fee_amount'])
            total_repay.append(i['total_repayment_amount'])
            shedule_payment.append(i['first_emi_payment_due_date'])
            loan_product.append(i['product_id'])
            lender_customer_id.append(i['lender_customer_id'])
            lender_returns.append(i['lender_returns'])
            product_name.append(i['product_name'])

        profile_customer_id = []
        profile_mobile_number = []
        profile_email = []
        for i in profile:
            profile_customer_id.append(i['customer_id'])
            profile_mobile_number.append(i['mobile'])
            profile_email.append(i['email_user'])

        log_index = 0
        if email in profile_email:
            log_index = profile_email.index(email)
        else:
            print("email not there")

        index_list = []
        for i in range(s):
            if lender_customer_id[i] == lender_customer_id[log_index] and loan_status[i] == 'closed':
                index_list.append(i)

        print(index_list)

        investment1 = []
        returns1 = []
        products1 = []
        a = 0
        for i in index_list:
            a += 1
            print(loan_amount[i], loan_amount[i] / 1000000)
            investment1.append(loan_amount[i] / 1000000)
            products1.append(product_name[i] + f'{a}')
            if lender_returns[i] != None:
                returns1.append(lender_returns[i] / 1000000)
            else:
                returns1.append(0)

        print(returns1)
        print(products1)
        print(investment1)

        # Create a figure and axis
        fig = Figure()

        # Data
        products = products1
        investment = investment1
        returns = returns1
        ax = fig.add_subplot(111)
        bar_width = 0.45
        investment_bars = ax.bar(products, investment, bar_width, label='Investment', color='blue')
        returns_bars = ax.bar(products, returns, bar_width, label='Returns', color='green')

        ax.set_xlabel('Product Details')
        ax.set_ylabel('Amount (0.1M = 100000)')
        ax.set_title('Investment and Returns by Product')
        ax.legend()

        # Annotate the investment bar with the investment amount
        for bar, inv in zip(investment_bars, investment):
            if inv * 1000000 > 0:  # Avoid displaying text for zero investments
                ax.text(bar.get_x() + bar.get_width() / 2, bar.get_height(), f'RS .{inv * 1000000}',
                        ha='center', va='bottom', fontsize=10, color='black')

        # Annotate the returns bar with the percentage
        for bar, inv, ret in zip(returns_bars, investment, returns):
            if inv > 0:  # Avoid division by zero
                percentage = (ret / inv) * 100
                ax.text(bar.get_x() + bar.get_width() / 2, bar.get_height(), f'{percentage:.1f}%',
                        ha='center', va='bottom', fontsize=12, color='white')

        # Render the figure as an image
        buf = io.BytesIO()
        fig.savefig(buf, format='png')
        buf.seek(0)

        # Save the image temporarily
        temp_file = "temp_plot.png"
        with open(temp_file, "wb") as f:
            f.write(buf.read())

        # Add the image to the main layout
        self.ids.image.source = temp_file

    def total_return_screeen(self):
        self.returns_screen = 'total'
        self.ids.user_returns.md_bg_color = '#a6ada8'
        self.ids.total_returns.md_bg_color = 0.043, 0.145, 0.278, 1
        data1 = app_tables.fin_loan_details.search()
        profile = app_tables.fin_user_profile.search()
        email = anvil.server.call('another_method')
        loan_id = []
        borrower_name = []
        cos_id1 = []
        loan_amount = []
        loan_amount_1 = []
        loan_status = []
        tenure = []
        interest = []
        monthly_emi = []
        emi_pay_type = []
        total_int_amount = []
        total_pro_fee_amount = []
        total_repay = []
        shedule_payment = []
        loan_product = []
        lender_customer_id = []
        lender_returns = []
        product_name = []
        s = 0
        for i in data1:
            s += 1
            loan_id.append(i['loan_id'])
            borrower_name.append(i['borrower_full_name'])
            cos_id1.append(i['borrower_customer_id'])
            loan_amount.append(i['loan_amount'])
            loan_amount_1.append(i['loan_amount'])
            loan_status.append(i['loan_updated_status'])
            tenure.append(i['tenure'])
            interest.append(i['interest_rate'])
            monthly_emi.append(i['monthly_emi'])
            emi_pay_type.append(i['emi_payment_type'])
            total_int_amount.append(i['total_interest_amount'])
            total_pro_fee_amount.append(i['total_processing_fee_amount'])
            total_repay.append(i['total_repayment_amount'])
            shedule_payment.append(i['first_emi_payment_due_date'])
            loan_product.append(i['product_id'])
            lender_customer_id.append(i['lender_customer_id'])
            lender_returns.append(i['lender_returns'])
            product_name.append(i['product_name'])

        profile_customer_id = []
        profile_mobile_number = []
        profile_email = []
        for i in profile:
            profile_customer_id.append(i['customer_id'])
            profile_mobile_number.append(i['mobile'])
            profile_email.append(i['email_user'])

        log_index = 0
        if email in profile_email:
            log_index = profile_email.index(email)
        else:
            print("email not there")

        lender_data = app_tables.fin_lender.search()
        lender_cus_id = []
        total_commitment = []
        lender_returns_on_lender = []
        for i in lender_data:
            lender_cus_id.append(i['customer_id'])
            total_commitment.append(i['lender_total_commitments'])
            lender_returns_on_lender.append(i['return_on_investment'])

        index_list = []
        for i in range(s):
            if lender_customer_id[i] == lender_customer_id[log_index] and loan_status[i] != 'lost opportunities' and \
                    loan_status[i] != 'rejected':
                index_list.append(i)

        print(index_list)
        lender_index = 0
        if profile_customer_id[log_index] in lender_cus_id:
            lender_index = lender_cus_id.index(profile_customer_id[log_index])

        print(total_commitment[lender_index])
        print(lender_returns_on_lender[lender_index])

        fig, ax = plt.subplots()

        # Data
        if total_commitment[lender_index] is not None and lender_returns_on_lender[lender_index] is not None:
            products = ['Total', 'Returns']
            investment = [total_commitment[lender_index] / 1000000, 0]  # Summarizing investment for 'Total'
            returns = [0, lender_returns_on_lender[lender_index] / 1000000]  # Summarizing returns for 'Returns'
            bar_width = 0.7
            # Calculate percentage of returns
            returns_percentage = (lender_returns_on_lender[lender_index] / total_commitment[lender_index]) * 100
        else:
            products = ['Total', 'Returns']
            investment = [0 / 1000000, 0]  # Summarizing investment for 'Total'
            returns = [0, 0 / 1000000]  # Summarizing returns for 'Returns'
            bar_width = 0.7
            returns_percentage = 0

        investment_bars = ax.bar(products, investment, bar_width, label='Investment', color='blue')
        returns_bars = ax.bar(products, returns, bar_width, label='Returns', color='green')
        # Annotate the returns bar with the percentage
        if returns_percentage > 0:
            ax.text(1, returns[1] + 0, f'{returns_percentage:.1f}%', ha='center', va='bottom', fontsize=12)

        # Annotate the investment bar with the investment amount
        for bar, inv in zip(investment_bars, investment * 1000000):
            if inv * 1000000 > 0:  # Avoid displaying text for zero investments
                ax.text(bar.get_x() + bar.get_width() / 2, bar.get_height(), f'RS. {inv * 1000000}',
                        ha='center', va='bottom', fontsize=10, color='black')

        ax.set_xlabel('Category')
        ax.set_ylabel('Amount (0.1M = 100000)')
        ax.set_title('Investment and Returns by Product')
        ax.legend()

        # Render the figure as an image
        buf = io.BytesIO()
        plt.savefig(buf, format='png')
        buf.seek(0)

        # Save the image temporarily
        temp_file = "temp_plot1.png"
        with open(temp_file, "wb") as f:
            f.write(buf.read())

        # Add the image to the main layout
        self.ids.image.source = temp_file

    def return_refresh(self):
        if self.returns_screen == 'total':
            self.total_return_screeen()
        elif self.returns_screen == 'user':
            self.user_return_screeen()


class CommitmentScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        data1 = app_tables.fin_loan_details.search()
        profile = app_tables.fin_user_profile.search()
        email = anvil.server.call('another_method')
        loan_id = []
        borrower_name = []
        cos_id1 = []
        loan_amount = []
        loan_amount_1 = []
        loan_status = []
        tenure = []
        interest = []
        monthly_emi = []
        emi_pay_type = []
        total_int_amount = []
        total_pro_fee_amount = []
        total_repay = []
        shedule_payment = []
        loan_product = []
        lender_customer_id = []
        lender_returns = []
        product_name = []
        s = 0
        for i in data1:
            s += 1
            loan_id.append(i['loan_id'])
            borrower_name.append(i['borrower_full_name'])
            cos_id1.append(i['borrower_customer_id'])
            loan_amount.append(i['loan_amount'])
            loan_amount_1.append(i['loan_amount'])
            loan_status.append(i['loan_updated_status'])
            tenure.append(i['tenure'])
            interest.append(i['interest_rate'])
            monthly_emi.append(i['monthly_emi'])
            emi_pay_type.append(i['emi_payment_type'])
            total_int_amount.append(i['total_interest_amount'])
            total_pro_fee_amount.append(i['total_processing_fee_amount'])
            total_repay.append(i['total_repayment_amount'])
            shedule_payment.append(i['first_emi_payment_due_date'])
            loan_product.append(i['product_id'])
            lender_customer_id.append(i['lender_customer_id'])
            lender_returns.append(i['lender_returns'])
            product_name.append(i['product_name'])

        profile_customer_id = []
        profile_mobile_number = []
        profile_email = []
        for i in profile:
            profile_customer_id.append(i['customer_id'])
            profile_mobile_number.append(i['mobile'])
            profile_email.append(i['email_user'])

        log_index = 0
        if email in profile_email:
            log_index = profile_email.index(email)
        else:
            print("email not there")

        lender_data = app_tables.fin_lender.search()
        lender_cus_id = []
        total_commitment = []
        lender_returns_on_lender = []
        present_commitments = []
        for i in lender_data:
            lender_cus_id.append(i['customer_id'])
            total_commitment.append(i['lender_total_commitments'])
            lender_returns_on_lender.append(i['return_on_investment'])
            present_commitments.append(i['present_commitments'])

        index_list = []
        for i in range(s):
            if lender_customer_id[i] == lender_customer_id[log_index] and loan_status[i] != 'lost opportunities' and \
                    loan_status[i] != 'rejected':
                index_list.append(i)

        print(index_list)
        lender_index = 0
        if profile_customer_id[log_index] in lender_cus_id:
            lender_index = lender_cus_id.index(profile_customer_id[log_index])

        print(total_commitment[lender_index])
        print(lender_returns_on_lender[lender_index])

        fig, ax = plt.subplots()

        # Data for pie chart
        if total_commitment[lender_index] != None and present_commitments[lender_index] != None:
            labels = ['Total               \nCommitments', 'Present\nCommitments']
            sizes = [total_commitment[lender_index], present_commitments[lender_index]]
            colors = ['orange', 'yellow']
            explode = (0.1, 0)  # explode the 1st slice (Total Investment)
        else:
            labels = ['Total               \nCommitments', 'Present\nCommitments']
            sizes = [0, 0]
            colors = ['orange', 'yellow']
            explode = (0.1, 0)  # explode the 1st slice (Total Investment)

        ax.pie(sizes, explode=explode, labels=labels, colors=colors, autopct='%1.1f%%',
               shadow=True, startangle=55)

        ax.set_title('Lender Commitments')

        # Render the figure as an image
        buf = io.BytesIO()
        plt.savefig(buf, format='png')
        buf.seek(0)

        # Save the image temporarily
        temp_file = "temp_plot2.png"
        with open(temp_file, "wb") as f:
            f.write(buf.read())

        # Add the image to the main layout
        self.ids.image.source = temp_file


class MyScreenManager(ScreenManager):
    pass
