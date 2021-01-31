FROM archlinux

ENV PATH="/scripts:${PATH}"

COPY ./requirements.txt /requirements.txt

RUN pacman -Syu --noconfirm
RUN pacman -S --noconfirm gcc linux-headers  python3 python-pip

RUN pip install -r /requirements.txt

RUN mkdir /qblock
COPY ./src /qblock
WORKDIR /qblock

COPY ./docker/app/entrypoint.sh /scripts/
RUN chmod +x /scripts/entrypoint.sh

RUN mkdir -p /vol/web/media
RUN mkdir -p /vol/web/static

RUN useradd -m user_d
RUN chown -R user_d:user_d /vol
RUN chown -R user_d:user_d /qblock

RUN chmod -R 755 /vol/web

CMD ["entrypoint.sh"]
USER user_d
RUN echo "__done__"
