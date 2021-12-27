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

Strings can be made from other variables thanks to the `str()` function:

```python
str(10.4)
str(True)
```

The `str()` function is also operating behind the scenes when the `print()` function is invoked.

## Escape character

The _backslash_ (`\n`) or _escape character_ provides a few other characters such as `t` or `n` with a special meaning. The most common one is the _carriage return_ or `\n`:

```python
poem = 'All that is gold does not glitter,\nNot all those who wander are lost;\nThe old that is strong does not wither,\nDeep roots are not reached by the frost'
print(poem)
tabs = 'The\tsoul\tbecomes\tdyed\twith\tthe\tcolour\t of\tits\tthoughts.'
print(tabs)
```

The backslash protects the literal meaning of the quotes and of the backslash itself:
```python
height = 'My height is 6\'2.8\", I can print this by using a \\'
print(height)
```

## Combination of strings

Strings can be combined by using the `+` sign or by directly putting them together. In the latter case, a parenthesis is useful to avoid escaping the line endings. The `print()` statement puts spaces between concatenated strings to improve readibility.

```python
word1 = 'speed'
word2 = 'and'
word3 = 'focus'
word1 + word2 + word3
```

```python
word4 = 'creating'
word5 = 'and'
word6 = 'exploiting'
word7 = 'vulnerabilities'
print(word4, word5, word6, word7)
```

```python
combat = ('surprise'
          'and'
          'boldness')
combat
```