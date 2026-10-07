import pandas as pd

df = pd.read_csv(r"C:\Users\lucas.magalhaes\Downloads\funcionarios.csv")

#print(df.info())
#print(df.columns)
#print(df.dtypes)
#print(df.shape)
#print(df.describe())
#print(df.loc[10:15, 'nome':'lucro'])
#print(df.iloc[0,0])

salarioativo = df.query('salario > 3000 and ativo == True')
print(salarioativo)