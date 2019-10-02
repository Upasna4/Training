x={'0':'Monday','1':'Tuesday','2':'Wednesday','3':'Thursday','4':'Friday','5':'Saturday','6':'Sunday'}
y=x.copy()
print(y)

g=x.get('3')
print(g)

g=x.setdefault('5')
print(g)

i=x.items()
print(i)

i=x.keys()
print(i)

i=x.values()
print(i)

i=x.fromkeys('123','hello')
print(i)

p=x.pop('3')
print(x)

p=x.popitem()
print(x)

ne={'5':'Sunday1'}

x.update(ne)
print(x)