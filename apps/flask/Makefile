project := devops-flask

init:
	python3.8 -m venv ~/.$(project)

install:
	pip install --upgrade pip && pip install -r requirements.txt

docker-build:
	docker build -t ${project} .

docker-run:
	docker run -d -p 80:80 ${project}
