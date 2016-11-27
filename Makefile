LANG=Resurrection

all:
	@./resurrection \
		--name "${LANG}" \
		--grammar "./build/${LANG}-grammar.txt" \
		--dict "./build/${LANG}-dictionary.txt" \
		--abc "./text/abc.txt:./build/${LANG}-abc.txt" \
		--text "./text/sentence.txt:./build/${LANG}-sentence.txt" \
		--text "./text/story.txt:./build/${LANG}-story.txt"
