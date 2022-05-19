# Жишиг кэйс : 312

# Оролтруу буруу утга дамжуулах үед алдааны MSG-ийг олно.

# Scenario бичиглэл 
# Then find personal info "Регистрийн дугаар" input and enter "ABCD" then error "Регистрийн дугаар зөв оруулна уу"

# Кодын бичиглэл
# @then("find personal info {arg} input and enter {arg} then error {arg}")
def step_impl(param1, param2, param3):
  # Эхлэлийн утгууд тохируулах
  page = constant.Init_Dynamicpage()
  labelName = param1
  value = param2
  errorText = param3
  
  # Label олох 
  label = page.FindElement("//label[.='" + labelName + "']")
  Log.Picture(label)
  
  # Оролт олох
  input = label.FindElement("..//input[@type='text']")
  input.Keys("^a [BS]" + value)
  Log.Picture(input)
  
  # Алдааны msg олох
  error = label.FindElement("../..//span[.='" + errorText + "']")
  Log.Picture(error)
  # Утга шалгах
  
  aqObject.CheckProperty(error, "contentText", cmpEqual, errorText)
