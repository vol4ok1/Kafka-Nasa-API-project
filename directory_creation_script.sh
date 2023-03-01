#1. To run bash directory_creation_script.sh
#2. For somereason it thows No such file or directory but it still creates folders

	#Make directories
		#Test dir
		
hdfs dfs -mkdir -p interns/test/landing/apod_edvin_test/api.analyst_data.apod_edvin_landing/
hdfs dfs -mkdir -p interns/test/landing/insight_edvin_test/api.analyst_data.insight_edvin_landing/

hdfs dfs -mkdir -p interns/test/base/api.analyst_data.apod_edvin_test/
hdfs dfs -mkdir -p interns/test/base/api.analyst_data.insight_edvin_test/

hdfs dfs -mkdir -p interns/test/analytical/api.analyst_data.apod_edvin_test
hdfs dfs -mkdir -p interns/test/analytical/api.analyst_data.insight_edvin_test

hdfs dfs -mkdir -p interns/test/error/edvin_volcok_log


		#Prod dir
		
hdfs dfs -mkdir -p interns/prod/landing/apod_edvin/api.analyst_data.apod_edvin_landing
hdfs dfs -mkdir -p interns/prod/landing/insight_edvin/api.analyst_data.insight_edvin_landing
 
hdfs dfs -mkdir -p interns/prod/base/api.analyst_data.apod_edvin
hdfs dfs -mkdir -p interns/prod/base/api.analyst_data.insight_edvin

hdfs dfs -mkdir -p interns/prod/analytical/api.analyst_data.apod_edvin
hdfs dfs -mkdir -p interns/prod/analytical/api.analyst_data.insight_edvin

hdfs dfs -mkdir -p interns/prod/error/edvin_volcok_log

		
		#checkpoint dir

hdfs dfs -mkdir -p interns/checkpoint/test/api.analyst_data.apod_edvin_test
hdfs dfs -mkdir -p interns/checkpoint/test/api.analyst_data.insight_edvin_test

hdfs dfs -mkdir -p interns/checkpoint/prod/api.analyst_data.apod_edvin
hdfs dfs -mkdir -p interns/checkpoint/prod/api.analyst_data.insight_edvin

#When doing with hdfs -dfs for some reason it even says what it's doing but neverthless its still completed it.