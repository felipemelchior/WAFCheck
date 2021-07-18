<h1 align="center">Bem-vindo ao WAFCheck 👋</h1>
<p>
</p>

> Ferramenta utilizada para testar ambientes montados com WAFs, verificando tempos de resposta e eficacia das regras configuradas

## Uso

```sh
python3 wafcheck.py -u <host> [-l <lista> -o <output>]
```

## Listas de Payloads

A versão atual da ferramenta disponibiliza 1.500 cargas úteis, agrupadas em 10 categorias/arquivos no diretório `payloads/`. As categorias foram definidas de acordo com as 10 vulnerabilidades mais recorrentes em aplicações Web segundo a OWASP 2020 (>https://owasp.org). 
- xss.txt: 200 cargas úteis XSS;
- sqli.txt: 200 cargas úteis SQLi;
- nosqli.txt: 50 cargas úteis NoSQL Injection;
- ldapi.txt: 20 cargas úteis LDAP Injection;
- xxe.txt: 100 cargas úteis XML External Entity (XXE);
- insecuredesearilization.txt: 10 cargas úteis Insecure Deserialization;
- lfi.txt: 900 cargas úteis Local File Inclusion (LFI);
- misconfiguration.txt: 7 cargas úteis Misconfiguration;
- sensitive.txt: 7 cargas úteis Sensitive Information Exposure;
- vulnerablecomponents.txt: 6 cargas úteis Vulnerable Components.

Para incluir uma lista personalizada de cargas úteis, é necessário:

* Crie um arquivo de texto contendo os payloads (um carga útil por linha) que farão parte da nova lista.
* Disponibilizar o arquivo no diretório `payloads`.
* Utilizar o parâmetro `-l` ou `--list` e o nome do arquivo (sem a extensão `.txt`) na linha de comando da ferramenta. 

Por exemplo, ao adicionar uma lista de RCE (arquivo `rce.txt`) no diretório `payloads`, basta executar a ferramenta como apresentado a seguir para que a lista de cargas úteis seja carregada nos testes:

```sh
python3 wafcheck.py -u <host> -l rce
```

Todas as listas disponíveis no diretório `payloads` são exibidas no menu de ajuda da ferramenta. Para visualizar a ajuda e as listas, basta digitar utilizar o parâmetro `-h`. 

```sh
python3 wafcheck.py -h
```

## Máquinas Virtuais (VMs) - ambiente pré-configurado para testes com WAFs
Para facilitar os testes com a ferramenta, disponibilizamos quatro máquinas virtuais com as soluções de Web Application Firewall ModSecurity, Naxsi, ShadowDaemon e xWAF já configuradas.

O link a seguir disponibiliza um arquivo compactado contendo as 4 (quatros) VMs. 
A integridade do arquivo pode ser verificada através do resumo criptográfico (saída hexadecimal da função de hash) SHA256 `03f8f5b57c2f9e8dee23fd848fbe851d86ce1decf82963f0cd49698a55f474d6`. 

>https://bit.ly/2RPzbU0

## Ambientes / Distribuições GNU/Linux

A ferramenta já foi testada e utilizada nos seguintes ambientes / distribuições GNU/Linux:

- Debian 10
```sh
Kernel = 4.19.0-5-amd64 #1 SMP Debian 4.19.37-5+deb10u2 (2019-08-08) x86_64 GNU/Linux
```
```sh
Python = Python 3.7.3, requests 2.21.0, colorama 0.3.7, PyYAML 3.13
```

- SystemRescue 8.03:
```sh
Kernel = 5.10.34-1-lts #1 SMP Sun, 02 May 2021 12:41:09 +0000 x86_64 GNU/Linux
```
```sh
Python = Python 3.9.4, requests 2.25.1, colorama 0.4.4, PyYAML 5.4.1
```
## Autor

👤 **Felipe Melchior**

* Github: [@felipemelchior](https://github.com/felipemelchior)

## Show your support

Give a ⭐ if this project helped you!

***
_This README was generated with ❤ by [readme-md-generator](https://github.com/kefranabg/readme-md-generator)_
