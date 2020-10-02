# Copyright 2020 System One LLC
# All rights reserved

# Need the environment variable set before running on Linux
# or an error at the bash prompt will appear.
# LD_PRELOAD=/usr/lib64/libGL.so; export LD_PRELOAD

import wx

# The root frame/window object
class myframe(wx.Frame):
  def __init__(self, parent, title):
    super(myframe, self).__init__(parent, title=title, size=(600,300))
    
    # Need a panel to put widget in
    panel = mypanel(self)

class mypanel(wx.Panel):
  def __init__(self, parent):
    super(mypanel, self).__init__(parent)
    self.SetBackgroundColour('red')
    sizer = wx.BoxSizer(wx.VERTICAL)
    self.label = wx.StaticText(self, label="Hello")
    sizer.Add(self.label)
    btn = wx.Button(self, label="Click Me")
    sizer.Add(btn)
    btn.Bind(wx.EVT_BUTTON, self.on_click)
    self.SetSizer(sizer)

  def on_click(self, event):
    self.label.SetLabelText("Changed Text")
    self.label.SetBackgroundColour('green')

class myapp(wx.App):
  def OnInit(self):
    frame = myframe(parent=None, title="WxPython Windows")
    frame.Show()
    return True



# Program entry point
def main():
  app = myapp()
  app.MainLoop()

# Standard boilerplate that calls the main() function if program is run directly.
# Do nothing if imported into another program.
if __name__ == '__main__':
  main()
