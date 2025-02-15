# Created By ANONYMOUSx46

## Firewall Server Rule:

Two Python based firewall server rules I coded as one of my CTF tasks.

In the task, I was told to simulate the firewall’s scripting language by using an HTTP Server and to assume the HTTP Server has no computational requirements and has the sole purpose of filtering incoming traffic.

## Firewall rule parameters:

• Block incoming traffic on client request path “/tomcatwar.jsp” 
<br>
• Block incoming traffic with HTTP headers:
<br>
o

suffix=%>//

c1=Runtime

c2=<%

DNT=1

Content-Type=application/x-www-form-urlencoded
