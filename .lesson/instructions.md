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

Strings can also be duplicated with the `*` operator:

```python
start = 'Once '
mid = 'upon '
end = 'a time'
print(start + mid*3 + end)
```

## Slicing with `[]`
The square brackets serve the purpose of indexing to get a single character or several characters from a string:

```python
sun_tzu = 'invincibility lies in the defense'
sun_tzu[0]
sun_tzu[2:14]
sun_tzu[2::2]
sun_tzu[-7:]
sun_tzu[-7:-4]
sun_tzu[-7::-4]
```

We will revisit the indexing conventions when dealing with `tuple` and `list`, but for the moment note several rules:
- the first character is accessed through `0`
- indexing also works backwards through the use of the `-` sign
- we can specify the beginning of the interval, end of the interval, and size of the steps with the convention `[beginning:end:interval]`

Strings are inmutable, so we cannot change them directly; we need string functions such as `replace`:
```python
sign = 'positive'
sign[0] = 'n' # this will fail
sign.replace('posi', 'nega')
```

Before moving forward, let's practice slicing a bit more and clarify some conventions:

| Slice | what it extracts |
|-------|-------------|
| `[:]` | the entire sequence|
| `[start :]`| from the _start_ offset to the end |
| `[: end]`| from the beginning to the _end_ offset minus one |
| `[start : end]`| from the _start_ offset to the _end_ offset minus 1 |
| `[start : end : step]`| from the _start_ offset to the _end_ offset minus 1, skipping characters by _step_ |

A few examples illustrating this:

```python
churchill = 'Battles are won by slaughter and manoeuver'
churchill[:]
churchill[20:]
churchill[12:]
churchill[12:28]
churchill[-9:]
churchill[19:-14]
churchill[::2]
churchill[12:28:2]
churchill[:28:4]
churchill[::-1]
```
## Get length and split

Length of a string (i.e. character count) can be measured with the function `len()`:
```python
len(churchill)
```

As opposed to `len()`, `split()` is a function that applies only to strings, and therefore can be invoked as a _method_; we will discuss this different later but for the moment it means that it can be appended to the name of the string with the structure `string.function(arguments)`:

```python
churchill.split()
```

The inverse function is `join()`, which uses the same structure: `string.join(list)`:
```python
neuro_list = ['serotonin', 'dopamine', 'norepinephrine']
neuro_str = ', '.join(neuro)
print('Some neurotransmitters are:', neuro_list)
print('Some neurotransmitters are:', neuro_str)
```
## Replace substrings

`replace()` allows for substitution of substrings, one or a given number of times:

# Strip

The `strip()` function removes leading or trailing "padding" characters (by default `' '`, `'\t'`, and `'\n'`); the companion functions `lstrip()` and `rstrip()` do it only from one side.

```python


```