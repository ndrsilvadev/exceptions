"""
This module contains the main function that calls the `withdraw_money()` 
function and handles exceptions.
"""
from core.exceptions import Error, InsufficientBalanceError


def withdraw_money():
    """
    Performs the money withdrawal operation.

    Raises an `InsufficientBalanceError` if the balance is insufficient.
    """
    # raise Error('Unexpected error.')
    raise InsufficientBalanceError(message='Insufficient balance.', balance=100, amount=200)

def main():
    """
    Main function that calls the `withdraw_money()` function and handles exceptions.
    """
    try:
        withdraw_money()
    except InsufficientBalanceError as exc:
        print(f'InsufficientBalanceError exc: {exc}')
        print(f'InsufficientBalanceError log: {exc.msg_log}')
        print(f'InsufficientBalanceError client: {exc.msg_cliente}')
    except Error as exc:
        print(f'Error log: {exc}')
    except Exception as exc:
        print(f'Exception log: {exc}')


if __name__ == '__main__':
    print('\n# Main')
    main()

    print('\n# InsufficientBalanceError')
    message: str = 'Insufficient balance.'
    print(
        repr(
            InsufficientBalanceError(
                message=message,
                balance=100,
                amount=200
            )
        )
    )
    print(
        str(
            InsufficientBalanceError(
                message=message,
                balance=100,
                amount=200
            )
        )
    )

    print('\n# Error')
    message: str = 'Insufficient balance.'
    print(repr(Error('Unexpected error.')))
    print(str(Error('Unexpected error.')))
