#import para acceso a red
import network
#Para usar protocolo MQTT
from umqtt.simple import MQTTClient

#Importamos modulos necesarios
from machine import Pin
import time

#Propiedades para conectar a un cliente MQTT
MQTT_BROKER = "192.168.137.166"
MQTT_USER = ""
MQTT_PASSWORD = ""
MQTT_CLIENT_ID = ""
MQTT_TOPIC = "jarm/casa/temperatura"
# MQTT_TOPIC_PUBLISH = "CAMBIAR_POR_TU_TOPICO"

MQTT_PORT = 1883

#Creo el objeto que me controlará el sensor
KY_019 = Pin(15, Pin.OUT)

#Función para conectar a WiFi
def conectar_wifi():
    print("Conectando a WiFi...", end="")
    sta_if = network.WLAN(network.STA_IF)
    sta_if.active(True)
    sta_if.connect('Armando', 'Hola1234')
    while not sta_if.isconnected():
        print(".", end="")
        time.sleep(0.3)
    print("\nWiFi Conectada!")



#Funcion para subscribir al broker, topic
def conecta_broker():
    client = MQTTClient(MQTT_CLIENT_ID,
    MQTT_BROKER, port=MQTT_PORT,
    user=MQTT_USER,
    password=MQTT_PASSWORD,
    keepalive=0)
    #client.set_callback(llegada_mensaje)
    client.connect()
    #client.subscribe(MQTT_TOPIC)
    print("Conectado a %s, en el topico %s"%(MQTT_BROKER, MQTT_TOPIC))
    return client

#Funcion encargada de encender un led cuando un mensaje se lo diga
def llegada_mensaje(topic, msg):
    """print("Mensaje:", msg)
    if msg == b'true':
        led.value(1)
    if msg == b'false':
        led.value(0)
"""

#Conectar a wifi
conectar_wifi()
#Conectando a un broker mqtt
client = conecta_broker()

#Ciclo infinito
while True:
    KY_019.value(1)
    state = "Encendido"
    print(state)
    client.publish(MQTT_TOPIC, f"{state}")
    time.sleep(2)
    
    KY_019.value(0)
    state = "Apagado"
    print(state)
    client.publish(MQTT_TOPIC, f"{state}")
    time.sleep(2)