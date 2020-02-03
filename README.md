# Jenkins-Github-Merge-2-Matser
Use this helper function if you need to trigger Jenkins multibranch build when changes successfully mered to master.

1. Generate Jenkins User's Token:
```	The API token is available in your personal configuration page. 
	Click your name on the top right corner on every page, then click "Configure" 
	to see your API token
```

2. Set necessary values in serverless.yml file:
```	
	environment:
      TRIGGER_BRANCHES: master,stage,etc,comma,separated
      REGION: ${self:custom.region}
      URL_DEFAULT_TTL: ${self:custom.url_default_ttl}
      JENKINS_USER: <username>
      JENKINS_USER_TOKEN: <token>
      JENKINS_URL: https://<jenkins_url>
      JENKINS_PIPELINE_NAME: <multibranch_pipeline_name>
```


3. Install Serverless Framework:
```	
	npm install serverless --global
	serverless plugin install --name serverless-python-requirements
```

4. Configure aws cli (use your preferred method):
```	
	aws configure --profile dev
	export AWS_PROFILE=dev;
```

5. Deploy an app:
```	serverless deploy```

6. Grab endpoint URL:
```
	serverless info
	 # endpoints:
	 # POST - https://4-20-time.execute-api.us-west-2.amazonaws.com/dev/trigger
```

7. Go to GitHub repository settings and create a Webhook:
```
	Payload URL 	= <lambda url>
	Content type 	= application/json
	Let me select individual events: 
		Pull requests;
		Pushes;
```

8. Check the setup (tail Lambda logs):
```
	serverless logs --function trigger --tail
```
