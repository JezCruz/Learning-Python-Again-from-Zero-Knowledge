#Numeric Operator Exercise 3.

#CCNA Exam fee in pesos plus 12% VAT.

ccna_exam_fee_usd = 250
vat = 0.12

#Convert USD to PHP
usd_to_php = 59.12
ccna_exam_fee_php = ccna_exam_fee_usd * usd_to_php

#Calculate VAT
vat_amount = ccna_exam_fee_php * vat
#Calculate total fee
total_fee = ccna_exam_fee_php + vat_amount

print("CCNA Exam Fee: " + str(ccna_exam_fee_php) + " PHP")

#output:
#CCNA Exam Fee: 14780.0 PHP