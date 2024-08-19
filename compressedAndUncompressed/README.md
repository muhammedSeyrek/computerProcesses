
## #extract
	python zipProcess.py extract "file.zip" "output path"

## #compress
	python zipProcess.py compress "file.txt" "output name"

	the sevenzipfile location located inside the file may be in a different location on zipProcess.py

##### In this study, it was tried to prove which zip opener is good.
	file size in test: 4.6 GB
	Compress times in a related file:
		Zipfile = 25.27
		Pyzipper = 21.15
		Patool = 14.08
		Sevenzip = 9.82
		
	as a result of the research, it was decided to make transactions with sevenzip through subprocess. Related file : zipProcess.py
