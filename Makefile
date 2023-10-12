# Change name of your application's entry point

dev-build:
	./tools/activate-venv.sh
	pex . -vvvv --disable-cache -r requirements.txt -m app:execute_app -o bin/app.pex
build:
	./tools/activate-venv.sh
	pex . -r requirements.txt -m app:execute_app -o bin/app.pex