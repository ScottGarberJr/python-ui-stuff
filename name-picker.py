import ui
import random
import dialogs

#----------------------------------------------------------------BUTTON EVENTS-----

def click_btn_auto(sender):		
	
	if len(list_available) > 0:
	
		if v['sld_option'].value >=0 and v['sld_option'].value < 0.25 :
			choice = pick_random()
		elif v['sld_option'].value >= 0.25 and v['sld_option'].value < 0.5:
			choice = pick_MSM()
		elif v['sld_option'].value >= 0.5 and v['sld_option'].value < 0.75:
			choice = pick_LCG(1)
		elif v['sld_option'].value >= 0.75 and v['sld_option'].value < 1.0:
			choice = pick_xorshift()	
		
		tbl_active.data_source.items.append(list_available[choice])
		list_active.append(list_available[choice])
		tbl_active.reload_data()
	
		tbl_available.data_source.items.remove(list_available[choice])
		list_available.remove(list_available[choice])
		tbl_available.reload_data()
		
		#print(len(list_available))
		v['btn_remove'].enabled = True
		
	
	if len(list_available) < 1:
		sender.enabled = False
		v['btn_manual'].enabled = False
		#dialogs.text_dialog(title="None Available", text="you need to remove someone from active to have someone available")
	
def click_btn_manual(sender):
	
	if len(list_available) > 0:
		tbl_active.data_source.items.append(list_available[tbl_available.selected_row[1]])
		list_active.append(list_available[tbl_available.selected_row[1]])
		tbl_active.reload_data()
	
		tbl_available.data_source.items.remove(list_available[tbl_available.selected_row[1]])
		list_available.remove(list_available[tbl_available.selected_row[1]])
		tbl_available.reload_data()
		
		v['btn_remove'].enabled = True
		
	if len(list_available) == 0:
		sender.enabled = False
		v['btn_auto'].enabled = False
		#dialogs.text_dialog(title="None Available", text="you need to remove someone from active to have someone available")
	
def click_btn_remove(sender):
	if len(list_active) > 0:
		#print(list_active[tbl_active.selected_row[1]] , tbl_active.selected_row[1])
		tbl_available.data_source.items.append(list_active[tbl_active.selected_row[1]])
		list_available.append(list_active[tbl_active.selected_row[1]])
		tbl_available.reload_data()
	
		tbl_active.data_source.items.remove(list_active[tbl_active.selected_row[1]])
		list_active.remove(list_active[tbl_active.selected_row[1]])
		tbl_active.reload_data()
	
		v['btn_auto'].enabled = True
		v['btn_manual'].enabled = True
		
	if len(list_active) == 0:
		sender.enabled = False
		#dialogs.text_dialog(title="None Active", text="you need to pick someone from available to have someone active")
	
#--------------------------------------------------------------SLIDER EVENTS--------	

def change_sld_option(sender):
	if sender.value >=0 and sender.value < 0.25 :
		v['lbl_option'].text = "Using Random Pick"
		
	elif sender.value >= 0.25 and sender.value < 0.5:
		v['lbl_option'].text = "Using MSM Algorithm" 
		
	elif sender.value >= 0.5 and sender.value < 0.75:
		v['lbl_option'].text = "Using LCG Algorithm"
		
	elif sender.value >= 0.75 and sender.value < 1.0:
		v['lbl_option'].text = "Using Xorshift Algorithm"
		

#----------------------------------------------------------------VIEW SETUP--------

#v = ui.View()
v = ui.load_view()
v.name = "Name Picker"

v.present("sheet")

#---------------------------------------------------------------LISTS & TABLEVIEWS--

list_available = [
	"Jay",    	  #0
	"Austin", 		#1
	"Nguyen",			#2
	"Dan",				#3
	"Dennis",			#4
	"Erick",			#5
	"Joe",				#6
	"Joshua",			#7
	"Valentine",	#8
	"Michael",		#9
	"Torrie",			#10
	"Scott",			#11
	"Billy",			#12
	"Yohan"				#13
	 ]

data_available = ui.ListDataSource(list_available)
tbl_available = v["tbl_available"]
tbl_available.data_source = data_available
tbl_available.delegate = data_available
tbl_available.reload()

list_active = []
tbl_active = v["tbl_active"]
data_active = ui.ListDataSource(list_active)
tbl_active.data_source = data_active
tbl_active.delegate = data_active

#-----------------------------------------------------------------------BUTTONS--------
btn_manual = ui.Button()
btn_manual.action = click_btn_manual

btn_remove = ui.Button()
btn_remove.action = click_btn_remove

btn_auto = ui.Button()
btn_auto.action = click_btn_auto


#----------SLIDER--------------
sld_option = ui.Slider()
sld_option.action = change_sld_option

#----------ALGORITHMS----------
def pick_random():
	return random.randint(0,len(list_available)-1)

def pick_MSM():
	print("called MSM")

def pick_LCG(m=2**32, a=1103515245, c=12345):
	X = (a * X + c) % m
	return X
	
def pick_xorshift():
	print("called xorshift")

