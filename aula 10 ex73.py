times = ('Palmeiras','Internacional','Fluminense','Corinthians','Flamengo',
         'Atletico-PR','Atletico-MG','Fortaleza','São Paulo','America-MG','Botafogo','Santos'
         ,'Goias','Bragantino','Coritiba','Cuiaba','Ceara','Atletico-GO','Avai','Juventude')
print('='*45)
print(f'Os 5 primeiros times são: {times[0:6]} ')
print('='*45)
print(f'Os 4 ultimos times são: {times[16:21]}')
print('='*45)
print(f'Times em ordem alfabetica : {(sorted(times))}')
print('='*45)
a=times.index('São Paulo')
print(f'O São Paulo está na {a}ª colocação')
print('='*45)