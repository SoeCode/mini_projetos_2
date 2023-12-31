'''
Imposto a pagar no Lucro Presumido
5% sobre faturamento de ISS (mensal)
0,65% de PIS sobre faturamento, (mensal)
3% de COFINS sobre faturmaneto, (mensal)
4.8% de IR (trimestral)
10% de IR Adicional sobre o que ultrapassar 20mil do faturamento (trimestral)
CSLL: 2,88% sobre faturamento (trimestral)

'''

faturamento = {
    'jan': 'R$ 95.141,98',
    'fev': 'R$ 95.425,16',
    'mar': 'R$ 89.716,31',
    'abr': 'R$ 78.459,99',
    'mai': 'R$ 71.087,28',
    'jun': 'R$ 83.911,06',
    'jul': 'R$ 56.467,26',
    'ago': 'R$ 88.513,58',
    'set': 'R$ 66.552,49',
    'out': 'R$ 80.164,07',
    'nov': 'R$ 66.964,33',
    'dez': 'R$ 71.525,25',
}

#DEFS
def transformar_numero(valor):
    valor = valor.replace('R$ ', '')
    valor = valor.replace('.', '')
    valor = valor.replace(',', '.')
    valor = float(valor)
    return valor

def calcular_imposto_mensal(valor):
    imposto_iss = valor * 0.05
    imposto_pis = valor * 0.0065
    imposto_cofins = valor * 0.03
    imposto_mensal = imposto_iss + imposto_pis + imposto_cofins
    return imposto_mensal

def calcular_imposto_trimestral(valor):
    imposto_ir = valor * 0.048
    imposto_csll = valor * 0.0288
    if valor > 20000:
        ir_adicional = (valor - 20000) * 0.1
    else:
        ir_adicional = 0
    imposto_trimestral = imposto_ir + imposto_csll + ir_adicional
    return imposto_trimestral


for mes in faturamento:
    valor = transformar_numero(faturamento[mes])
    imposto_mensal = calcular_imposto_mensal(valor)
    imposto_trimestal = calcular_imposto_trimestral(valor)

    faturamento[mes] = (f'R${valor:,.2f}, R${imposto_mensal:,.2f}, R${imposto_trimestal:,.2f}')
#print(faturamento)

for item in faturamento:
    print(item, faturamento[item])