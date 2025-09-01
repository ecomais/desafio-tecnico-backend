import os
import json
import logging
from datetime import datetime
from sqlalchemy import create_engine, text
import paho.mqtt.client as mqtt
from dotenv import load_dotenv

load_dotenv()

#TODO: Criação do algoritmo de processamento de dados MQTT -> PostgreSQL
