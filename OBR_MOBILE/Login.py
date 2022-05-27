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