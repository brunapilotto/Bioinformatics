#!/bin/bash

# Loop através de todas as pastas no diretório atual
for folder in */; do
    # Verifica se a pasta contém arquivos .fastq
    if [ -n "$(find "$folder" -maxdepth 1 -type f -name "*.fastq" 2>/dev/null)" ]; then
        # Obtem nome da pasta
	folder_name=$(basename "$folder" /)

	# Copia e renomeia os arquivos .fastq para o diretório de destino
        cp "$folder"*.fastq "./$folder_name.fastq"
        echo "Arquivos .fastq movidos da pasta $folder"
    else
        echo "Nenhum arquivo .fastq encontrado na pasta $folder"
    fi
done

echo "Concluído!"
