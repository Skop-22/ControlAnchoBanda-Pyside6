from pyroute2 import IPRoute

def dispositivos():
    with IPRoute() as ipr:
        devices = ipr.get_links()
        print("Dispositivos de red disponibles:")
        for device in devices:
            print(f"Nombre: {device.get_attr('IFLA_IFNAME')}, Tipo: {device.get_attr('IFLA_LINKINFO')}")

