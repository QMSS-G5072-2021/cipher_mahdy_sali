def cipher(text, shift, encrypt=True):
    """
    Encrypts text.

    Parameters
    ----------
    text: A string that will be encrypted. (str)
    shift: The number of positions shifted up or down the alphabet. (int)
    encrypt: If True will be shifted by the integer indicated. If False will be a negative shift (bool)

    Returns
    -------
    Returns text that is encrypted.
    
    Examples
    --------
    >>> from cipher_sfm2136 import cipher_sfm2136
    >>> text= 'apple'
    >>> shift= 1
    >>> cipher_sfm2136.cipher(text, shift)
    "bqqmf"
    """
    alphabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    new_text = ''
    for c in text:
        index = alphabet.find(c)
        if index == -1:
            new_text += c
        else:
            new_index = index + shift if encrypt == True else index - shift
            new_index %= len(alphabet)
            new_text += alphabet[new_index:new_index+1]
    return new_text