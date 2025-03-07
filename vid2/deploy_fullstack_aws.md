## Create frontend and backend instances on AWS

- 2 ec2 instances

## Create SSL certificate:

- Purchase domain `nhamhhung.net`
- Create SSL certificate with AWS Certificate Manager and link to domain

## Create Application Load Balancer

- Forward HTTPS (port 443) requests to the respective targets:
  - `/` to frontend instance
  - `/api/*` to backend instance

## How frontend requests from backend

- User go to `https://nhamhhung.net` with default path `/`
- User request goes to port `443` of ALB due to `https` connection
- Request decrypted and forwarded to port `80` of listening Nginx server due to path matching `/`, which is serving static files of front end `build` such as `index.html`
- The web UI gets displayed on `https://nhamhhung.net`
- User clicks a button such as `Extract Text`
- Frontend send requests to `https://nhamhhung.net/api/extract-text`
- User request goes to port `443` of ALB due to `https` connection
- Request decrypted and forwarded to port `3000` of listening backend server due to path matching `/api/*`
- Backend listening on port `3000` and make AWS API call to extract text out of image and return response to frontend for display

## For frontend, serve with nginx:

- `ssh -i "/path/to/private_key.pem" ec2-user@ec2-instance` to SSH to server
- Install dependencies like `npm, nginx`
- `sudo vim /etc/nginx/sites-available/default`

```
server {
    listen 80;
    server_name your_domain.com;
    location / {
        root /path/to/your/frontend/build;
        try_files $uri /index.html;
    }
}
```

- `sudo service nginx start`
- `systemctl status nginx`
- `npm run build`
- `rsync -avz -e "ssh -i /path/to/private_key.pem" /path/to/build/ ec2-user@ec2-instance:/var/www/html/`
- Send request to `https://nhamhhung.net/api/*` for backend

## For backend, directly run on server:

- `ssh -i "/path/to/private_key.pem" ec2-user@ec2-instance` to SSH to server
- Install dependencies like `npm, postgresql`
- `sudo -u postgres psql` to connect to DB
- `ALTER USER your_username WITH PASSWORD 'new_password';` to change password
- `psql -h localhost -d postgres -U nhamhhung -p 5432` to access DB `postgres`
- `pm2 start/stop/restart app.js` to run as a background process
- `pm2 list` to view running processes
- `netstat -tuln | grep 3000` to double check port 3000 being run
