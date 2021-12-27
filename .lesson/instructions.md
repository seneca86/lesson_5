# Strings

## Definition

Strings are sequences of _characters_, which are the smallest units in a writing system. The basic set of characters that is used most often in computer science is called `ASCII`, which stands for American Standard Code for Information Interchange. Later in the course we will learn about `Unicode` characters, which are a generalization of the former.

## Creation

Strings can be created with either single or double quotes:
```python
s1 = 'Good'
s2 = "Good"
s1 == s2
```

Sometimes you will see an `f` right before the definition of a string: this stands for "formatting", and enhances some of the capabililies of the string, mainly enabling it to include values of variables:

```python
name = 'Python'
print(f'{name} is the most useful language')
```

Other times we will put an `r` before a string to prevent "escape sequences", which typically involve `\`:

```python
print('this will \not work')
print(r'this will \work')
```

If the string actually contains quotes, you may combine the double and single quotes. Additionally, you can also use three single quotes or three double quotes, which are particulary useful for multiline strings:

```python
kennedy = '"If not us, who? If not now, when?" said Kennedy'
munger = "'The big money is not in the buying or selling, but in the waiting', said Charlie Munger"
volker = """
'The only thing useful banks have invented in 20 years
is the ATM',
said Paul Volker
"""
lynch = '''
"Far more money has been lost by investors preparing for corrections,
than has been lost in corrections themselves",
said Peter Lynch
'''
print(kennedy)
print(munger)
print(volker)
print(lynch)
```

The `print()` command strips the strings from quotes and _carriage returns_ (`\n`) in order to show a nicely formatted output.

## Create with `str()`