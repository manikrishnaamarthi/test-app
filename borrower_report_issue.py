import re
from datetime import datetime

import anvil
from anvil.tables import app_tables
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen
from kivymd.toast import toast
from kivymd.uix.button import MDFlatButton
from kivymd.uix.dialog import MDDialog
from kivymd.uix.filemanager import MDFileManager

report_issue = '''
<WindowManager>:
    ReportScreen:

<ReportScreen>:
    BoxLayout:
        orientation: 'vertical'

        MDTopAppBar:
            title: "Report Your Issues"
            elevation: 3
            left_action_items: [['arrow-left', lambda x: root.go_back()]]
            right_action_items: [['refresh', lambda x: root.refresh()]]
            md_bg_color: 0.043, 0.145, 0.278, 1

        MDScrollView:
            MDGridLayout:
                cols: 1
                adaptive_height: True
                padding: dp(25)
                spacing: dp(2)

                MDLabel:
                    text: "Name:"
                    size_hint_y: None
                    height: dp(30)
                    halign: "left"
                    font_size: 20
                MDTextField:
                    id: name
                    hint_text: "Enter your name"   
                    multiline: False
                    size_hint_y: None
                    height: dp(40)
                    mode: "rectangle"
                MDLabel:
                    text: "Email ID:"
                    size_hint_y: None
                    height: dp(30)
                    halign: "left"
                    font_size: 20
                MDTextField:
                    id: email
                    hint_text: "Enter your email"
                    multiline: False
                    size_hint_y: None
                    height: dp(40)
                    mode: "rectangle"

                MDLabel:
                    text: "Mobile Number:"
                    size_hint_y: None
                    height: dp(30)
                    halign: "left"
                    font_size: 20
                MDTextField:
                    id: mobile_no
                    hint_text: "Enter mobile number"
                    multiline: False
                    size_hint_y: None
                    height: dp(40)
                    mode: "rectangle"

                MDLabel:
                    text: "Category:"
                    size_hint_y: None
                    height: dp(30)
                    halign: "left"
                    font_size: 20
                Spinner:
                    id: Category
                    text: "Select Category"
                    size_hint_y: None
                    size_hint_x: None
                    height: dp(40)
                    width: dp(300)
                    halign: "left"
                    color: 0, 0, 0, 1  # This sets the text color to black
                    background_color: 0, 0, 0, 0
                    on_text: root.update_subcategories()
                    canvas:
                        Color:
                            rgba: 0.5, 0.5, 0.5, 1  # Black color for the line
                        Line:
                            rectangle: self.x, self.y, self.width, self.height
                            width: 2 

                MDLabel:
                    text: "SubCategory:"
                    size_hint_y: None
                    height: dp(30)
                    halign: "left"
                    font_size: 20
                Spinner:
                    id: SubCategory
                    text: "Select SubCategory"
                    size_hint_y: None
                    size_hint_x: None
                    height: dp(40)
                    width: dp(300)
                    halign: "left"
                    background_color: 0, 0, 0, 0
                    color: 0, 0, 0, 1  # This sets the text color to black
                    canvas:
                        Color:
                            rgba: 0.5, 0.5, 0.5, 1  # Black color for the line
                        Line:
                            rectangle: self.x, self.y, self.width, self.height
                            width: 2 
                MDBoxLayout:
                    size_hint_y: None
                    height: dp(50)
                    #padding: dp(3)
                    orientation: 'horizontal'
                    MDCheckbox:
                        id: urgent_checkbox
                        size_hint: None, None
                        size: dp(25), dp(50)
                    MDLabel:
                        text: "Is it urgent?"
                        size_hint_y: None
                        height: dp(50)
                        halign: "left"
                        valign: "center"
                        width: self.texture_size[0] 
                MDLabel:
                    text: "Describe the issue:"
                    size_hint_y: None
                    height: dp(30)
                    halign: "left"
                    font_size: 20
                MDTextField:
                    id: issue_input
                    hint_text: "Describe the issue"
                    multiline: True
                    size_hint_y: None
                    height: dp(200)
                    mode: "rectangle"

                MDBoxLayout:
                    size_hint_y: None
                    height: dp(60)
                    padding: dp(10)
                    MDLabel:
                        text: "Report Image:"
                        size_hint_y: None
                        height: dp(30)
                        halign: "left"
                        valign: "center"
                        font_size: 20
                    MDIconButton:
                        icon: 'upload'
                        on_release: root.file_manager_open()
                    Image:
                        id: selected_image
                        size_hint: None, None
                        size: dp(50), dp(40)
                        source: ''

                MDBoxLayout:
                    orientation: "vertical"
                    pos_hint: {'center_y': .5}
                    adaptive_height: True
                    spacing: 20
                    MDFillRoundFlatButton:
                        text: "Submit Complaint"
                        md_bg_color: 0.043, 0.145, 0.278, 1
                        font_name: "Roboto-Bold"
                        on_release: root.save_edited_data()
                        pos_hint: {"center_x": .5, 'center_y': .5}
'''

Builder.load_string(report_issue)


class ReportScreen(Screen):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.dialog = None

        log_email = anvil.server.call('another_method')

        user_email_log = app_tables.fin_user_profile.get(email_user=log_email)
        if user_email_log:
            self.user_photo = user_email_log['user_photo']
            self.customer_id = user_email_log['customer_id']
            self.ids.name.text = user_email_log['full_name']
            self.ids.email.text = user_email_log['email_user']
            self.ids.mobile_no.text = user_email_log['mobile']

        self.file_manager = MDFileManager(
            exit_manager=self.exit_manager,
            select_path=self.select_path
        )
        self.selected_image_path = None

        # Fetching the data for category and subcategory details
        borrower_sub_issue_data = app_tables.fin_borrower_subcategory_loan_issue.search()
        technical_issue_data = app_tables.fin_subcategory_technical_issue.search()
        category_data = app_tables.fin_issue_category.search()

        self.category_list = [item['issue_category'] for item in category_data]
        print(self.category_list)
        self.subcategory_loan_list = [item['borrower_subcategory_loan_issue'] for item in borrower_sub_issue_data]
        print(self.subcategory_loan_list)
        self.subcategory_Technical_list = [item['subcategory_technical_issue'] for item in technical_issue_data]
        print(self.subcategory_Technical_list)

        self.Report_category = list(set(self.category_list))

        if self.Report_category:
            self.ids.Category.values = self.Report_category
        else:
            self.ids.Category.values = ['Select a category']

        self.subcategory_list = []

    # this method is to load the subcategory details based on selected category item
    def update_subcategories(self):
        selected_category = self.ids.Category.text
        if selected_category == "Loan Issue":
            self.subcategory_list = self.subcategory_loan_list
        elif selected_category == "Technical Issue":
            self.subcategory_list = self.subcategory_Technical_list
        else:
            self.subcategory_list = []

        if self.subcategory_list:
            self.ids.SubCategory.values = self.subcategory_list
        else:
            self.ids.SubCategory.values = ['Select a SubCategory']

    # this method for image fetching
    def file_manager_open(self):
        self.file_manager.show('/')  # Open the file manager at the root directory

    def select_path(self, path):
        self.selected_image_path = path
        self.ids.selected_image.source = path  # Display the selected image
        toast(path)
        self.exit_manager()

    def exit_manager(self, *args):
        self.file_manager.close()

    # Email validation
    def validate_email(self, email):
        email_regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        return re.match(email_regex, email) is not None

    # Mobile number validation
    def validate_mobile(self, mobile_number):
        mobile_regex = r'^\+?1?\d{9,15}$'
        return re.match(mobile_regex, mobile_number) is not None

        # Method to show a dialog

    # dialog box
    def show_dialog(self, title, text):
        if not self.dialog:
            self.dialog = MDDialog(
                title=title,
                text=text,
                buttons=[
                    MDFlatButton(
                        text="OK",
                        on_release=self.close_dialog
                    )
                ],
            )
        self.dialog.open()

    def close_dialog(self, *args):
        if self.dialog:
            self.dialog.dismiss()
            self.dialog = None

    # this methos for retrieve data from UI
    def save_edited_data(self):
        # Retrieve the edited data from the UI
        User_photo = self.user_photo
        customer_id = self.customer_id
        name = self.ids.name.text
        email = self.ids.email.text
        mobile_number = self.ids.mobile_no.text
        Category = self.ids.Category.text
        SubCategory = self.ids.SubCategory.text
        issue_description = self.ids.issue_input.text
        it_is_urgent = self.ids.urgent_checkbox.active

        # Category  validation
        if Category == "Select a category" or Category == "Select Category":
            self.show_dialog("Invalid Input", "Select Category!")
            return

        # Subcategory validation
        if SubCategory == "Select a SubCategory" or SubCategory == "Select SubCategory":
            self.show_dialog("Invalid Input", "Select SubCategory!")
            return

        # Validate email and mobile number
        if not self.validate_email(email):
            self.show_dialog("Invalid Input", "Invalid email format")
            return
        if not self.validate_mobile(mobile_number):
            self.show_dialog("Invalid Input", "Invalid mobile number format")
            return

        # for check user email and input email same
        user_profile = app_tables.fin_user_profile.get(email_user=email)

        if not user_profile:
            self.show_dialog("Something Went Wrong!", "User profile not found")
            return

        # for check mobile number same or not
        user_profile_number = app_tables.fin_user_profile.get(mobile=mobile_number)
        if not user_profile_number:
            self.show_dialog("Something Went Wrong!", "Mobile Number Not Registered")
            return

        user_profile_number = app_tables.fin_user_profile.get(full_name=name)
        if not user_profile_number:
            self.show_dialog("Something Went Wrong!", "User Name Not Registered!")
            return

        user_type = user_profile['usertype']
        # Check if the current user is a borrower
        if user_type != 'borrower':
            self.show_dialog("Something Went Wrong!", "Enter Same Email ID As Registered")
            return

        print(customer_id,name, email,User_photo, mobile_number, Category, SubCategory, issue_description, it_is_urgent, user_type)
        self.fin_reported_problems(customer_id,name,User_photo, email, mobile_number, Category, SubCategory, issue_description, it_is_urgent,
                                   user_type)

    # this method for adding the data in to the tables
    def fin_reported_problems(self, customer_id,name,User_photo, email, mobile_number, Category, SubCategory, issue_description, it_is_urgent,
                              user_type):
        # Get the current date and time
        current_date = datetime.now().replace(tzinfo=None, microsecond=0, fold=0)
        #img_media = anvil.BlobMedia('image/png', b'') if self.selected_image_path is None else anvil.media.from_file(
        #    self.selected_image_path)  # Use a blank image as placeholder if no file is selected
        img_media = None if self.selected_image_path is None else anvil.media.from_file(self.selected_image_path)
        app_tables.fin_reported_problems.add_row(
            user_photo=User_photo,
            customer_id=customer_id,
            name=name,
            email=email,
            mobile_number=int(mobile_number),
            category=Category,
            subcategory=SubCategory,
            issue_description=issue_description,
            report_date=current_date,  # Add the current date
            issue_photo=img_media,
            it_is_urgent=it_is_urgent,
            usertype=user_type,
            status=False
        )
        print("Success")
        self.show_dialog("Success", "Issue reported successfully")
        self.refresh()

    # this method for go back to dashboard
    def go_back(self):
        # Logic to go back to the previous screen
        self.manager.current = 'DashboardScreen'  # replace 'dashboard' with your actual screen name

    # this method for refresh the page
    def refresh(self):
        # Logic to refresh the screen
        log_email = anvil.server.call('another_method')
        user_email_log = app_tables.fin_user_profile.get(email_user=log_email)
        if user_email_log:
            self.ids.name.text = user_email_log['full_name']
            self.ids.email.text = user_email_log['email_user']
            self.ids.mobile_no.text = user_email_log['mobile']

        self.ids.Category.text = 'Select a category'
        self.ids.SubCategory.text = 'Select a SubCategory'
        self.ids.issue_input.text = ''
        self.ids.selected_image.source = ''
        self.selected_image_path = None
        self.ids.urgent_checkbox.active = False
        print("Refreshed....")