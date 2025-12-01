#!/bin/bash

# Script para desplegar en IBM Cloud Code Engine

echo "Desplegando EEG Quantum Net en IBM Cloud..."

# Configurar variables
PROJECT_NAME="eeg-quantum-net"
REGION="us-south"
RESOURCE_GROUP="default"

# Login en IBM Cloud
ibmcloud login --apikey $IBM_CLOUD_API_KEY -r $REGION -g $RESOURCE_GROUP

# Configurar IBM Quantum
ibmcloud quantum service enable -s qiskit-runtime

# Desplegar en Code Engine
ibmcloud ce project select -n $PROJECT_NAME || ibmcloud ce project create -n $PROJECT_NAME

# Desplegar API
ibmcloud ce app create \
  --name eeg-quantum-api \
  --build-source . \
  --dockerfile Dockerfile.api \
  --env IBM_QUANTUM_TOKEN=$IBM_QUANTUM_TOKEN \
  --port 8000 \
  --cpu 2 \
  --memory 4G \
  --min-scale 1 \
  --max-scale 3

# Desplegar Web
ibmcloud ce app create \
  --name eeg-quantum-web \
  --build-source ./web \
  --dockerfile Dockerfile.web \
  --port 5173 \
  --env VITE_API_URL=https://eeg-quantum-api.appdomain.cloud \
  --cpu 1 \
  --memory 2G

echo "Despliegue completado!"