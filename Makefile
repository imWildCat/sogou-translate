default:
	rm -rf dist && python setup.py bdist_wheel --universal && twine upload dist/*
tag:
	git tag $(TAG) -m $(MSG) && git push --tags origin master
delete-tag:
	git tag --delete $(TAG) ; git push --delete origin $(TAG)