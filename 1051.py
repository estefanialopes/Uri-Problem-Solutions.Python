sal = float(input())

if sal <= 2000.00:
    ir = 0
    print('Isento')
    
if 2000.00 < sal <= 3000.00:
    tx8 = sal - 2000.00
    ir = tx8 * (8 / 100)
    
if 3000.00 < sal <= 4500.00:
    ir8 = (8 / 100) * (1000.00)
    tx18 = sal - 3000.00
    ir = tx18 * (18 / 100) + ir8
    
if sal > 4500.00:
    ir8 = (8 / 100) * (1000.00)
    ir18 = (18 / 100) * (1500.00)
    tx28 = sal - 4500.00
    ir = ir18 + ir8 + tx28 * (28 / 100)

if sal > 2000.00:
    ir = float(ir)
    print('R$ {:.2f}'.format(ir))
