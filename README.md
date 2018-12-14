# myPhytonWebserver 
# caution: the servers use different ip adresses Dockerfile and command has to be adjusted
After cloning this project run

# 1. Run docker build
sudo docker build --tag mypythonserver .

# 2. Start docker image 
sudo docker run -it -p 8888:9000 --rm mypythonserver

# 3. Start Brower

 http://localhost:8888
 
 # -------------------------------------------------------
 # Without port mapping
 # ------------------------------------------------------
 
 
 # Start docker image
 sudo docker run -it --rm mypythonserver
 
 # get container Id
 sudo docker ps
 
 # get container ip address
 sudo docker insprect <containerId> | grep IPAdress
  
  # start browser with ip adress
  http:// ip-adress :900
 
