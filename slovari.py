phones=['iphone xs','samsung s3','mi9 plus']
print(phones)
phones_count=len(phones)
print(phones_count)
#print(len(phones))

phones.append('kusok govna')
print(phones)

print(phones.count('mi9 plus'))

print(phones.index('samsung s3'))


product={
"name": "iphone Xs",
"stock": 5,
"price" : 65000,
'recomend': phones
}
#print(product)
#print(product['recomend'])
#print(product['recomend'][1])

product['recomend'].append('iphone1')
#print(product)

stock=[
    {"name": "iphone Xs","stock": 10,"price" : 65001,'recomend': ['samsung s3','samsung s4']},
    {"name": "iphone 5s","stock": 20,"price" : 33333,'discount': 5000},
    {"name": "moom","stock": 55,"price" : 999}
]
#print(stock[0]['name'])

stock[0]['price']+=10000
#print(stock[0])

#print('mi9 plus' in phones)
del phones[2]
#print(phones)
phones.remove('iphone xs')
#print(phones)