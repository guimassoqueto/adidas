# install pre-commit, update its dependencies and install hook for commit messages
pc:
	pre-commit install && pre-commit autoupdate && pre-commit install --hook-type commit-msg

# init env
env:
	cp .env.sample .env

# open repository on browser
or:
	open https://github.com/guimassoqueto/adidas

a:
	poetry run python main.py

docker-build:
	docker build -t guimas/adidas:latest . -f dev.Dockerfile --no-cache

docker-run:
	docker run -d --name test guimas/adidas:latest

exec:
	docker exec -it test bash