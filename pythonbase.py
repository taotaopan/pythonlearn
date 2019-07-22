#python学习第一课
# 陆禹廷
# chinese_zoodiac='鼠牛虎兔龙蛇马羊猴鸡狗猪'
# print(chinese_zoodiac[0:4])
# print(chinese_zoodiac[-1])
# 白羊座：3月21日～4月20日 (Aries)
#
# 金牛座：4月21日～5月21日 (Taurus)
#
# 双子座：5月22日～6月21日 (Gemini)
#
# 巨蟹座：6月22日～7月22日 (Cancer)
#
# 狮子座：7月23日～8月23日 (Leo)
#
# 处女座：8月24日～9月23日 (Virgo)
#
# 天秤座：9月24日～10月23日 (Libra)
#
# 天蝎座：10月24日～11月22日 (Scorpio)
#
# 射手座：11月23日～12月21日 (Sagittarius)
#
# 摩羯座：12月22日～1月20日 (Capricorn)
#
# 水瓶座：1月21日～2月19日 (Aquarius)
#
# 双鱼座：2月20日～3月20日 (Pisces)

stardiac=(u'摩羯座',u'水瓶座',u'双鱼座',u'白羊座',u'金牛座',u'双子座',u'巨蟹座',u'狮子座',u'处女座',u'天秤座',u'天蝎座',u'射手座')
starmonth=((1,21),(2,20),(3,21),(4,21),(5,22),(6,22),(7,23),(8,24),(9,24),(10,24),(11,23),(12,22))
(month,day)=(12,20)

diac_day=filter(lambda x: x <= (month,day) ,starmonth)

print(diac_day)

day_l=len(list(diac_day))
print(day_l)

print(stardiac[day_l%12])