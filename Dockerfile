From mitmproxy/mitmproxy:latest

COPY .mitmproxy /home/mitmproxy/.mitmproxy

EXPOSE 8080 8081
CMD ["mitmweb", "--no-web-open-browser"]

