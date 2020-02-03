#!/bin/bash
curl -X POST \
	-u "<jenk_username>:<jenk_user_token>"\
	"https://<jenkins_url>/job/<pipeline_name>/job/<branch>/build?token=BUILD_TOKEN"
