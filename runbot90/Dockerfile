# docker build -t runbot .
# docker run -d -e POSTGRES_USER=runbot -e POSTGRES_PASSWORD=runbot --name dbrunbot postgres
# docker run -itP --link dbrunbot:dbrunbot runbot

FROM vauxoo/odoo-80-image
MAINTAINER Moises Lopez <moylop260@vauxoo.com>
RUN adduser --home=/home/runbot --disabled-password --gecos "" --shell=/bin/bash runbot

RUN echo 'root:runbot' |chpasswd
RUN mkdir /home/runbot/.ssh
ADD files/id_rsa /home/runbot/.ssh/id_rsa
ADD files/odoo_runbot.conf /home/runbot/.openerp_serverrc
ADD files/entrypoint.sh /entrypoint.sh
RUN mkdir -p /home/runbot/.local/share/Odoo/filestore
RUN chown runbot:runbot -R /home/runbot \
    && chown runbot:runbot /entrypoint.sh
RUN ln -s /usr/sbin/nginx /usr/bin/nginx

RUN pip install --upgrade git+https://github.com/Vauxoo/panama-dv.git

# Install ngrok to run fowardporting in developer environment
RUN  curl https://dl.ngrok.com/ngrok_2.0.19_linux_amd64.zip -o /tmp/ngrok.zip \
    && unzip -o /tmp/ngrok.zip -d /usr/local/bin/ \
    && rm -rf /tmp/ngrok.zip

USER runbot
RUN ssh-keyscan github.com > ${HOME}/.ssh/known_hosts \
    && ssh-keyscan launchpad.net >> ${HOME}/.ssh/known_hosts \
    && ssh-keyscan bitbucket.org >> ${HOME}/.ssh/known_hosts \
    && ssh-keyscan gitlab.com >> ${HOME}/.ssh/known_hosts
RUN git config --global user.email "runbot@vauxoo.com"
RUN git config --global user.name "Runbot Vauxoo"
RUN /bin/bash -c "mkdir -p /home/runbot/instance/{config,extra_addons}"
RUN git clone -b 8.0 git@github.com:odoo/odoo.git ${HOME}/instance/odoo \
    && git clone -b 8.0-vauxoo git@github.com:Vauxoo/runbot-addons.git ${HOME}/instance/extra_addons/runbot-addons \
    && git clone -b 8.0-vauxoo git@github.com:Vauxoo/odoo-extra.git ${HOME}/instance/extra_addons/odoo-extra \
    && git clone -b 8.0 --single-branch --depth=1 git@github.com:Vauxoo/odoo-themes.git ${HOME}/instance/extra_addons/odoo-themes \
    && git clone -b 8.0 --single-branch --depth=1 git@github.com:Vauxoo/server-tools.git ${HOME}/instance/extra_addons/server-tools

VOLUME ["/home/runbot/.local/share/Odoo/filestore", "/home/runbot/instance/extra_addons/odoo-extra/runbot/static"]

EXPOSE 8069
EXPOSE 8072
EXPOSE 8080

# CMD /entry_point.py
