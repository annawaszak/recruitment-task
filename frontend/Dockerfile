# Use the official Node.js image from the Docker Hub
FROM node:16

# Set the working directory
WORKDIR /app

# Install dependencies
COPY package.json /app/
COPY package-lock.json /app/
RUN npm install

# Copy the application
COPY . /app/

# Expose the port
EXPOSE 3000

# Run the application
CMD ["npm", "start"]
