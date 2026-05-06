"""
This module contains the `Error` and `InsufficientBalanceError` classes,
which are derived from the `Exception` class.
"""
class Error(Exception):
    """ Base exception class."""
    def __init__(self, message: str = ''):
        self._message: str = message
        self.msg_log: str = self._build_message()

        super().__init__(self._message)

    def _build_message(self) -> str:
        return self._message or self.__class__.__name__

    def __str__(self) -> str:
        return f'{self.msg_log}'


class InsufficientBalanceError(Error):
    """Insufficient balance exception."""
    def __init__(self, message: str = '', balance: float = None, amount: float = None):
        self._message: str = message
        self._balance: float = balance
        self._amount: float = amount

        self.msg_log: str = self._build_message()
        self.msg_cliente: str = 'You have insufficient balance to complete the transaction.'

        super().__init__(self.msg_log)

    def _build_message(self) -> str:
        fallback_message: str = (
            'Insufficient balance to complete the transaction. '
            f'Balance: {self._balance} / '
            f'Amount to withdraw: {self._amount}'
        )
        return self._message or fallback_message

    def __repr__(self) -> str:
        return (
            f"{self.__class__.__name__}(message={self.msg_log!r}, "
            f"balance={self._balance!r}, amount={self._amount!r})"
        )
