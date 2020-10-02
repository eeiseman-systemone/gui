# Copyright 2020 System One LLC
# All rights reserved

# Need the environment variable set before running on Linux
# or an error at the bash prompt will appear.
# LD_PRELOAD=/usr/lib64/libGL.so; export LD_PRELOAD

import wx
import requests

# Using a custom CA cert and API key
def elasticsearch(label):
  # Set the URL
  url = 'https://mineral.systemone.app:9200/_cluster/health'
  
  # Set the API key in headers
  headers = {'Authorization':'ApiKey aUMwaUVuUUJFNUp0UGdWVXoyNnU6RnBEMUQyVW1UN3FKdkxfeEg2d0hDUQ=='}
  
  # Visual Studio Code uses the root of the project for the current directory
  # Specifying the relative path of the CA cert file
  cacert = 'systemoneca.crt'
  
  # Put it all together and sent the GET
  response = requests.get(url, verify=cacert, headers=headers)
  
  # Print the raw, plain text of the response
  label.SetLabel(response.json()['status'])
  return
  
  # Since we're getting JSON back, there is a method format the reponse as
  # a JSON object
  # print(response.json())

def on_click(label):
  label.SetLabel("Changed")
  return 

# Program entry point
def main():
  statusapp = wx.App()

  frame01 = wx.Frame(parent=None, title="Hello World!")

  panel01 = wx.Panel(parent=frame01, name="panel01")

  grid_sizer = wx.GridSizer(4, 4, 5, 5)

  label01 = wx.StaticText(parent=panel01)
  label01.SetLabel("Start")
  
  

  button01 = wx.Button(parent=panel01, label="Button01")
  button01.Bind(wx.EVT_BUTTON, lambda dummy: elasticsearch(label01))
  grid_sizer.Add(button01)
  grid_sizer.Add(label01)

  panel01.SetSizer(grid_sizer)

  frame01.Show()

  statusapp.MainLoop()
  
# Standard boilerplate that calls the main() function if program is run directly.
# Do nothing if imported into another program.
if __name__ == '__main__':
  main()
