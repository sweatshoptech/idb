.DEFAULT_GOAL := test

ifeq ($(CI), true)                # Travis CI
    PYTHON   := python3.5
    PIP      := pip3.5
    PYLINT   := pylint
    COVERAGE := coverage-3.5
    PYDOC    := pydoc3.5
    AUTOPEP8 := autopep8
else                                   # UTCS
    PYTHON   := python3
    PIP      := pip3
    PYLINT   := pylint3
    COVERAGE := coverage-3.5
    PYDOC    := pydoc3.5
    AUTOPEP8 := autopep8
endif

format:
	$(AUTOPEP8) -i models.py 
	$(AUTOPEP8) -i idb.py
	$(AUTOPEP8) -i config.py
	$(AUTOPEP8) -i tables.py

html:
	pydoc -w models.py
	mv models.html IDB1.html

log:
	git log > IDB1.log

pylint:
	$(PYLINT) models.py

clean:
	rm -f *.pyc
	rm -f *.html
	rm -f *.log
	rm -f .coverage

test: format pylint html log
	echo "success"

versions:
	which make
	make --version
	@echo
	which git
	git --version
	@echo
	which $(PYTHON)
	$(PYTHON) --version
	@echo
	which $(PIP)
	$(PIP) --version
	@echo
	which $(PYLINT)
	$(PYLINT) --version
	@echo
	which $(COVERAGE)
	$(COVERAGE) --version
	@echo
	-which $(PYDOC)
	-$(PYDOC) --version
	@echo
	which $(AUTOPEP8)
	$(AUTOPEP8) --version
	@echo
	$(PIP) list
