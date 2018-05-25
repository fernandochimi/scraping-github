PROJECT_ID := scraping-github
DCMP = docker-compose

build:
		${DCMP} build

start:
		${DCMP} up

startd:
		${DCMP} up -d

stop:
		${DCMP} stop

clean:
		find . -name "*.pyc" -exec rm -rf {} \;
		rm -rf .cache
		rm -rf src.egg-info
		rm -rf .coverage
		rm -rf *.log

execute:
		sudo chown -R $(USER):$(USER) .
		${MAKE} clean
		${MAKE} build
		${MAKE} start