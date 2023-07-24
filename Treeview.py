'''
Author             :Sumeeth Yarlagadda
Project            : CRM Application for Srikanth
Verion             : CRMV1.0
Date               : 23/07/2023
'''


from tkinter import *
from tkinter import ttk

# tkinter is a python library used to create a GUI.

root = Tk()  # root referes to main window or the toplevel window of the application

root.title("CRM Application")  # creating a title page for main window
# to set icon fot the root window
root.iconbitmap('E:\CRM APPLICATION\ICM files')
root.geometry("1000x500")

# Add some style

style = ttk.Style()

# Add theme
style.theme_use('default')

# configure the treeview colors

style.configure('Treeview',
                background="#688b96",
                foreground="black",
                rowheight=25,
                fieldbackground="#688b96")
''''background color give #rrggbb", foreground color = "specified color", rowheight = 25, fielbackground = #rrggbb"'''

# change selected background

style.map('Treeview',
          background=[('selected', "#2e313b")])

# create Treeview Frame

tree_frame = Frame(root)
tree_frame.pack(pady=10)

# create Tree view Scrollbar

tree_scroll = Scrollbar(tree_frame)

# scroll bar should be right side and it moving co-ordinate are in y axis
tree_scroll.pack(side=RIGHT, fill=Y)

# create TreeView

my_tree = ttk.Treeview(
    tree_frame, yscrollcommand=tree_scroll.set, selectmode="extended")
my_tree.pack()

# configure the scroll bar

tree_scroll.config(command=my_tree.yview)

# define our columns

my_tree['columns'] = ("First Name", "Last Name", "ID",
                      "City", "Vehicle NO", "Phone Number", "Zipcode")

# format our columns

my_tree.column("#0", width=0, stretch=0)
my_tree.column("First Name", anchor=W, width=140)
my_tree.column("Last Name", anchor=W, width=140)
my_tree.column("ID", anchor=CENTER, width=100)
my_tree.column("City", anchor=CENTER, width=140)
my_tree.column("Vehicle NO", anchor=CENTER, width=140)
my_tree.column("Phone Number", anchor=CENTER, width=140)
my_tree.column("Zipcode", anchor=CENTER, width=140)

# create headings
my_tree.heading("#0", text="", anchor=W)
my_tree.heading("First Name", text="First Name", anchor=W)
my_tree.heading("Last Name", text="Last Name", anchor=W)
my_tree.heading("ID", text="ID", anchor=CENTER)
my_tree.heading("City", text="City", anchor=CENTER)
my_tree.heading("Vehicle NO", text="Vehicle NO", anchor=CENTER)
my_tree.heading("Phone Number", text="Phone Number", anchor=CENTER)
my_tree.heading("Zipcode", text="Zipcode", anchor=CENTER)


# Add Fake Data

data = [
    ["sumeeth", "Yarlagadda", "Y0001", "Hyderabad",
        "AP28J5770", "8143561144", "500083"],
    ["sindhura", "dandamudi", "D0001", "Miltonkeynes",
        "MK32J1122", "970074065", "MK5108"],
    ["aruna kumari", "Yarlagadda", "Y0002", "Hyderabad",
        "TS16EB3841", "9491138754", " 500083"],
    ["siva prasad", "Yarlagadda", "Y0003", "Hyderabad",
        "Ap25M4940", "9441404494", "500083"],
    ["Mounika", "Yarlagadda", "Y0004", "Hyderabad",
        "TS09EE7086", "9121787275", "500083"],
    ["Bhaskaramma", "Yarlagadda", "Y0005",
        "Hyderabad", "000000", "987654321", "500083"],
    ["ksjdfh", "sdjkfh", "Y0006", "banglore", "0dfgd", "9876545521", "500082"],
    ["amma", "Yarlagadda", "Y0006", "Chennai", "65654", "987655641", "500088"],
    ["Bdfgda", "Ydfgh", "Y0007", "Chennai", "0000sdf", "9854321", "500084"],
    ["dsfsadgdf", "safd", "Y0008", "Hyad", "asdfa", "934534531", "500045"],
    ["sumeeth", "Yarlagadda", "Y0001", "Hyderabad",
        "AP28J5770", "8143561144", "500083"],
    ["sindhura", "dandamudi", "D0001", "Miltonkeynes",
        "MK32J1122", "970074065", "MK5108"],
    ["aruna kumari", "Yarlagadda", "Y0002", "Hyderabad",
        "TS16EB3841", "9491138754", " 500083"],
    ["siva prasad", "Yarlagadda", "Y0003", "Hyderabad",
        "Ap25M4940", "9441404494", "500083"],
    ["Mounika", "Yarlagadda", "Y0004", "Hyderabad",
        "TS09EE7086", "9121787275", "500083"],
    ["Bhaskaramma", "Yarlagadda", "Y0005",
        "Hyderabad", "000000", "987654321", "500083"],
    ["ksjdfh", "sdjkfh", "Y0006", "banglore", "0dfgd", "9876545521", "500082"],
    ["amma", "Yarlagadda", "Y0006", "Chennai", "65654", "987655641", "500088"],
    ["Bdfgda", "Ydfgh", "Y0007", "Chennai", "0000sdf", "9854321", "500084"],
    ["dsfsadgdf", "safd", "Y0008", "Hyad", "asdfa", "934534531", "500045"],
]

# create a stripe rows

my_tree.tag_configure('oddrow', background="white")
my_tree.tag_configure('evenrow', background="lightblue")

# add our data to the screen

global count
count = 0

for record in data:
    if count %  2 == 0:
        my_tree.insert(parent='', index='end', iid=count, text='', values=(record[0], record[1], record[2], record[3], record[4], record[5], record[6]), tags=('evenrow',))
    else:
        my_tree.insert(parent='', index='end', iid=count, text='', values=(record[0], record[1], record[2], record[3], record[4], record[5], record[6]), tags=("oddrow",))

    # increment counter
    count += 1
