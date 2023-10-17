
#TODO === 1° - Site Random quote === ok
#? === 1° Primeira resolução ===
#* ====1.1° Scraping em 1 nivel. 
#* ==== 1.2° Scraping em 2 nivel (duas paginas dentro do mesmo site).
#? === 2° Segunda resolução ===
#* ====2.1° Scraping em 1 nivel. 
#* ====2.2° Scraping em 2 nivel (duas paginas dentro do mesmo site).

#TODO === 2° - Default Quotes === ok
#! === 1 - Enviando n requisição por site. ===
#? === 1° Primeira resolução ===
#* ====1.1° Scraping em 1 nivel. 
#* ==== 1.2° Scraping em 2 nivel (duas paginas dentro do mesmo site).
#? === 2° Segunda resolução ===
#* ====2.1° Scraping em 1 nivel. 
#* ====2.2° Scraping em 2 nivel (duas paginas dentro do mesmo site).
#? === 3° Terceira resolução ===
#* ====3.1° Scraping em 1 nivel. 
#* ====3.2° Scraping em 2 nivel (duas paginas dentro do mesmo site).
#! === 2 - Enviando apenas 1 requisição por site e paginação. ===
#? === 1° Primeira resolução ===
#* ====1.1° Scraping em 1 nivel. 
#* ==== 1.2° Scraping em 2 nivel (duas paginas dentro do mesmo site). 
#? === 2° Segunda resolução ===
#* ====2.1° Scraping em 1 nivel. 
#* ====2.2° Scraping em 2 nivel (duas paginas dentro do mesmo site). 
#? === 3° Terceira resolução ===
#* ====3.1° Scraping em 1 nivel. 
#* ====3.2° Scraping em 2 nivel (duas paginas dentro do mesmo site). 
#TODO === 3° - Site no Tableful === ok
#? === 1° Primeira resolução ===
#? === 2° Primeira resolução ===
#TODO === 4° Site login === ok
#? === 1° Primeira resolução ===
#? === 2° Segunda resolução ===
#? === 3° Terceira resolução ===
#? === 4° Quarta resolução ===
#TODO === 5° - Requisições com paginas em scroll infinito === ok
#? === 1° Primeira resolução ===
#? === 2° Segunda resolução ===
#TODO === 6° - Conteúdo gerado por JavaScript ===
#! === 1 - Usando a biblioteca chompjs. === ok
#? === 1° Primeira resolução ===
#? === 2° Primeira resolução === 
#! === 2 - Usando a biblioteca json. ===
#? === 1° Primeira resolução === ?
#? === 2° Segunda resolução === 
#TODO === 7° - Conteúdo gerado por JavaScript com Delayed === ok
#? === 1° Primeira resolução ===
#? === 2° Segunda resolução ===
#TODO === 8° - Com um formulário de filtro baseado em AJAX com ViewStates === ok
#? === 1° Primeira resolução ===
#? === 2° Segunda resolução ===


#TODO === Parametros de uma spider. ===

# Esses parâmetros são estatísticas e informações que o Scrapy coleta durante a execução de uma spider (um programa de web scraping). Eles fornecem insights sobre como a spider está funcionando e podem ser úteis para depuração e otimização. Aqui está uma explicação de cada um desses parâmetros:

# downloader/request_bytes: O total de bytes enviados em todas as solicitações feitas pela spider.

# downloader/request_count: O número total de solicitações feitas pela spider.

# downloader/request_method_count/GET: O número de solicitações feitas usando o método HTTP GET.

# downloader/response_bytes: O total de bytes recebidos em todas as respostas das solicitações.

# downloader/response_count: O número total de respostas recebidas.

# downloader/response_status_count/200: O número de respostas com status HTTP 200 (OK).

# downloader/response_status_count/404: O número de respostas com status HTTP 404 (Página não encontrada).

# elapsed_time_seconds: O tempo total decorrido, em segundos, desde o início até o fim da execução da spider.

# feedexport/success_count/FileFeedStorage: O número de itens exportados com sucesso para um feed (arquivo de saída).

# finish_reason: O motivo pelo qual a spider terminou (por exemplo, "finished" significa que a spider terminou com sucesso).

# finish_time: A data e hora em que a spider terminou a execução.

# item_scraped_count: O número total de itens (dados) coletados pela spider.

# log_count/DEBUG: O número de mensagens de log no nível DEBUG durante a execução.

# log_count/INFO: O número de mensagens de log no nível INFO durante a execução.

# request_depth_max: A profundidade máxima alcançada nas solicitações. Isso pode ser útil para rastrear o quão profundamente a spider navegou em um site.

# response_received_count: O número total de respostas recebidas pela spider.

# robotstxt/request_count: O número de solicitações feitas para o arquivo robots.txt do site.

# robotstxt/response_count: O número de respostas recebidas ao acessar o arquivo robots.txt.

# robotstxt/response_status_count/404: O número de respostas com status HTTP 404 ao acessar o arquivo robots.txt.

# scheduler/dequeued: O número de solicitações retiradas da fila de agendamento.

# scheduler/dequeued/memory: O número de solicitações retiradas da fila de agendamento que estavam na memória.

# scheduler/enqueued: O número de solicitações adicionadas à fila de agendamento.

# scheduler/enqueued/memory: O número de solicitações adicionadas à fila de agendamento que foram armazenadas na memória.

# start_time: A data e hora em que a spider foi iniciada.

# Esses parâmetros podem ajudar a entender o desempenho da spider, identificar possíveis problemas e ajustar o comportamento da spider conforme necessário. Por exemplo, se você estiver recebendo muitas respostas com status 404, pode ser necessário verificar as URLs solicitadas ou ajustar a lógica da spide