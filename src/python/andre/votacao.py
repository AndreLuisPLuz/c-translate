import sys
import os
import inspect

current_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
root_dir = os.path.dirname(os.path.realpath(current_dir))
sys.path.append(root_dir)

from commons import get_valid_input  # noqa: E402

if __name__ == "__main__":
    presidency_candidates = {
        12: "Ciro Gomes (PDT)",
        13: "Fernando Haddad (PT)",
        15: "Henrique Meirelles (MDB)",
        16: "Vera Lúcia (PSTU)",
        17: "Jair Bolsonaro (PSL)",
        18: "Marina Silva (Rede)",
        19: "Álvaro Dias (Podemos)",
        27: "Eymael (CD)",
        30: "João Amoêdo (Novo)",
        45: "Geraldo Alckmin (PSDB)",
        50: "Guilherme Boulos (PSOL)",
        51: "Cabo Daciolo (Patriota)",
        54: "João Vicente Goulart (PPL)"
    }

    valid_vote = False
    while (not valid_vote):
        vote = get_valid_input(
            "Insira o número do candidato em que deseja votar: ",
            int
        )

        try:
            candidate = presidency_candidates[vote]
            print(f"Você votou no candidato {candidate} - {vote}.")

            valid_vote = True
        except KeyError:
            print("Voto inválido. Tente novamente!")