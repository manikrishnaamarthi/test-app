import anvil
from anvil.tables import app_tables
from kivy import properties
from kivy.metrics import dp
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.image import Image
from kivy.uix.widget import Widget
from kivymd.uix.card import MDCard
from kivymd.uix.datatables import MDDataTable
from pytz import utc
from kivy.core.window import Window
from kivy.properties import ListProperty, Clock
from kivy.uix.modalview import ModalView
from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen, ScreenManager, SlideTransition
from kivymd.uix.button import MDRectangleFlatButton, MDRaisedButton, MDFillRoundFlatButton
from kivymd.uix.list import ThreeLineAvatarIconListItem, IconLeftWidget, TwoLineAvatarIconListItem
from kivymd.uix.slider import MDSlider
from kivymd.uix.label import MDLabel
import sqlite3
from math import pow
from kivymd.uix.dialog import MDDialog, dialog
import anvil.server
from kivy.uix.spinner import Spinner
from datetime import datetime, timezone, timedelta, date

from kivymd.uix.spinner import MDSpinner
import anvil.tables.query as q
from borrower_wallet import WalletScreen
from datetime import datetime
from kivy.uix.label import Label
import base64
from kivy.core.image import Image as CoreImage
from io import BytesIO

user_helpers2 = """
<WindowManager>:
    BorrowerDuesScreen:
    DuesScreen:
    LastScreenWallet:
    PartPayment:
<DuesScreen>:
    BoxLayout:
        orientation: 'vertical'
        MDTopAppBar:
            title:"Today's Dues"
            elevation: 2
            left_action_items: [['arrow-left', lambda x: root.go_back()]]
            right_action_items: [['refresh', lambda x: root.refresh()]]
            md_bg_color: 0.043, 0.145, 0.278, 1
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



<BorrowerDuesScreen>:
    GridLayout:
        cols: 1

        MDTopAppBar:
            title:"Today's Dues"
            md_bg_color:0.043, 0.145, 0.278, 1
            theme_text_color: 'Custom'
            text_color: 1,1,1,1 
            size_hint:1,None
            elevation: 3
            left_action_items: [['arrow-left', lambda x: root.go_back()]]
            right_action_items: [['wallet']]
            pos_hint: {'top': 1} 

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
                    theme_text_color: 'Custom'  
                    text_color: 0, 0, 0, 1
                    bold: True

                MDLabel:
                    id: loan_amount1
                    halign: 'left'
                    bold: True
                    theme_text_color: 'Custom'  
                    text_color: 0, 0, 0, 1
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
                    ttheme_text_color: 'Custom'  
                    text_color: 0, 0, 0, 1
                    bold: True

                MDLabel:
                    id: name
                    halign: 'left'
                    theme_text_color: 'Custom' 
                    text_color: 140/255, 140/255, 140/255, 1
                    bold: True   

            MDGridLayout:
                cols: 2
                MDLabel:
                    text: 'Tenure'
                    halign: 'left'
                    theme_text_color: 'Custom'  
                    text_color: 0, 0, 0, 1
                    bold: True

                MDLabel:
                    id: tenure
                    halign: 'left'
                    theme_text_color: 'Custom' 
                    text_color: 140/255, 140/255, 140/255, 1
                    bold: True
            

            MDGridLayout:
                cols: 2
                MDLabel:
                    text: 'Interest Rate'
                    halign: 'left'
                    theme_text_color: 'Custom'  
                    text_color: 0, 0, 0, 1
                    bold: True

                MDLabel:
                    id: interest_rate
                    halign: 'left'
                    theme_text_color: 'Custom' 
                    text_color: 140/255, 140/255, 140/255, 1
                    bold: True

            MDGridLayout:
                cols: 2
                MDLabel:
                    text: 'Account Number'
                    halign: 'left'
                    theme_text_color: 'Custom'  
                    text_color: 0, 0, 0, 1
                    bold: True

                MDLabel:
                    id: account_number
                    halign: 'left'
                    theme_text_color: 'Custom' 
                    text_color: 140/255, 140/255, 140/255, 1
                    bold: True
            MDGridLayout:
                cols: 2
                MDLabel:
                    text: 'Loan Status'
                    halign: 'left'
                    theme_text_color: 'Custom'  
                    text_color: 0, 0, 0, 1
                    bold: True

                MDLabel:
                    id: status
                    halign: 'left'
                    theme_text_color: 'Custom' 
                    text_color: 140/255, 140/255, 140/255, 1
                    bold: True

            MDGridLayout:
                cols: 2
                MDLabel:
                    text: 'Emi Amount'
                    halign: 'left'
                    theme_text_color: 'Custom'  
                    text_color: 0, 0, 0, 1
                    bold: True

                MDLabel:
                    id: emi_amount
                    halign: 'left'
                    theme_text_color: 'Custom' 
                    text_color: 140/255, 140/255, 140/255, 1
                    bold: True

            MDGridLayout:
                cols: 2
                MDLabel:
                    id: extra
                    text: 'Extra Payment'
                    halign: 'left'
                    theme_text_color: 'Custom'  
                    text_color: 0, 0, 0, 1
                    bold: True

                MDLabel:
                    id: extra_amount
                    halign: 'left'
                    theme_text_color: 'Custom' 
                    text_color: 140/255, 140/255, 140/255, 1
                    bold: True

            MDGridLayout:
                cols: 2
                MDLabel:
                    id: total
                    text: 'Total Amount'
                    halign: 'left'
                    theme_text_color: 'Custom'  
                    text_color: 0, 0, 0, 1
                    bold: True

                MDLabel:
                    id: total_amount
                    halign: 'left'
                    theme_text_color: 'Custom' 
                    text_color: 140/255, 140/255, 140/255, 1
                    bold: True
                    
            MDGridLayout:
                cols: 2
    
                MDLabel:
                    text: "Payment Details"
                    font_size:dp(16)
                    bold:True
                    halign:"left"
    
                Button:
                    text:'View Payments                   '
                    background_color: 0, 0, 0, 0
                    color: 0, 0.5, 1, 1
                    font_size: '15sp'
                    halign:"left"
                    size_hint: None, None
                    size: self.texture_size
                    pos_hint: {'center_x': 0.5, 'center_y': 0.28}
                    on_release: root.go_to_menu_screen()
                    halign:"left"
                    
              


        MDLabel:
            text: ''
            halign: 'left'
            size_hint_y: None
            height: dp(55)

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
                text: "Part Payment"
                md_bg_color:0.043, 0.145, 0.278, 1
                on_release: root.go_to_part_payment()
                pos_hint: {'center_x': 0.5, 'center_y': 2}
                size_hint: 0.4, None 
                font_name:"Roboto-Bold"
                font_size:dp(15) 

            MDRaisedButton:
                id: pay
                text: "Pay Now"
                md_bg_color:0.043, 0.145, 0.278, 1
                on_release: root.go_to_paynow()
                pos_hint: {'center_x': 0.5, 'center_y': 2}
                size_hint: 0.4, None 
                font_name:"Roboto-Bold"
                font_size:dp(15) 

<PartPayment>          
    GridLayout:
        cols: 1
        MDTopAppBar:
            title: "Part Payment"
            elevation: 3
            left_action_items: [['arrow-left', lambda x: root.on_back_button_press()]]
            md_bg_color: 0.043, 0.145, 0.278, 1 
            title_align: 'left'

        ScrollView:
            GridLayout:
                cols: 1
                size_hint_y: None
                height: self.minimum_height 

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
                            bold: True
                            theme_text_color: 'Custom'  
                            text_color: 0, 0, 0, 1
                    MDGridLayout:
                        cols: 2
                        MDIconButton:
                            icon: 'currency-inr'
                            halign: 'left'
                            size_hint_y: None
                            height: dp(1)
                            bold: True
                            theme_text_color: 'Custom'  
                            text_color: 0, 0, 0, 1

                        MDLabel:
                            id: loan_amount1
                            halign: 'left'
                            theme_text_color: 'Custom' 
                            text_color: 0, 0, 0, 1
                            bold: True

                    MDLabel:
                        text: ''
                        halign: 'left'
                        size_hint_y: None
                        height: dp(5)

                    MDGridLayout:
                        cols: 2
                        MDLabel:
                            text: "Borrower Name"
                            halign: "left"
                            bold: True
                            theme_text_color: 'Custom'  
                            text_color: 0, 0, 0, 1
                        MDLabel:
                            id: name
                            halign: 'left' 
                            theme_text_color: 'Custom' 
                            text_color: 140/255, 140/255, 140/255, 1
                            bold: True

                    MDGridLayout: 
                        cols: 2    
                        MDLabel:
                            text: "Tenure" 
                            halign: "left"
                            bold: True
                            theme_text_color: 'Custom'  
                            text_color: 0, 0, 0, 1
                        MDLabel:
                            id: tenure
                            halign: 'left' 
                            theme_text_color: 'Custom' 
                            text_color: 140/255, 140/255, 140/255, 1
                            bold: True

                    MDGridLayout: 
                        cols: 2       
                        MDLabel:
                            text: "Interest Amount" 
                            halign: "left"
                            bold: True
                            theme_text_color: 'Custom'  
                            text_color: 0, 0, 0, 1
                        MDLabel:
                            id: interest_rate
                            halign: 'left' 
                            theme_text_color: 'Custom' 
                            text_color: 140/255, 140/255, 140/255, 1
                            bold: True

                    MDGridLayout: 
                        cols: 2 
                        MDLabel:
                            text: "Account number" 
                            halign: "left"
                            bold: True
                            theme_text_color: 'Custom'  
                            text_color: 0, 0, 0, 1
                        MDLabel:
                            id: account_number
                            halign: 'left' 
                            theme_text_color: 'Custom' 
                            text_color: 140/255, 140/255, 140/255, 1
                            bold: True

                    MDGridLayout:
                        cols: 2
                        MDLabel:
                            text: 'Loan Status'
                            halign: 'left'
                            theme_text_color: 'Custom'  
                            text_color: 0, 0, 0, 1
                            bold: True

                        MDLabel:
                            id: status
                            halign: 'left'
                            theme_text_color: 'Custom' 
                            text_color: 140/255, 140/255, 140/255, 1
                            bold: True

                    MDGridLayout: 
                        cols: 2 
                        MDLabel:
                            text: "Emi Amount" 
                            halign: "left"
                            bold: True
                            theme_text_color: 'Custom'  
                            text_color: 0, 0, 0, 1
                        MDLabel:
                            id: emi_amount
                            halign: 'left' 
                            theme_text_color: 'Custom' 
                            text_color: 140/255, 140/255, 140/255, 1
                            bold: True

                    MDGridLayout: 
                        cols: 2 
                        MDLabel:
                            text: "Remaining Amount" 
                            halign: "left"
                            bold: True
                            theme_text_color: 'Custom'  
                            text_color: 0, 0, 0, 1
                        MDLabel:
                            id: remain
                            halign: 'left' 
                            theme_text_color: 'Custom' 
                            text_color: 140/255, 140/255, 140/255, 1
                            bold: True
                    MDGridLayout:
                        cols: 2
                        MDLabel:
                            id: extra
                            text: 'Extra Payment'
                            halign: 'left' 
                            bold: True
                            theme_text_color: 'Custom'  
                            text_color: 0, 0, 0, 1

                        MDLabel:
                            id: extra_amount
                            halign: 'left'
                            theme_text_color: 'Custom' 
                            text_color: 140/255, 140/255, 140/255, 1
                            bold: True
                    MDGridLayout:
                        cols: 2
                        MDLabel:
                            id: total
                            text: 'Total Amount'
                            halign: 'left'  
                            bold: True
                            theme_text_color: 'Custom'  
                            text_color: 0, 0, 0, 1

                        MDLabel:
                            id: total_amount
                            halign: 'left'
                            theme_text_color: 'Custom' 
                            text_color: 140/255, 140/255, 140/255, 1
                            bold: True

                    MDGridLayout: 
                        cols: 2 
                        MDLabel:
                            text: "Part Payment Amount" 
                            halign: "left"
                            bold: True
                            theme_text_color: 'Custom'  
                            text_color: 0, 0, 0, 1
                        MDLabel:
                            id: amount1
                            halign: 'left' 
                            theme_text_color: 'Custom'  
                            text_color: 140/255, 140/255, 140/255, 1

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
                        text: "Back"
                        md_bg_color: 0.043, 0.145, 0.278, 1
                        theme_text_color: 'Custom'
                        text_color: 1, 1, 1, 1
                        size_hint: 1, 1

                    MDRaisedButton:
                        text: "Pay Now"
                        theme_text_color: 'Custom'
                        on_release: root.go_to_paynow1()
                        text_color: 1, 1, 1, 1
                        md_bg_color: 0.043, 0.145, 0.278, 1
                        size_hint: 1, 1

<LastScreenWallet>:
    MDTopAppBar:
        title: "Today Due Request Submitted"
        elevation: 2
        pos_hint: {'top': 1}
        title_align: 'center'
        md_bg_color: 0.043, 0.145, 0.278, 1
    BoxLayout:
        orientation: 'vertical'
        padding: dp(20)
        spacing: dp(20)
        pos_hint: {'center_x': 0.5, 'center_y': 0.5}
        MDLabel:
            text: " "
        MDLabel:
            text: " "
        MDLabel:
            text: " "

        Image:
            source: "checkmark.png"
            size_hint: None, None
            size: "70dp", "70dp"
            pos_hint: {'center_x': 0.5}

        MDLabel:
            text: "Thank You"
            font_style: 'H4'
            bold: True
            halign: 'center'

        MDLabel:
            text: "The payment has been successfully completed. Your transaction has been processed"
            font_style: 'Body1'
            halign: 'center'
            size_hint_y: None
            height: self.texture_size[1]

        MDLabel:
            text: " "
        MDLabel:
            text: " "
        MDLabel:
            text: " "

        MDRaisedButton:
            text: "Go Back Home"
            on_press: root.go_back_home()
            md_bg_color: 0.043, 0.145, 0.278, 1
            theme_text_color: 'Custom'
            text_color: 1, 1, 1, 1
            size_hint: None, None
            size: "200dp", "50dp"
            pos_hint: {'center_x': 0.5}
            font_name: "Roboto-Bold"
        MDLabel:
            text: " "    
            
<ViewPaymentDetails>:

    MDGridLayout:
        cols: 1
        MDTopAppBar:
            title: "Today Due Payment List"
            elevation: 2
            pos_hint: {'top': 1}
            left_action_items: [['arrow-left', lambda x: root.go_back()]]
            title_align: 'center'
            md_bg_color: 0.043, 0.145, 0.278, 1
            
        MDBoxLayout:
            orientation: 'vertical'
            id: container1          

"""
Builder.load_string(user_helpers2)


class BorrowerDuesScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def initialize_with_value(self, value, shechule_date):
        print(value)
        self.shechule_date = shechule_date
        self.loan_id = value
        today_date = datetime.now(tz=utc).date()
        emi_data = app_tables.fin_emi_table.search()
        emi_loan_id = []
        emi_num = []
        next_payment = []
        part_payment_type = []
        part_payment_done = []
        remaining_tenure = []
        for i in emi_data:
            emi_loan_id.append(i['loan_id'])
            emi_num.append(i['emi_number'])
            next_payment.append(i['next_payment'])
            part_payment_type.append((i['payment_type']))
            part_payment_done.append(i['part_payment_done'])
            remaining_tenure.append(i['remaining_tenure'])

        product = app_tables.fin_product_details.search()
        product_id = []
        lapsed_fee = []
        default_fee_percentage = []
        default_fee_amount = []
        npa_percentage = []
        npa_fee_amount = []
        default_type = []
        npa_type = []

        for i in product:
            product_id.append(i['product_id'])
            lapsed_fee.append(i['lapsed_fee'])
            default_fee_percentage.append(i['default_fee'])
            default_fee_amount.append(i['default_fee_amount'])
            default_type.append(i['default_select_percentage_amount'])
            npa_percentage.append(i['npa'])
            npa_fee_amount.append(i['npa_amount'])
            npa_type.append(i['npa_select_percentage_amount'])
        data1 = app_tables.fin_loan_details.search()
        user_profile = app_tables.fin_user_profile.search()

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
        emi_amount = []
        for i in data1:
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
            emi_amount.append(i['monthly_emi'])
        index = 0

        if value in loan_id:
            index = loan_id.index(value)
            self.ids.name.text = str(borrower_name[index])
            self.ids.loan_amount1.text = str(loan_amount[index])
            self.ids.tenure.text = str(tenure[index])
            self.ids.status.text = str(loan_status[index])
            self.ids.interest_rate.text = str(interest[index])
            self.ids.emi_amount.text = str(monthly_emi[index])

        cos_id = []
        account_num = []
        for i in user_profile:
            cos_id.append(i['customer_id'])
            account_num.append(i['account_number'])

        if cos_id1[index] in cos_id:
            index1 = cos_id1.index(cos_id1[index])
            self.ids.account_number.text = str(account_num[index1])

        last_index = 0
        if value not in emi_loan_id:
            emi_number = 1
        else:
            last_index = len(emi_loan_id) - 1 - emi_loan_id[::-1].index(value)

        if value in emi_loan_id:
            if part_payment_type[last_index] == 'pay now' and part_payment_done[last_index] == None:
                self.ids.pay.opacity = 1
                self.ids.pay.disabled = False
            elif part_payment_type[last_index] != "part payment" and part_payment_done[last_index] != 1 and emi_loan_id[
                last_index] != value:
                self.ids.pay.opacity = 1
                self.ids.pay.disabled = False
            else:
                self.ids.pay.opacity = 0
                self.ids.pay.disabled = True
        else:
            self.ids.pay.opacity = 1
            self.ids.pay.disabled = False

        extend_row = None
        extend_amount = 0
        foreclose_amount1 = 0
        emi_amount1 = 0
        new_emi_amount = 0

        if loan_status[index] == "disbursed":
            extra_amount = 0
            print(loan_status[index])
            print(extra_amount)
            log_email = anvil.server.call('another_method')
            profile = app_tables.fin_user_profile.search()
            print(log_email)
            email_user = []
            for i in profile:
                email_user.append(i['email_user'])
            log_index = 0
            if log_email in email_user:
                log_index = email_user.index(log_email)
            setting = app_tables.fin_loan_settings.search()
            a = 0
            date_type = []
            max_days = []
            min_days = []
            for i in setting:
                a += 1
                date_type.append(i['loans'])
                min_days.append(i['minimum_days'])
                max_days.append(i['maximum_days'])
            print(log_index)
            days_left = (today_date - shechule_date[value]).days
            print(days_left)
            late_fee = None
            for i in range(a):
                if days_left >= min_days[i] and days_left < max_days[i]:
                    late_fee = date_type[i]
                    if days_left > min_days[i]:
                        days_left = (today_date - shechule_date[value]).days - (min_days[i] + 1)
                    else:
                        days_left = 0
                    break
            if late_fee == 'lapsed fee':
                product_index = product_id.index(loan_product[index])
                lapsed_percentage = lapsed_fee[product_index] + days_left
                lapsed_amount = (monthly_emi[index] * lapsed_percentage) / 100
                print(lapsed_amount)
                print(lapsed_percentage)
                print(days_left)
                total_amount = monthly_emi[index] + extra_amount
                self.ids.extra.text = "Extra Payment (Late payment Fee)"
                self.ids.extra_amount.text = str(round(extra_amount + lapsed_amount, 2))
                self.ids.total_amount.text = str(round(total_amount + lapsed_amount, 2))
                data1[index]['loan_state_status'] = "lapsed"

            elif late_fee == 'default fee':
                default_amount = 0
                product_index = product_id.index(loan_product[index])
                default_percentage = default_fee_percentage[product_index] + days_left
                print(days_left)
                print(default_percentage)
                if default_type[product_index] == 'Default fee (%)':
                    default_amount = (monthly_emi[index] * default_percentage) / 100
                elif default_type[product_index] == 'Default fee (₹)':
                    default_amount = default_fee_amount[product_index] * days_left
                lapsed_percentage = lapsed_fee[product_index] + days_left
                lapsed_amount = (monthly_emi[index] * lapsed_percentage) / 100
                total_amount = monthly_emi[index] + extra_amount
                self.ids.extra.text = "Extra Payment (Default and Late payment Fee)"
                self.ids.extra_amount.text = str(round(extra_amount + default_amount + lapsed_amount, 2))
                self.ids.total_amount.text = str(round(total_amount + default_amount + lapsed_amount, 2))
                data1[index]['loan_state_status'] = 'default'

            elif late_fee == 'NPA fee':
                product_index = product_id.index(loan_product[index])
                npa_amount = 0
                npa_percentage = npa_percentage[product_index] + days_left
                print(npa_percentage)
                print(days_left)
                if npa_type[product_index] == 'Non Performing Asset (%)':
                    npa_amount = (monthly_emi[index] * npa_percentage) / 100
                elif npa_type[product_index] == 'Non Performing Asset (₹)':
                    npa_amount = default_fee_amount[product_index]
                lapsed_percentage = lapsed_fee[product_index] + days_left
                lapsed_amount = (monthly_emi[index] * lapsed_percentage) / 100
                default_amount = 0
                default_percentage = default_fee_percentage[product_index] + days_left
                if default_type[product_index] == 'Default fee (%)':
                    default_amount = (monthly_emi[index] * default_percentage) / 100
                elif default_type[product_index] == 'Default fee (₹)':
                    default_amount = default_fee_amount[product_index] * days_left
                extra_payment_total = extra_amount + npa_amount + lapsed_amount + default_amount
                total_amount = monthly_emi[index] + extra_payment_total
                self.ids.extra.text = "Extra Payment (NPA, Default, and Late payment Fee)"
                self.ids.extra_amount.text = str(round(extra_payment_total, 2))
                self.ids.total_amount.text = str(round(total_amount, 2))
                data1[index]['loan_state_status'] = 'npa'
            else:
                total_amount = round(monthly_emi[index] + extra_amount)
                self.ids.extra_amount.text = str(round(extra_amount, 2))
                self.ids.total_amount.text = str(round(total_amount, 2))
                self.ids.extra.text = "Extra Payment "

            if value not in emi_loan_id:
                if emi_pay_type[index].strip() == 'Three Months' and tenure[index] > 3 and tenure[index] < 6:
                    r = tenure[index] - 3
                    i = monthly_emi[index] / 3
                    emi = i * r
                    print(monthly_emi[index], emi)
                    self.ids.total_amount.text = str(round(float(self.ids.total_amount.text), 2) + emi)
            if value in emi_loan_id:
                if emi_pay_type[index].strip() == 'Three Months' and remaining_tenure[last_index] != None and remaining_tenure[last_index] > 3 and \
                        remaining_tenure[last_index] < 6:
                    r = remaining_tenure[last_index] - 3
                    i = monthly_emi[index] / 3
                    emi = i * r
                    print(monthly_emi[index], emi)
                    self.ids.total_amount.text = str(round(float(self.ids.total_amount.text), 2) + emi)
            if value not in emi_loan_id:
                if emi_pay_type[index].strip() == 'Six Months' and tenure[index] > 6 and tenure[index] < 12:
                    r = tenure[index] - 6
                    i = monthly_emi[index] / 6
                    emi = i * r
                    print(monthly_emi[index], emi)
                    self.ids.total_amount.text = str(round(float(self.ids.total_amount.text), 2) + emi)
            if value in emi_loan_id:
                if emi_pay_type[index].strip() == 'Six Months' and remaining_tenure[last_index] > 6 and \
                        remaining_tenure[last_index] < 12:
                    r = remaining_tenure[last_index] - 6
                    i = monthly_emi[index] / 6
                    emi = i * r
                    print(monthly_emi[index], emi)
                    self.ids.total_amount.text = str(round(float(self.ids.total_amount.text), 2) + emi)


        elif loan_status[index] == "extension":
            emi_number = 0
            emi_data = app_tables.fin_emi_table.search(loan_id=str(value))
            if emi_data:
                emi = emi_data[0]
                emi_number = emi['emi_number']
            print(loan_status[index])
            extend_row = app_tables.fin_extends_loan.get(
                loan_id=str(value),
                emi_number=emi_number
            )
            if extend_row is not None and extend_row['status'] == "approved":
                extend_amount += extend_row['extension_amount']
                new_emi_amount += extend_row['new_emi']
                total_amount = new_emi_amount + extend_amount
                print(new_emi_amount, extend_amount)
                print(extend_amount)
                next_emi_num = emi_number + 1
                next_emi = app_tables.fin_emi_table.get(loan_id=str(value), emi_number=next_emi_num)

                if next_emi is not None:
                    next_payment_amount = next_emi['amount_paid']
                    extend_amount += next_payment_amount
                log_email = anvil.server.call('another_method')
                profile = app_tables.fin_user_profile.search()
                print(log_email)
                email_user = []
                for i in profile:
                    email_user.append(i['email_user'])
                log_index = 0
                if log_email in email_user:
                    log_index = email_user.index(log_email)
                setting = app_tables.fin_loan_settings.search()
                a = 0
                date_type = []
                max_days = []
                min_days = []
                for i in setting:
                    a += 1
                    date_type.append(i['loans'])
                    min_days.append(i['minimum_days'])
                    max_days.append(i['maximum_days'])
                print(log_index)
                days_left = (today_date - shechule_date[value]).days
                print(days_left)
                late_fee = None
                for i in range(a):
                    if days_left >= min_days[i] and days_left < max_days[i]:
                        late_fee = date_type[i]
                        if days_left > min_days[i]:
                            days_left = (today_date - shechule_date[value]).days - (min_days[i] + 1)
                        else:
                            days_left = 0
                        break
                if late_fee == 'lapsed fee':
                    product_index = product_id.index(loan_product[index])
                    lapsed_percentage = lapsed_fee[product_index] + days_left
                    lapsed_amount = (monthly_emi[index] * lapsed_percentage) / 100
                    self.ids.extra_amount.text = str(round(extend_amount + lapsed_amount, 2))
                    self.ids.emi_amount.text = str(new_emi_amount)
                    self.ids.total_amount.text = str(round(total_amount + lapsed_amount, 2))
                    self.ids.extra.text = "Extra Payment (Late payment Fee)"
                    data1[index]['loan_state_status'] = "lapsed"
                elif late_fee == 'default fee':
                    default_amount = 0
                    product_index = product_id.index(loan_product[index])
                    default_percentage = default_fee_percentage[product_index] + days_left
                    print(default_percentage)
                    print(days_left)
                    if default_type[product_index] == 'Default fee (%)':
                        default_amount = (monthly_emi[index] * default_percentage) / 100
                    elif default_type[product_index] == 'Default fee (₹)':
                        default_amount = default_fee_amount[product_index]
                    lapsed_percentage = lapsed_fee[product_index] + days_left
                    lapsed_amount = (monthly_emi[index] * lapsed_percentage) / 100
                    extra_payment = extend_amount + default_amount + lapsed_amount
                    total_payment = total_amount + default_amount + lapsed_amount
                    self.ids.extra_amount.text = str(round(extra_payment, 2))
                    self.ids.emi_amount.text = str(new_emi_amount)
                    self.ids.total_amount.text = str(round(total_payment, 2))
                    self.ids.extra.text = "Extra Payment (Default and Late payment Fee)"
                    data1[index]['loan_state_status'] = "default"
                    print(default_amount)
                elif late_fee == 'NPA fee':
                    npa_amount = 0
                    product_index = product_id.index(loan_product[index])
                    npa_percentage = npa_percentage[product_index] + days_left
                    if npa_type[product_index] == 'Non Performing Asset (%)':
                        npa_amount = (monthly_emi[index] * npa_percentage) / 100
                    elif npa_type[product_index] == 'Non Performing Asset (₹)':
                        npa_amount = default_fee_amount[product_index]
                    lapsed_percentage = lapsed_fee[product_index] + days_left
                    lapsed_amount = (monthly_emi[index] * lapsed_percentage) / 100
                    default_amount = 0
                    default_percentage = default_fee_percentage[product_index] + days_left
                    if default_type[product_index] == 'Default fee (%)':
                        default_amount = (monthly_emi[index] * default_percentage) / 100
                    elif default_type[product_index] == 'Default fee (₹)':
                        default_amount = default_fee_amount[product_index]
                    extra_payment_total = extend_amount + npa_amount + lapsed_amount + default_amount
                    total_payment = total_amount + npa_amount + lapsed_amount + default_amount
                    self.ids.extra_amount.text = str(round(extra_payment_total, 2))
                    self.ids.emi_amount.text = str(new_emi_amount)
                    self.ids.total_amount.text = str(round(total_payment, 2))
                    self.ids.extra.text = "Extra Payment (NPA, Default, and Late payment Fee)"
                    data1[index]['loan_state_status'] = 'npa'
                else:
                    self.ids.extra_amount.text = str(round(extend_amount))
                    self.ids.emi_amount.text = str(new_emi_amount)
                    self.ids.total_amount.text = str(round(total_amount))
                    self.ids.extra.text = "Extra Payment"
                print(extend_amount, new_emi_amount, total_amount)


        elif loan_status[index] == "foreclosure":
            print(loan_status[index])
            foreclosure_row = app_tables.fin_foreclosure.get(
                loan_id=str(value)
            )
            if foreclosure_row is not None and foreclosure_row['status'] == 'approved':
                foreclose_amount1 += foreclosure_row['foreclose_amount']
                emi_amount1 += foreclosure_row['total_due_amount']
                total_amount = foreclose_amount1 + emi_amount1
                log_email = anvil.server.call('another_method')
                profile = app_tables.fin_user_profile.search()
                print(log_email)
                email_user = []
                for i in profile:
                    email_user.append(i['email_user'])
                log_index = 0
                if log_email in email_user:
                    log_index = email_user.index(log_email)
                setting = app_tables.fin_loan_settings.search()
                a = 0
                date_type = []
                max_days = []
                min_days = []
                for i in setting:
                    a += 1
                    date_type.append(i['loans'])
                    min_days.append(i['minimum_days'])
                    max_days.append(i['maximum_days'])
                print(log_index)
                days_left = (today_date - shechule_date[value]).days
                print(days_left)
                late_fee = None
                for i in range(a):
                    if days_left >= min_days[i] and days_left < max_days[i]:
                        late_fee = date_type[i]
                        if days_left > min_days[i]:
                            days_left = (today_date - shechule_date[value]).days - (min_days[i] + 1)
                        else:
                            days_left = 0
                        break
                if late_fee == 'lapsed fee':
                    product_index = product_id.index(loan_product[index])
                    lapsed_percentage = lapsed_fee[product_index] + days_left
                    lapsed_amount = (monthly_emi[index] * lapsed_percentage) / 100
                    self.ids.extra_amount.text = str(round(foreclose_amount1 + lapsed_amount, 2))
                    self.ids.emi_amount.text = str(emi_amount1)
                    self.ids.total_amount.text = str(round(total_amount + lapsed_amount, 2))
                    self.ids.total.text = "Total Amount (Late payment Fee)"
                    data1[index]['loan_state_status'] = "lapsed"



                elif late_fee == 'default fee':
                    default_amount = 0
                    product_index = product_id.index(loan_product[index])
                    default_percentage = default_fee_percentage[product_index] + days_left
                    if default_type[product_index] == 'Default fee (%)':
                        default_amount = (monthly_emi[index] * default_percentage) / 100
                    elif default_type[product_index] == 'Default fee (₹)':
                        default_amount = default_fee_amount[product_index]
                    lapsed_percentage = lapsed_fee[product_index] + days_left
                    lapsed_amount = (monthly_emi[index] * lapsed_percentage) / 100
                    extra_payment_total = foreclose_amount1 + default_amount + lapsed_amount
                    total_payment = total_amount + default_amount + lapsed_amount
                    self.ids.extra_amount.text = str(round(extra_payment_total, 2))
                    self.ids.emi_amount.text = str(emi_amount1)
                    self.ids.total_amount.text = str(round(total_payment, 2))
                    self.ids.total.text = "Total Amount (Default and Late payment Fee)"
                    data1[index]['loan_state_status'] = "default"

                elif late_fee == 'NPA fee':
                    default_amount = 0
                    npa_amount = 0
                    product_index = product_id.index(loan_product[index])
                    npa_percentage = npa_percentage[product_index] + days_left
                    if npa_type[product_index] == 'Non Performing Asset (%)':
                        npa_amount = (monthly_emi[index] * npa_percentage) / 100
                    elif npa_type[product_index] == 'Non Performing Asset (₹)':
                        npa_amount = default_fee_amount[product_index]
                    lapsed_percentage = lapsed_fee[product_index] + days_left
                    lapsed_amount = (monthly_emi[index] * lapsed_percentage) / 100
                    default_percentage = default_fee_percentage[product_index] + days_left
                    if default_type[product_index] == 'Default fee (%)':
                        default_amount = (monthly_emi[index] * default_percentage) / 100
                    elif default_type[product_index] == 'Default fee (₹)':
                        default_amount = default_fee_amount[product_index]
                    extra_payment_total = foreclose_amount1 + npa_amount + lapsed_amount + default_amount
                    total_payment = total_amount + npa_amount + lapsed_amount + default_amount
                    self.ids.extra_amount.text = str(round(extra_payment_total, 2))
                    self.ids.emi_amount.text = str(emi_amount1)
                    self.ids.total_amount.text = str(round(total_payment, 2))
                    self.ids.extra.text = "Extra Payment (NPA, Default, and Late payment Fee)"
                    data1[index]['loan_state_status'] = "default"


                else:
                    self.ids.extra.text = "Extra Payment"
                    self.ids.extra_amount.text = str(round(foreclose_amount1, 2))
                    self.ids.emi_amount.text = str(emi_amount1)
                    self.ids.total_amount.text = str(round(total_amount, 2))

                print(foreclose_amount1, emi_amount1, total_amount)

    def go_to_paynow(self):
        emi_data = app_tables.fin_emi_table.search()
        ex_amount = app_tables.fin_platform_fees.search()
        emi_loan_id = []
        emi_num = []
        next_payment = []
        paid_amount = []
        remain_tenure = []
        remain_amo = []

        for i in emi_data:
            emi_loan_id.append(i['loan_id'])
            emi_num.append(i['emi_number'])
            next_payment.append(i['next_payment'])
            paid_amount.append(i['amount_paid'])
            remain_tenure.append(i['remaining_tenure'])
            remain_amo.append(i['total_remaining_amount'])

        value = self.loan_id
        data1 = app_tables.fin_loan_details.search()
        wallet = app_tables.fin_wallet.search()
        total = self.ids.total_amount.text
        extra_amount = self.ids.extra_amount.text
        user_profile = app_tables.fin_user_profile.search()
        tenure = self.ids.tenure.text

        platform_fee = []
        for i in ex_amount:
            platform_fee.append(i['platform_returns'])

        schedule_date = []
        loan_id = []
        cos_id1 = []
        emi_type_pay = []
        lender_customer_id = []
        borrower_email = []
        lender_email = []
        total_repay_amount = []
        loan_amount = []
        tenure_months = []
        interest_rate = []
        emi_amount = []
        for i in data1:
            loan_id.append(i['loan_id'])
            cos_id1.append(i['borrower_customer_id'])
            schedule_date.append(i['first_emi_payment_due_date'])
            emi_type_pay.append(i['emi_payment_type'])
            lender_customer_id.append(i['lender_customer_id'])
            borrower_email.append(i['borrower_email_id'])
            lender_email.append(i['lender_email_id'])
            total_repay_amount.append(i['total_repayment_amount'])
            loan_amount.append(i['loan_amount'])
            tenure_months.append(i['tenure'])
            interest_rate.append(i['interest_rate'])
            emi_amount.append(i['monthly_emi'])

        cos_id = []
        account_num = []

        for i in user_profile:
            cos_id.append(i['customer_id'])
            account_num.append(i['account_number'])
        index = 0
        if cos_id1[index] in cos_id:
            index2 = cos_id.index(cos_id1[index])
            self.ids.account_number.text = str(account_num[index2])

        wallet_customer_id = []
        wallet_amount = []
        for i in wallet:
            wallet_customer_id.append(i['customer_id'])
            wallet_amount.append(i['wallet_amount'])

        lender_customer_id = []
        loan_id_list = []
        for i in data1:
            loan_id_list.append(i['loan_id'])
            lender_customer_id.append(i['lender_customer_id'])

        index = 0
        last_index = 0
        if value in loan_id:
            index = loan_id.index(value)
        if value not in emi_loan_id:
            remain_amount_emi = total_repay_amount[index] - emi_amount[index]
        else:
            last_index = len(emi_loan_id) - 1 - emi_loan_id[::-1].index(value)
            remain_amount_emi = remain_amo[last_index] - emi_amount[index]
        emi_number = 0

        wallet = app_tables.fin_wallet.search()
        wallet_customer_id = []
        wallet_amount = []
        wallet_email = []
        wallet_id = []
        for i in wallet:
            wallet_customer_id.append(i['customer_id'])
            wallet_amount.append(i['wallet_amount'])
            wallet_email.append(i['user_email'])
            wallet_id.append(i['wallet_id'])

        lender_data = app_tables.fin_lender.search()
        lender_cus_id = []
        create_date = []
        for i in lender_data:
            lender_cus_id.append(i['customer_id'])

        transaction = app_tables.fin_wallet_transactions.search()
        t_id = []
        for i in transaction:
            t_id.append(i['transaction_id'])

        if len(t_id) >= 1:
            transaction_id = 'TA' + str(int(t_id[-1][2:]) + 1).zfill(4)
        else:
            transaction_id = 'TA0001'
        transaction_date_time = datetime.today()

        if value not in emi_loan_id:
            emi_number = 1
        else:
            last_index = len(emi_loan_id) - 1 - emi_loan_id[::-1].index(value)
            emi_number = emi_num[last_index] + 1

        lender_returns = 0
        if value in loan_id:
            index = loan_id.index(value)
            interest_amount = (loan_amount[index] * interest_rate[index]) / 100
            total_interest_amount = loan_amount[index] + interest_amount
            lender_returns = total_interest_amount - loan_amount[index]
        else:
            print("loan id not found")

        monthly_lender_returns = lender_returns / tenure_months[index]

        if emi_type_pay[index].strip() == 'Monthly':
            monthly_lender_returns = lender_returns / tenure_months[index]
        elif emi_type_pay[index].strip() == 'Three Months':
            monthly_lender_returns = lender_returns / (tenure_months[index] / 3)
        elif emi_type_pay[index].strip() == 'Six Months':
            monthly_lender_returns = lender_returns / (tenure_months[index] / 6)
        elif emi_type_pay[index].strip() == 'One Time':
            if tenure:
                monthly_lender_returns = lender_returns / (tenure_months[index] / tenure_months[index])

        print(monthly_lender_returns)
        print(lender_returns)

        next_payment_date = None
        b_index = 0
        l_index = 0

        index1 = 0
        print(lender_customer_id[index] in wallet_customer_id)
        print(int(cos_id1[index]) in wallet_customer_id)
        if lender_customer_id[index] in wallet_customer_id and int(cos_id1[index]) in wallet_customer_id:
            b_index = wallet_customer_id.index(int(cos_id1[index]))
            l_index = wallet_customer_id.index(lender_customer_id[index])
        print(wallet[b_index]['wallet_amount'])
        print(total)
        print(b_index)
        if wallet[b_index]['wallet_amount'] >= float(total):
            wallet[b_index]['wallet_amount'] -= float(total)
            wallet[l_index]['wallet_amount'] += float(total)

            if emi_type_pay[index].strip() == 'Monthly':
                next_payment_date = self.shechule_date[value] + timedelta(days=30)
                print(schedule_date[index])
            elif emi_type_pay[index].strip() == 'Three Months':
                next_payment_date = self.shechule_date[value] + timedelta(days=90)
            elif emi_type_pay[index].strip() == 'Six Months':
                next_payment_date = self.shechule_date[value] + timedelta(days=180)
            elif emi_type_pay[index].strip() == 'One Time':
                if tenure:
                    next_payment_date = self.shechule_date[value] + timedelta(days=30 * int(tenure))

            if len(platform_fee) < 1:
                app_tables.fin_platform_fees.add_row(
                    platform_returns=float(extra_amount)
                )
            else:
                if ex_amount[0]['platform_returns'] is None:
                    ex_amount[0]['platform_returns'] = 0.0
                ex_amount[0]['platform_returns'] += float(extra_amount)

            paid_amount1 = 0
            for i in emi_loan_id:
                if i == value:
                    index3 = emi_loan_id.index(value)
                    paid_amount1 += paid_amount[index3]
                else:
                    paid_amount1 = 0
            remain_amount = total_repay_amount[index] - paid_amount1

            if value not in emi_loan_id:
                re_ten = int(tenure)
            else:
                last_index = len(emi_loan_id) - 1 - emi_loan_id[::-1].index(value)
                re_ten = remain_tenure[last_index]

            if emi_type_pay[index].strip() == 'Monthly':
                if re_ten == 1:
                    re_ten = 0
                    data1[index]['loan_updated_status'] = 'closed'
                else:
                    re_ten -= 1
                print(re_ten)

            elif emi_type_pay[index].strip() == 'Three Months':
                if re_ten > 3 and re_ten < 6:
                    re_ten = 0
                    data1[index]['loan_updated_status'] = 'closed'
                    remain_amount_emi = 0
                elif re_ten == 3:
                    re_ten = 0
                    data1[index]['loan_updated_status'] = 'closed'
                    remain_amount_emi = 0
                else:
                    re_ten -= 3
                print(re_ten)

            elif emi_type_pay[index].strip() == 'Six Months':
                if re_ten > 6 and re_ten < 12:
                    re_ten = 0
                    data1[index]['loan_updated_status'] = 'closed'

                elif re_ten == 6:
                    re_ten = 0
                    data1[index]['loan_updated_status'] = 'closed'
                else:
                    re_ten -= 6

            elif emi_type_pay[index].strip() == 'One Time':
                if tenure:
                    re_ten = 0
                    data1[index]['loan_updated_status'] = 'closed'

            app_tables.fin_emi_table.add_row(
                loan_id=str(value),
                extra_fee=float(extra_amount),
                amount_paid=float(total),
                scheduled_payment_made=datetime.today(),
                scheduled_payment=schedule_date[index],
                next_payment=next_payment_date,
                account_number=account_num[index1],
                emi_number=emi_number,
                borrower_email=borrower_email[index],
                borrower_customer_id=cos_id1[index],
                lender_customer_id=lender_customer_id[index],
                lender_email=lender_email[index],
                remaining_tenure=re_ten,
                total_remaining_amount=float(remain_amount_emi),
                payment_type="pay now"

            )

            app_tables.fin_wallet_transactions.add_row(transaction_id=transaction_id,
                                                       customer_id=wallet_customer_id[b_index],
                                                       user_email=wallet_email[b_index],
                                                       transaction_type="amount transferred",
                                                       amount=float(total),
                                                       status='success', wallet_id=wallet_id[b_index],
                                                       transaction_time_stamp=transaction_date_time,
                                                       receiver_customer_id=wallet_customer_id[l_index],
                                                       receiver_email=wallet_email[l_index])
            app_tables.fin_wallet_transactions.add_row(transaction_id=transaction_id,
                                                       customer_id=wallet_customer_id[l_index],
                                                       user_email=wallet_email[l_index],
                                                       transaction_type="amount received",
                                                       amount=float(total),
                                                       status='success', wallet_id=wallet_id[l_index],
                                                       transaction_time_stamp=transaction_date_time,
                                                       receiver_customer_id=wallet_customer_id[b_index],
                                                       receiver_email=wallet_email[b_index])

            if lender_customer_id[index] in lender_cus_id:
                len_index = lender_cus_id.index(lender_customer_id[index])
                if lender_data[len_index]['return_on_investment'] == None:
                    lender_data[len_index]['return_on_investment'] = 0
                    lender_data[len_index]['return_on_investment'] += float(round(monthly_lender_returns, 2))
                else:
                    lender_data[len_index]['return_on_investment'] += float(round(monthly_lender_returns, 2))
            else:
                print('customer id is not there')

            if data1[index]['lender_returns'] == None:
                data1[index]['lender_returns'] = 0
                data1[index]['lender_returns'] += float(round(monthly_lender_returns, 2))
            else:
                data1[index]['lender_returns'] += float(round(monthly_lender_returns, 2))

            if data1[index]['loan_updated_status'] == 'foreclosure':
                data1[index]['loan_updated_status'] = 'closed'
            data1[index]['total_amount_paid'] = float(paid_amount1)
            data1[index]['remaining_amount'] = float(remain_amount)
            anvil.server.call('loan_text', None)
            sm = self.manager
            wallet_screen = LastScreenWallet(name='LastScreenWallet')
            sm.add_widget(wallet_screen)
            sm.current = 'LastScreenWallet'

        elif wallet_amount[b_index] < float(total):
            self.show_success_dialog2(f"Insufficient Balance Please Deposit {float(total)}")
            anvil.server.call('loan_text', total)

            sm = self.manager
            # Create a new instance of the LenderWalletScreen
            wallet_screen = WalletScreen(name='WalletScreen', loan_amount_text=float(total))
            # Add the LenderWalletScreen to the existing ScreenManager
            sm.add_widget(wallet_screen)
            # Switch to the LenderWalletScreen
            sm.current = 'WalletScreen'

    def go_to_menu_screen(self):
        sm = self.manager

        # Create a new instance of the LoginScreen
        payment_details = ViewPaymentDetails(name='ViewPaymentDetails')

        # Add the LoginScreen to the existing ScreenManager
        sm.add_widget(payment_details)

        # Switch to the LoginScreen
        sm.current = 'ViewPaymentDetails'
        self.manager.get_screen('ViewPaymentDetails').initialize_with_value(self.loan_id, self.shechule_date)

    def go_to_part_payment(self):
        sm = self.manager

        # Create a new instance of the LoginScreen
        profile = PartPayment(name='PartPayment')

        # Add the LoginScreen to the existing ScreenManager
        sm.add_widget(profile)

        # Switch to the LoginScreen
        sm.current = 'PartPayment'
        self.manager.get_screen('PartPayment').initialize_with_value(self.loan_id, self.shechule_date)

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

    def show_success_dialog2(self, text):
        dialog = MDDialog(
            text=text,
            size_hint=(0.8, 0.3),
            buttons=[
                MDRaisedButton(
                    text="OK",
                    on_release=lambda *args: self.open_dashboard_screen2(dialog),
                    theme_text_color="Custom",
                    text_color=(0.043, 0.145, 0.278, 1),
                )
            ]
        )
        dialog.open()

    def open_dashboard_screen(self, dialog):

        dialog.dismiss()
        self.manager.current = 'DashboardScreen'

    def open_dashboard_screen2(self, dialog):

        dialog.dismiss()
        self.manager.current = 'WalletScreen'

    def on_pre_enter(self, *args):
        Window.bind(on_keyboard=self.on_back_button)

    def on_pre_leave(self):
        Window.unbind(on_keyboard=self.on_back_button)

    def on_back_button(self, instance, key, scancode, codepoint, modifier):
        if key == 27:
            self.go_back()
            return True
        return False

    def go_back(self):
        self.manager.transition = SlideTransition(direction='right')
        self.manager.current = 'DuesScreen'

    def current(self):
        self.manager.current = 'DuesScreen'
class ViewPaymentDetails(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def initialize_with_value(self, value,shechule_date):
        print(value)
        self.shechule_date = shechule_date
        loan = app_tables.fin_loan_details.search()
        user_profile = app_tables.fin_user_profile.search()
        product_details = app_tables.fin_product_details.search()
        emi_data = app_tables.fin_emi_table.search()
        extension = app_tables.fin_extends_loan.search()
        foreclose = app_tables.fin_foreclosure.search()
        customer_id = []
        schedule_date = []
        loan_id = []
        emi_payment = []
        loan_status =[]
        tenure = []
        interest = []
        repayment_amount = []
        loan_amount = []
        emi_amount = []
        product_id = []
        total_repay_amount = []
        s = 0
        for i in loan:
            s += 1
            customer_id.append(i['borrower_customer_id'])
            schedule_date.append(i['first_emi_payment_due_date'])
            loan_id.append(i['loan_id'])
            emi_payment.append(i['emi_payment_type'])
            loan_status.append(i['loan_updated_status'])
            tenure.append(i['tenure'])
            interest.append(i['interest_rate'])
            repayment_amount.append(i['total_repayment_amount'])
            loan_amount.append(i['loan_amount'])
            emi_amount.append(i['monthly_emi'])
            product_id.append(i['product_id'])
            total_repay_amount.append(i['total_repayment_amount'])
        index = 0
        if value in loan_id:
            index = loan_id.index(value)

        cos_id = []
        account_num = []

        for i in user_profile:
            cos_id.append(i['customer_id'])
            account_num.append(i['account_number'])
        index2 = 0
        if customer_id[index] in cos_id:
            index2 = cos_id.index(customer_id[index])
            print(account_num[index2])
            print(customer_id[index])
            print(cos_id[index2])

        pro_id = []
        process_fee = []
        for i in product_details:
            pro_id.append(i['product_id'])
            process_fee.append(i['processing_fee'])
        index3 = 0
        if product_id[index] in pro_id:
            index3 = pro_id.index(product_id[index])

        extra_fee = []
        loan_id3 = []
        emi_num = []
        schedule_payment = []
        remain_tenure = []
        remain_amount1 = []
        for i in emi_data:
            loan_id3.append(i['loan_id'])
            extra_fee.append(i['extra_fee'])
            emi_num.append(i['emi_number'])
            schedule_payment.append((i['scheduled_payment_made']))
            remain_tenure.append(i['remaining_tenure'])
            remain_amount1.append(i['total_remaining_amount'])

        emi_indices = [i for i, lid in enumerate(loan_id3) if lid == value]

        index4 = 0
        if value in loan_id3:
            index4 = loan_id3.index(value)

        loan_id4 = []
        extend_loan_status =[]
        extend_months = []
        for i in extension:
            loan_id4.append(i['loan_id'])
            extend_loan_status.append(i['status'])
            extend_months.append(i['total_extension_months'])
        index5 = 0
        if value in loan_id4:
            index5 = loan_id4.index(value)

        loan_id5 = []
        foreclose_status = []
        for i in foreclose:
            loan_id5.append(i['loan_id'])
            foreclose_status.append(i['status'])
        index6 = 0
        if value in loan_id5:
            index6 = loan_id5.index(value)

        monthly_tenure = 0
        principal_amount = 0
        interest_amount = 0
        for i in range(s):
            if loan_status[i] == "disbursed":

                if emi_payment[index].strip() == "Monthly":

                    monthly_tenure = tenure[index]
                    loan_beginning = loan_amount[index]
                    interest_amount = round(loan_beginning * (interest[index] / 100) / 12)
                    principal_amount = emi_amount[index] - interest_amount


                elif emi_payment[index].strip() == "Three Months":
                    monthly_tenure = tenure[index]//3
                    loan_beginning = loan_amount[index]
                    interest_amount = round(loan_beginning * (interest[index] / 100) / 12)
                    principal_amount = emi_amount[index] - interest_amount


                elif emi_payment[index].strip() == "Six Months":
                    monthly_tenure = tenure[index]//6
                    loan_beginning = loan_amount[index]
                    interest_amount = round(loan_beginning * (interest[index] / 100) / 12)
                    principal_amount = emi_amount[index] - interest_amount

                elif emi_payment[index].strip() == "One Time":
                    monthly_tenure = tenure[index]//tenure[index]
                    loan_beginning = loan_amount[index]
                    interest_amount = loan_beginning * (interest[index] / 100) / 12
                    principal_amount = emi_amount[index] - interest_amount

            elif loan_status[i] == "extension" and extend_loan_status[index5] == "approved" or extend_loan_status[index6] == "rejected":
                if emi_payment[index].strip() == "Monthly":

                    monthly_tenure = tenure[index] + extend_months[index5]
                    loan_beginning = loan_amount[index]
                    interest_amount = round(loan_beginning * (interest[index] / 100) / 12)
                    principal_amount = emi_amount[index] - interest_amount


                elif emi_payment[index].strip() == "Three Months":
                    monthly_tenure = (tenure[index] + extend_months[index5]) // 3
                    loan_beginning = loan_amount[index]
                    interest_amount = round(loan_beginning * (interest[index] / 100) / 12)
                    principal_amount = emi_amount[index] - interest_amount


                elif emi_payment[index].strip() == "Six Months":
                    monthly_tenure = (tenure[index] + extend_months[index5])// 6
                    loan_beginning = loan_amount[index]
                    interest_amount = round(loan_beginning * (interest[index] / 100) / 12)
                    principal_amount = emi_amount[index] - interest_amount

                elif emi_payment[index].strip() == "One Time":
                    monthly_tenure = (tenure[index] + extend_months[index5]) // tenure[index]
                    loan_beginning = loan_amount[index]
                    interest_amount = round(loan_beginning * (interest[index] / 100) / 12)
                    principal_amount = emi_amount[index] - interest_amount


            elif loan_status[i] == "foreclosure" and foreclose_status[index6] == "approved" or foreclose_status[index6] == "rejected":

                if emi_payment[index].strip() == "Monthly":

                    monthly_tenure = tenure[index]
                    loan_beginning = loan_amount[index]
                    interest_amount = round(loan_beginning * (interest[index]/100)/12)
                    principal_amount = emi_amount[index] - interest_amount


                elif emi_payment[index].strip() == "Three Months":
                    monthly_tenure = tenure[index]//3
                    loan_beginning = loan_amount[index]
                    interest_amount = round(loan_beginning * (interest[index] / 100) / 12)
                    principal_amount = emi_amount[index] - interest_amount


                elif emi_payment[index].strip() == "Six Months":
                    monthly_tenure = tenure[index]//6
                    loan_beginning = loan_amount[index]
                    interest_amount = round(loan_beginning * (interest[index] / 100) / 12)
                    principal_amount = emi_amount[index] - interest_amount

                elif emi_payment[index].strip() == "One Time":
                    monthly_tenure = tenure[index]//tenure[index]
                    loan_beginning = loan_amount[index]
                    interest_amount = round(loan_beginning * (interest[index] / 100) / 12, 2)
                    principal_amount = emi_amount[index] - interest_amount

        width_id = 20
        width_date = 15
        width_amount = 20
        row_data = []

        if value not in emi_data:
            re_ten = int(tenure[index])
        else:
            last_index = len(emi_data) - 1 - emi_data[::-1].index(value)
            re_ten = remain_tenure[last_index]

        self.amount = emi_amount[index]
        amo = (emi_amount[index]/3) * (re_ten % 3)
        amo1 = (emi_amount[index] / 6) * (re_ten % 6)
        print(re_ten % 3)
        print(amo)

        for i in range(monthly_tenure):
            extra_payment = extra_fee[emi_indices[i]] if i < len(emi_indices) else 0
            scheduled = schedule_payment[emi_indices[i]] if i < len(emi_indices) else 0
            total_amount = emi_amount[index] + extra_payment
            next_payment_date = None
            if emi_payment[index].strip() == 'Monthly':
                next_payment_date = self.shechule_date[value] + timedelta(days=30 * i+1)
            elif emi_payment[index].strip() == 'Three Months':
                next_payment_date = self.shechule_date[value] + timedelta(days=90 * i+1)
                if re_ten % 3 != 0 and i == (monthly_tenure - 1):
                    self.amount = round(emi_amount[index] + amo, 2)

            elif emi_payment[index].strip() == 'Six Months':
                next_payment_date = self.shechule_date[value] + timedelta(days=180 * i+1)
                if re_ten % 6 != 0 and i == (monthly_tenure - 1):
                    self.amount = round(emi_amount[index] + amo1, 2)

            elif emi_payment[index].strip() == 'One Time':
                if tenure:
                    next_payment_date = self.shechule_date[value] + timedelta(days=30 * int(tenure[index]))
            next_pay = next_payment_date.strftime("%d/%m/%Y")
            if isinstance(scheduled, datetime):
                scheduled_date = scheduled.date()
                scheduled_time = scheduled.strftime("%H:%M:%S")

            else:
                scheduled_date = "N/A"
                scheduled_time = "N/A"
            row_data.append((
                f"{i + 1}".center(width_id),
                f"{next_pay}".center(width_date),
                f"{repayment_amount[index]}".center(width_amount),
                f"{self.amount}".center(width_amount),
                f"{extra_payment}".center(width_amount),
                f"{total_amount}".center(width_amount),
                f"{principal_amount}".center(width_amount),
                f"{interest_amount}".center(width_amount),
                f"{0}".center(width_id),
                f"{scheduled_date}".center(width_date),
                f"{scheduled_time}".center(width_date),
                f"{account_num[index2]}".center(width_amount),
                f"{process_fee[index3]}".center(width_amount)
            ))

        layout = AnchorLayout()
        data_tables = MDDataTable(
            size_hint=(1, 1),
            use_pagination=True,
            rows_num=12,
            column_data=[
                ("Payment No", dp(30)),
                ("Next Payment Date", dp(30)),
                ("Beginning Balance", dp(30)),
                ("Payment Due", dp(30)),
                ("Extra Payment", dp(30)),
                ("Total Payment", dp(30)),
                ("Principal Amount", dp(30)),
                ("Interest Amount", dp(30)),
                ("Ending Balance", dp(30)),
                ("Payment Date", dp(30)),
                ("Payment Time", dp(30)),
                ("Account Number", dp(30)),
                ("Processing Fee", dp(30)),
            ],
            row_data=row_data,
        )
        layout.add_widget(data_tables)
        self.ids.container1.clear_widgets()
        self.ids.container1.add_widget(layout)
    def go_back(self):
        self.manager.current = 'DuesScreen'



class LastScreenWallet(Screen):

    def go_back_home(self):
        self.manager.current = 'DashboardScreen'


class PartPayment(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def initialize_with_value(self, value, shechule_date):
        self.loan_id = value
        print(value)
        today_date = datetime.now(tz=utc).date()
        emi_data = app_tables.fin_emi_table.search()
        emi_loan_id = []
        emi_num = []
        next_payment = []
        for i in emi_data:
            emi_loan_id.append(i['loan_id'])
            emi_num.append(i['emi_number'])
            next_payment.append(i['next_payment'])

        product = app_tables.fin_product_details.search()
        product_id = []
        lapsed_fee = []
        default_fee_percentage = []
        default_fee_amount = []
        npa_percentage = []
        npa_fee_amount = []
        default_type = []
        npa_type = []

        for i in product:
            product_id.append(i['product_id'])
            lapsed_fee.append(i['lapsed_fee'])
            default_fee_percentage.append(i['default_fee'])
            default_fee_amount.append(i['default_fee_amount'])
            default_type.append(i['default_select_percentage_amount'])
            npa_percentage.append(i['npa'])
            npa_fee_amount.append(i['npa_amount'])
            npa_type.append(i['npa_select_percentage_amount'])
        data1 = app_tables.fin_loan_details.search()
        user_profile = app_tables.fin_user_profile.search()

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
        for i in data1:
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

        loan_details = app_tables.fin_loan_details.search()
        loan_id1 = []
        remain_amount = []
        for i in loan_details:
            loan_id1.append(i['loan_id'])
            remain_amount.append(i['remaining_amount'])
        if value in loan_id1:
            index0 = loan_id1.index(value)
            self.ids.remain.text = str(remain_amount[index0])

        index = 0

        if value in loan_id:
            index = loan_id.index(value)
            self.ids.name.text = str(borrower_name[index])
            self.ids.loan_amount1.text = str(loan_amount[index])
            self.ids.tenure.text = str(tenure[index])
            self.ids.status.text = str(loan_status[index])
            self.ids.interest_rate.text = str(interest[index])
            self.ids.emi_amount.text = str(monthly_emi[index])

        cos_id = []
        account_num = []
        for i in user_profile:
            cos_id.append(i['customer_id'])
            account_num.append(i['account_number'])

        if cos_id1[index] in cos_id:
            index1 = cos_id1.index(cos_id1[index])
            self.ids.account_number.text = str(account_num[index1])

        extend_row = None
        extend_amount = 0
        foreclose_amount1 = 0
        emi_amount1 = 0
        new_emi_amount = 0

        if loan_status[index] == "disbursed":
            extra_amount = 0
            print(loan_status[index])
            print(extra_amount)
            log_email = anvil.server.call('another_method')
            profile = app_tables.fin_user_profile.search()
            email_user = []
            for i in profile:
                email_user.append(i['email_user'])
            log_index = 0
            if log_email in email_user:
                log_index = email_user.index(log_email)
            setting = app_tables.fin_loan_settings.search()
            a = 0
            date_type = []
            max_days = []
            min_days = []
            for i in setting:
                a += 1
                date_type.append(i['loans'])
                min_days.append(i['minimum_days'])
                max_days.append(i['maximum_days'])
            print(log_index)
            days_left = (today_date - shechule_date[value]).days
            print(days_left)
            late_fee = None
            for i in range(a):
                print(days_left >= min_days[i] and days_left < max_days[i])
                print(days_left, min_days[i], max_days[i])
                if days_left >= min_days[i] and days_left < max_days[i]:
                    late_fee = date_type[i]
                    if days_left > min_days[i]:
                        days_left = (today_date - shechule_date[value]).days - (min_days[i] + 1)

                    else:
                        days_left = 0

            print(late_fee)

            if late_fee == 'lapsed fee':
                product_index = product_id.index(loan_product[index])
                lapsed_percentage = lapsed_fee[product_index] + days_left
                print(lapsed_percentage)
                lapsed_amount = (monthly_emi[index] * lapsed_percentage) / 100
                total_amount = monthly_emi[index] + extra_amount
                ex_free = extra_amount + lapsed_amount
                part_pay = (total_amount + ex_free) / 2
                self.ids.extra.text = "Extra Payment (Late payment Fee)"
                self.ids.extra_amount.text = str(round(extra_amount + lapsed_amount, 2))
                self.ids.total_amount.text = str(round(total_amount + ex_free, 2))
                self.ids.amount1.text = str(round(part_pay, 2))
                data1[index]['loan_state_status'] = "lapsed"

            elif late_fee == 'default fee':
                default_amount = 0
                product_index = product_id.index(loan_product[index])
                lapsed_percentage = lapsed_fee[product_index] + days_left
                lapsed_amount = (monthly_emi[index] * lapsed_percentage) / 100
                default_percentage = default_fee_percentage[product_index] + days_left
                print(default_percentage)
                print(days_left)
                if default_type[product_index] == 'Default fee (%)':
                    default_amount = (monthly_emi[index] * default_percentage) / 100
                elif default_type[product_index] == 'Default fee (₹)':
                    default_amount = default_fee_amount[product_index] * days_left

                total_amount = monthly_emi[index] + extra_amount
                ex_free = extra_amount + default_amount + lapsed_amount
                part_pay = (total_amount + ex_free) / 2
                self.ids.extra.text = "Extra Payment(Default)"
                self.ids.extra_amount.text = str(round(extra_amount + default_amount + lapsed_amount, 2))
                self.ids.total_amount.text = str(round(total_amount + ex_free, 2))
                self.ids.amount1.text = str(round(part_pay, 2))
                data1[index]['loan_state_status'] = 'default'
                print(default_amount)
                print(default_type[product_index] == 'Non Performing Asset (%)')
                print(default_type[product_index] == 'Non Performing Asset (₹)')
                print(default_type[product_index])

            elif late_fee == 'NPA fee':
                npa_amount = 0
                default_amount = 0
                product_index = product_id.index(loan_product[index])
                lapsed_percentage = lapsed_fee[product_index] + days_left
                lapsed_amount = (monthly_emi[index] * lapsed_percentage) / 100
                default_percentage = default_fee_percentage[product_index] + days_left
                print(default_percentage)
                print(days_left)
                if default_type[product_index] == 'Default fee (%)':
                    default_amount = (monthly_emi[index] * default_percentage) / 100
                elif default_type[product_index] == 'Default fee (₹)':
                    default_amount = default_fee_amount[product_index] * days_left
                npa_percentage = npa_percentage[product_index] + days_left
                print(days_left)
                if npa_type[product_index] == 'Non Performing Asset (%)':
                    npa_amount = (monthly_emi[index] * npa_percentage) / 100
                elif npa_type[product_index] == 'Non Performing Asset (₹)':
                    npa_amount = default_fee_amount[product_index]
                total_amount = monthly_emi[index] + extra_amount
                ex_free = extra_amount + npa_amount + lapsed_amount + default_amount
                part_pay = (total_amount + ex_free) / 2

                self.ids.extra.text = "Extra Payment(NPA)"
                self.ids.extra_amount.text = str(round(extra_amount + npa_amount + lapsed_amount + default_amount, 2))
                self.ids.total_amount.text = str(round(total_amount +ex_free, 2))
                self.ids.amount1.text = str(round(part_pay, 2))

                data1[index]['loan_state_status'] = 'npa'

            else:
                total_amount = monthly_emi[index] + extra_amount
                part_pay = (total_amount + extra_amount) / 2
                self.ids.extra_amount.text = str(round(extra_amount, 2))
                self.ids.total_amount.text = str(round(total_amount))
                self.ids.extra.text = "Extra Payment "
                self.ids.amount1.text = str(round(part_pay, 2))



        elif loan_status[index] == "extension":
            emi_number = 0
            emi_data = app_tables.fin_emi_table.search(loan_id=str(value))
            if emi_data:
                emi = emi_data[0]
                emi_number = emi['emi_number']
            print(loan_status[index])
            extend_row = app_tables.fin_extends_loan.get(
                loan_id=str(value),
                emi_number=emi_number
            )
            if extend_row is not None and extend_row['status'] == "approved":
                extend_amount += extend_row['extension_amount']
                new_emi_amount += extend_row['new_emi']
                total_amount = new_emi_amount + extend_amount
                print(new_emi_amount, extend_amount)
                print(extend_amount)
                next_emi_num = emi_number + 1
                next_emi = app_tables.fin_emi_table.get(loan_id=str(value), emi_number=next_emi_num)

                if next_emi is not None:
                    next_payment_amount = next_emi['amount_paid']
                    extend_amount += next_payment_amount
                log_email = anvil.server.call('another_method')
                profile = app_tables.fin_user_profile.search()
                email_user = []
                for i in profile:
                    email_user.append(i['email_user'])
                log_index = 0
                if log_email in email_user:
                    log_index = email_user.index(log_email)
                setting = app_tables.fin_loan_settings.search()
                a = 0
                date_type = []
                max_days = []
                min_days = []
                for i in setting:
                    a += 1
                    date_type.append(i['loans'])
                    min_days.append(i['minimum_days'])
                    max_days.append(i['maximum_days'])
                days_left = (today_date - shechule_date[value]).days
                late_fee = None
                for i in range(a):
                    if days_left >= min_days[i] and days_left < max_days[i]:
                        late_fee = date_type[i]
                        if days_left > min_days[i]:
                            days_left = (today_date - shechule_date[value]).days - (min_days[i] + 1)
                        else:
                            days_left = 0
                        break
                if late_fee == 'lapsed fee':
                    product_index = product_id.index(loan_product[index])
                    lapsed_percentage = lapsed_fee[product_index] + days_left
                    lapsed_amount = (monthly_emi[index] * lapsed_percentage) / 100
                    extend_amount += extend_row['extension_amount'] + lapsed_amount
                    part_pay = (total_amount + extend_amount) / 2
                    self.ids.extra_amount.text = str(round(extend_amount + lapsed_amount, 2))
                    self.ids.emi_amount.text = str(new_emi_amount)
                    self.ids.total_amount.text = str(round(total_amount + lapsed_amount, 2))
                    self.ids.extra.text = "Extra Payment (Late payment Fee)"
                    self.ids.amount1.text = str(round(part_pay, 2))
                    data1[index]['loan_state_status'] = "lapsed"
                elif late_fee == 'default fee':
                    default_amount = 0
                    product_index = product_id.index(loan_product[index])
                    lapsed_percentage = lapsed_fee[product_index] + days_left
                    lapsed_amount = (monthly_emi[index] * lapsed_percentage) / 100
                    default_percentage = default_fee_percentage[product_index] + days_left
                    if default_type[product_index] == 'Default fee (%)':
                        default_amount = (monthly_emi[index] * default_percentage) / 100
                    elif default_type[product_index] == 'Default fee (₹)':
                        default_amount = default_fee_amount[product_index]
                    extend_amount += extend_row['extension_amount'] + lapsed_amount + default_amount
                    part_pay = (total_amount + extend_amount) / 2
                    self.ids.extra_amount.text = str(round(extend_amount + default_amount + lapsed_amount, 2))
                    self.ids.emi_amount.text = str(new_emi_amount)
                    self.ids.total_amount.text = str(round(total_amount + default_amount + lapsed_amount, 2))
                    self.ids.extra.text = "Extra Payment (Default)"
                    self.ids.amount1.text = str(round(part_pay, 2))
                    data1[index]['loan_state_status'] = "default"

                elif late_fee == 'NPA fee':
                    npa_amount = 0
                    default_amount = 0
                    product_index = product_id.index(loan_product[index])
                    lapsed_percentage = lapsed_fee[product_index] + days_left
                    lapsed_amount = (monthly_emi[index] * lapsed_percentage) / 100
                    default_percentage = default_fee_percentage[product_index] + days_left
                    if default_type[product_index] == 'Default fee (%)':
                        default_amount = (monthly_emi[index] * default_percentage) / 100
                    elif default_type[product_index] == 'Default fee (₹)':
                        default_amount = default_fee_amount[product_index]
                    npa_percentage = npa_percentage[product_index] + days_left
                    if npa_type[product_index] == 'Non Performing Asset (%)':
                        npa_amount = (monthly_emi[index] * npa_percentage) / 100
                    elif npa_type[product_index] == 'Non Performing Asset (₹)':
                        npa_amount = default_fee_amount[product_index]
                    extend_amount += extend_row['extension_amount'] + lapsed_amount + default_amount + npa_amount
                    part_pay = (total_amount + extend_amount) / 2
                    self.ids.extra_amount.text = str(
                        round(extend_amount + npa_amount + lapsed_amount + default_amount, 2))
                    self.ids.emi_amount.text = str(new_emi_amount)
                    self.ids.total_amount.text = str(
                        round(total_amount + npa_amount + lapsed_amount + default_amount, 2))
                    self.ids.extra.text = "Extra Payment (Default)"
                    self.ids.amount1.text = str(round(part_pay, 2))
                    data1[index]['loan_state_status'] = 'npa'
                else:
                    extend_amount += extend_row['extension_amount']
                    total_amount = monthly_emi[index] + extend_amount
                    part_pay = (total_amount) / 2
                    self.ids.extra_amount.text = str(round(extend_amount))
                    self.ids.emi_amount.text = str(new_emi_amount)
                    self.ids.total_amount.text = str(round(total_amount))
                    self.ids.extra.text = "Extra Payment"
                    self.ids.amount1.text = str(round(part_pay, 2))

        elif loan_status[index] == "foreclosure":
            print(loan_status[index])
            foreclosure_row = app_tables.fin_foreclosure.get(
                loan_id=str(value)
            )
            if foreclosure_row is not None and foreclosure_row['status'] == 'approved':
                foreclose_amount1 += foreclosure_row['foreclose_amount']
                emi_amount1 += foreclosure_row['total_due_amount']
                total_amount = foreclose_amount1 + emi_amount1
                log_email = anvil.server.call('another_method')
                profile = app_tables.fin_user_profile.search()
                email_user = []
                for i in profile:
                    email_user.append(i['email_user'])
                log_index = 0
                if log_email in email_user:
                    log_index = email_user.index(log_email)
                setting = app_tables.fin_loan_settings.search()
                a = 0
                date_type = []
                max_days = []
                min_days = []
                for i in setting:
                    a += 1
                    date_type.append(i['loans'])
                    min_days.append(i['minimum_days'])
                    max_days.append(i['maximum_days'])
                print(log_index)
                days_left = (today_date - shechule_date[value]).days
                print(days_left)
                late_fee = None
                for i in range(a):
                    if days_left >= min_days[i] and days_left < max_days[i]:
                        late_fee = date_type[i]
                        if days_left > min_days[i]:
                            days_left = (today_date - shechule_date[value]).days - (min_days[i] + 1)
                        else:
                            days_left = 0
                        break
                if late_fee == 'lapsed fee':
                    product_index = product_id.index(loan_product[index])
                    lapsed_percentage = lapsed_fee[product_index] + days_left
                    lapsed_amount = (monthly_emi[index] * lapsed_percentage) / 100
                    foreclose_amount1 += foreclosure_row['foreclose_amount'] + lapsed_amount
                    part_pay = (total_amount + foreclose_amount1) / 2
                    self.ids.extra_amount.text = str(round(foreclose_amount1 + lapsed_amount, 2))
                    self.ids.emi_amount.text = str(emi_amount1)
                    self.ids.total_amount.text = str(round(total_amount + lapsed_amount, 2))
                    self.ids.total.text = "Total Amount (Late payment Fee)"
                    self.ids.amount1.text = str(round(part_pay, 2))
                    data1[index]['loan_state_status'] = "lapsed"
                    data1[index]['loan_updated_status'] = "closed"

                elif late_fee == 'default fee':
                    default_amount = 0
                    product_index = product_id.index(loan_product[index])
                    lapsed_percentage = lapsed_fee[product_index] + days_left
                    lapsed_amount = (monthly_emi[index] * lapsed_percentage) / 100
                    default_percentage = default_fee_percentage[product_index] + days_left
                    if default_type[product_index] == 'Default fee (%)':
                        default_amount = (monthly_emi[index] * default_percentage) / 100
                    elif default_type[product_index] == 'Default fee (₹)':
                        default_amount = default_fee_amount[product_index]
                    foreclose_amount1 += foreclosure_row['foreclose_amount'] + lapsed_amount + default_amount
                    part_pay = (total_amount + foreclose_amount1) / 2
                    self.ids.extra_amount.text = str(round(foreclose_amount1 + default_amount + lapsed_amount, 2))
                    self.ids.emi_amount.text = str(emi_amount1)
                    self.ids.total_amount.text = str(round(total_amount + default_amount + lapsed_amount, 2))
                    self.ids.total.text = "Total Amount (Default)"
                    self.ids.amount1.text = str(round(part_pay, 2))
                    data1[index]['loan_state_status'] = "default"
                    data1[index]['loan_updated_status'] = "closed"

                elif late_fee == 'NPA fee':
                    npa_amount = 0
                    default_amount = 0
                    product_index = product_id.index(loan_product[index])
                    lapsed_percentage = lapsed_fee[product_index] + days_left
                    default_percentage = default_fee_percentage[product_index] + days_left
                    lapsed_amount = (monthly_emi[index] * lapsed_percentage) / 100
                    if default_type[product_index] == 'Default fee (%)':
                        default_amount = (monthly_emi[index] * default_percentage) / 100
                    elif default_type[product_index] == 'Default fee (₹)':
                        default_amount = default_fee_amount[product_index]
                    npa_percentage = npa_percentage[product_index] + days_left
                    if npa_type[product_index] == 'Non Performing Asset (%)':
                        npa_amount = (monthly_emi[index] * npa_percentage) / 100
                    elif npa_type[product_index] == 'Non Performing Asset (₹)':
                        npa_amount = default_fee_amount[product_index]
                    foreclose_amount1 += foreclosure_row['foreclose_amount'] + lapsed_amount + npa_amount + default_amount
                    part_pay = (total_amount + foreclose_amount1) / 2
                    self.ids.extra_amount.text = str(
                        round(foreclose_amount1 + npa_amount + default_amount + lapsed_amount, 2))
                    self.ids.emi_amount.text = str(emi_amount1)
                    self.ids.total_amount.text = str(
                        round(total_amount + npa_amount + default_amount + lapsed_amount, 2))
                    self.ids.extra.text = "Extra Payment (Default)"
                    self.ids.amount1.text = str(round(part_pay, 2))
                    data1[index]['loan_state_status'] = "default"
                    data1[index]['loan_updated_status'] = "closed"

                else:
                    foreclose_amount1 += foreclosure_row['foreclose_amount']
                    total_amount = monthly_emi[index] + foreclose_amount1
                    part_pay = (total_amount + foreclose_amount1) / 2
                    self.ids.extra.text = "Extra Payment"
                    self.ids.extra_amount.text = str(round(foreclose_amount1))
                    self.ids.emi_amount.text = str(emi_amount1)
                    self.ids.total_amount.text = str(round(total_amount))
                    self.ids.amount1.text = str(round(part_pay, 2))
                    data1[index]['loan_updated_status'] = "closed"

    def go_to_paynow1(self):
        emi_data = app_tables.fin_emi_table.search()
        emi_loan_id = []
        emi_num = []
        next_payment = []
        paid_amount = []
        part_payment_type = []
        part_payment_done = []
        payment_date = []
        part_payment_amount = []
        remain_amo = []
        for i in emi_data:
            emi_loan_id.append(i['loan_id'])
            emi_num.append(i['emi_number'])
            next_payment.append(i['next_payment'])
            paid_amount.append(i['amount_paid'])
            part_payment_type.append((i['payment_type']))
            part_payment_done.append(i['part_payment_done'])
            payment_date.append(i['part_payment_date'])
            part_payment_amount.append(i['part_payment_amount'])
            remain_amo.append(i['total_remaining_amount'])

        value = self.loan_id
        data1 = app_tables.fin_loan_details.search()
        wallet = app_tables.fin_wallet.search()
        total = self.ids.total_amount.text
        pay = self.ids.amount1.text
        extra_amount = self.ids.extra_amount.text
        user_profile = app_tables.fin_user_profile.search()
        tenure = self.ids.tenure.text

        emi_number = 0
        last_index = 0
        if value not in emi_loan_id:
            emi_number = 1
        else:
            last_index = len(emi_loan_id) - 1 - emi_loan_id[::-1].index(value)
            emi_number = emi_num[last_index] + 1

        schedule_date = []
        loan_id = []
        cos_id1 = []
        emi_type_pay = []
        lender_customer_id = []
        borrower_email = []
        lender_email = []
        total_repay_amount = []
        emi_amount = []
        loan_amount = []
        tenure_months = []
        interest_rate = []
        emi_amount = []
        for i in data1:
            loan_id.append(i['loan_id'])
            cos_id1.append(i['borrower_customer_id'])
            emi_amount.append(i['monthly_emi'])
            schedule_date.append(i['first_emi_payment_due_date'])
            emi_type_pay.append(i['emi_payment_type'])
            lender_customer_id.append(i['lender_customer_id'])
            borrower_email.append(i['borrower_email_id'])
            lender_email.append(i['lender_email_id'])
            total_repay_amount.append(i['total_repayment_amount'])
            loan_amount.append(i['loan_amount'])
            tenure_months.append(i['tenure'])
            interest_rate.append(i['interest_rate'])
            emi_amount.append(i['monthly_emi'])

        cos_id = []
        account_num = []

        for i in user_profile:
            cos_id.append(i['customer_id'])
            account_num.append(i['account_number'])
        index = 0
        if cos_id1[index] in cos_id:
            index2 = cos_id1.index(cos_id1[index])
            self.ids.account_number.text = str(account_num[index2])

        wallet_customer_id = []
        wallet_amount = []
        for i in wallet:
            wallet_customer_id.append(i['customer_id'])
            wallet_amount.append(i['wallet_amount'])

        lender_customer_id = []
        loan_id_list = []
        for i in data1:
            loan_id_list.append(i['loan_id'])
            lender_customer_id.append(i['lender_customer_id'])

        index = 0
        if value in loan_id:
            index = loan_id.index(value)
        if value not in emi_loan_id:
            remain_amount_emi = total_repay_amount[index] - emi_amount[index]
        else:
            last_index = len(emi_loan_id) - 1 - emi_loan_id[::-1].index(value)
            remain_amount_emi = remain_amo[last_index] - emi_amount[index]

        lender_data = app_tables.fin_lender.search()
        lender_cus_id = []
        create_date = []
        for i in lender_data:
            lender_cus_id.append(i['customer_id'])

        lender_returns = 0
        if value in loan_id:
            index = loan_id.index(value)
            interest_amount = (loan_amount[index] * interest_rate[index]) / 100
            total_interest_amount = loan_amount[index] + interest_amount
            lender_returns = total_interest_amount - loan_amount[index]
        else:
            print("loan id not found")

        monthly_lender_returns = lender_returns / tenure_months[index]

        if emi_type_pay[index].strip() == 'Monthly':
            monthly_lender_returns = lender_returns / tenure_months[index]
        elif emi_type_pay[index].strip() == 'Three Months':
            monthly_lender_returns = lender_returns / (tenure_months[index] / 3)
        elif emi_type_pay[index].strip() == 'Six Months':
            monthly_lender_returns = lender_returns / (tenure_months[index] / 6)
        elif emi_type_pay[index].strip() == 'One Time':
            if tenure:
                monthly_lender_returns = lender_returns / (tenure_months[index] / tenure_months[index])

        print(monthly_lender_returns)
        print(lender_returns)

        wallet = app_tables.fin_wallet.search()
        wallet_customer_id = []
        wallet_amount = []
        wallet_email = []
        wallet_id = []
        for i in wallet:
            wallet_customer_id.append(i['customer_id'])
            wallet_amount.append(i['wallet_amount'])
            wallet_email.append(i['user_email'])
            wallet_id.append(i['wallet_id'])

        transaction = app_tables.fin_wallet_transactions.search()
        t_id = []
        for i in transaction:
            t_id.append(i['transaction_id'])

        if len(t_id) >= 1:
            transaction_id = 'TA' + str(int(t_id[-1][2:]) + 1).zfill(4)
        else:
            transaction_id = 'TA0001'
        transaction_date_time = datetime.today()

        next_payment_date = None
        b_index = 0
        l_index = 0

        index1 = 0
        print(lender_customer_id[index] in wallet_customer_id and int(cos_id1[index]) in wallet_customer_id)
        if lender_customer_id[index] in wallet_customer_id and int(cos_id1[index]) in wallet_customer_id:
            b_index = wallet_customer_id.index(int(cos_id1[index]))
            l_index = wallet_customer_id.index(lender_customer_id[index])

        if wallet[b_index]['wallet_amount'] >= float(total):
            wallet[b_index]['wallet_amount'] -= float(total)
            wallet[l_index]['wallet_amount'] += float(total)

            if value not in emi_loan_id:
                if value not in emi_loan_id:
                    emi_number = 1
                else:
                    last_index = len(emi_loan_id) - 1 - emi_loan_id[::-1].index(value)
                    emi_number = emi_num[last_index] + 1

                if emi_type_pay[index].strip() == 'Monthly':
                    payment_date = schedule_date[index]
                    print(schedule_date[index])
                elif emi_type_pay[index].strip() == 'Three Months':
                    payment_date = schedule_date[index]
                elif emi_type_pay[index].strip() == 'Six Months':
                    payment_date = schedule_date[index]
                elif emi_type_pay[index].strip() == 'One Time':
                    if tenure:
                        payment_date = schedule_date[index]
                paid_amount1 = 0
                for i in emi_loan_id:
                    if i == value:
                        index3 = emi_loan_id.index(value)
                        paid_amount1 += paid_amount[index3] * emi_number
                    else:
                        paid_amount1 = 0
                remain_amount = round(total_repay_amount[index] - paid_amount1, 2)

                app_tables.fin_emi_table.add_row(
                    loan_id=str(value),
                    extra_fee=float(extra_amount),
                    total_amount_pay=float(total),
                    amount_paid=float(pay),
                    scheduled_payment_made=datetime.today(),
                    scheduled_payment=schedule_date[index],
                    part_payment_date=datetime.today().date(),
                    account_number=account_num[index1],
                    emi_number=emi_number,
                    borrower_email=borrower_email[index],
                    borrower_customer_id=cos_id1[index],
                    lender_customer_id=lender_customer_id[index],
                    lender_email=lender_email[index],
                    total_remaining_amount=float(remain_amount_emi),
                    payment_type="part payment",
                    part_payment_amount=float(pay),
                    part_payment_done=int(1),
                    next_payment=payment_date
                )
                app_tables.fin_wallet_transactions.add_row(transaction_id=transaction_id,
                                                           customer_id=wallet_customer_id[b_index],
                                                           user_email=wallet_email[b_index],
                                                           transaction_type="amount transferred",
                                                           amount=float(pay),
                                                           status='success', wallet_id=wallet_id[b_index],
                                                           transaction_time_stamp=transaction_date_time,
                                                           receiver_customer_id=wallet_customer_id[l_index],
                                                           receiver_email=wallet_email[l_index])
                app_tables.fin_wallet_transactions.add_row(transaction_id=transaction_id,
                                                           customer_id=wallet_customer_id[l_index],
                                                           user_email=wallet_email[l_index],
                                                           transaction_type="amount received",
                                                           amount=float(pay),
                                                           status='success', wallet_id=wallet_id[l_index],
                                                           transaction_time_stamp=transaction_date_time,
                                                           receiver_customer_id=wallet_customer_id[b_index],
                                                           receiver_email=wallet_email[b_index])

                if lender_customer_id[index] in lender_cus_id:
                    len_index = lender_cus_id.index(lender_customer_id[index])
                    if lender_data[len_index]['return_on_investment'] == None:
                        lender_data[len_index]['return_on_investment'] = 0
                        lender_data[len_index]['return_on_investment'] += float(round(monthly_lender_returns/2, 2))
                    else:
                        lender_data[len_index]['return_on_investment'] += float(round(monthly_lender_returns/2, 2))
                else:
                    print('customer id is not there')

                if data1[index]['lender_returns'] == None:
                    data1[index]['lender_returns'] = 0
                    data1[index]['lender_returns'] += float(round(monthly_lender_returns/2, 2))
                else:
                    data1[index]['lender_returns'] += float(round(monthly_lender_returns/2, 2))

                data1[index]['total_amount_paid'] = float(paid_amount1)
                data1[index]['remaining_amount'] = float(remain_amount)
                anvil.server.call('loan_text', None)
                sm = self.manager
                wallet_screen = LastScreenWallet(name='LastScreenWallet')
                sm.add_widget(wallet_screen)
                sm.current = 'LastScreenWallet'
            elif value in emi_loan_id and part_payment_type[last_index] != 'part payment':
                if value not in emi_loan_id:
                    emi_number = 1
                else:
                    last_index = len(emi_loan_id) - 1 - emi_loan_id[::-1].index(value)
                    emi_number = emi_num[last_index] + 1

                if emi_type_pay[index].strip() == 'Monthly':
                    payment_date = schedule_date[index] + timedelta(days=30)
                    print(schedule_date[index])
                elif emi_type_pay[index].strip() == 'Three Months':
                    payment_date = schedule_date[index] + timedelta(days=90)
                elif emi_type_pay[index].strip() == 'Six Months':
                    payment_date = schedule_date[index] + timedelta(days=180)
                elif emi_type_pay[index].strip() == 'One Time':
                    if tenure:
                        payment_date = schedule_date[index] + timedelta(days=30 * int(tenure))

                paid_amount1 = 0
                for i in emi_loan_id:
                    if i == value:
                        index3 = emi_loan_id.index(value)
                        paid_amount1 += paid_amount[index3] * emi_number
                    else:
                        paid_amount1 = 0
                remain_amount = round(total_repay_amount[index] - paid_amount1, 2)
                app_tables.fin_emi_table.add_row(
                    loan_id=str(value),
                    extra_fee=float(extra_amount),
                    total_amount_pay=float(total),
                    amount_paid=float(pay),
                    scheduled_payment_made=datetime.today(),
                    scheduled_payment=schedule_date[index],
                    part_payment_date=datetime.today().date(),
                    account_number=account_num[index1],
                    emi_number=emi_number,
                    borrower_email=borrower_email[index],
                    borrower_customer_id=cos_id1[index],
                    lender_customer_id=lender_customer_id[index],
                    lender_email=lender_email[index],
                    payment_type="part payment",
                    part_payment_amount=float(pay),
                    total_remaining_amount=float(remain_amount_emi),
                    part_payment_done=int(1),
                    next_payment= payment_date
                )
                app_tables.fin_wallet_transactions.add_row(transaction_id=transaction_id,
                                                           customer_id=wallet_customer_id[b_index],
                                                           user_email=wallet_email[b_index],
                                                           transaction_type="amount transferred",
                                                           amount=float(pay),
                                                           status='success', wallet_id=wallet_id[b_index],
                                                           transaction_time_stamp=transaction_date_time,
                                                           receiver_customer_id=wallet_customer_id[l_index],
                                                           receiver_email=wallet_email[l_index])
                app_tables.fin_wallet_transactions.add_row(transaction_id=transaction_id,
                                                           customer_id=wallet_customer_id[l_index],
                                                           user_email=wallet_email[l_index],
                                                           transaction_type="amount received",
                                                           amount=float(pay),
                                                           status='success', wallet_id=wallet_id[l_index],
                                                           transaction_time_stamp=transaction_date_time,
                                                           receiver_customer_id=wallet_customer_id[b_index],
                                                           receiver_email=wallet_email[b_index])

                if lender_customer_id[index] in lender_cus_id:
                    len_index = lender_cus_id.index(lender_customer_id[index])
                    if lender_data[len_index]['return_on_investment'] == None:
                        lender_data[len_index]['return_on_investment'] = 0
                        lender_data[len_index]['return_on_investment'] += float(round(monthly_lender_returns/2, 2))
                    else:
                        lender_data[len_index]['return_on_investment'] += float(round(monthly_lender_returns/2, 2))
                else:
                    print('customer id is not there')

                if data1[index]['lender_returns'] == None:
                    data1[index]['lender_returns'] = 0
                    data1[index]['lender_returns'] += float(round(monthly_lender_returns/2, 2))
                else:
                    data1[index]['lender_returns'] += float(round(monthly_lender_returns/2, 2))
                data1[index]['total_amount_paid'] = float(paid_amount1)
                data1[index]['remaining_amount'] = float(remain_amount)
                anvil.server.call('loan_text', None)
                sm = self.manager
                wallet_screen = LastScreenWallet(name='LastScreenWallet')
                sm.add_widget(wallet_screen)
                sm.current = 'LastScreenWallet'
            elif value in emi_loan_id and part_payment_done[last_index] == 1 and part_payment_type[last_index] == 'part payment':

                if value not in emi_loan_id:
                    emi_number = 1
                else:
                    last_index = len(emi_loan_id) - 1 - emi_loan_id[::-1].index(value)
                    emi_number = emi_num[last_index]

                if emi_type_pay[index].strip() == 'Monthly':
                    payment_date = schedule_date[index] + timedelta(days=30)
                    print(schedule_date[index])
                elif emi_type_pay[index].strip() == 'Three Months':
                    payment_date = schedule_date[index] + timedelta(days=90)
                elif emi_type_pay[index].strip() == 'Six Months':
                    payment_date = schedule_date[index] + timedelta(days=180)
                elif emi_type_pay[index].strip() == 'One Time':
                    if tenure:
                        payment_date = schedule_date[index] + timedelta(days=30 * int(tenure))

                paid_amount1 = 0
                for i in emi_loan_id:
                    if i == value:
                        index3 = emi_loan_id.index(value)
                        paid_amount1 += paid_amount[index3] * emi_number
                    else:
                        paid_amount1 = 0

                print(paid_amount1)
                remain_amount = total_repay_amount[index] - paid_amount1
                print(remain_amount)

                app_tables.fin_wallet_transactions.add_row(transaction_id=transaction_id,
                                                           customer_id=wallet_customer_id[b_index],
                                                           user_email=wallet_email[b_index],
                                                           transaction_type="amount transferred",
                                                           amount=float(pay),
                                                           status='success', wallet_id=wallet_id[b_index],
                                                           transaction_time_stamp=transaction_date_time,
                                                           receiver_customer_id=wallet_customer_id[l_index],
                                                           receiver_email=wallet_email[l_index])
                app_tables.fin_wallet_transactions.add_row(transaction_id=transaction_id,
                                                           customer_id=wallet_customer_id[l_index],
                                                           user_email=wallet_email[l_index],
                                                           transaction_type="amount received",
                                                           amount=float(pay),
                                                           status='success', wallet_id=wallet_id[l_index],
                                                           transaction_time_stamp=transaction_date_time,
                                                           receiver_customer_id=wallet_customer_id[b_index],
                                                           receiver_email=wallet_email[b_index])

                if lender_customer_id[index] in lender_cus_id:
                    len_index = lender_cus_id.index(lender_customer_id[index])
                    if lender_data[len_index]['return_on_investment'] == None:
                        lender_data[len_index]['return_on_investment'] = 0
                        lender_data[len_index]['return_on_investment'] += float(round(monthly_lender_returns/2, 2))
                    else:
                        lender_data[len_index]['return_on_investment'] += float(round(monthly_lender_returns/2, 2))
                else:
                    print('customer id is not there')

                if data1[index]['lender_returns'] == None:
                    data1[index]['lender_returns'] = 0
                    data1[index]['lender_returns'] += float(round(monthly_lender_returns/2, 2))
                else:
                    data1[index]['lender_returns'] += float(round(monthly_lender_returns/2, 2))

                emi_data[last_index]['part_payment_date'] = datetime.today().date()
                emi_data[last_index]['payment_type'] = "pay now"
                emi_data[last_index]['part_payment_amount'] = float(pay) + float(pay)
                emi_data[last_index]['part_payment_done'] = int(2)
                emi_data[last_index]['next_payment'] = payment_date


                data1[index]['total_amount_paid'] = float(paid_amount1)
                data1[index]['remaining_amount'] = float(remain_amount)
                anvil.server.call('loan_text', None)
                sm = self.manager
                wallet_screen = LastScreenWallet(name='LastScreenWallet')
                sm.add_widget(wallet_screen)
                sm.current = 'LastScreenWallet'

        elif wallet_amount[b_index] < float(total):
            self.show_success_dialog2(f"Insufficient Balance Please Deposit {float(total)}")
            anvil.server.call('loan_text', total)

            sm = self.manager
            # Create a new instance of the LenderWalletScreen
            wallet_screen = WalletScreen(name='WalletScreen', loan_amount_text=float(total))
            # Add the LenderWalletScreen to the existing ScreenManager
            sm.add_widget(wallet_screen)
            # Switch to the LenderWalletScreen
            sm.current = 'WalletScreen'

    def on_back_button_press(self):
        self.manager.transition = SlideTransition(direction='right')
        self.manager.current = 'BorrowerDuesScreen'



    def show_success_dialog2(self, text):
        dialog = MDDialog(
            text=text,
            size_hint=(0.8, 0.3),
            buttons=[
                MDRaisedButton(
                    text="OK",
                    on_release=lambda *args: self.open_dashboard_screen2(dialog),
                    theme_text_color="Custom",
                    text_color=(0.043, 0.145, 0.278, 1),
                )
            ]
        )
        dialog.open()

    def open_dashboard_screen(self, dialog):

        dialog.dismiss()
        self.manager.current = 'DashboardScreen'

    def open_dashboard_screen2(self, dialog):

        dialog.dismiss()
        self.manager.current = 'WalletScreen'

    def on_pre_enter(self, *args):
        Window.bind(on_keyboard=self.on_back_button)

    def on_pre_leave(self):
        Window.unbind(on_keyboard=self.on_back_button)

    def on_back_button(self, instance, key, scancode, codepoint, modifier):
        if key == 27:
            self.go_back()
            return True
        return False

    def go_back(self):
        self.manager.transition = SlideTransition(direction='right')
        self.manager.current = 'DuesScreen'

    def current(self):
        self.manager.current = 'DuesScreen'


class DuesScreen(Screen):
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

        today_date = datetime.now(tz=utc).date()
        data = app_tables.fin_loan_details.search()
        emi_data = app_tables.fin_emi_table.search()
        profile = app_tables.fin_user_profile.search()
        customer_id = []
        loan_id = []
        loan_status = []
        borrower_id = []
        borrower_name = []
        schedule_date = []
        interest_rate = []
        tenure = []
        loan_amount = []

        s = 0

        for i in data:
            s += 1
            loan_id.append(i['loan_id'])
            customer_id.append(i['borrower_customer_id'])
            loan_status.append(i['loan_updated_status'])
            borrower_id.append(i['borrower_customer_id'])
            borrower_name.append(i['borrower_full_name'])
            schedule_date.append(i['first_emi_payment_due_date'])
            interest_rate.append(i['interest_rate'])
            tenure.append(i['tenure'])
            loan_amount.append(i['loan_amount'])

        emi_loan_id = []
        emi_num = []
        next_payment = []
        part_payment_type = []
        part_payment_done = []
        for i in emi_data:
            emi_loan_id.append(i['loan_id'])
            emi_num.append(i['emi_number'])
            next_payment.append(i['next_payment'])
            part_payment_type.append((i['payment_type']))
            part_payment_done.append(i['part_payment_done'])
        profile_customer_id = []
        profile_mobile_number = []
        profile_email_id = []
        for i in profile:
            profile_customer_id.append(i['customer_id'])
            profile_mobile_number.append(i['mobile'])
            profile_email_id.append(i['email_user'])
        email = anvil.server.call('another_method')

        cos_id = None
        index = 0
        if email in profile_email_id:
            index = profile_email_id.index(email)
            cos_id = profile_customer_id[index]
        index_list = []
        a = -1
        shedule_date = {}
        for i in range(s):
            a += 1
            print(customer_id[i], profile_customer_id[index])
            if customer_id[i] == profile_customer_id[index] and loan_status[i] == "disbursed" or loan_status[
                i] == "extension" or loan_status[i] == "foreclosure":
                if loan_id[i] not in emi_loan_id and schedule_date[i] is not None and today_date >= schedule_date[i]:
                    index_list.append(i)
                    shedule_date[loan_id[i]] = schedule_date[i]
                elif loan_id[i] in emi_loan_id:
                    last_index = len(emi_loan_id) - 1 - emi_loan_id[::-1].index(loan_id[i])
                    if next_payment[last_index] is not None and today_date >= next_payment[last_index]:
                        index_list.append(i)
                        shedule_date[loan_id[i]] = next_payment[last_index]

        print(index_list)
        print(shedule_date)
        b = 1
        k = -1
        for i in reversed(index_list):
            b += 1
            k += 1
            if customer_id[i] in profile_customer_id:
                number = profile_customer_id.index(customer_id[i])
            else:
                number = 0
            card = MDCard(
                orientation='vertical',
                size_hint=(None, None),
                size=("320dp", "240dp"),
                padding="10dp",
                spacing="3dp",
                elevation=3
            )
            horizontal_layout = BoxLayout(orientation='horizontal')
            if photo_texture:
                image = Image(texture=photo_texture, size_hint_x=None, height="30dp", width="60dp")
                horizontal_layout.add_widget(image)

            horizontal_layout.add_widget(Widget(size_hint_x=None, width='20dp'))
            text_layout = BoxLayout(orientation='vertical')
            text_layout.add_widget(MDLabel(
                text=f"[b]{borrower_name[i]}[/b],\n[b]{profile_mobile_number[number]}[/b]",
                theme_text_color='Custom',
                text_color=(0, 0, 0, 1),
                halign='left',
                markup=True,
            ))
            text_layout.add_widget(Widget(size_hint_y=None, height=dp(10)))
            # text_layout.add_widget(MDLabel(
            #     text=f"[b]Mobile No[/b]: {profile_mobile_number[number]}",
            #     theme_text_color='Custom',
            #     text_color=(0, 0, 0, 1),
            #     halign='left',
            #     markup=True,
            # ))
            text_layout.add_widget(MDLabel(
                text=f"[b]Loan Amount[/b]: {loan_amount[number]}",
                theme_text_color='Custom',
                text_color=(0, 0, 0, 1),
                halign='left',
                markup=True,
            ))
            # text_layout.add_widget(MDLabel(
            #     text=f"[b]Scheduled Payment:[/b] {scheduled_payment[number]}",
            #     theme_text_color='Custom',
            #     text_color=(0, 0, 0, 1),
            #     halign='left',
            #     markup=True,
            # ))
            text_layout.add_widget(MDLabel(
                text=f"[b]Interest Rate:[/b] {interest_rate[i]}",
                theme_text_color='Custom',
                text_color=(0, 0, 0, 1),
                halign='left',
                markup=True,
                # font_size='10sp'
            ))
            text_layout.add_widget(MDLabel(
                text=f"[b]Tenure:[/b] {tenure[i]}",
                theme_text_color='Custom',
                text_color=(0, 0, 0, 1),
                halign='left',
                markup=True,
            ))
            text_layout.add_widget(MDLabel(
                text=f"[b]Due Date[/b]: {shedule_date[loan_id[i]]}",
                theme_text_color='Custom',
                text_color=(0, 0, 0, 1),
                halign='left',
                markup=True,
            ))
            text_layout.add_widget(MDLabel(
                text=f"[b]Day Passed Due Date[/b] : {(today_date - shedule_date[loan_id[i]]).days}",
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
                spacing="35dp"
            )
            button2 = MDFillRoundFlatButton(
                text="     Pay Now     ",
                size_hint=(None, None),
                height="40dp",
                width="250dp",
                pos_hint={"center_x": 0},
                md_bg_color=(0, 0.502, 0, 1),
                on_release=lambda x, loan_id=loan_id[i]: self.icon_button_clicked(instance, loan_id, shedule_date)
            )
            button1 = MDFillRoundFlatButton(
                text="  Payment Details  ",
                size_hint=(None, None),
                height="40dp",
                width="250dp",
                pos_hint={"center_x": 1},
                md_bg_color=(0.043, 0.145, 0.278, 1),
                on_release=lambda x, loan_id=loan_id[i]: self.go_to_menu_screen(instance, loan_id, shedule_date)
            )
            button_layout.add_widget(button1)
            button_layout.add_widget(button2)
            card.add_widget(button_layout)

            # card.bind(on_release=lambda instance, loan_id=loan_id[i]: self.icon_button_clicked(instance, loan_id))
            self.ids.container.add_widget(card)
            # item = ThreeLineAvatarIconListItem(
            #     IconLeftWidget(
            #         icon="card-account-details-outline"
            #     ),
            #     text=f"Borrower Name : {borrower_name[i]}",
            #     secondary_text=f"Borrower Mobile Number : {profile_mobile_number[number]}",
            #     tertiary_text=f"Scheduled Date : {shedule_date[loan_id[i]]}",
            #     text_color=(0, 0, 0, 1),  # Black color
            #     theme_text_color='Custom',
            #     secondary_text_color=(0, 0, 0, 1),
            #     secondary_theme_text_color='Custom',
            #     tertiary_text_color=(0, 0, 0, 1),
            #     tertiary_theme_text_color='Custom'
            # )
            # item.bind(on_release=lambda instance, loan_id=loan_id[i],: self.icon_button_clicked(instance, loan_id,
            #                                                                                     shedule_date))
            # self.ids.container.add_widget(item)

    def get_email(self):
        # Make a call to the Anvil server function
        # Replace 'another_method' with the actual name of your Anvil server function
        return anvil.server.call('another_method')

    def icon_button_clicked(self, instance, loan_id, shedule_date):
        self.loan_id = loan_id
        self.shechule_date = shedule_date
        sm = self.manager

        # Create a new instance of the LoginScreen
        profile = BorrowerDuesScreen(name='BorrowerDuesScreen')

        # Add the LoginScreen to the existing ScreenManager
        sm.add_widget(profile)

        # Switch to the LoginScreen
        sm.current = 'BorrowerDuesScreen'
        self.manager.get_screen('BorrowerDuesScreen').initialize_with_value(loan_id, shedule_date)

    def go_to_menu_screen(self, instance, loan_id, shedule_date):
        sm = self.manager

        # Create a new instance of the LoginScreen
        payment_details = ViewPaymentDetails(name='ViewPaymentDetails')

        # Add the LoginScreen to the existing ScreenManager
        sm.add_widget(payment_details)

        # Switch to the LoginScreen
        sm.current = 'ViewPaymentDetails'
        self.manager.get_screen('ViewPaymentDetails').initialize_with_value(loan_id, shedule_date)

    def on_pre_enter(self):
        # Bind the back button event to the on_back_button method
        Window.bind(on_keyboard=self.on_back_button)

    def on_pre_leave(self):
        # Unbind the back button event when leaving the screen
        Window.unbind(on_keyboard=self.on_back_button)

    def on_back_button(self, instance, key, scancode, codepoint, modifier):

        if key == 27:
            self.go_back()
            return True
        return False

    def refresh(self):
        self.ids.container.clear_widgets()
        self.__init__()

    def go_back(self):
        self.manager.current = 'DashboardScreen'