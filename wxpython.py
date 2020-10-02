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

    # define layout method
    # pack things in a column
    # vboxsizer = wx.BoxSizer(wx.VERTICAL)
    
    # pack things in a row
    # vboxsizer = wx.BoxSizer(wx.HORIZONTAL)

    # rows, columns, row padding, column padding
    grid_sizer = wx.GridSizer(4, 4, 5, 5)

    for i in range(1,17):
      btn = "Button" + str(i)

      grid_sizer.Add(wx.Button(self, label=btn), 1, wx.EXPAND)
      self.SetSizer(grid_sizer)

    # label01 = wx.StaticText(self, label="First Label")
    # vboxsizer.Add(label01)  

    # label02 = wx.StaticText(self, label="Second Label")
    # vboxsizer.Add(label02)

    # label03 = wx.StaticText(self, label="Third Label")
    # vboxsizer.Add(label03)

    # self.SetSizer(vboxsizer)

    # label = wx.StaticText(self, label="This is a label", pos=(100,100))
    # label2 = wx.StaticText(self, label="This is a label2", pos=(130,130))

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
