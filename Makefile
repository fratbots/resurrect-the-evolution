LANG=Resurrection

all:
	@./resurrection \
		--name "${LANG}" \
		--grammar "./build/${LANG}-grammar.txt" \
		--abc "./build/${LANG}-abc.txt" \
		--dict "./build/${LANG}-dictionary.txt" \
		--text "./text/story.txt:./build/${LANG}-story.txt"
