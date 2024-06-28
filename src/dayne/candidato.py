print("_______________________________________________\n")
print("__________________ELEIÇÕES_____________________\n")
print("_______________________________________________\n\n\n")

pres = int(input("INSIRA O NÚMERO DO SEU CANDIDATO A PRESIDÊNCIA:"));
print("_______________________________________________\n\n\n")

opPres = {19:"Alvari Dias",51:"Cabo Daciolo",12:"Ciro Gomes",27:"Eymael",13:"Fernando Haddad",45:"Geraldo tavivo",50:"Guilherme Anarquia",15:"Henrique Meirelles",17:"Jair quefasebrasil",30:"João Amoêdo",54:"João Vicente Goulart",18:"Marina Silva",16:"Vera Lúcia"}

try:
    validandoPres = opPres[pres] 
    print(f"{validandoPres} - {pres} \n\n\n")
except KeyError:
    print("_____________Candidato Inválido________________ \n\n\n");


print("_______________________________________________\n\n\n");
gov = int(input("INSIRA O NÚMERO DO SEU CANDIDATO A GOVERNADOR:"));
print("_______________________________________________\n\n\n");

opGov = {11:"Cida Borghetti",13:"Doutor Rosinha",28:"Geonísio Marinh",15:"João Arruda",18:"Jorge Bernardi",17:"Ogier Buchi",29:"Priscila Ebara",16:"Professor Ivan Bernardo",50:"Professor Piva",55:"Ratinho Junior"}
try:
    validandoGov = opGov[gov] 
    print(f"{validandoGov} - {gov} \n\n\n")
except KeyError:
    print("_____________Candidato Inválido________________ \n\n\n");



