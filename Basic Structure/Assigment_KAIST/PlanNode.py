class PlanNode:
    def __init__(self, numNo, strSerialNumber, strModel, numModelNumber, dateStart, numAssemblyOrder, dateEnd,
                 strOrderOrigin):
        self.numNo = numNo
        self.strSerialNumber = strSerialNumber
        self.strModel = strModel
        self.numModelNumber = numModelNumber
        self.dateStart = dateStart
        self.numAssemblyOrder = numAssemblyOrder
        self.dateEnd = dateEnd
        self.strOrderOrigin = strOrderOrigin
        
        self.next = ''
        self.prev = ''

    def printOut(self):
        print('No :', self.numNo, ', SerialNum : ', self.strSerialNumber, ',Model:', self.strModel, ',Start Date:',
              self.dateStart)


    def setNextNode(self, node):
        # Problem 1. complete this method
        self.next = node

    def setPrevNode(self, node):
        # Problem 1. complete this method
        self.prev = node
