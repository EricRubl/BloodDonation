from Dispatcher.DataBaseConnector import DataBaseConnector


class Controller:
    def __init__(self):
        """
        todo documentation
        """
        self.db_connector = DataBaseConnector()

    def get_all_donors(self):
        query_result = self.db_connector.call_procedure("GetAllDonors")
        print(query_result)


if __name__ == '__main__':
    ctrl = Controller()
    ctrl.get_all_donors()

