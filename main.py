# %%
s1 = 'Good'
s2 = "Good"
s1 == s2
# %%
name = 'Python'
print(f'{name} is the most useful language')
# %%
print('this will \not work')
print(r'this will \work')
# %%
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
# %%
str(10.4)
str(True)
# %%
poem = 'All that is gold does not glitter,\nNot all those who wander are lost;\nThe old that is strong does not wither,\nDeep roots are not reached by the frost'
print(poem)
tabs = 'The\tsoul\tbecomes\tdyed\twith\tthe\tcolour\t of\tits\tthoughts.'
print(tabs)
# %%
height = 'My height is 6\'2.8\", I can print this by using a \\'
print(height)
# %%
word1 = 'speed'
word2 = 'and'
word3 = 'focus'
word1 + word2 + word3
# %%
word4 = 'creating'
word5 = 'and'
word6 = 'exploiting'
word7 = 'vulnerabilities'
print(word4, word5, word6, word7)
# %%
combat = ('surprise'
          'and'
          'boldness')
combat
# %%
start = 'Once '
mid = 'upon '
end = 'a time'
print(start + mid*3 + end)
# %%
sun_tzu = 'invincibility lies in the defense'
sun_tzu[0]
sun_tzu[2:14]
sun_tzu[2::2]
sun_tzu[-7:]
sun_tzu[-7:-4]
sun_tzu[-7::-4]
# %%
sign = 'positive'
sign.replace('posi', 'nega')
# %%
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
# %%
len(churchill)
# %%
churchill.split()
# %%
