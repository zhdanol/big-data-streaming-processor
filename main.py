import re

def extract_domains_streaming(input_file, output_file):
    domain_pattern = re.compile(r'(?:[a-z0-9](?:[a-z0-9-]{0,61}[a-z0-9])?\.)+[a-z0-2]{2,63}')

    try:

        with open(input_file, 'r', encoding='utf-8', errors='ignore') as infile, \
                open(output_file, 'w', encoding='utf-8') as outfile:

            for line in infile:
                domains = domain_pattern.findall(line.lower())

                for domain in domains:
                    outfile.write(domain + '\n')

    except FileNotFoundError:
        print("Ошибка: Файл не найден.")
