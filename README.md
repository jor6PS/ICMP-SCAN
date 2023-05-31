# ICMP-SCAN

## DESCRIPCIÓN

Herramienta de escaneo ICMP para el descubrimeinto de activos desarrollada en python. ünicamente emite un paquete por activo y espera un segundo a su respuesta para que no se demore mucho el escaneo. 

## USAGE

python```
python3 icmp_scan.py -r <rangp> -t <hilos>

# EJEMPLO

python3 icmp_scan.py -r 192.168.0.0/16 -t 30
```
