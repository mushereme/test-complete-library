# import constant file like page 

# initial values
page = ''
constant = ''
Log = ''
aqObject = ''
cmpEqual = ''

# @then("find table column {arg} and value {arg}")
def impl(param1, param2):

  # Эхлэлийн утгууд зарлах
  page = constant.Init_Dynamicpage()
  column = param1
  value = param2
  colIndex = False
  
  # хүснэгт чангах
  table = page.FindElement(".//table")
  tHead = table.FindElement("./thead")
  tr = tHead.FindElement("./tr")
  thList = tr.FindElements("./th")
  thLen = len(thList)
   
  # Хайж буй баганы дугаар олох
  if thLen > 1:
    for i in range(0, thLen):
        if thList[i].contentText == column:
            colIndex = i
            break
        if i == thLen - 1:
            if colIndex == False:
                Log.Error("Can't find: " + column) 
            
  # Сүүлийн мөрийг ололгүйгээр хайж буй багаар давталж гүйлгэж хайсан утгатай тэнцэж байгаа эсэхийг шалгаарай
  trList = table.FindElements('.//tbody//tr')
  trLen = len(trList)
  
  for i in range(0, trLen): 
    tdList = trList[i].FindElements('.//td')
    tdLen = len(tdList)
    for j in range(0, tdLen):
      colValue = tdList[colIndex]
      if colValue.contentText == value: 
        Log.Message(colValue.contentText)
        aqObject.CheckProperty(colValue, "Visible", cmpEqual, True)
        break
      else: 
        if j == tdLen - 1: 
          Log.Message("Can't find value")