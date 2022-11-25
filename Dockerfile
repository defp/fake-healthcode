From mitmproxy/mitmproxy:latest

COPY .mitmproxy /home/mitmproxy/.mitmproxy

EXPOSE 8080 8081
ENTRYPOINT ["mitmweb", "--no-web-open-browser", "--set", "block_global=false", "--web-host", "0.0.0.0"]

