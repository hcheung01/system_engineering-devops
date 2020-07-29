## Postmortem

Service unavailability
Incident Report for LAMP stack powered Wordpress site was not loading
1. Issue Summary:
On March 3 at 14:45 UTC: Website is unresponsive with a returned response code status 500 when trying to access the site through the browser or CURL command with GET method to IP address. All users internal or external were unable to access the webpage, it was just not loading. At 17:35 UTC, found the root cause. 18:15 UTC, deployed automated fixed using Puppet.
2. Timeline
14:45 UTC: webpage found unresponsive after receiving email regarding this issue.
15:00 UTC: Verified with Chrome browser and CURL commands with GET requests.
The original assumption for root cause was the server down. Checked error.log, access.log, then restarted the server while checking logs again but found no related error codes.
Check server’s configuration files, history changes and found new uploaded PHP contents at 13:08 UTC same day.
15:50 UTC: successfully debugged by using strace command
16:15 UTC: deployed automated fix with Puppet scripty to fix spelling error. One of the PHP file’s extension was spelled “.phpp”.
16:30 UTC: Successfully fixed issue
3. Root cause and resolution:
New PHP files were uploaded 2 hours before the incident and WordPress configuration file was changed to include the new files. Server detected the error because it did not find the file listed in the config. Found resolution by using strace command with -p flag to track the child process(PID) of the Apache2 server when listening to requests while sending curl GET requests on a different terminal. strace returned -1 on missing PHP and HTML files. Determined fixed using a Docker container and deployed the automated fix using Puppet.
4. Corrective and preventative measures:
Going forward, please make sure to double check all filename spelling before deployment.
Test all servers are running properly on container first with no errors.
Send requests to the server to make sure the contents are returned with status code 200 and content is correct.
Hope this helps, thanks for reading.