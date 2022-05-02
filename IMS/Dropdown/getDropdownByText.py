# import constant file like page 

# initial values
page = ''
constant = ''
Log = ''
aqObject = ''
cmpEqual = ''

# @then("filter label {arg} select {arg} dropdown from {arg}")
def step_impl(param1, param2, param3):
  # Динамик пэйж дуудах
  page = constant.Init_Dynamicpage()
  
  filter = param1
  value = param2
  index = int(param3)
  
  # хайж буй утгыг олох
  filterLabel = constant.Init_Dynamicpage().FindElement("//span[.='"+ filter + ":']")
  # selectBtn = filterLabel.FindElement("..//span[.=' " + column + " ']")
  selectBtnContainerList = filterLabel.FindElements("..//lib-select")
  selectBtnContainer = selectBtnContainerList[index]
  selectBtn = selectBtnContainer.FindElement("./div/span")
  # visible = selectBtn.FindElement("../../../span")
  selectBtn.Click()
  
  # хайж буй утгаар dropdown-д байгаа 
  dropDown = constant.Init_Dynamicpage().WaitElement("//span[contains(@class, 'select2-dropdown')]")
  liList = dropDown.FindElements("li")
  
  dropDownEl = dropDown.WaitElement("//li[contains(text(), '" + value + "')]")
  dropDownEl.Click() 
  
  aqObject.CheckProperty(selectBtn, "contentText", cmpEqual, value)