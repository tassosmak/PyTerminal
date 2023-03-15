from src import utils
utils.add_depend(str(utils.sys.argv[1]))
from Kernel.RendererKit import Renderer as RD

def temp_convert():
  RD.CommandQuest(type='3', msg="Input The Temperature You Like To Convert (e.g., 70F, 20C etc.)")
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
      RD.CommandQuest(type='2', msg="Input proper convention")
  output = f'The temperature in {o_convention}, {result}'
  RD.CommandPush(message=output)

def measure_convert():
  RD.CommandQuest(type='3', msg='Enter Distance In feet:')
  d_ft = int(RD.Quest_result)
  d_inches = d_ft * 12
  d_yards = d_ft / 3.0
  d_miles = d_ft / 5280.0
  
  d_miles = round(d_miles, 2)
  d_yards = round(d_yards, 2)

  output = f'The distance in inches is {d_inches} inches\nThe distance in yards is {d_yards} yards\nThe distance in miles is {d_miles} miles'
  RD.CommandPush(output)

RD.CommandQuest(type='1', Button1='Temp', Button2='Distance', msg='What Do You Want To Convert')
if RD.Quest_result == 'Temp':
  temp_convert()
elif RD.Quest_result == 'Distance':
  measure_convert()