FROM node:slim
RUN mkdir /code
COPY . /code/
WORKDIR /code/

RUN yarn

CMD [ "./entrypoint.sh" ]
