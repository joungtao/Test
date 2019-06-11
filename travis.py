#-*- coding: utf-8 -*-
# Copyright 2019 ibelie, Chen Jie, Joungtao. All rights reserved.
# Use of this source code is governed by The MIT License
# that can be found in the LICENSE file.

from properform.travis import Travis

def test(git_repo, output_dir):
	travis = Travis()
	travis.run(
		# repository to be analyzed
		git_repo,
		#the language that is used for your project
		language = 'python',
		#the revision that need to be analyzed
		commits = (
			'4029e8373597b1ef6c8043074d26796ea01c5c02',
		),
		#extra command that are needed to do after running the scripts in the .travis.yml
		extra_commands = (
			'cp demo.prof /home/travis/output/demo.prof',
		),
		#bind local folder to docker
		extra_volumes = {
			output_dir: {'bind': '/home/travis/output', 'mode': 'rw'},
		}
		#more parameters:
		#log_dir = '', mem_limit = '1G', cpu_count = 1, repeat_count = 1, yaml_files = (), extra_commands = (), extra_volumes = {}, environment = {}
		)

if __name__ == '__main__':
	import sys
	test(*sys.argv[1:])
