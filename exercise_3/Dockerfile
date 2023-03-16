# base image - nginx with tag "latest"
FROM nginx:latest

# update command then upgrade command
RUN apt-get update && apt-get upgrade -y

# copy local HTML file (source) to the new Docker container (destination)
COPY index.html /usr/share/nginx/html/index.html

# the server listens at PORT 8080
EXPOSE 8080
 
CMD ["nginx", "-g", "daemon off;"]