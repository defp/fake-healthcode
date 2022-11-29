FROM mitmproxy/mitmproxy:latest

COPY .mitmproxy /home/mitmproxy/.mitmproxy

EXPOSE 8080 8081
ENTRYPOINT ["mitmweb", "--no-web-open-browser", "--set", "connection_strategy=lazy", "--set", "block_global=false", "--web-host", "0.0.0.0", "--scripts", "/scripts/healthcode.py"]

