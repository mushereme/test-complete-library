# import constant file like page 

# initial values
page = ''
constant = ''
Log = ''
aqObject = ''
cmpEquals = ''

# @then("find table column {arg} and value {arg}")
def impl(param1, param2):
     
  column = param1
  value = param2
  colIndex = False
  
  # хүснэгт чангах
  table = page.FindElement(".//table")
  tHead = table.FindElement("./thead")
  tr = tHead.FindElement("./tr")
  thList = tr.FindElements("./th")
  thLen = len(thLen)
   
  # Хайж буй баганы дугаар олох
  if len(thLen) > 1:
    for i in range(0, thLen):
        if thList[i].contentText == column:
            colIndex = i
            break
        if i == thLen - 1:
            if colIndex == False:
                Log.Error("Can't find: " + column) 
            
  # Сүүлийн мөр олох
  tr = table.FindElements(".//tbody//tr")
  trLen = len(tr)
  trLast = tr[trLen - 1]
  Log.Picture(trLast)       
  
  # Хайж буй баганы утга авах
  tdList = trLast.FindElements(".//td")
  input = tdList[colIndex].FindElement(".//input[@name='format-order-number']")
  input.Keys(value)
  
  
  # Эхний баганд тоо оруулах
  tdList = trLast.FindElements(".//td")
  td = tdList[colIndex]
  
  aqObject.CheckProperty(td, "Visible", cmpEquals, True)
  