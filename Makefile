clean:
	rm -rf cache output 

serve:
	nikola auto

.PHONY: clean serve
