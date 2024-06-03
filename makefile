CHROME_PATH = ""

test:
	CHROME_PATH=$(CHROME_PATH) pytest tests -vv
