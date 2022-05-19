# Case ID: 304
# INPUT төрөлтэй оролтод оруулах утга болон зөв бичиглэл дамжуулсанаар бичигдэх текст ямар ч байсан шалгах текстээ шалгана

# Scenario бичиглэл
# Then find personal info "Регистрийн дугаар" input and enter "ER96100511" then "96100511"

# Кодын бичиглэл
# @then("find personal info {arg} input and enter {arg} then {arg}")
def step_impl(param1, param2, param3):
  # Эхлэлийн утгууд тохируулах
  page = constant.Init_Dynamicpage()
  labelName = param1
  value = param2
  result = param3
  
  # Label олох 
  label = page.FindElement("//label[.='" + labelName + "']")
  Log.Picture(label)
  
  # Оролт олох
  input = label.FindElement("..//input[@type='text']")
  input.Keys("^a [BS]" + value)
  Log.Picture(input)
  
  # Утга шалгах
  aqObject.CheckProperty(input, "value", cmpEqual, result)