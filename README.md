# myPhytonWebserver 
# caution: the servers use different ip adresses; Dockerfile and commands has to be adjusted
After cloning this project run

# 1. Run docker build
sudo docker build --tag mypythonserver .

# 2. Start docker image 
sudo docker run -it -p 8888:9000 --rm mypythonserver

# 3. Start Brower

 http://localhost:8888
 
 # Alternatively you can start Docker without port mapping
  
 # a) Start docker image
 sudo docker run -it --rm mypythonserver
 
 # b) get container Id
 sudo docker ps
 
 # c) get container ip address
 sudo docker inspect container-Id | grep IPAddress
 
 Result looks like this:
  josef@josef-VirtualBox:$ sudo docker inspect 3e7a161430b1 | grep IPAddress
            "SecondaryIPAddresses": null,
            "IPAddress": "172.17.0.2",
                    "IPAddress": "172.17.0.2",
  josef@josef-VirtualBox:$ 

  
  # d) start browser with ip adress
  http:// ip-adress :9000
  
  First container often gets this address
  
  http://172.17.0.2:9000/
 
