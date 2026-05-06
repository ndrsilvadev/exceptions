"""
This module contains the main function that calls the `withdraw_money()` 
function and handles exceptions.
"""
from core.exceptions import ErrorDataclass, InsufficientBalanceErrorDataclass


def withdraw_money() -> None:
    """
    Performs the money withdrawal operation.

    Raises an `InsufficientBalanceError` if the balance is insufficient.
    """
    raise InsufficientBalanceErrorDataclass(
        message="",
        balance=100,
        amount=200,
    )


def main() -> None:
    """
    Main function that calls the `withdraw_money()` function and handles exceptions.
    """
    try:
        withdraw_money()
    except InsufficientBalanceErrorDataclass as exc:
        print(f"InsufficientBalanceErrorDataclass exc: {exc}")
        print(f"InsufficientBalanceErrorDataclass log: {exc.msg_log}")
        print(f"InsufficientBalanceErrorDataclass client: {exc.msg_cliente}")
    except ErrorDataclass as exc:
        print(f"ErrorDataclass log: {exc}")
    except Exception as exc:
        print(f"Exception log: {exc}")


if __name__ == "__main__":
    print("\n# Main")
    main()

    print("\n# InsufficientBalanceErrorDataclass")
    message: str = "Insufficient balance."
    print(
        repr(
            InsufficientBalanceErrorDataclass(
                message=message,
                balance=100,
                amount=200,
            )
        )
    )
    print(
        str(
            InsufficientBalanceErrorDataclass(
                message=message,
                balance=100,
                amount=200,
            )
        )
    )

    print("\n# ErrorDataclass")
    print(repr(ErrorDataclass("Unexpected error.")))
    print(str(ErrorDataclass("Unexpected error.")))
