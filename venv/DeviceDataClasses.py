class DeviceInformation:
    def __init__(self,
                 mac,
                 ip,
                 error_rx,
                 broadcast,
                 netmask,
                 error_tx,
                 tx_bytes,
                 number_device,
                 mtu,
                 rx_bytes,
                 device_name,
                 flags):
        self.mac = mac
        self.ip = ip
        self.error_rx = error_rx
        self.broadcast = broadcast
        self.netmask = netmask
        self.error_tx = error_tx
        self.tx_bytes = tx_bytes
        self.number_device = number_device
        self.mtu = mtu
        self.rx_bytes = rx_bytes
        self.device_name = device_name
        self.flags = flags


class Device:
    def __init__(self,
                 name,
                 information1,
                 information2,
                 information3):
        self.name = name
        self.information1 = information1
        self.information2 = information2
        self.information3 = information3

