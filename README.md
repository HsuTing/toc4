#TOC 4

##use

```
	python tocHw4.py (filename) (query)

	example:

		python tocHw4.py input.txt 0xxx.in
```

##Environment

```
	ubuntu 14.04.2 LTS
```

##Language

```
	python
```

##Flie

> tocHw4.py

```
	First check input is enough(must have two input), and open file.
	Then read every line in file, check if it has "Links", and find url in "url" or "href".
	But if query in url or (xxx).(xxx) is not between "/" and "?", remove this url.
	Finally, count every type in url, and print it.
```
