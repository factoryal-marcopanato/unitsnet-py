from enum import Enum
import math
import string


class DurationUnits(Enum):
        """
            DurationUnits enumeration
        """
        
        Year365 = 'year365'
        """
            
        """
        
        Month30 = 'month30'
        """
            
        """
        
        Week = 'week'
        """
            
        """
        
        Day = 'day'
        """
            
        """
        
        Hour = 'hour'
        """
            
        """
        
        Minute = 'minute'
        """
            
        """
        
        Second = 'second'
        """
            
        """
        
        JulianYear = 'julian_year'
        """
            
        """
        
        NanoSecond = 'nano_second'
        """
            
        """
        
        MicroSecond = 'micro_second'
        """
            
        """
        
        MilliSecond = 'milli_second'
        """
            
        """
        
    
class Duration:
    """
    Time is a dimension in which events can be ordered from the past through the present into the future, and also the measure of durations of events and the intervals between them.

    Args:
        value (float): The value.
        from_unit (DurationUnits): The Duration unit to create from, The default unit is Second
    """
    def __init__(self, value: float, from_unit: DurationUnits = DurationUnits.Second):
        if math.isnan(value):
            raise ValueError('Invalid unit: value is NaN')
        self.__value = self.__convert_to_base(value, from_unit)
        
        self.__years365 = None
        
        self.__months30 = None
        
        self.__weeks = None
        
        self.__days = None
        
        self.__hours = None
        
        self.__minutes = None
        
        self.__seconds = None
        
        self.__julian_years = None
        
        self.__nano_seconds = None
        
        self.__micro_seconds = None
        
        self.__milli_seconds = None
        

    def __convert_from_base(self, from_unit: DurationUnits) -> float:
        value = self.__value
        
        if from_unit == DurationUnits.Year365:
            return (value / (365 * 24 * 3600))
        
        if from_unit == DurationUnits.Month30:
            return (value / (30 * 24 * 3600))
        
        if from_unit == DurationUnits.Week:
            return (value / (7 * 24 * 3600))
        
        if from_unit == DurationUnits.Day:
            return (value / (24 * 3600))
        
        if from_unit == DurationUnits.Hour:
            return (value / 3600)
        
        if from_unit == DurationUnits.Minute:
            return (value / 60)
        
        if from_unit == DurationUnits.Second:
            return (value)
        
        if from_unit == DurationUnits.JulianYear:
            return (value / (365.25 * 24 * 3600))
        
        if from_unit == DurationUnits.NanoSecond:
            return ((value) / 1e-09)
        
        if from_unit == DurationUnits.MicroSecond:
            return ((value) / 1e-06)
        
        if from_unit == DurationUnits.MilliSecond:
            return ((value) / 0.001)
        
        return None


    def __convert_to_base(self, value: float, to_unit: DurationUnits) -> float:
        
        if to_unit == DurationUnits.Year365:
            return (value * 365 * 24 * 3600)
        
        if to_unit == DurationUnits.Month30:
            return (value * 30 * 24 * 3600)
        
        if to_unit == DurationUnits.Week:
            return (value * 7 * 24 * 3600)
        
        if to_unit == DurationUnits.Day:
            return (value * 24 * 3600)
        
        if to_unit == DurationUnits.Hour:
            return (value * 3600)
        
        if to_unit == DurationUnits.Minute:
            return (value * 60)
        
        if to_unit == DurationUnits.Second:
            return (value)
        
        if to_unit == DurationUnits.JulianYear:
            return (value * 365.25 * 24 * 3600)
        
        if to_unit == DurationUnits.NanoSecond:
            return ((value) * 1e-09)
        
        if to_unit == DurationUnits.MicroSecond:
            return ((value) * 1e-06)
        
        if to_unit == DurationUnits.MilliSecond:
            return ((value) * 0.001)
        
        return None


    @property
    def base_value(self) -> float:
        return self.__value

    
    @staticmethod
    def from_years365(years365: float):
        """
        Create a new instance of Duration from a value in years365.

        

        :param meters: The Duration value in years365.
        :type years365: float
        :return: A new instance of Duration.
        :rtype: Duration
        """
        return Duration(years365, DurationUnits.Year365)

    
    @staticmethod
    def from_months30(months30: float):
        """
        Create a new instance of Duration from a value in months30.

        

        :param meters: The Duration value in months30.
        :type months30: float
        :return: A new instance of Duration.
        :rtype: Duration
        """
        return Duration(months30, DurationUnits.Month30)

    
    @staticmethod
    def from_weeks(weeks: float):
        """
        Create a new instance of Duration from a value in weeks.

        

        :param meters: The Duration value in weeks.
        :type weeks: float
        :return: A new instance of Duration.
        :rtype: Duration
        """
        return Duration(weeks, DurationUnits.Week)

    
    @staticmethod
    def from_days(days: float):
        """
        Create a new instance of Duration from a value in days.

        

        :param meters: The Duration value in days.
        :type days: float
        :return: A new instance of Duration.
        :rtype: Duration
        """
        return Duration(days, DurationUnits.Day)

    
    @staticmethod
    def from_hours(hours: float):
        """
        Create a new instance of Duration from a value in hours.

        

        :param meters: The Duration value in hours.
        :type hours: float
        :return: A new instance of Duration.
        :rtype: Duration
        """
        return Duration(hours, DurationUnits.Hour)

    
    @staticmethod
    def from_minutes(minutes: float):
        """
        Create a new instance of Duration from a value in minutes.

        

        :param meters: The Duration value in minutes.
        :type minutes: float
        :return: A new instance of Duration.
        :rtype: Duration
        """
        return Duration(minutes, DurationUnits.Minute)

    
    @staticmethod
    def from_seconds(seconds: float):
        """
        Create a new instance of Duration from a value in seconds.

        

        :param meters: The Duration value in seconds.
        :type seconds: float
        :return: A new instance of Duration.
        :rtype: Duration
        """
        return Duration(seconds, DurationUnits.Second)

    
    @staticmethod
    def from_julian_years(julian_years: float):
        """
        Create a new instance of Duration from a value in julian_years.

        

        :param meters: The Duration value in julian_years.
        :type julian_years: float
        :return: A new instance of Duration.
        :rtype: Duration
        """
        return Duration(julian_years, DurationUnits.JulianYear)

    
    @staticmethod
    def from_nano_seconds(nano_seconds: float):
        """
        Create a new instance of Duration from a value in nano_seconds.

        

        :param meters: The Duration value in nano_seconds.
        :type nano_seconds: float
        :return: A new instance of Duration.
        :rtype: Duration
        """
        return Duration(nano_seconds, DurationUnits.NanoSecond)

    
    @staticmethod
    def from_micro_seconds(micro_seconds: float):
        """
        Create a new instance of Duration from a value in micro_seconds.

        

        :param meters: The Duration value in micro_seconds.
        :type micro_seconds: float
        :return: A new instance of Duration.
        :rtype: Duration
        """
        return Duration(micro_seconds, DurationUnits.MicroSecond)

    
    @staticmethod
    def from_milli_seconds(milli_seconds: float):
        """
        Create a new instance of Duration from a value in milli_seconds.

        

        :param meters: The Duration value in milli_seconds.
        :type milli_seconds: float
        :return: A new instance of Duration.
        :rtype: Duration
        """
        return Duration(milli_seconds, DurationUnits.MilliSecond)

    
    @property
    def years365(self) -> float:
        """
        
        """
        if self.__years365 != None:
            return self.__years365
        self.__years365 = self.__convert_from_base(DurationUnits.Year365)
        return self.__years365

    
    @property
    def months30(self) -> float:
        """
        
        """
        if self.__months30 != None:
            return self.__months30
        self.__months30 = self.__convert_from_base(DurationUnits.Month30)
        return self.__months30

    
    @property
    def weeks(self) -> float:
        """
        
        """
        if self.__weeks != None:
            return self.__weeks
        self.__weeks = self.__convert_from_base(DurationUnits.Week)
        return self.__weeks

    
    @property
    def days(self) -> float:
        """
        
        """
        if self.__days != None:
            return self.__days
        self.__days = self.__convert_from_base(DurationUnits.Day)
        return self.__days

    
    @property
    def hours(self) -> float:
        """
        
        """
        if self.__hours != None:
            return self.__hours
        self.__hours = self.__convert_from_base(DurationUnits.Hour)
        return self.__hours

    
    @property
    def minutes(self) -> float:
        """
        
        """
        if self.__minutes != None:
            return self.__minutes
        self.__minutes = self.__convert_from_base(DurationUnits.Minute)
        return self.__minutes

    
    @property
    def seconds(self) -> float:
        """
        
        """
        if self.__seconds != None:
            return self.__seconds
        self.__seconds = self.__convert_from_base(DurationUnits.Second)
        return self.__seconds

    
    @property
    def julian_years(self) -> float:
        """
        
        """
        if self.__julian_years != None:
            return self.__julian_years
        self.__julian_years = self.__convert_from_base(DurationUnits.JulianYear)
        return self.__julian_years

    
    @property
    def nano_seconds(self) -> float:
        """
        
        """
        if self.__nano_seconds != None:
            return self.__nano_seconds
        self.__nano_seconds = self.__convert_from_base(DurationUnits.NanoSecond)
        return self.__nano_seconds

    
    @property
    def micro_seconds(self) -> float:
        """
        
        """
        if self.__micro_seconds != None:
            return self.__micro_seconds
        self.__micro_seconds = self.__convert_from_base(DurationUnits.MicroSecond)
        return self.__micro_seconds

    
    @property
    def milli_seconds(self) -> float:
        """
        
        """
        if self.__milli_seconds != None:
            return self.__milli_seconds
        self.__milli_seconds = self.__convert_from_base(DurationUnits.MilliSecond)
        return self.__milli_seconds

    
    def to_string(self, unit: DurationUnits = DurationUnits.Second) -> string:
        """
        Format the Duration to string.
        Note! the default format for Duration is Second.
        To specify the unit format set the 'unit' parameter.
        """
        
        if unit == DurationUnits.Year365:
            return f"""{self.years365} yr"""
        
        if unit == DurationUnits.Month30:
            return f"""{self.months30} mo"""
        
        if unit == DurationUnits.Week:
            return f"""{self.weeks} wk"""
        
        if unit == DurationUnits.Day:
            return f"""{self.days} d"""
        
        if unit == DurationUnits.Hour:
            return f"""{self.hours} h"""
        
        if unit == DurationUnits.Minute:
            return f"""{self.minutes} m"""
        
        if unit == DurationUnits.Second:
            return f"""{self.seconds} s"""
        
        if unit == DurationUnits.JulianYear:
            return f"""{self.julian_years} jyr"""
        
        if unit == DurationUnits.NanoSecond:
            return f"""{self.nano_seconds} """
        
        if unit == DurationUnits.MicroSecond:
            return f"""{self.micro_seconds} """
        
        if unit == DurationUnits.MilliSecond:
            return f"""{self.milli_seconds} """
        
        return f'{self.__value}'


    def get_unit_abbreviation(self, unit_abbreviation: DurationUnits = DurationUnits.Second) -> string:
        """
        Get Duration unit abbreviation.
        Note! the default abbreviation for Duration is Second.
        To specify the unit abbreviation set the 'unit_abbreviation' parameter.
        """
        
        if unit_abbreviation == DurationUnits.Year365:
            return """yr"""
        
        if unit_abbreviation == DurationUnits.Month30:
            return """mo"""
        
        if unit_abbreviation == DurationUnits.Week:
            return """wk"""
        
        if unit_abbreviation == DurationUnits.Day:
            return """d"""
        
        if unit_abbreviation == DurationUnits.Hour:
            return """h"""
        
        if unit_abbreviation == DurationUnits.Minute:
            return """m"""
        
        if unit_abbreviation == DurationUnits.Second:
            return """s"""
        
        if unit_abbreviation == DurationUnits.JulianYear:
            return """jyr"""
        
        if unit_abbreviation == DurationUnits.NanoSecond:
            return """"""
        
        if unit_abbreviation == DurationUnits.MicroSecond:
            return """"""
        
        if unit_abbreviation == DurationUnits.MilliSecond:
            return """"""
        

    def __str__(self):
        return self.to_string()


    def __add__(self, other):
        if not isinstance(other, Duration):
            raise TypeError("unsupported operand type(s) for +: 'Duration' and '{}'".format(type(other).__name__))
        return Duration(self.__value + other.__value)


    def __mul__(self, other):
        if not isinstance(other, Duration):
            raise TypeError("unsupported operand type(s) for *: 'Duration' and '{}'".format(type(other).__name__))
        return Duration(self.__value * other.__value)


    def __sub__(self, other):
        if not isinstance(other, Duration):
            raise TypeError("unsupported operand type(s) for -: 'Duration' and '{}'".format(type(other).__name__))
        return Duration(self.__value - other.__value)


    def __truediv__(self, other):
        if not isinstance(other, Duration):
            raise TypeError("unsupported operand type(s) for /: 'Duration' and '{}'".format(type(other).__name__))
        return Duration(self.__value / other.__value)


    def __mod__(self, other):
        if not isinstance(other, Duration):
            raise TypeError("unsupported operand type(s) for %: 'Duration' and '{}'".format(type(other).__name__))
        return Duration(self.__value % other.__value)


    def __pow__(self, other):
        if not isinstance(other, Duration):
            raise TypeError("unsupported operand type(s) for **: 'Duration' and '{}'".format(type(other).__name__))
        return Duration(self.__value ** other.__value)


    def __eq__(self, other):
        if not isinstance(other, Duration):
            raise TypeError("unsupported operand type(s) for ==: 'Duration' and '{}'".format(type(other).__name__))
        return self.__value == other.__value


    def __lt__(self, other):
        if not isinstance(other, Duration):
            raise TypeError("unsupported operand type(s) for <: 'Duration' and '{}'".format(type(other).__name__))
        return self.__value < other.__value


    def __gt__(self, other):
        if not isinstance(other, Duration):
            raise TypeError("unsupported operand type(s) for >: 'Duration' and '{}'".format(type(other).__name__))
        return self.__value > other.__value


    def __le__(self, other):
        if not isinstance(other, Duration):
            raise TypeError("unsupported operand type(s) for <=: 'Duration' and '{}'".format(type(other).__name__))
        return self.__value <= other.__value


    def __ge__(self, other):
        if not isinstance(other, Duration):
            raise TypeError("unsupported operand type(s) for >=: 'Duration' and '{}'".format(type(other).__name__))
        return self.__value >= other.__value