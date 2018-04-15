clean:
	rm -rf cache output 

serve:
	nikola build
	nikola serve

.PHONY: clean serve
