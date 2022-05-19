import pyodbc
msa_drivers = [x for x in pyodbc.drivers() if 'access']
print(f'MS-Access Drivers:{msa_drivers}')