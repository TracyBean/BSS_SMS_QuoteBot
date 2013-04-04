'''
Configuration Settings

Includes keys for Twilio, etc.  Second stanza intended for Heroku deployment.
'''

# Uncommet to configure in file.
ACCOUNT_SID = "ACc6bc4e62ba004615fe9bbcf9b244d2e8" 
AUTH_TOKEN = "600da7b3d7304f152b0525d57b16fd28"
BSSSPAM_APP_SID = "AP10ff593f6419c4ec108fe574f6e265e2"
BSS_SPAM_ID = "+1 508-401-7549"


# Begin Heroku configuration - configured through environment variables.
import os
ACCOUNT_SID = os.environ['ACCOUNT_SID']
AUTH_TOKEN = os.environ['AUTH_TOKEN']
BSSSPAM_APP_SID = os.environ['BSSSPAM_APP_SID']
BSS_SPAM_ID = os.environ['BSS_SPAM_ID']
