from datetime import datetime, timezone

from anvil.tables import app_tables
from bson import utc
from kivy.factory import Factory
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.metrics import dp
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.image import Image
from kivy.uix.screenmanager import Screen, SlideTransition, ScreenManager
from kivy.uix.widget import Widget
from kivymd.app import MDApp
from kivymd.uix.button import MDRaisedButton, MDFillRoundFlatButton
from kivymd.uix.card import MDCard
from kivymd.uix.dialog import MDDialog
from kivymd.uix.label import MDLabel
from kivymd.uix.list import ThreeLineAvatarIconListItem, IconLeftWidget
import anvil.server
import anvil.server
from kivy.uix.label import Label
import base64
from kivy.core.image import Image as CoreImage
from io import BytesIO

lender_today_due = '''

<WindowManager>:
    TodayDuesTD:
    ViewProfileTD:

<TodayDuesTD>
    BoxLayout:
        orientation: 'vertical'
        MDTopAppBar:
            title: "Today's Dues"
            elevation: 3
            left_action_items: [['arrow-left', lambda x: root.go_back()]]
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
<ViewProfileTD>:
    GridLayout:
        cols: 1

        MDTopAppBar:
            title:"Today's Dues"
            md_bg_color:0.043, 0.145, 0.278, 1
            theme_text_color: 'Custom'
            text_color: 1,1,1,1 
            size_hint:1,None
            elevation: 3
            left_action_items: [['arrow-left', lambda x: root.on_back_button_press()]]
            pos_hint: {'top': 1} 

        ScrollView:
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

                    MDLabel:
                        id: loan_amount1
                        halign: 'left'
                        bold: True
                        text_color: 140/255, 140/255, 140/255, 1
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
                        theme_text_color: 'Custom'  
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
                        text: 'Payment Type '
                        halign: 'left'
                        theme_text_color: 'Custom'  
                        text_color: 0, 0, 0, 1 
                        bold: True

                    MDLabel:
                        id: pay
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
                        text: 'Total Amount'
                        halign: 'left'
                        theme_text_color: 'Custom'  
                        bold: True

                    MDLabel:
                        id: total_amount
                        halign: 'left'
                        theme_text_color: 'Custom'
                        text_color: 140/255, 140/255, 140/255, 1
                        bold: True
'''
Builder.load_string(lender_today_due)
date = datetime.today().date()
print(date)


class TodayDuesTD(Screen):
    def __init__(self, instance=None, **kwargs):
        super().__init__(**kwargs)

        data = app_tables.fin_emi_table.search()
        data1 = app_tables.fin_loan_details.search()
        today_date = datetime.now(timezone.utc).date()
        profile = app_tables.fin_user_profile.search()
        loan_id = []
        customer_id = []
        loan_status = []
        borrower_name = []
        schedule_date = []
        lender_customer_id = []
        loan_amount = []
        interest_rate = []
        tenure = []
        email = anvil.server.call('another_method')
        s = 0

        for i in data1:
            s += 1
            loan_id.append(i['loan_id'])
            customer_id.append(i['borrower_customer_id'])
            loan_status.append(i['loan_updated_status'])
            borrower_name.append(i['borrower_full_name'])
            schedule_date.append(i['first_emi_payment_due_date'])
            lender_customer_id.append(i['lender_customer_id'])
            loan_amount.append(i['loan_amount'])
            interest_rate.append(i['interest_rate'])
            tenure.append(i['tenure'])

        emi_loan_id = []
        emi_num = []
        next_payment = []
        for i in data:
            emi_loan_id.append(i['loan_id'])
            emi_num.append(i['emi_number'])
            next_payment.append(i['next_payment'])
        profile_customer_id = []
        profile_mobile_number = []
        profile_email = []
        profile_photo = {}
        for i in profile:
            profile_customer_id.append(i['customer_id'])
            profile_mobile_number.append(i['mobile'])
            profile_email.append(i['email_user'])

            # Load profile photo if available
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

        log_index = 0
        if email in profile_email:
            log_index = profile_email.index(email)
        else:
            print("email not there")

        index_list = []
        a = -1
        shedule_date = {}
        for i in range(s):
            a += 1
            if loan_status[i] == "disbursed" or loan_status[i] == "extension" or loan_status[i] == "foreclosure":
                if loan_id[i] not in emi_loan_id and schedule_date[i] != None and today_date >= schedule_date[i]:
                    index_list.append(i)
                    shedule_date[loan_id[i]] = schedule_date[i]
                elif loan_id[i] in emi_loan_id:
                    last_index = len(emi_loan_id) - 1 - emi_loan_id[::-1].index(loan_id[i])
                    if today_date >= next_payment[last_index]:
                        index_list.append(i)
                        shedule_date[loan_id[i]] = next_payment[last_index]

        print(index_list)
        print(shedule_date)
        today_date = datetime.now(timezone.utc).date()

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
            text_layout.add_widget(MDLabel(
                text=f"[b]Loan Amount[/b]: {loan_amount[number]}",
                theme_text_color='Custom',
                text_color=(0, 0, 0, 1),
                halign='left',
                markup=True,
            ))
            text_layout.add_widget(MDLabel(
                text=f"[b]Interest Rate:[/b] {interest_rate[i]}",
                theme_text_color='Custom',
                text_color=(0, 0, 0, 1),
                halign='left',
                markup=True,
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
            button1 = MDFillRoundFlatButton(
                text="            View Details             ",
                height="40dp",
                width="250dp",
                pos_hint={"center_x": 0.5, "center_y": 0.5},
                md_bg_color=(0.043, 0.145, 0.278, 1),
                on_release=lambda x, loan_id=loan_id[i]: self.icon_button_clicked(instance, loan_id, shedule_date)
            )

            card.add_widget(button1)
            self.ids.container2.add_widget(card)

        lender_data = app_tables.fin_lender.search()
        lender_cus_id = []
        create_date = []
        returns = []
        present_commitment = []

        for i in lender_data:
            lender_cus_id.append(i['customer_id'])
            create_date.append(i['member_since'])
            returns.append(i['return_on_investment'])
            present_commitment.append(i['present_commitments'])

        a = -1
        total_commitment = []
        present_commitmet = []
        for i in range(s):
            a += 1
            if lender_customer_id[i] == profile_customer_id[log_index] and loan_status[i] != 'lost opportunities' and \
                    loan_status[i] != 'rejected':
                total_commitment.append(loan_amount[i])

            if lender_customer_id[i] == profile_customer_id[log_index] and loan_status[i] != 'lost opportunities' and \
                    loan_status[i] != 'rejected' and loan_status[i] != 'closed':
                present_commitmet.append(loan_amount[i])

        if len(total_commitment) >= 1:
            if lender_customer_id[log_index] in lender_cus_id:
                lender_index = lender_cus_id.index(lender_customer_id[log_index])
                lender_data[lender_index]['lender_total_commitments'] = sum(total_commitment)
                print(total_commitment, sum(total_commitment))
            else:
                print('customer id not there')

        if len(present_commitmet) >= 1:
            if lender_customer_id[log_index] in lender_cus_id:
                lender_index = lender_cus_id.index(lender_customer_id[log_index])
                lender_data[lender_index]['present_commitments'] = sum(present_commitmet)
                print(present_commitmet, sum(present_commitmet))
            else:
                print('customer id not there')
    def icon_button_clicked(self, instance, loan_id, shedule_date):
        sm = self.manager

        # Create a new instance of the LoginScreen
        lender_today_due = ViewProfileTD(name='ViewProfileTD')

        # Add the LoginScreen to the existing ScreenManager
        sm.add_widget(lender_today_due)

        # Switch to the LoginScreen
        sm.current = 'ViewProfileTD'
        self.manager.get_screen('ViewProfileTD').initialize_with_value(loan_id, shedule_date)

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
        self.ids.container2.clear_widgets()
        self.__init__()

    def go_back(self):
        self.manager.current = 'LenderDashboard'


class ViewProfileTD(Screen):
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
        extra_fee = []
        total_amount = []
        for i in emi_data:
            emi_loan_id.append(i['loan_id'])
            emi_num.append(i['emi_number'])
            next_payment.append(i['next_payment'])
            part_payment_type.append((i['payment_type']))
            part_payment_done.append(i['part_payment_done'])
            extra_fee.append(i['extra_fee'])
            total_amount.append(i['total_amount_pay'])

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
        lender_customer_id = []
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
            lender_customer_id.append(i['lender_customer_id'])
        index = 0
        if value in loan_id:
            index = loan_id.index(value)
            self.ids.name.text = str(borrower_name[index])
            self.ids.loan_amount1.text = str(loan_amount[index])
            self.ids.tenure.text = str(tenure[index])
            self.ids.interest_rate.text = str(interest[index])
            self.ids.emi_amount.text = str(monthly_emi[index])

        last_index = 0
        if value not in emi_loan_id:
            last_index = index
            emi_number = 1
            self.ids.pay.text = "Not Paid"

        else:
            last_index = len(emi_loan_id) - 1 - emi_loan_id[::-1].index(value)
            emi_number = emi_num[last_index] + 1
            self.ids.pay.text = str(part_payment_type[last_index])
        cos_id = []
        account_num = []
        for i in user_profile:
            cos_id.append(i['customer_id'])
            account_num.append(i['account_number'])
        index1 = 0
        if cos_id1[index] in cos_id:
            index1 = cos_id.index(cos_id1[index])
            self.ids.account_number.text = str(account_num[index1])

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
                total_amount = monthly_emi[index] + extra_amount
                self.ids.extra_amount.text = str(round(extra_amount, 2))
                self.ids.total_amount.text = str(round(total_amount))
                self.ids.extra.text = "Extra Payment "


        elif loan_status[index] == "extension":
            emi_num = 0
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

    def on_back_button_press(self):
        self.manager.add_widget(Factory.TodayDuesTD(name='TodayDuesTD'))
        self.manager.current = 'TodayDuesTD'

    def current(self):
        self.manager.current = 'DuesScreen'


class LastScreenWallet(Screen):

    def go_back_home(self):
        self.manager.current = 'DashboardScreen'


class MyScreenManager(ScreenManager):
    pass
