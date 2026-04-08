FROM --platform=linux/amd64 python:3.11-slim
FROM python:3.10-slim

# Instala as bibliotecas necessárias
RUN pip install pipecat-ai[daily,openai,deepgram]

# Copia seu código para dentro do robô
COPY bot.py .

# Comando para ligar o bot
CMD ["python", "bot.py"]
