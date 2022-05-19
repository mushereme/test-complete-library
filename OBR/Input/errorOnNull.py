# CASE ID: 309

# Оролтод тохирсон хайх shortpath буцаана
def findInputType(type):
  inputTypes = {
    "select": "..//div[contains(@class, 'ant-select')]",
    "input": "..//input[@type='text']"
  }
  return inputTypes[type]

# Then error on personal info "Нэр" input "input" then "Үргэлжлүүлэх"
# @then("error on personal info {arg} input {arg} then {arg}")
def step_impl(param1, param2, param3):
  # Эхлэлийн утгууд тохируулах
  page = constant.Init_Dynamicpage()
  labelName = param1
  type = param2
  buttonText = param3
  
  # Label олох 
  label = page.FindElement("//label[.='" + labelName + "']")
  Log.Picture(label)
  
  # Input олох
  inputType = findInputType(type) # Оролтын төрлөөс хамаарч хайх утгыг буцаана
  input = label.FindElement(inputType)
  Log.Picture(input)
  
  # Үргэлжлүүлэх товч олж дарах
  button = page.FindElement("//button[.='" + buttonText + "']")
  Log.Picture(button)
  button.Click()
  
  # Алдааны msg олох
  
  errorLabel = label.FindElement("../..//span[contains(@class, 'field-error')]")
  Log.Picture(errorLabel)
  
  aqObject.CheckProperty(errorLabel, "Visible", cmpEqual, True)
