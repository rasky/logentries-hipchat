logentries-hipchat
------------------
Simple integration between logentries and hipchat

How to install and run (with development server):

     virtualenv venv
     venv/bin/pip install -r requirements.txt
     cp logentries-hipchat.cfg.template logentries-hipchat.cfg
     vi logentries-hipchat.cfg    # fill with data
     venv/bin/python logentries-hipchat.py

