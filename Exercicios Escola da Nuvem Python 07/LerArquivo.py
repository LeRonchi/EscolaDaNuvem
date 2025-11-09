import re
import statistics

def analyze_ml_log_file():
    filename = input("Digite o nome do arquivo de log (ex: training_log.txt): ")
    execution_times = []

    try:
        with open(filename, 'r', encoding='utf-8') as f:
            for line in f:
                match = re.search(r'(?:Execution Time|tempo de execu(?:ção|cao)): (\d+(?:\.\d+)?)s?', line, re.IGNORECASE)
                if match:
                    try:
                        time_value = float(match.group(1))
                        execution_times.append(time_value)
                    except ValueError:
                        print(f"Aviso: Não foi possível converter '{match.group(1)}' para número na linha: {line.strip()}")

        if not execution_times:
            print("Nenhum tempo de execução encontrado no arquivo com o padrão especificado.")
            print("Por favor, verifique o formato do log e ajuste a expressão regular (regex) no código se necessário.")
            return

        mean_time = statistics.mean(execution_times)
        stdev_time = statistics.stdev(execution_times) if len(execution_times) > 1 else 0.0

        print(f"\n--- Análise do arquivo de log '{filename}' ---")
        print(f"Total de tempos de execução encontrados: {len(execution_times)}")
        print(f"Média do tempo de execução: {mean_time:.2f} segundos")
        print(f"Desvio padrão do tempo de execução: {stdev_time:.2f} segundos")

    except FileNotFoundError:
        print(f"Erro: O arquivo '{filename}' não foi encontrado. Verifique o nome e o caminho.")
    except Exception as e:
        print(f"Ocorreu um erro inesperado: {e}")

analyze_ml_log_file()