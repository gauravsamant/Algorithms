def find_payment(loan: float, r: float, m: int):
    '''
    Assume Loan and r are float, m an integer
    Return the montly payment for the mortage of size loan at a monthly rate of r for m month.
    '''

    return loan((r * (1 + r) ** m) / (((1 + r) ** m) - 1))

class Mortgage(object):
    '''Abstract class for implementing different kinds of mortages'''
    def __init__(self: "Mortgage", loan: float, annual_rate: float, months: int) -> None:
        '''Assume loan and annual_rate are float, month an integer
        Create a Mortgage with loan amount, for months month with rate of interest annual_rate'''
        self._loan = loan
        self._month = months
        self._annual_rate = annual_rate / 12
        self._payments_list =[]
