#!/bin/bash
while [ $password != $password2 ] ; do 
read -s -p "Choose your Password: " password
echo
read -s -p "Re-enter Password: " password2
echo
done

echo "VM Sizes:"
echo "Standard_NC6 Standard_NC12 Standard_NC24 Standard_NC6s_v3 Standard_NC12s_v3 Standard_NC24s_v3"
read -p "Choose VM size (default: Standard_NC6)" vmsizeinput
vmsize=${vmsizeinput:=Standard_NC6}

vmzone="westeurope"
vmname="fai"

echo "Instance: $vmsize" 
echo "Creating resource group"
az group create --name $vmname -l $vmzone
echo "Creating Azure Data Science VM $vmname..."
az vm create --name $vmname -g $vmname --image microsoft-dsvm:ubuntu-1804:1804:latest  --priority Regular --size $vmsize --storage-sku StandardSSD_LRS --admin-user fastuser --admin-password $password

IP=$(az vm show -d -g ${vmname} --name ${vmname} --query publicIps -o tsv)

echo "IP:" ${IP}





