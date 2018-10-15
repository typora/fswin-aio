{
	'targets':[
		{
			'target_name':'fswin',
			'include_dirs': [
				'<!(node -e "require(\'nan\')")'
			],
			'conditions':[
				['OS=="win"',{
					'sources':[
						'src/fswin.cpp'
					]
				}]
			]
		}
	]
}