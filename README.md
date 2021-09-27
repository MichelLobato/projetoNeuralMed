# ApiRest que faz o upload da imagem e encaminha para outra aplicacao que entao redimensiona e devolve em um html

Extrura
```
.
├── Dockerfile
├── docker-compose.yml
├── README.md
├── app
│   ├── app.py
│   ├── tasks.py
│   └── templates
│       ├── download.html
│       └── index.html
├── scripts
│   ├── run_celery.sh
│   └── run_web.sh
└── requirements.txt
```

Foram usados nesse projeto as seguintes bliotecas

- Flask para criar ApiRest
- Celery para criar jobs e workes e apontar para os brokers (REDIS E RABBIT)
- Redis e Rabbit amqp, para armazenar e transmitir as mensagens

# Montando imagem

Basta executar os comandos 
` docker-compose build && docker-compose up `
