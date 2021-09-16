Security weakness name: Hard-coded (username), Admin By Default
Security weakness location: Variable 'sat_user' in line 19
Security weakness usage:
	file: Workshop3.play1.yaml
		line   4 | Play name: Create RHEL product
		line   7 | Play name: Create RHEL repo in the product
		line  10 | Play name: Create Sat Tools product
		line  13 | Play name: Create Sat Tools repo in the product
		line  17 | Play name: Sync RHEL via async
		line  21 | Play name: Sync RHEL without async
		line  25 | Play name: Sync Sat Tools via async
		line  29 | Play name: Sync Sat Tools without async
		line  34 | Play name: Create content view
		line  37 | Play name: Add RHEL repo to the content view
		line  40 | Play name: Add Sat Tools repo to the content view
		line  44 | Play name: Publish and promote content view via async
		line  48 | Play name: Publish and promote content view without async
		line  53 | Play name: Create client domain (on 6.4+)
		line  57 | Play name: Create client domain (on 6.3-)
		line  62 | Play name: Create host group
		line  65 | Play name: Create activation key
		line  68 | Play name: Determine '{{ content_rhel_name }}' subscription ID
		line  72 | Play name: Determine '{{ content_sattools_name }}' subscription ID
		line  81 | Play name: Add subscriptions to the activation key
	file: Workshop3.play2.yaml
		line  33 | Play name: Create product
		line  39 | Play name: Create repos
		line  44 | Play name: Start sync asynchronously
		line  57 | Play name: Wait for synces to finish
		line  71 | Play name: Create lifecycle environment
		line  75 | Play name: Create content views
		line  80 | Play name: Publish content views
		line  85 | Play name: Wait for publish to finish
		line  99 | Play name: Promote content views
		line 104 | Play name: Wait for promote to finish

Security weakness name: Hard-coded secret (password)
Security weakness location: Variable 'sat_pass' in line 20
Security weakness usage:
	file: Workshop3.play1.yaml
		line   4 | Play name: Create RHEL product
		line   7 | Play name: Create RHEL repo in the product
		line  10 | Play name: Create Sat Tools product
		line  13 | Play name: Create Sat Tools repo in the product
		line  17 | Play name: Sync RHEL via async
		line  21 | Play name: Sync RHEL without async
		line  25 | Play name: Sync Sat Tools via async
		line  29 | Play name: Sync Sat Tools without async
		line  34 | Play name: Create content view
		line  37 | Play name: Add RHEL repo to the content view
		line  40 | Play name: Add Sat Tools repo to the content view
		line  44 | Play name: Publish and promote content view via async
		line  48 | Play name: Publish and promote content view without async
		line  53 | Play name: Create client domain (on 6.4+)
		line  57 | Play name: Create client domain (on 6.3-)
		line  62 | Play name: Create host group
		line  65 | Play name: Create activation key
		line  68 | Play name: Determine '{{ content_rhel_name }}' subscription ID
		line  72 | Play name: Determine '{{ content_sattools_name }}' subscription ID
		line  81 | Play name: Add subscriptions to the activation key
	file: Workshop3.play2.yaml
		line  33 | Play name: Create product
		line  39 | Play name: Create repos
		line  44 | Play name: Start sync asynchronously
		line  57 | Play name: Wait for synces to finish
		line  71 | Play name: Create lifecycle environment
		line  75 | Play name: Create content views
		line  80 | Play name: Publish content views
		line  85 | Play name: Wait for publish to finish
		line  99 | Play name: Promote content views
		line 104 | Play name: Wait for promote to finish

Security weakness name: Use of HTTP without TLS
Security weakness location: Variable 'content_rhel_url' in line 104
Security weakness usage:
	file: Workshop3.play1.yaml
		line   7 | Play name: Create RHEL repo in the product

Security weakness name: Use of HTTP without TLS
Security weakness location: Variable 'content_sattools_url' in line 107
Security weakness usage:
	file: Workshop3.play1.yaml
		line  13 | Play name: Create Sat Tools repo in the product

Security weakness name: Use of HTTP without TLS
Security weakness location: Variable 'test_sync_repositories_url_template' in line 156
Security weakness usage:
	file: Workshop3.play2.yaml
		line  22 | Play name: No Play Name Available
		line  39 | Play name: Create repos
