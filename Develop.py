import asyncio
import toga
from toga.style import Pack
from toga.style.pack import COLUMN
import sqlite3 as sql




class RecordApp(toga.App):
    def startup(self):
        # Main box
        self.content_box = toga.Box(style=Pack(direction=COLUMN, margin=150, align_items="center"))

        self.message_label = toga.Label("", style=Pack(direction=COLUMN))
        self.content_box.add(self.message_label)

        # Buttons for actions
        self.new_button = toga.Button(
            "New Record",
            on_press=self.new_record_form,
            style=Pack(margin=5, height=150, width=150)
        )
        self.content_box.add(self.new_button)

        self.correct_button = toga.Button(
            "Correct Record",
            on_press=self.correct_record,
            style=Pack(margin=5, height=150, width=150)
        )
        self.content_box.add(self.correct_button)

        self.main_window = toga.MainWindow(title="Container Records Management", size=(800, 600))
        self.main_window.content = self.content_box
        self.main_window.show()

    def go_back(self, widget):
        self.main_window.content = self.content_box


    temp_values=[]
    async def add_to_database(self, widget):
        if self.check_box.value == False:
            for record in self.records["TextInputs"]:
                if record.value is None or str(record.value).strip() == "":
                    await self.main_window.dialog(toga.ErrorDialog("Value Error", "You must enter a value in every row!"))
                    return
            else:
                conn = sql.connect('products.db')
                cursor = conn.cursor()
                cursor.execute('INSERT INTO products (product_name,length,width,weight) VALUES (?,?,?,?)', (self.desc_input.value, self.length_input.value, self.width_input.value, self.weight_input.value))
                conn.commit()
                conn.close()
                await self.main_window.dialog(toga.InfoDialog("Add Complete", "The record was stored!"))

        elif self.check_box.value == True:

            if self.check_box.value:
                self.temp_values.append([""])
                for record in self.records["TextInputs"]:
                    self.temp_values[-1].append(record.value)
                self.temp_values[-1].remove("")

    async def validate_string(self, widget):

        value = widget.value
        if not value.isalpha() and value != "":
            await self.main_window.dialog(toga.ErrorDialog("Value Error","Please enter a string!"))

    async def validate_number(self, widget):

        value = widget.value.strip()
        if (value.isalpha() or not value.isdigit()) and value !="":
            await self.main_window.dialog(toga.ErrorDialog("Value Error","Please enter a integer!"))

    def new_record_form(self, widget):

        self.new_record_box = toga.Box(style=Pack(direction=COLUMN,  margin=20))
        self.new_record_box.add()

        self.desc_input = toga.TextInput(placeholder="Description", on_change=self.validate_string)
        self.length_input = toga.TextInput(placeholder="Length", on_change=self.validate_number)
        self.width_input = toga.TextInput(placeholder="Width", on_change=self.validate_number)
        self.weight_input = toga.TextInput(placeholder="Weight", on_change=self.validate_number)
        self.check_box = toga.Switch(text="Keep the records in memory", on_change=self.checked_box)

        self.save_button = toga.Button(
            "Save Record",
            on_press= self.add_to_database,
              style=Pack(margin_top=10)
        )

        self.exit_button = toga.Button(
            "Exit Back",
            on_press=self.go_back,
            style=Pack(margin_top=10)
        )

        self.new_record_box.add(toga.Label("Add New Record", style=Pack(text_align="center", margin=10)))
        self.new_record_box.add(self.desc_input)
        self.new_record_box.add(self.length_input)
        self.new_record_box.add(self.width_input)
        self.new_record_box.add(self.weight_input)
        self.new_record_box.add(self.check_box)

        self.new_record_box.add(self.save_button)
        self.new_record_box.add(self.exit_button)

        self.main_window.content = self.new_record_box

        # Store the names of the values
        self.records = {"TextInputs":[self.desc_input, self.length_input, self.width_input, self.weight_input]}

    def checked_box(self, widget):

        temp_values =[]
        if widget.value:
            temp_values = [record.value for record in self.records["TextInputs"]]
        else:
            print("Not checked!")

    def update_record(self, button):
        conn = sql.connect('products.db')
        cursor = conn.cursor()
        cursor.execute('UPDATE products SET product_name=? ,length= ?,width=? ,weight=? WHERE product_name = ?', (self.desc_input.value,self.length_input.value,self.width_input.value,self.weight_input.value,self.desc_input.value))
        conn.commit()
        conn.close()
        self.main_window.show()

    def on_row_update(self, widget):

        self.update_box = toga.Box(style=Pack(direction=COLUMN,  margin=20))
        self.update_box.add()

        self.label = toga.Label("Record Update", style=Pack(text_align="center", margin=10,font_weight="bold"))
        self.desc_input = toga.TextInput(placeholder="Description", on_change=self.validate_string)
        self.length_input = toga.TextInput(placeholder="Length", on_change=self.validate_number)
        self.width_input = toga.TextInput(placeholder="Width", on_change=self.validate_number)
        self.weight_input = toga.TextInput(placeholder="Weight", on_change=self.validate_number)
        self.ok_button = toga.Button(
            "Update Record",
            on_press= self.update_record,
              style=Pack(margin_top=10)
)

        self.update_box.add(self.label)
        self.update_box.add(self.desc_input)
        self.update_box.add(self.length_input)
        self.update_box.add(self.width_input)
        self.update_box.add(self.weight_input)
        self.update_box.add(self.ok_button)

        self.popupWindow= toga.Window(title = "Popup")
        self.popupWindow.content = self.update_box
        self.popupWindow.show()
        #
        # self.selected_index = widget.selection.__getattribute__("id")
        # print(self.selected_index)
        # self.table.data[self.selected_index] = [self.selected_index,"A",0,0,0]
        # print(self.table.data[self.selected_index])


    def correct_record(self, button):
        conn = sql.connect('products.db')
        cursor = conn.cursor()
        results =cursor.execute("SELECT * FROM products ")
        results = cursor.fetchall()

        # self.new_record_boxadd(toga.Label("Add New Record", style=Pack(text_align="center", margin=10)))

        self.results_box = toga.Box( style=Pack(direction=COLUMN))
        self.results_box.add()

        self.label =toga.Label("Current Records", style=Pack(text_align="center",font_style="italic", font_weight="bold",font_size=14), margin_top=50)
        self.table = toga.Table(headings=["ID", "Description", "Length", "Width", "Weight"], data=results, style=Pack(direction=COLUMN, flex=1), margin=10)
        self.results_box.add(self.label)

        self.results_box.add(self.table)

        self.update_button = toga.Button(" Update Value",  style=Pack(margin_top=10), on_press=self.on_row_update)
        self.results_box.add(self.update_button)

        self.exit_button = toga.Button("Exit Back",on_press=self.go_back,style=Pack(margin_top=10))
        self.results_box.add(self.exit_button)

        self.main_window.content = self.results_box
        self.main_window.show()




app = RecordApp(formal_name="Hello, world!", app_id="hello.world")

app.main_loop()