---
title: "Bash script vs Python script for sysadmin tasks?"
slug: "bash-script-vs-python-script-for-sysadmin-tasks"
author: "TaiKedz"
source: "devto_python"
published: "Wed, 24 Jun 2026 09:28:54 +0000"
description: "Which do you prefer to sling around, a bash command or a python script? In my goal to write more python and less shell, for the benefit of my colleagues' san..."
keywords: "host, python, run, return, grep, script, command, def"
generated: "2026-06-24T09:40:50.188874"
---

# Bash script vs Python script for sysadmin tasks?

## Overview

Which do you prefer to sling around, a bash command or a python script? In my goal to write more python and less shell, for the benefit of my colleagues' sanity, I have been trying to favour Python - specifically, readable and maintainable python. I have moaned before about how sysadmin scripts often look very messy and unmaintainable, and I have found a perfect example of how that arises. I needed my team to send me the hostnames, IPs and MAC addresses of their VMs to send to IT for reserving in DHCP, and I started cooking up a python script. Just as I was finishing, I had a flash of inspiration and thought... can't I do just a one-liner in shell? It's just a matter of getting the default IP and looking for the interface that uses it... I wrote the scirpt so that it could give result for a local host, or a series of specified remote hosts. Which would you prefer to commit to a tooling repo? :-) Here's the python script, idiomatic, and hopefully easy to read and maintain. I was going to tell my colleagues "Please clone (script repo) and run the script, supplying the hosts as arguments, like 'gather-ips.py jack@machine1 jack@machine2 ...' (yeah, I would need to send instructions too) #!/usr/bin/env python import re import subprocess import sys class SubprocessError ( Exception ): pass def run ( command : list [ str ]) -> str : proc = subprocess . Popen ( command , stdout = subprocess . PIPE , text = True ) stdout , _ = proc . communicate () if proc . returncode > 0 : raise SubprocessError ( f " Failed { command } , see stderr. " ) return stdout def read_ipa ( ipa_lines ): ipa_entries = {} current = None for line in ipa_lines : m = re . match ( r " ^[0-9]+:\s+(\S+?):.* " , line ) if m : current = m . group ( 1 ) ipa_entries [ current ] = {} continue if current is None : continue current_entry = ipa_entries [ current ] eth_m = re . match ( r " .+link/ether ([a-fA-F0-9:]+) " , line ) if eth_m : current_entry [ " mac " ] = eth_m . group ( 1 ) inet_m = re . match ( r " \s+inet ([0-9.]+)/[0-9]+ " , line ) if inet_m : current_entry [ " ipv4 " ] = inet_m . group ( 1 ) return ipa_entries def get_default_ip ( ipr_lines ): default_line = [ line for line in ipr_lines if ' default via ' in line ][ 0 ] return re . findall ( r " src [0-9.]+ " , default_line )[ 0 ][ 4 :] def get_ipra_lines ( host ): if host : lines = run ([ " ssh " , host , " ip r; echo ===; ip a " ]). split ( " \n " ) idx = 0 for n in range ( len ( lines )): if lines [ n ] == " === " : idx = n break ipr_lines = lines [: idx ] ipa_lines = lines [ idx + 1 :] else : ipr_lines = run ([ " ip " , " r " ]). split ( " \n " ) ipa_lines = run ([ " ip " , " a " ]). split ( " \n " ) return ipr_lines , ipa_lines def ublat ( host_string : str ): try : i = host_string . index ( " @ " ) return host_string [ i + 1 :] except ValueError : return host_string def get_target ( host = None ): ipr_lines , ipa_lines = get_ipra_lines ( host ) entries = read_ipa ( ipa_lines ) def_ip = get_default_ip ( ipr_lines ) hostname = ublat ( host ) if host else run ([ " hostname " ]). strip () for _ , data in entries . items (): if def_ip in data . get ( " ipv4 " , "" ): print ( f " { hostname } \t { data . get ( ' ipv4 ' ) } \t { data . get ( ' mac ' ) } " ) return print ( f " # Nothing in { entries } " ) def main (): if not sys . argv [ 1 :] or " get " in sys . argv [ 1 :]: get_target () return for host in sys . argv [ 1 :]: get_target ( host ) main () For sake of comparison, this is its bash equivalent - it does EXACTLY the same thing: command = "echo \"\$ (hostname) \$ (ip a|grep \"\$ (ip r|grep 'default via'|grep -Po '(?<=src )[0-9.]+') \" -B 1|grep -Po '(?<=ether |inet )( \S +)') \" |xargs echo" if [[ -z " $* " ]] ; then bash -c " $command " exit fi for node in " $@ " ; do ssh " $node " " $command " done In the end, I sent a message to the team and told them: Hi all, Please run this on each of your VMs and send me the output via email echo "$(hostname) $(ip a|grep "$(ip r|grep 'default via'|grep -Po '(?<=src )[0-9.]+')\" -B 1|grep -Po '(?<=ether |inet )(\S+)')"|xargs echo A one-liner in a single message. No sending scripts around. No instructing to clone and execute. Just "run this on each machine." Which approach would you have taken

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/taikedz/bash-script-vs-python-script-for-sysadministration-33dp

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
