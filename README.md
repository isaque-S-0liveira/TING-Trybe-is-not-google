# TING (trybe is not google)

## Contexto

O foco principal deste projeto é, com base nos ensinamentos da **Trybe**, implementar uma aplicação que simula um algoritmo de indexação de documentos similar ao do Google, capaz de identificar ocorrências de termos em arquivos de texto (formato **.txt**).

<details>
  <summary>O que é a Trybe?🤔</summary>
  A Trybe é uma escola de desenvolvimento web genuinamente comprometida com o sucesso profissional de seus estudantes. Com o Modelo de Sucesso Compartilhado (MSC) oferecido pela Trybe Fintech, uma instituição financeira autorizada pelo Banco Central do Brasil, os alunos têm a opção de pagar apenas quando estiverem trabalhando.
</details>

### A aplicação é composta por dois módulos principais:

1. **Módulo de Gerenciamento de Arquivos**: Responsável por permitir a inserção e remoção de arquivos TXT, utilizando uma fila para controlar a ordem de processamento dos arquivos.
   
2. **Módulo de Busca**: Fornece funcionalidades de busca de termos dentro dos arquivos previamente anexados, retornando a ocorrência de palavras específicas, sem distinção entre maiúsculas e minúsculas (case insensitive).

Neste projeto, várias estruturas de dados clássicas foram implementadas e manipuladas, como **Pilhas**, **Filas**, **Deques** e **Listas Ligadas**. O desafio principal foi desenvolver algoritmos que utilizam essas estruturas de forma eficiente, permitindo a otimização do processamento e busca em grandes quantidades de arquivos.

Além disso, o projeto inclui a implementação de uma fila de prioridade, onde arquivos pequenos (com menos de 5 linhas) são processados com prioridade, afetando diretamente o comportamento dos métodos de inserção e remoção.

### Funcionalidades Principais:
- **Manipulação de Arquivos**: Importação e armazenamento de arquivos em uma fila, além da remoção e exibição de metadados de arquivos.
- **Busca de Palavras**: Busca case insensitive por termos em todos os arquivos anexados.
- **Fila de Prioridade**: Implementação de uma fila de prioridade para processar arquivos pequenos de forma prioritária.
- **Testes Automatizados**: Implementação de testes para garantir o correto funcionamento da fila de prioridade e das buscas.

---

## Tecnologias Usadas

- [Python](https://www.python.org/) - Linguagem de programação utilizada para implementar a solução.
- [Pytest](https://docs.pytest.org/en/7.0.x/) - Ferramenta de testes automatizados para validar a funcionalidade dos algoritmos.
- [Unittest](https://docs.python.org/3/library/unittest.html) - Framework de testes nativo do Python utilizado para criar e executar os testes automatizados.
- **Algoritmos de Busca** - Técnicas para encontrar elementos em listas e arrays.
- **Estruturas de Dados**: Manipulação de **filas**, **deques**, **listas ligadas** e **listas duplamente ligadas** para organizar e processar os arquivos de texto.
- **Manipulação de Arquivos TXT**: Leitura, processamento e busca de informações em arquivos de texto.


## Entre em contato:
<a href="mailto:zazac3179@gmail.com" target="_blank">
  <img align="center" src="https://img.shields.io/badge/Gmail-D14836?style=for-the-badge&logo=gmail&logoColor=white" alt="E-mail" height="40" width="auto" />
</a>
<a href="https://www.linkedin.com/in/isaque-s-oliveira/" target="blank"><img align="center" src="https://raw.githubusercontent.com/rahuldkjain/github-profile-readme-generator/master/src/images/icons/Social/linked-in-alt.svg" alt="isaque oliveira" height="30" width="40" /></a>
<a href="https://wa.me/5574981510614" target="blank"><img align="center" src="https://raw.githubusercontent.com/rahuldkjain/github-profile-readme-generator/master/src/images/icons/Social/whatsapp.svg" alt="WhatsApp" height="30" width="40" /></a>
