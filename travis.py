#-*- coding: utf-8 -*-
# Copyright 2019 ibelie, Chen Jie, Joungtao. All rights reserved.
# Use of this source code is governed by The MIT License
# that can be found in the LICENSE file.

from properform.travis import Travis

def test(git_repo, output_dir):
	travis = Travis()
	travis.run(git_repo,
		language = 'python',
		commits = (
			'4029e8373597b1ef6c8043074d26796ea01c5c02',
		),
		extra_commands = (
			'cp demo.prof /home/travis/output/demo.prof',
		),
		extra_volumes = {
			output_dir: {'bind': '/home/travis/output', 'mode': 'rw'},
		})

if __name__ == '__main__':
	import sys
	test(*sys.argv[1:])
