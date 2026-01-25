freeze:
	@pip freeze > requirements.txt
install:
	@uv add -r requirements.txt	
