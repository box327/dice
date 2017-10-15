class messageManager:
    def __init__(self):
        self.eventDic = {}

    def listen(self,message,actor):
        eventList = self.eventDic.get(message)
        if eventList is None:
            eventList = []

        eventList.append(actor)
        self.eventDic[message] = eventList

    def send(self,message,parameter):
        eventList = self.eventDic.get(message)
        if eventList is None:
            return

        for event in eventList:
            event(parameter)
