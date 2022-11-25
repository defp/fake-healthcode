From mitmproxy/mitmproxy:latest

COPY .mitmproxy /home/mitmproxy/.mitmproxy

CMD ["mitmweb", "--no-web-open-browser"]

