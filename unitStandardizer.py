#The following function converts all the different units of measurement to centimeter. The main feature implemented in the program is that it can automatically detect the unit being used in the code.
#The conversion rates are selected upon thorough research regarding the shortest and tallest possible height in which a human being can survive.
#50cm(500mm, 0.5m, 1'64ft) and 300cm(3000mm, 3m, 9'8ft) respectively being the shortest and longest survivable height for a human.
class scaleUnits:
    @staticmethod
    def unitStandard(value,unit=None):
        if unit=='mm' or unit=='MM' or unit=='Mm':
            return value/10
        elif unit=='m' or unit=="M":
            return value*100
        elif unit==None: #If unit is not provided
            if value>50 and value<300:
                return value #Already in centimetres and doesnt need conversion
            elif value>0.5 and value<3.0: #Converting Metre to Centimeter
                return value*100
            elif value>500 and value<3000: #Converting Millimetre to Centimetre
                return value/10
            else: #Converting Inch to Centimeter
                return value*30.48
