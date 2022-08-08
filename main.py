from pywinauto.application import Application
from pywinauto import mouse
from pywinauto.keyboard import send_keys
from time import sleep

# --------------------------GoConfig--------------------------------------------------------------------

open = True

app = Application(backend='uia').start('.\\GODEX\\GoTools_V1.006\\GoConfig.exe')
app.window(title_re='GoConfig*').wait('enabled')

okno = app.window(title_re='GoConfig*')

okno.child_window(title='Otwórz', auto_id='DropDown', control_type='Button', found_index=11).click()

send_keys('{UP}')
send_keys('{ENTER}')

okno.child_window(title='Otwórz', auto_id='DropDown',control_type='Button', found_index=10).click()
send_keys('{DOWN}')
send_keys('{ENTER}')

okno.child_window(title='Otwórz', auto_id='DropDown',control_type='Button', found_index=8).click()
send_keys('{UP}')
send_keys('{ENTER}')

okno.child_window(control_type="Edit", found_index=0).set_edit_text('30')
okno.child_window(control_type="Edit", found_index=1).set_edit_text('15')
okno.child_window(control_type="Edit", found_index=2).set_edit_text('11')

okno.child_window(title="Set", control_type="Button").click()

while open:
    if len(app.windows()) == 2:
        open = False

send_keys('{ENTER}')

app.kill() #myself

# -------------------------------Ustawienia drukarki-------------------------------------------------------

send_keys('{LWIN down} r {LWIN up} control {SPACE} printers {ENTER}')

printer_name = "Godex RT200"

panel = Application(backend='uia')
panel.connect(title_re='Urządzenia*', timeout=100).window(title_re='Urządzenia*').wait('enabled')
panel_okno = panel.window()

item = panel_okno.child_window(title=printer_name, control_type="ListItem").select()

send_keys('{ENTER}')

printer = panel.window(title_re='Godex*')
printer.wait('enabled')

printer.child_window(title="Drukarka", control_type="MenuItem").select()

send_keys('{UP} {UP} {ENTER}')

settings = panel.window(title='Właściwości: '+printer_name)
settings.wait('enabled')

settings.child_window(title_re="Preferencje*", control_type="Button").click()

preferences = panel.window(title='Preferencje drukowania: '+printer_name)
preferences.wait('enabled')
preferences.child_window(title="Nowy...", control_type="Button").click()

new_material= preferences.window(title_re='Nowy mat*')
new_material.wait('enabled')
send_keys('{BACKSPACE} EZD {TAB} {TAB} {TAB} 50 {TAB} 30 {TAB} {ENTER}')

preferences = panel.window(title='Preferencje drukowania: '+printer_name)
preferences.wait('enabled')

preferences.child_window(title="OK", control_type="Button").click()
settings.child_window(title="Narzędzia", control_type="TabItem").select()
settings.child_window(title="Konfiguruj", control_type="Button").click()
send_keys('{DOWN} {ENTER}')
time= settings.child_window(title_re='Ustaw zeg*', found_index=0)
time.wait('enabled')
time.child_window(title="Określ czas ręcznie", control_type="RadioButton").click()
time.child_window(title="Użyj bieżącego czasu systemowego", control_type="RadioButton").click
time.child_window(title="OK", control_type="Button").click()

settings.child_window(title="Narzędzia", control_type="TabItem").select()
settings.child_window(title="Działanie", control_type="Button").click()
send_keys('{DOWN} {DOWN} {ENTER}')
sleep(3)

settings.child_window(title="Drukuj", control_type="Button").click()
send_keys('{UP} {ENTER}')
sleep(1)
settings.child_window(title="Drukuj", control_type="Button").click()
send_keys('{DOWN} {ENTER}')
sleep(1)
settings.child_window(title="OK", control_type="Button").click()

panel.window(title_re='Godex*').close()
panel_okno.close()

