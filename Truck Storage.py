
import sqlite3 as sql
import toga
from toga.style import Pack

# Connect to (or create) a database file
conn = sql.connect("products.db")

# Create a cursor object to interact with the database
cursor = conn.cursor()

# # Create the table
# cursor.execute("""
# CREATE TABLE products (
#     id INTEGER PRIMARY KEY AUTOINCREMENT,
#     product_name TEXT NOT NULL,
#     length INTEGER NOT NULL,
#     width INTEGER NOT NULL,
#     weight INTEGER NOT NULL)
# """)
#
# # Insert some test data
# sample_data = [
#     ("AAA", 120, 80, 451),
#     ("BBB", 120, 80, 547),
#     ("CCC", 120, 100, 657)
# ]
#
# cursor.executemany("""
# INSERT INTO products (product_name, length, width, weight)
# VALUES (?, ?, ?, ?)
# """, sample_data)

# Delete specific row by ID

# cursor.execute("DELETE FROM products WHERE id = 6")
# conn.commit()



cursor.execute("SELECT * FROM products")
rows = cursor.fetchall()

for row in rows:
    print(row)

#Create the GUI to interact with the DataBase and add records
#
# import toga
# from toga.style import Pack
# from toga.style.pack import COLUMN, ROW
#
#
# class RecordApp(toga.App):
#     def startup(self):
#         # Main box
#         layout = toga.Box(style=Pack(direction=COLUMN, padding=10))
#
#         # Buttons for actions
#         self.new_button = toga.Button(
#             "New Record",
#             on_press=self.new_record,
#             style=Pack(padding=5, width=150)
#         )
#         self.correct_button = toga.Button(
#             "Correct Record",
#             on_press=self.show_correct_record_list,
#             style=Pack(padding=5, width=150)
#         )
#
#         # Button box
#         button_box = toga.Box(style=Pack(direction=ROW, padding=10))
#         button_box.add(self.new_button)
#         button_box.add(self.correct_button)
#
#         self.main_box.add(button_box)
#
#         # Placeholder for dynamic content
#         self.content_box = toga.Box(style=Pack(direction=COLUMN, padding=10))
#         self.main_box.add(self.content_box)
#
#         # Store records
#         self.records = []
#
#         # Create main window
#         self.main_window = toga.MainWindow(title="Record Manager")
#         self.main_window.content = self.main_box
#         self.main_window.show()
#
#     # === NEW RECORD MODE ===
#     def show_new_record_form(self, widget):
#         self.content_box.clear()
#
#         self.desc_input = toga.TextInput(placeholder="Description")
#         self.length_input = toga.TextInput(placeholder="Length")
#         self.width_input = toga.TextInput(placeholder="Width")
#         self.weight_input = toga.TextInput(placeholder="Weight")
#
#         save_button = toga.Button(
#             "Save Record",
#             on_press=self.save_record,
#             style=Pack(padding_top=10)
#         )
#
#         self.content_box.add(toga.Label("Add New Record:"))
#         self.content_box.add(self.desc_input)
#         self.content_box.add(self.length_input)
#         self.content_box.add(self.width_input)
#         self.content_box.add(self.weight_input)
#         self.content_box.add(save_button)
#
#     def save_record(self, widget):
#         record = {
#             "Description": self.desc_input.value,
#             "Length": self.length_input.value,
#             "Width": self.width_input.value,
#             "Weight": self.weight_input.value
#         }
#         self.records.append(record)
#         self.main_window.info_dialog("Saved", "Record added successfully!")
#         self.content_box.clear()
#
#     # === CORRECT RECORD MODE ===
#     def show_correct_record_list(self, widget):
#         self.content_box.clear()
#
#         if not self.records:
#             self.content_box.add(toga.Label("No records available."))
#             return
#
#         self.table = toga.Table(
#             headings=["Description", "Length", "Width", "Weight"],
#             data=[[r["Description"], r["Length"], r["Width"], r["Weight"]] for r in self.records],
#             on_select=self.edit_selected_record
#         )
#
#         self.content_box.add(toga.Label("Select a record to correct:"))
#         self.content_box.add(self.table)
#
#     def edit_selected_record(self, widget, row):
#         if row is None:
#             return
#
#         self.content_box.clear()
#         idx = widget.data.index(row)
#         record = self.records[idx]
#
#         self.edit_desc = toga.TextInput(value=record["Description"])
#         self.edit_length = toga.TextInput(value=record["Length"])
#         self.edit_width = toga.TextInput(value=record["Width"])
#         self.edit_weight = toga.TextInput(value=record["Weight"])
#
#         save_button = toga.Button(
#             "Save Changes",
#             on_press=lambda w: self.save_corrections(idx),
#             style=Pack(padding_top=10)
#         )
#
#         self.content_box.add(toga.Label("Edit Record:"))
#         self.content_box.add(self.edit_desc)
#         self.content_box.add(self.edit_length)
#         self.content_box.add(self.edit_width)
#         self.content_box.add(self.edit_weight)
#         self.content_box.add(save_button)
#
#     def save_corrections(self, index):
#         self.records[index] = {
#             "Description": self.edit_desc.value,
#             "Length": self.edit_length.value,
#             "Width": self.edit_width.value,
#             "Weight": self.edit_weight.value
#         }
#         self.main_window.info_dialog("Updated", "Record updated successfully!")
#         self.show_correct_record_list(None)
#
#
# def main():
#     return RecordApp("Record Manager", "org.example.recordapp")
