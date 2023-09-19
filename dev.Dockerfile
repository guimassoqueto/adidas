FROM python:3.11.5 as build
WORKDIR /app
COPY . .
RUN pip install --upgrade pip && \
    pip install poetry && \
    poetry export -f requirements.txt --output requirements.txt        

FROM python:3.11.5
WORKDIR /adidas
COPY --from=build /app/app app/
COPY --from=build /app/main.py .
COPY --from=build /app/requirements.txt .
ENV ADIDAS_API "https://www.adidas.com.br/api/plp/content-engine?query=tenis-outlet"
ENV MAX_CONCURRENCY 8
RUN pip install --upgrade pip && \
    pip install -r requirements.txt
CMD [ "sleep", "3000" ]
