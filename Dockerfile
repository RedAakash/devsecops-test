FROM nginx:1.19
RUN rm /etc/nginx/conf.d/default.conf
RUN addgroup -S nginxgrp &amp;&amp; adduser -S nginxusr -G nginxgrp
USER nginxusr
EXPOSE 80
CMD [&quot;nginx&quot;, &quot;-g&quot;, &quot;daemon off;&quot;]
