'''
Custom Icon example based on pyWinGUI, author Maxim Kolosov (2012)
this example is based on C++ MSDN CreateIcon example
see Platform SDK: Windows User Interface "Creating an Icon"
'''

from pywingui.gdi import *
from pywingui.wtl import *

ANDmaskIcon = (BYTE*128)(
0xFF, 0xFF, 0xFF, 0xFF,
0xFF, 0xFF, 0xC3, 0xFF,
0xFF, 0xFF, 0x00, 0xFF,
0xFF, 0xFE, 0x00, 0x7F,
0xFF, 0xFC, 0x00, 0x1F,
0xFF, 0xF8, 0x00, 0x0F,
0xFF, 0xF8, 0x00, 0x0F,
0xFF, 0xF0, 0x00, 0x07,
0xFF, 0xF0, 0x00, 0x03,
0xFF, 0xE0, 0x00, 0x03,
0xFF, 0xE0, 0x00, 0x01,
0xFF, 0xE0, 0x00, 0x01,
0xFF, 0xF0, 0x00, 0x01,
0xFF, 0xF0, 0x00, 0x00,
0xFF, 0xF8, 0x00, 0x00,
0xFF, 0xFC, 0x00, 0x00,
0xFF, 0xFF, 0x00, 0x00,
0xFF, 0xFF, 0x80, 0x00,
0xFF, 0xFF, 0xE0, 0x00,
0xFF, 0xFF, 0xE0, 0x01,
0xFF, 0xFF, 0xF0, 0x01,
0xFF, 0xFF, 0xF0, 0x01,
0xFF, 0xFF, 0xF0, 0x03,
0xFF, 0xFF, 0xE0, 0x03,
0xFF, 0xFF, 0xE0, 0x07,
0xFF, 0xFF, 0xC0, 0x0F,
0xFF, 0xFF, 0xC0, 0x0F,
0xFF, 0xFF, 0x80, 0x1F,
0xFF, 0xFF, 0x00, 0x7F,
0xFF, 0xFC, 0x00, 0xFF,
0xFF, 0xF8, 0x03, 0xFF,
0xFF, 0xFC, 0x3F, 0xFF)

XORmaskIcon = (BYTE*128)(
0x00, 0x00, 0x00, 0x00,
0x00, 0x00, 0x00, 0x00,
0x00, 0x00, 0x00, 0x00,
0x00, 0x00, 0x00, 0x00,
0x00, 0x00, 0x00, 0x00,
0x00, 0x00, 0x00, 0x00,
0x00, 0x00, 0x00, 0x00,
0x00, 0x00, 0x38, 0x00,
0x00, 0x00, 0x7C, 0x00,
0x00, 0x00, 0x7C, 0x00,
0x00, 0x00, 0x7C, 0x00,
0x00, 0x00, 0x38, 0x00,
0x00, 0x00, 0x00, 0x00,
0x00, 0x00, 0x00, 0x00,
0x00, 0x00, 0x00, 0x00,
0x00, 0x00, 0x00, 0x00,
0x00, 0x00, 0x00, 0x00,
0x00, 0x00, 0x00, 0x00,
0x00, 0x00, 0x00, 0x00,
0x00, 0x00, 0x00, 0x00,
0x00, 0x00, 0x00, 0x00,
0x00, 0x00, 0x00, 0x00,
0x00, 0x00, 0x00, 0x00,
0x00, 0x00, 0x00, 0x00,
0x00, 0x00, 0x00, 0x00,
0x00, 0x00, 0x00, 0x00,
0x00, 0x00, 0x00, 0x00,
0x00, 0x00, 0x00, 0x00,
0x00, 0x00, 0x00, 0x00,
0x00, 0x00, 0x00, 0x00,
0x00, 0x00, 0x00, 0x00,
0x00, 0x00, 0x00, 0x00)

class MyWindow(Window):
	_window_title_ = 'Custom Icon example window (Maxim Kolosov), based on MSDN CreateIcon example'
	_window_background_ = GetStockObject(gdi.WHITE_BRUSH)
	_window_icon_ = _window_icon_sm_ = IconEx(NULL, 32, 32, 1, 1, ANDmaskIcon, XORmaskIcon)

	def OnDestroy(self, event):
		application.Quit()

	msg_handler(WM_DESTROY)(OnDestroy)

myWindow = MyWindow()

application = Application()
application.Run()
