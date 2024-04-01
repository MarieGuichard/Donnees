import datetime

def bonFormatDate(d):
    """
    cette fonction permet simplement la verification d'un bon format de date ( JJ/MM/AAAA )
    
    Returns:
        True : Si la date D est bien existante et si elle a le bon format
        False: Sinon
    """
    format = "%d/%m/%Y"
    try:
        datetime.datetime.strptime(d, format)
        return True
    except ValueError:
        return False

