#Божидара разполага с няколко къщи на Черноморието и желае да озелени дворовете на някои от тях,
# като по този начин създаде уютна обстановка и комфорт на гостите си. За целта е наела фирма.
#Напишете програма, която изчислява необходимате сума, които Божидара ще трябва да заплати на фирмата
# изпълнител на проекта. Цената на един кв. м. е 7.61 лв със ДДС. Понеже нейният двор е доста голям,
# фирмата изпълнител предлага 18% отстъпка от крайната цена.

square_meters_for_landscaping = float(input())
price_per_square_meter = 7.61

the_final_price_is = (square_meters_for_landscaping * price_per_square_meter) -(square_meters_for_landscaping * price_per_square_meter * 0.18)
the_discount_is = square_meters_for_landscaping*price_per_square_meter*0.18

print(f'The final price is: {the_final_price_is}lv')
print(f'The discount is: {the_discount_is}lv')