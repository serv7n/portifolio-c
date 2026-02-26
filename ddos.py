import aiohttp
import asyncio
import logging

logging.basicConfig(filename='resultados.log', level=logging.INFO, format='%(asctime)s - %(message)s')

async def fazer_requisicao(session, url):
    try:
        async with session.get(url) as resposta:
            logging.info(f"Status: {resposta.status}")
            print(f"Status: {resposta.status}")
    except Exception as e:
        logging.error(f"Erro: {e}")
        print(f"Erro: {e}")

async def teste_carga(url, num_requisicoes):
    async with aiohttp.ClientSession() as session:
        tarefas = [fazer_requisicao(session, url) for _ in range(num_requisicoes)]
        await asyncio.gather(*tarefas)

if __name__ == "__main__":
    url = "https://dronefire.online/"  # Altere para a URL desejada
    num_requisicoes = 100000  # Número total de requisições
    asyncio.run(teste_carga(url, num_requisicoes))
    print("Teste de carga concluído. Verifique o arquivo 'resultados.log' para mais detalhes.")
