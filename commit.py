#-*- coding: utf-8 -*-
# Copyright 2019 ibelie, Chen Jie, Joungtao. All rights reserved.
# Use of this source code is governed by The MIT License
# that can be found in the LICENSE file.

import time
import os
import re

from properform import properform

def commit(url, token, profile):
	originRe = re.compile(r'https://github.com/(?P<user>[^/]+)/(?P<project>[^\.]+).git', re.I)
	with os.popen('git remote get-url origin') as proc:
		line = proc.readline()
		while line:
			m = originRe.match(line)
			if m:
				user = m.group('user')
				project = m.group('project')
			line = proc.readline()

	with os.popen('git branch') as proc:
		line = proc.readline().strip()
		while line:
			if line.startswith('* '):
				branch = line[2:]
			line = proc.readline().strip()

	with os.popen('git rev-parse HEAD') as proc:
		line = proc.readline().strip()
		while line:
			commit, line = line, proc.readline().strip()

	properform.Push(url + '/properform', token, project, commit, profile, branch)

if __name__ == '__main__':
	import sys
	commit(*sys.argv[1:])
