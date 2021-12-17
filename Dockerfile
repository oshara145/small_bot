FROM oshara145/small_bot

# set timezone
ENV TZ=Asia/Kolkata

RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone \

    # cloning the repo and installing requirements.
    && git clone https://github.com/oshara145/small_bot.git /root/small_bot/ \
    && pip3 install --no-cache-dir -r root/small_bot/requirements.txt \
    && pip3 uninstall av -y && pip3 install av --no-binary av

# changing workdir
WORKDIR /root/small_bot/

# start the bot
CMD ["bash", "resources/startup/startup.sh"]
