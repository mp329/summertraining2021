#!/usr/bin/python3
import subprocess
import cgi

print("content-type: text/html")
print()

f = cgi.FieldStorage()
cmd = f.getvalue("var")


lower_cmd = cmd.lower()
l_str = lower_cmd.split()

Filter=["k8s","kubernetes","provide","for","just","up","me","my","to","or","plzz","please","do","using",      "is","which","whose","has","can","could","pods","pod","you","u","port","number","no.","deployment","hi","a",
",","no","with","the","all","having","name","named","hello","hey","display","print","of","upto","deployments",
"image"]

for i in range(0,len(l_str)):
	if l_str[i] in Filter:
		l_str[i] = ""

j_str = " ".join(l_str)

j_str = j_str.split()

if ("create" in j_str or "deploy" in j_str or "launch" in j_str or "make" in j_str) and len(j_str)<4:
	command = "kubectl create deployment " + j_str[1] + " --image=httpd --kubeconfig admin.conf"

elif ("create" in j_str or "deploy" in j_str or "launch" in j_str) and (len(j_str)<5 and "id" in j_str):
	command = "kubectl create deployment " + j_str[1] + " --image=" + j_str[3] + " --kubeconfig admin.conf"

elif ("get" in j_str or "show" in j_str) and len(j_str)<2:
	command = "kubectl get pods --kubeconfig admin.conf"

elif "describe" in j_str:
	command = "kubectl describe pods --kubeconfig admin.conf"

elif "expose" in j_str:
	command = "kubectl expose deployment " + j_str[1] + " --type='NodePort' --port " + j_str[2] + " --kubeconfig admin.conf"

elif "cluster" in j_str or "cluster's" in j_str or "cluster-info" in j_str or "info" in j_str or "details" in j_str:
	command = "kubectl cluster-info --kubeconfig admin.conf"

elif ("replicas" in j_str or "replica" in j_str or "copies" in j_str or "copy" in j_str) and len(j_str)>3:
	command = "kubectl scale deployment " + j_str[3] + " --replicas=" + j_str[1] + " --kubeconfig admin.conf"

elif "scale" in j_str:
	command = "kubectl scale deployment " + j_str[1] + " --replicas=" + j_str[2] + " --kubeconfig admin.conf"

elif "delete" in j_str and ("svc" in j_str or "service" in j_str):
	command = "kubectl delete svc " + j_str[2] + " --kubeconfig admin.conf"

elif "delete" in j_str or "remove" in j_str:
	command = "kubectl delete pod " + j_str[1] + " --kubeconfig admin.conf"

elif "service" in j_str or "svc" in j_str or "services" in j_str:
	command = "kubectl get svc --kubeconfig admin.conf"

else:
        print("Check your command")



output = subprocess.getoutput(command)
print(output)












