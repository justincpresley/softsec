Security weakness name: Hard-coded (username), Admin By Default
Security weakness location: Variable 'sat_user' in line 19
Security weakness usage:
	file Workshop3.play1.yaml, lines [4, 7, 10, 13, 17, 21, 25, 29, 34, 37, 40, 44, 48, 53, 57, 62, 65, 68, 72, 81]
	file Workshop3.play2.yaml, lines [33, 39, 44, 57, 71, 75, 80, 85, 99, 104]

Security weakness name: Hard-coded secret (password)
Security weakness location: Variable 'sat_pass' in line 20
Security weakness usage:
	file Workshop3.play1.yaml, lines [4, 7, 10, 13, 17, 21, 25, 29, 34, 37, 40, 44, 48, 53, 57, 62, 65, 68, 72, 81]
	file Workshop3.play2.yaml, lines [33, 39, 44, 57, 71, 75, 80, 85, 99, 104]

Security weakness name: Use of HTTP without TLS
Security weakness location: Variable 'content_rhel_url' in line 104
Security weakness usage:
	file Workshop3.play1.yaml, lines [7]

Security weakness name: Use of HTTP without TLS
Security weakness location: Variable 'content_sattools_url' in line 107
Security weakness usage:
	file Workshop3.play1.yaml, lines [13]

Security weakness name: Use of HTTP without TLS
Security weakness location: Variable 'test_sync_repositories_url_template' in line 156
Security weakness usage:
	file Workshop3.play2.yaml, lines [22, 39]
