from src import utils
utils.add_makro()
from Makro.MakroCore.RendererKit import Renderer as RD

def temp_convert():
  RD.CommandShow(msg="Input The Temperature You Like To Convert (e.g., 70F, 20C etc.)").Input()
  temp = RD.Quest_result
  degree = int(temp[:-1])
  i_convention = temp[-1]

  if i_convention.upper() == "C":
    result = int(round((9 * degree) / 5 + 32))
    o_convention = "Fahrenheit"
  elif i_convention.upper() == "F":
    result = int(round((degree - 32) * 5 / 9))
    o_convention = "Celsius"
  else:
      RD.CommandShow(msg="Input proper convention").Info()
  output = f'The temperature in {o_convention} is {result}'
  RD.CommandShow(output).Push()

def distance_convert():
  RD.CommandShow(msg='Enter Distance In feet:').Input()
  d_ft = int(RD.Quest_result)
  d_inches = d_ft * 12
  d_yards = d_ft / 3.0
  d_miles = d_ft / 5280.0
  
  d_miles = round(d_miles, 2)
  d_yards = round(d_yards, 2)

  output = f'The distance in inches is {d_inches} inches\nThe distance in yards is {d_yards} yards\nThe distance in miles is {d_miles} miles'
  RD.CommandShow(output).Push()

RD.CommandShow(msg='What Do You Want To Convert').Choice(Button1='Temp', Button2='Distance')
if RD.Quest_result.lower() == 'temp':
  temp_convert()
elif RD.Quest_result.lower() == 'distance':
  distance_convert()