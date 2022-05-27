# Given Mobile login as "hpy29" and "qweqwe12"
# @given("Mobile login as {arg} and {arg}")
def step_impl(param1, param2):
  # Эхлэл утгууд тодорхойлох
  process = Init_Dynamicprocess()
  userText = param1
  passText = param2
  
  # Нэр оруулах
  username = process.FindElementByXPath("//android.view.ViewGroup[2]/android.widget.EditText")
  username.Touch()
  username.Keys("^a [BS]" + userText)
  
  # Нууц үг оруулах
  password = process.FindElementByXPath("//android.view.ViewGroup[3]/android.widget.EditText")
  password.Touch()
  password.Keys("^a [BS]" + passText)
  
  logo = process.FindElementByXPath("//android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[1]")
  logo.Touch()
  
  # Нэвтрэх товч дарах
  button = process.FindElementByXPath('//*[@text=\"НЭВТРЭХ\"]')
  button.Touch()
  button.Click()
  
# Dynamic process
def Init_Dynamicprocess():
  # Апптай холбогдох серверийн тохиргоо
  server = "http://127.0.0.1:4723/wd/hub"
  dynamic = '*'
  capabilities = {
      "app": "D:\\projects\\automation\\mobile\\apk\\Khan bank_1.3.6.apk", 
      "deviceName": "Pixel 2", 
      "platformName": "Android", 
      "platformVersion": "11"
  }
  
  # Mobile.ConnectDevice(server, capabilities, 600)
  
  return Mobile.Device(dynamic).Process(dynamic)