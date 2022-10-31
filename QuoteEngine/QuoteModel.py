"""QuoteModel Package."""


class QuoteModel():
    """QuoteModel Class."""

    def __init__(self, body: str, author: str):
        """Create quote object which encapsulates body and author.

        Arguments:
            body {str} -- body of text.
            author {str} -- author.
        Returns:
            quote {obj} -- quote object.
        """
        body = body.strip(' " " ')
        body = body.encode("ascii", "ignore")
        body = body.decode()

        self.body = body
        self.author = author

    def __str__(self):
        """Represent string for Quote."""
        return f'{self.body} - {self.author}'

    def __repr__(self):
        """Return `repr(self)`, a computer-readable string representation."""
        return f"body={self.body!r}, author={self.author!r})"
