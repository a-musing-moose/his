.PHONY: build test rm-images rm-pytemp rm-build-dirs clean

ALL_SERVICES = $(wildcard services/*/)
ALL_SHARED = $(wildcard shared/*/)
IMAGES = $(shell docker image ls | grep "his/" | awk '{print $$3}')

build:
	@for shared in $(ALL_SHARED) ; do \
		echo BUILDING SHARED LIBRARY $$shared ; \
		cd $$shared && $(MAKE) build ; \
	done
	@for service in $(ALL_SERVICES) ; do \
		echo BUILDING SERVICE $$service ; \
	    cd $$service && $(MAKE) build ; \
	done

test:
	@for shared in $(ALL_SHARED) ; do \
		echo TESTING SHARED LIBRARY $$shared ; \
		cd $$shared && $(MAKE) test ; \
	done
	@for service in $(ALL_SERVICES) ; do \
		echo TESTING SERVICE $$service ; \
	    cd $$service && $(MAKE) test ; \
	done

rm-images:
	@echo Removing docker images
	@for image in $(IMAGES) ; do \
		docker image rm $$image ; \
	done
	@echo ...done

rm-pytemp:
	@echo Removing temporary files
	@find . -name "*.pyc" -exec rm -rf {} \;
	@find . -name "__pycache__" -exec rm -rf {} \;
	@find . -name ".cache" -exec rm -rf {} \;
	@find . -name ".coverage" -exec rm -rf {} \;
	@echo ...done

rm-build-dirs:
	@for shared in $(ALL_SHARED) ; do \
		echo REMOVING BUILD DIRS FROM $$shared ; \
		cd $$shared && rm -rf build && rm -rf dist ; \
	done

clean: rm-pytemp rm-images rm-build-dirs
