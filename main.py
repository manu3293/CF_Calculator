# Definizione di insiemi per le vocali e le consonanti
vocali = set('aeiou')
consonanti = set('bcdfghjklmnpqrstvwxyz')


def acquisizione_dati():
    """
    The function `acquisizione_dati` prompts the user to input personal information such as name,
    surname, gender, date of birth, place of birth, and birth province in Python.
    :return: The function `acquisizione_dati` is returning a tuple containing the following information
    in order: `nome` (name), `cognome` (surname), `sesso` (gender), `data_di_nascita` (date of birth),
    `luogo_di_nascita` (place of birth), and `provincia_di_nascita` (province of birth).
    """
    nome = input('Nome: ')
    cognome = input('Cognome: ')
    sesso = input('Sesso F/M: ')
    data_di_nascita = input('Data di Nascita (DD/MM/YYYY): ')
    luogo_di_nascita = input('Luogo di Nascita: ')
    provincia_di_nascita = input('Provincia di Nascita (XX): ')
    return nome, cognome, sesso, data_di_nascita, luogo_di_nascita, provincia_di_nascita


def calcola_codice_catastale_comune(luogo_di_nascita, provincia_di_nascita):
    """
    The function `calcola_codice_catastale_comune` reads a file containing Italian municipalities data
    and returns the corresponding cadastral code based on the input birthplace and province.

    :param luogo_di_nascita: The `calcola_codice_catastale_comune` function reads from a file named
    'comuni_italiani.txt' to find the codice catastale (cadastral code) of a specific comune
    (municipality) based on the input parameters `luogo_di_n
    :param provincia_di_nascita: The parameter `provincia_di_nascita` refers to the province of birth.
    It is typically a string representing the province where a person was born. For example, "Milano",
    "Roma", "Napoli", etc
    :return: The function `calcola_codice_catastale_comune` is returning the codice catastale (cadastral
    code) of the specified `luogo_di_nascita` (place of birth) and `provincia_di_nascita` (province of
    birth) by reading from a file named 'comuni_italiani.txt'.
    """
    with open('comuni_italiani.txt', 'r', encoding='utf-8') as file:
        for line in file:
            _, comune, provincia, _, _, codice_catastale = line.strip().split('\t')
            if comune == luogo_di_nascita and provincia == provincia_di_nascita:
                return codice_catastale


def calcola_cognome(cognome):
    """
    The function `calcola_cognome` takes a surname as input, removes spaces, extracts the first three
    consonants or vowels (or 'X' if not enough), and returns them as a string.

    :param cognome: It looks like the code you provided is a function called `calcola_cognome` that
    takes a surname as input and calculates a shortened version of the surname based on the first three
    consonants or vowels in the surname. If there are not enough consonants or vowels in the surname, it
    uses
    :return: The function `calcola_cognome` returns a string of the first three consonants or vowels (in
    order of appearance) from the input `cognome` after removing any spaces. If there are not enough
    consonants or vowels in the input, 'X' is used to fill the remaining characters to make a total of
    three characters.
    """
    cognome = cognome.replace(' ', '')
    lettere_cognome = ''
    vocali_cognome = [
        lettera for lettera in cognome if lettera.lower() in vocali]
    consonanti_cognome = [
        lettera for lettera in cognome if lettera.lower() in consonanti]
    while len(lettere_cognome) < 3:
        if consonanti_cognome:
            lettere_cognome += consonanti_cognome.pop(0)
        elif vocali_cognome:
            lettere_cognome += vocali_cognome.pop(0)
        else:
            lettere_cognome += 'X'
    return lettere_cognome


def calcola_nome(nome):
    """
    The function "calcola_nome" takes a name as input, removes spaces, extracts vowels and consonants,
    and returns the first three letters alternating between consonants and vowels or 'X' if needed.

    :param nome: The function `calcola_nome` takes a name as input, removes any spaces in the name, and
    then extracts the vowels and consonants from the name. It then constructs a new name by alternating
    between consonants and vowels (or 'X' if there are not enough letters) until the new
    :return: The function `calcola_nome` takes a name as input, removes any spaces in the name, and then
    extracts the vowels and consonants from the name. It then constructs a new string `lettere_nome` by
    alternating between consonants and vowels until the length of the new string is at least 3
    characters long. If there are not enough consonants or vowels to complete the new string,
    """
    nome = nome.replace(' ', '')
    lettere_nome = ''
    vocali_nome = [lettera for lettera in nome if lettera.lower() in vocali]
    consonanti_nome = [
        lettera for lettera in nome if lettera.lower() in consonanti]
    while len(lettere_nome) < 3:
        if consonanti_nome:
            lettere_nome += consonanti_nome.pop(0)
        elif vocali_nome:
            lettere_nome += vocali_nome.pop(0)
        else:
            lettere_nome += 'X'
    return lettere_nome


def calcola_mese_di_nascita(mese_di_nascita):
    """
    The function `calcola_mese_di_nascita` takes a numerical month of birth as input and returns the
    corresponding letter representation based on a predefined mapping.

    :param mese_di_nascita: The function `calcola_mese_di_nascita` takes the month of birth as input and
    returns the corresponding letter code based on the provided mapping. The mapping assigns a letter to
    each month from 1 to 12
    :return: The function `calcola_mese_di_nascita` takes a numerical input representing a month of
    birth and returns the corresponding letter code for that month based on the provided dictionary
    `mese_di_nascita_lettera`.
    """
    mese_di_nascita_lettera = {1: 'A', 2: 'B', 3: 'C', 4: 'D', 5: 'E',
                               6: 'H', 7: 'L', 8: 'M', 9: 'P', 10: 'R', 11: 'S', 12: 'T'}
    return mese_di_nascita_lettera[int(mese_di_nascita)]


def calcola_codice_di_controllo(cf_senza_controllo):
    """
    The function `calcola_codice_di_controllo` calculates the control code for an Italian fiscal code
    (codice fiscale) based on the input code without the control code.

    :param cf_senza_controllo: The function `calcola_codice_di_controllo` calculates the control code
    for an Italian fiscal code (Codice Fiscale) based on the input string `cf_senza_controllo`, which
    represents the fiscal code without the control code
    :return: the control code for the given Italian fiscal code (codice fiscale) without the control
    code.
    """
    conv_pari = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6, 'H': 7, 'I': 8, 'J': 9, 'K': 10, 'L': 11, 'M': 12, 'N': 13,
                 'O': 14, 'P': 15, 'Q': 16, 'R': 17, 'S': 18, 'T': 19, 'U': 20, 'V': 21, 'W': 22, 'X': 23, 'Y': 24, 'Z': 25, '0': 0, '1': 1, '2': 2,
                 '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
    conv_dispari = {'A': 1, 'B': 0, 'C': 5, 'D': 7, 'E': 9, 'F': 13, 'G': 15, 'H': 17, 'I': 19, 'J': 21, 'K': 2, 'L': 4, 'M': 18, 'N': 20,
                    'O': 11, 'P': 3, 'Q': 6, 'R': 8, 'S': 12, 'T': 14, 'U': 16, 'V': 10, 'W': 22, 'X': 25, 'Y': 24, 'Z': 23, '0': 1, '1': 0, '2': 5,
                    '3': 7, '4': 9, '5': 13, '6': 15, '7': 17, '8': 19, '9': 21}
    corrisp = {0: 'A', 1: 'B', 2: 'C', 3: 'D', 4: 'E', 5: 'F', 6: 'G', 7: 'H', 8: 'I',
               9: 'J', 10: 'K', 11: 'L', 12: 'M', 13: 'N', 14: 'O', 15: 'P', 16: 'Q',
               17: 'R', 18: 'S', 19: 'T', 20: 'U', 21: 'V', 22: 'W', 23: 'X', 24: 'Y', 25: 'Z'}
    tot = 0
    for i, carattere in enumerate(cf_senza_controllo):
        if i % 2 == 0:
            tot += conv_dispari[carattere]
        else:
            tot += conv_pari[carattere]
    return corrisp[tot % 26]


def codice_fiscale_completo(nome, cognome, sesso, data_di_nascita, luogo_di_nascita, provincia_di_nascita):
    """
    The function `codice_fiscale_completo` generates a complete Italian fiscal code based on personal
    information such as name, surname, gender, date and place of birth.

    :param nome: It seems like you were about to provide some information about the parameters for the
    function `codice_fiscale_completo`, but the message got cut off. Could you please provide more
    details about the parameters so that I can assist you further?
    :param cognome: The "cognome" parameter in the function represents the surname or last name of an
    individual. It is used to calculate a specific set of letters in the Italian fiscal code (codice
    fiscale)
    :param sesso: The parameter "sesso" in the function "codice_fiscale_completo" is used to indicate
    the gender of the person. It is a string that can have two possible values: 'M' for male or 'F' for
    female. This information is used in the calculation of
    :param data_di_nascita: It seems like you were about to provide more information about the
    parameters for the function `codice_fiscale_completo`, but the message got cut off. Could you please
    provide more details or let me know if you need help with something specific related to the function
    or its parameters?
    :param luogo_di_nascita: The parameter `luogo_di_nascita` represents the place of birth. It is
    typically the city or town where a person is born
    :param provincia_di_nascita: The parameter "provincia_di_nascita" refers to the province of birth.
    In the context of the Italian fiscal code (codice fiscale) calculation, it is used to determine the
    code for the birthplace. This code is a specific alphanumeric value associated with the province
    where the individual was
    :return: The function `codice_fiscale_completo` is returning the complete Italian fiscal code
    (codice fiscale) for a person based on their personal information such as name, surname, gender,
    date of birth, place of birth, and province of birth. The fiscal code is a unique identifier used in
    Italy for tax purposes and official documents.
    """
    lettere_cognome = calcola_cognome(cognome)
    lettere_nome = calcola_nome(nome)
    giorno_di_nascita, mese_di_nascita, anno_di_nascita = data_di_nascita.split(
        '/')
    lettera_mese_di_nascita = calcola_mese_di_nascita(mese_di_nascita)
    giorno_di_nascita = giorno_di_nascita if sesso == 'M' else int(
        giorno_di_nascita) + 40
    codice_catastale_comune = calcola_codice_catastale_comune(
        luogo_di_nascita, provincia_di_nascita)
    cf_senza_controllo = lettere_cognome + lettere_nome + \
        anno_di_nascita[2:] + lettera_mese_di_nascita + \
        str(giorno_di_nascita) + codice_catastale_comune
    cdc = calcola_codice_di_controllo(cf_senza_controllo)
    return cf_senza_controllo + cdc


def main():
    """
    The main function acquires personal data and generates a complete fiscal code based on the input.
    """
    nome, cognome, sesso, data_di_nascita, luogo_di_nascita, provincia_di_nascita = acquisizione_dati()
    cf = codice_fiscale_completo(
        nome.upper(), cognome.upper(), sesso.upper(), data_di_nascita, luogo_di_nascita.upper(), provincia_di_nascita.upper())
    print(cf)


# The `if __name__ == '__main__':` block in Python is a common idiom used to make a file both usable
# as a standalone script and importable as a module.
if __name__ == '__main__':
    main()
