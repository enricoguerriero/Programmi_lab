#crea oggetto CSV file
#inizialissa sul nome del file csv 
#attributo name che contenga il nome
#metodo get_data che torni i dati del file con una lista


#oggetto CSVFile
#  - init (filename)
#  - name
#  - get_data()
#    return dati


class CSVFile:
    
    def __init__(self,name):
        self.name = name
    
    def get_data(self):
        return [1,2,3,4]
    # Inizializzo una lista vuota per salvare i valori
    values = []
    # Apro e leggo il file, linea per linea
    my_file = open("self.name", "r")
    for line in my_file:
        # Faccio lo split di ogni riga sulla virgola
        elements = line.split(',')
        # Se NON sto processando l’intestazione...
        if elements[0] != 'Date':
            # Setto la data e il valore
            date = elements[0]
            value = elements[1]
            # Aggiungo alla lista dei valori questo valore
            values.append(float(value))


mio_file = CSVFile(name='shampoo_sales.csv')

print(mio_file.name)
print(mio_file.get_data())


