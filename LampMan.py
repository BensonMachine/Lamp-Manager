#!/usr/bin/python3
import gi, os
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

class Handler:
    def DoDestroy(self, *args):
        Gtk.main_quit()

    def ApacheStartClick(self, button):
        os.system('systemctl start apache2')
        entry.set_text('Apache is started')
    
    def ApacheStopClick(self, button):
        os.system('systemctl stop apache2')
        entry.set_text('Apache is stoped')
    
    def ApacheRestartClick(self, button):
        os.system('systemctl restart apache2')
        entry.set_text('Apache is restarted')

    def MySQLStartClick(self, button):
        os.system('systemctl start mysql.service')
        entry.set_text('mysql is started')

    def MySQLStopClick(self, button):
        os.system('systemctl stop mysql.service')
        entry.set_text('mysql is stoped')

    def MySQLRestartClick(self, button):
        os.system('systemctl restart mysql.service')
        entry.set_text('mysql is restarted')


builder = Gtk.Builder()
builder.add_from_file("GUI.glade")
builder.connect_signals(Handler())

entry = builder.get_object('LeText')    

window = builder.get_object("MainMachine")
window.show_all()

Gtk.main()
