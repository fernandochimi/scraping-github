# Scraping Github
Product to scrap Github repositories and save in a file

Check if you have a Docker in your machine. If don't, please install [Docker Engine](https://docs.docker.com/engine/installation/) and [Docker Compose](https://docs.docker.com/compose/install/).

Check if you have a Git in your machine. If don't, please install [Git](https://git-scm.com/downloads).

## Run application
1. First, clone this repository into your local machine:
`git clone https://github.com/fernandochimi/scraping-github.git`
2. Run `make execute` to build and run the application
3. Go! :rocket:

PS: The file `api_env` is for environment values from the application. Contains the URL for api.

## `Makefile` tips
* `make execute` - This command will execute the following commands:
	* `sudo chown -R $(USER):$(USER) .` - Attribute permisions to this directory for manipulating files of project.
	* `clean` - Clean useless files in the project structure.
	* `build` - It will be build the project container.
	* `startd` - This command will execute the container in background.
* `start` - This command will execute the container and exhibit logs.
* `stop` - This command will stop the container.
