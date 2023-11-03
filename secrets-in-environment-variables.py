
# Instead of including API keys and authorization tokens in your code, it is safer to store them as environment variables,
# and this will be available in the environment in which you are running the code. To achieve this;


import os                                                               # We need to import the os module

export AUTHENTICATION_TOKEN=f707963d20349e6d497deb5566093356                      # (without quotation marks)
# Then when calling that variable in your code, instead of doing auth_token=f707963d20349e6d497deb5566093356, we do

auth_token=os.environ.get("AUTHENTICATION_TOKEN")                       # This is what appears inside your code

