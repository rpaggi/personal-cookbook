# Laravel 5 Express

## Módulo 1

### Instalação Laravel

* Instalar PHP > 5.x - No linux usar sudo apt-get install php
* Instalar Composer (https://getcomposer.org) e configurar ele nas variaveis de ambiente(Link simbólico para o arquivo composer.phar e adicionar a pasta ~/.composer/vendor/bin nas variáveis de ambiente)
* Instalar Laravel(https://laravel.com/docs/5.3)

### Iniciando um projeto
> laravel new nome-do-projeto

### Iniciando um servidor na pasta do projeto
Entrar na pasta e usar o compando
> php artisan serve

### Estrutura das pastas
- server.php - arquivo 
	* Arquivo que ajuda a simular o mod_rewrite, nunca iremos mexer mas é bom saber que ele existe.

- .env - arquivo
	* Arquivo que vai guardar todas as configurações do seu ambiente, usuario e senha de banco de dados, tipos de driver, etc.
	* APP_ENV quer dizer em qual ambiente está rodando(local, production)
	* APP_DEBUG=true irá exibir erros(true or false)

- app/Console
	* Quando precisar criar comandos expecificos para aplicação e que ele seja reconhecido por exemplo no artisan, é nesta pasta que você irá guardar estes comandos de console.

- app/Exceptions
	* Se você precisar criar exceptions personalizadas para a aplicação.

- app/Http
	* Essa pasta é onde mais vamos trabalhar, ela basicamente cuidam das requisições que vão chegar via HTTP para a aplicação.

- app/Http/Controllers
	* São onde ficam os controllers da aplicação

- app/Http/Middleware
	* São funções que ficam entre as nossas requisições e as nossas respostas. Ele intercepta a nossa requisição e por exemplo podemos com ele verificar se o usuário está logado ou não, então a gente consegue fazer algumas verificações durante a requisição.

- app/Http/Requests
	* Onde focam Requests personalizados que podemos criar, por exemplo para fazer validação. Imagine que criamos um Request que quando o cara for criar um usuário, essa requisição vai validar todas as regras deste cadastro.

- app/Jobs - pasta
	* Jobs é uma pasta que você pode guardar classes de comandos que você vai executar. Mas não comandos no console, imagine que você tem uma tarefa que você quer executar em backgroud. 
	* Ex: O usuário fez uma compra no cartão de crédiito, mas você não quer validar ou aguardar o resultado da transação do Cartão de crédito naquele momento, pode haver um congestionamento e o usuário ficar esperando por muito tempo, então você processa em background e você deixa o status de "Pagamento Pendente".

- app/Events e app/Listners - pasta
	* Pastar trabalham em conjunto. Sempre que houver um evento(Cadastro de Usuario) tem um listener que executa uma ação(Enviar email de confirmação)

- app/Providers - pasta
	* Arquivos onde são registrados serviços, eventos e rotas.

- bootstrap - pasta
	* Ficam arquivos que dão o boot no laravel

- config - pasta
	* Onde ficam diversos arquivos de configuração

- database - pasta
	* Pasta responsável por atividades do banco de dados.

- database/factories - pasta
	* São onde ficam arquivos que tem objetos para o banco de dados.
	
- database/migrations - pasta
	* São onde ficam arquivos que geram as estruturas do banco de dados.

- database/seeds - pasta
	* São onde ficam dados de testes para serem carregados no banco de dados.

- public - pasta(uma das principais pastas da aplicação)
	* É a pasta Documment_ROOT da aplicação, quando a pessoa acessar ela cai direto nesta pasta, ela não tem acesso as outras pastas.

- resources - pasta
	* Onde vamos guardar CSSs, arquivos de SASS, COMPASS, LESS, traduções e views(HTMLS).

- routes - paste
	* Onde ficam as rotas da aplicação, pelo que vi no curso(que utiliza o Laravel 5.1), é o mesmo que o arquivo contido na ./app/routes.php

- storage - pasta
	* É uma pasta para armazenar arquivos gerados pelo framework, como sessões, cache, arquivos compilados de view, arquivos de log e arquivos referentes a aplicação.

- testes - pasta
	* É onde ficam guardados os testes da aplicação

- vendor - pasta
	* Quem cuida desta pasta é o composer, são bibliotecas de terceiros que são utilizados no projeto.

### Artisan

- Ele é um facilitador das tarefas do framework

---

> php artisan clear-compiled  

	Limpa o cache das classes compiladas.

---

> php artisan down  

	Coloca a aplicação em manutenção.

---

> php artisan up  

	Tira a aplicação do modo manutenção.

---

> php artisan env  

	Mostra em qual ambiente a aplicação está rodando

---

> php artisan optmize  

	Optimiza a aplicação gerando cache de tudo fazendo que tenha uma melhora de performance

---

> php artisan migrate  

	Roda os arquivos de migração de banco de dados

---

> php artisan app:name  

	Este comando você pode mudar o namespace da sua aplicação

---

> php artisan tinker  

	É um console interativo do Laravel, onde você consegue acessar inclusive suas próprias classes. Você consegue programar PHP dentro dele.

---

## Módulo 2

### Introdução ao MVC
