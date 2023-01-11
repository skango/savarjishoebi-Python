# მოდულის მუდმივები; ხელი არ ახლოთ! (OOPS AMIS GAMOYENEBA DAMAVIWYDA :DD ARAUSHAVS MAINC  AR MCHIRDEBA)
SEC_IN_MIN = 60
MIN_IN_HOUR = 60
HOUR_IN_DAY = 24
DAY_IN_WEEK = 7
WEEK_IN_YEAR = 52


def detect_funcntion_type(index, parameter):
    functions = [years_to_secs, week_to_secs, days_to_secs, hours_to_secs, minutes_to_secs]
    return functions[index](parameter)


"""
0. დაწერეთ ფუნქცია რომელიც არგუმენტად მიწოდბულ წლებს 
წამებში გადაიყვანს


:param wlebi: float წლების რაოდენობა
:return: float შედეგად მიღებული წამები
"""


def years_to_secs(wlebi):
   return wlebi * (60 * 60 * 24 * 365)


"""
1. დაწერეთ ფუნქცია რომელიც არგუმენტად მიწოდბულ კვირებს 
წამებში გადაიყვანს 


:param kvirebi: float კვირების რაოდენობა
:return: float შედეგად მიღებული წამები
"""
def week_to_secs(kvirebi):
    return kvirebi * (60 * 60 * 24 * 7)


"""
2. დაწერეთ ფუნქცია რომელიც არგუმენტად მიწოდბულ დღეებს 
წამებში გადაიყვანს 


:param dgheebi: float დღეების რაოდენობა
:return: float შედეგად მიღებული წამები
"""
def days_to_secs(dgeebi):
    return dgeebi * (60 * 60 * 24)


"""
3. დაწერეთ ფუნქცია რომელიც არგუმენტად მიწოდბულ საათებს 
წამებში გადაიყვანს


:param saatebi: float საათების რაოდენობა
:return: float შედეგად მიღებული წამები
"""
def hours_to_secs(saatebi):
    return saatebi * (60 * 60)

"""
4. დაწერეთ ფუნქცია რომელიც არგუმენტად მიწოდბულ წუთებს 
წამებში გადაიყვანს


:param tsutebi: float წუთების რაოდენობა
:return: float შედეგად მიღებული წამები
"""
def minutes_to_secs(wutebi):
    return wutebi * 60

