import os


class Communicator:
    def send(self, receiver: str, messageType: str, message: str):
        self.write_result_ressource(receiver, messageType, message)

    def write_result_ressource(self, folder: str, file_name: str, ressource: str):
        path = os.path.join("example_inbox/" + folder)
        if not os.path.exists(path):
            os.makedirs(path)
        with open(f"{path}/{file_name}", "w") as file:
            file.write(ressource)
            file.close()
