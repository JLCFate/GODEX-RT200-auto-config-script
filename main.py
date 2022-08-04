from pywinauto.application import Application
from pywinauto import mouse
from pywinauto.keyboard import send_keys
from time import sleep

# --------------------------GoConfig--------------------------------------------------------------------

open = True

app = Application(backend='uia').start('C:\\Users\\FateStalker\\Desktop\\GoTools_V1.006\\GoConfig.exe')
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

printer_name = "Microsoft XPS Document Writer"

panel = Application(backend='uia')
panel.connect(title_re='Urządzenia*', timeout=100).window(title_re='Urządzenia*').wait('enabled')
panel_okno = panel.window()

item = panel_okno.child_window(title=printer_name, control_type="ListItem").select()

send_keys('{ENTER}')

drukarka = panel.window(title=printer_name)
drukarka.wait('enabled')

drukarka.child_window(title="Drukarka", control_type="MenuItem").select()

send_keys('{UP} {UP} {UP} {ENTER}')

settings = panel.window(title='Właściwości: '+printer_name)
settings.wait('enabled')

settings.child_window(title_re="Preferencje*", control_type="Button").click()