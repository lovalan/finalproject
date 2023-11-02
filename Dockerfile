# Utilisez une image de base Ubuntu
FROM ubuntu:20.04

# Installez Node.js
RUN apt-get update && apt-get install -y nodejs

# Copiez votre application dans le conteneur
COPY . /app

# Définissez le répertoire de travail
WORKDIR /app

# Exécutez l'application lorsque le conteneur démarre
CMD ["node", "app.js"]
