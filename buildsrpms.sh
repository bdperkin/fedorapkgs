#! /bin/bash

REL="epel-7-x86_64"
DIST="el7"

for SPEC in $(ls SPECS/*.spec); do
	sudo mock -r ${REL} --buildsrpm --spec ${SPEC} --sources SOURCES
	if [ $? -ne 0 ]; then
		echo "mock buildsrpm failed:"
		echo "================================================="
		grep ^BUILDSTDERR /var/lib/mock/${REL}/result/build.log
		echo "================================================="
		exit 1
	fi
	sudo mv -v /var/lib/mock/${REL}/result/*.${DIST}.src.rpm SRPMS
	if [ $? -ne 0 ]; then
		echo "move of SRPM failed"
		exit 1
	fi
done
