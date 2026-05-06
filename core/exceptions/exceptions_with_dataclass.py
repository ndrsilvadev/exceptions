"""
This module contains the `ErrorDataclass` and `InsufficientBalanceErrorDataclass` classes,
which are derived from the `Error` and `InsufficientBalanceError` classes, respectively.
"""
from dataclasses import dataclass, field


@dataclass
class ErrorDataclass(Exception):
    """Base exception using dataclass."""

    message: str = ""
    msg_log: str = field(init=False)

    def __post_init__(self) -> None:
        self.msg_log = self._build_message()
        super().__init__(self.msg_log)

    def _build_message(self) -> str:
        return self.message or self.__class__.__name__

    def __str__(self) -> str:
        return self.msg_log

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(message={self.msg_log!r})"


@dataclass
class InsufficientBalanceErrorDataclass(ErrorDataclass):
    """Insufficient balance exception using dataclass."""

    balance: float | None = None
    amount: float | None = None
    msg_cliente: str = field(init=False)

    def __post_init__(self) -> None:
        self.msg_log = self._build_message()
        self.msg_cliente = (
            "You have insufficient balance to complete the transaction."
        )
        super().__post_init__()

    def _build_message(self) -> str:
        fallback_message: str = (
            "Insufficient balance to complete the transaction. "
            f"Balance: {self.balance} / "
            f"Amount to withdraw: {self.amount}"
        )
        return self.message or fallback_message

    def __repr__(self) -> str:
        return (
            f"{self.__class__.__name__}(message={self.msg_log!r}, "
            f"balance={self.balance!r}, amount={self.amount!r})"
        )
