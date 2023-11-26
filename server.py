import PodSixNet.Channel
import PodSixNet.Server
from time import sleep


class ClientChannel(PodSixNet.Channel.Channel):
    def network(self, data):
        print(data)


class DoNotMissFinalServer(PodSixNet.Server.Server):
    channelClass = ClientChannel

    def Connected(self, channel, addr):
        print(f"New connection: {channel}")


if __name__ == "__main__":
    print("STARTING SERVER ON LOCAL HOST")

    do_not_miss_final_server = DoNotMissFinalServer(localaddr=("0.0.0.0", 12345))

    print("SERVER SUCCESFULLY ONLINE")

    while True:
        do_not_miss_final_server.Pump()
        sleep(0.01)
