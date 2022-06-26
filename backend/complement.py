from datetime import datetime

def StringToDate(date):
    return datetime.strptime(date, '%Y-%m-%d')

def StringToDatetime(date):
    return datetime.strptime(date, '%Y-%m-%d %H:%M:%S')

def DateToDate(date): 
    return datetime.strptime(date, '%d %B %Y')