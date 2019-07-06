from machine import ADC

'''
ADC (analog to digital conversion)
ADC is available on a dedicated pin. Note that input voltages on the ADC pin must be between 0v and 1.0v.

Use the machine.ADC class:
'''

adc = ADC(0)
adc.init(bits=9)  # set 9 bit return values (returned range 0-511)
# set 11dB input attentuation (voltage range roughly 0.0v - 3.6v)
adc_v = adc.channel(pin='P13', attn=ADC.ATTN_11DB)

value = adc_v.value()
voltage = adc_v.voltage()  # 0-4095 across voltage range 0.0v - 1.0v

print("ADC vegetronix value:" + str(value))
print("ADC vegetronix voltage:" + str(voltage))


'''
ADC.atten(attenuation)
This method allows for the setting of the amount of attenuation on the input of the ADC. This allows for a wider possible input voltage range, at the cost of accuracy (the same number of bits now represents a wider range). The possible attenuation options are:

ADC.ATTN_0DB: 0dB attenuation, gives a maximum input voltage of 1.00v - this is the default configuration
ADC.ATTN_2_5DB: 2.5dB attenuation, gives a maximum input voltage of approximately 1.34v
ADC.ATTN_6DB: 6dB attenuation, gives a maximum input voltage of approximately 2.00v
ADC.ATTN_11DB: 11dB attenuation, gives a maximum input voltage of approximately 3.6v
Warning

Despite 11dB attenuation allowing for up to a 3.6v range, note that the absolute maximum voltage rating for the input pins is 3.6v, and so going near this boundary may be damaging to the IC!
'''
