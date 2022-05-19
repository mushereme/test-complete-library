# Then find personal info "Таны хэн болох?" input and select "Эх" 
# @then("find personal info {arg} input and select {arg}")

def step_impl(param1, param2):
  # Эхлэлийн утгууд тохируулах
  page = constant.Init_Dynamicpage()
  labelName = param1
  value = param2
  
  # Label олох 
  label = page.FindElement("//label[.='" + labelName + "']")
  Log.Picture(label)
  
  # Оролт олж дарах
  inputContainer = label.FindElement("../div")
  input = inputContainer.FindElement(".//div[contains(@class, 'ant-select')]")
  input.Click()
  
  # Сонголтоос сонгох 
  option = inputContainer.FindElement("//div[@title='" + value + "']")
  option.Click()
  
  aqObject.CheckProperty(option, "contentText", cmpEqual, value)
