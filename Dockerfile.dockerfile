# Usa a imagem oficial do Nginx como base
FROM nginx:alpine

# Remove o conteúdo padrão do Nginx
RUN rm -rf /usr/share/nginx/html/*

# Copia os arquivos do site para o diretório padrão do Nginx
COPY . /usr/share/nginx/html

# Expõe a porta 80 para acesso HTTP
EXPOSE 80

# Comando para iniciar o Nginx em primeiro plano
CMD ["nginx", "-g", "daemon off;"]