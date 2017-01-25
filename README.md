An extendable markdown processor -- basic markdown, with plugin capability for easily defining supersets of the language. 

I personally want to use something like this for creating a Markdown variant with action items in lists, so as to have reference data and actions for a GTD system inline. Could be pretty neat! Couldn't find anything similar, but [this](https://github.com/samueljohn/remarkable) is close... just no code. Good ideas though, and something for me to be inspired by. 

Some questions:

* Should plugins be identified in the YAML frontmatter, like LaTeX plugins are in the preamble? That might make it easier for a document to specify what it's been written to look like. It would also mean the writer could specify a few typographic elements etc, which would be really neat.
* *Does* anything like this already exist? Have I missed something?
* Is Python the best langauge to do this in?
* Is it worth writing a markdown interpreter from scratch?
* ...if not, is CommonMark the best one to pick? What else is there?

This is still very much incomplete and unusuable, but I'm excited to give it a go!
