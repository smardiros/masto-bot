from mastodon import Mastodon
import re

#   Set up Mastodon
mastodon = Mastodon(
    access_token = 'token.secret',
    api_base_url = 'https://botsin.space/'
)

#mastodon.status_post("test post!", spoiler_text="Moby Dick")

format_chars = r'[_]'


text_file = open("dick.txt", "r", encoding="utf8")


lines = text_file.readlines()

paragraph = ""
para_line = 0
prev_paragraph = ""
prev_para_line = 0

count = 0
current_chapter = ""

for i, line in enumerate(lines[:20]):
	print(line)
	# GROUPING

	if re.match(r'^CHAPTER \d+\.', line):
		current_chapter = line[:-1]
	else:
		if line != "\n":
			paragraph += re.sub(format_chars, 's', line[:-1]) + " "
		else:
			print("aha!")
			if len(paragraph) + len(prev_paragraph) < 400:

				prev_paragraph += "\n" + paragraph
				paragraph = ""
				para_line = i

			elif len(paragraph) < 400:

				prev_paragraph, prev_para_line = paragraph, para_line
				paragraph = ""
				para_line = i

			elif len(paragraph) > 10:
				print(paragraph)

				# prev_paragraph = paragraph
				# paragraph = ""




print(count)