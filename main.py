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
neuro_list = ['serotonin', 'dopamine', 'norepinephrine']
neuro_str = ', '.join(neuro)
print('Some neurotransmitters are:', neuro_list)
print('Some neurotransmitters are:', neuro_str)
# %%
sleep = 'Sleeping is pretty creepy: for a third \
of your life you are just not there, \
floating in this suspended state, \
with your brain making your eyelids all twitchy.'
sleep.replace('Sleeping', 'Daydreaming')
sleep.replace('your', 'my', 2)
# %%
padded = '  pure  '
padded.strip()
padded.lstrip()
padded.rstrip()
# %%
question = 'Who? What?'
question.strip('?')
# %%
import string
string.punctuation
string.whitespace
many_questions = 'How so!!???'
many_questions.strip(string.punctuation)
many_whitespaces = '    aaa     '
many_whitespaces.strip(string.whitespace)
# %%
art_of_war = 'Now an army may be likened to water, \
for just as flowing water avoids the heighs and \
hastens to the lowlands, so an army avoids \
strengths and strikes weakness.'
# %%
art_of_war.startswith('Now')
art_of_war.endswith('weakness.')
art_of_war.find('water')
art_of_war.rfind('water')
art_of_war.count('water')
art_of_war.isalnum()
# %%
