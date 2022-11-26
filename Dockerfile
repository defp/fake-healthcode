FROM mitmproxy/mitmproxy:latest

COPY .mitmproxy /home/mitmproxy/.mitmproxy

COPY healthcode.py /scripts/healthcode.py

EXPOSE 8080 8081
ENTRYPOINT ["mitmweb", "--no-web-open-browser", "--set", "block_global=false", "--web-host", "0.0.0.0", "--scripts", "/scripts/healthcode.py"]

