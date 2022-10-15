class QuoteModel():

    def __init__(self, body:str, author:str):
        """Create quote object which encapsulates body and author
        
        Arguments:
            body {str} -- body of text.
            author {str} -- author.
        Returns:
            quote {obj} -- quote object.
        """
        self.body = body
        self.author = author

    def __str__(self):
        return f'"{self.body}” - {self.author}'
