<h1 align="center">Bem-vindo ao WAFCheck 👋</h1>
<p>
</p>

> Ferramenta utilizada para testar ambientes montados com WAFs, verificando tempos de resposta e eficacia das regras configuradas

## Uso

```sh
python3 wafcheck.py -u <host> [-l <lista> -o <output>]
```

## Adição de novas listas

A versão atual da ferramenta disponibiliza 1.500 cargas úteis, agrupadas em 10 categorias/arquivos no diretório `payloads/`. As categorias foram definidas de acordo com as 10 vulnerabilidades mais recorrentes em aplicações Web segundo a OWASP 2020. 
- xss.txt: 200 cargas úteis XSS;
- sqli.txt: 200 cargas úteis SQLi;
- 50 NoSQL \textit{Injection}, 20 LDAP \textit{Injection}, 100 XML \textit{External Entity} (XXE), 10 \textit{Insecure Deserialization}, 900 \textit{Local File Inclusion} (LFI), 7 \textit{Misconfiguration}, 7 \textit{Sensitive Information Exposure} e 6 \textit{Vulnerable Components}.

Para que uma lista personalizada fique disponível para utilização na ferramenta, siga os seguintes passos:

* Crie um arquivo de texto contendo os payloads que serão utilizados.
* Mova o arquivo para o diretório `payloads`.
* Utilize o parâmetro `-l` ou `--list` definindo a nova lista.

Por exemplo, a lista `rce.txt` foi adicionada ao diretório, basta utilizar:

```sh
python3 wafcheck.py -u <host> -l rce
```

Todas as listas disponíveis são exibidas no menu de ajuda da ferramenta, é possível visualizar essa mensagem através da utilização do parâmetro `-h`

## Máquinas Virtuais (VMs) - ambiente pré-configurado para testes com WAFs
Para facilitar os testes com a ferramenta, disponibilizamos quatro máquinas virtuais com as soluções de Web Application Firewall ModSecurity, Naxsi, ShadowDaemon e xWAF já configuradas.

O link a seguir disponibiliza um arquivo compactado contendo as 4 (quatros) VMs. 
A integridade do arquivo pode ser verificada através do resumo criptográfico (saída hexadecimal da função de hash) SHA256 `03f8f5b57c2f9e8dee23fd848fbe851d86ce1decf82963f0cd49698a55f474d6`. 

>https://bit.ly/2RPzbU0

## Autor

👤 **Felipe Melchior**

* Github: [@felipemelchior](https://github.com/felipemelchior)

## Show your support

Give a ⭐ if this project helped you!

***
_This README was generated with ❤ by [readme-md-generator](https://github.com/kefranabg/readme-md-generator)_
