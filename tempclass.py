class temperature:
    def __init__(self,temp):
        self.temp = temp
    def celcius(self):
        self.cel= (self.temp-32)*5/9
        return self.cel
    def fahrenheit(self):
        self.fah= self.temp*(9/5)+32
        return self.fah
        
cel2fah=int(input("Enter the temperature in fehrenheit"))
convert = temperature(cel2fah)
print(cel2fah,"degree fahrenheit is:",convert.celcius(),"celcius")
fah2cel = int(input("Enter the temperature in cel"))
convert = temperature(fah2cel)
print(fah2cel,"degree celcius is:",convert.fahrenheit(),"fahrenheit")