#!/bin/bash

# add back the ones we love
alias l="ls -lah --color"
alias tl="tail -f /var/log/ldap/ldap.log"
alias tm="tail -f /var/log/messages"
alias tms="tail -f /var/log/secure"
alias tmm="tail -f /var/log/mail/{errors,info,warnings}"
alias cds="cd /etc/init.d;ls"

# remove the ones we hate
unalias s > /dev/null 2>&1 || :

