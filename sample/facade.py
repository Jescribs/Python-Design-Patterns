"""
Based on https://sourcemaking.com/design_patterns/facade/cpp/1
 "facade" object that provides a single, simplified interface to the many, potentially complex, individual interfaces within the subsystem.
 In this example, the "subsystem" for responding to a networking service request has been modeled, and a facade (FacilitiesFacade) interposed. The facade "hides" the twisted and bizarre choreography necessary to satisfy even the most basic of requests.
"""
from enum import Enum


class States(Enum):
    'Enumeration with the different states of a network service request'
    Received = 0
    DenyAllKnowledge = 1
    ReferClientToFacilities = 2
    FacilitiesHasNotSentPaperwork = 3
    ElectricianIsNotDone = 4
    ElectricianDidItWrong = 5
    DispatchTechnician = 6
    SignedOff = 7
    DoesNotWork = 8
    FixElectriciansWiring = 9
    Complete = 10


class StatesEU(Enum):
    Received = 0
    RejectTheForm = 1
    SizeTheJob = 2
    SmokeAndJokeBreak = 3
    WaitForAuthorization = 4
    DoTheWrongJob = 5
    BlameTheEngineer = 6
    WaitToPunchOut = 7
    DoHalfAJob = 8
    ComplainToEngineer = 9
    GetClarification = 10
    CompleteTheJob = 11
    TurnInThePaperwork = 12
    Complete = 13


class StatesFD(Enum):
    Received = 0
    AssignToEngineer = 1
    EngineerResearches = 2
    RequestIsNotPossible = 3
    EngineerLeavesCompany = 4
    AssignToNewEngineer = 5
    NewEngineerResearches = 6
    ReassignEngineer = 7
    EngineerReturns = 8
    EngineerResearchesAgain = 9
    EngineerFillsOutPaperWork = 10
    Complete = 11


class StatesFacade(Enum):
    Received = 0
    SubmitToEngineer = 1
    SubmitToElectrician = 2
    SubmitToTechnician = 3


class MisDepartment:
    'Department that allows request for network servcie and process its states in a very efficient way '

    def __init__(self):
        self.__state = 0

    def checkOnStatus(self):
        self.__state += 1
        if States(self.__state) == States.Complete:
            return 1
        return 0

    def submitNetworkRequest(self):
        self.__state = 0


class ElectricianUnion:
    'Department that allows request for network servcie and process its states in a very efficient way '

    def __init__(self):
        self.__state = 0

    def checkOnStatus(self):
        self.__state += 1
        if StatesEU(self.__state) == StatesEU.Complete:
            return 1
        return 0

    def submitNetworkRequest(self):
        self.__state = 0


class FacilitiesDepartment:
    'Department that allows request for network servcie and process its states in a very efficient way '

    def __init__(self):
        self.__state = 0

    def checkOnStatus(self):
        self.__state += 1
        if StatesFD(self.__state) == StatesFD.Complete:
            return 1
        return 0

    def submitNetworkRequest(self):
        self.__state = 0


class FacilitiesFacade:
    'Department that allows request for network servcie and process its states in a very efficient way '

    def __init__(self):
        self.__state = 0
        self.__count = 0
        self.__electrician = ElectricianUnion()
        self.__engineer = FacilitiesDepartment()
        self.__technician = MisDepartment()

    def submitNetworkRequest(self):
        self.__state = 0

    def checkOnStatus(self):
        self.__count += 1
        # Job request has just been received
        if StatesFacade(self.__state) == StatesFacade.Received:
            self.__state += 1
            # Forward the job request to the engineer
            self.__engineer.submitNetworkRequest()
            print("submitted to Facilities - ", self.__count, " phone calls so far")

        elif StatesFacade(self.__state) == StatesFacade.SubmitToEngineer:
            # If engineer is complete, forward to electrician
            if self.__engineer.checkOnStatus():
                self.__state += 1
                self.__electrician.submitNetworkRequest()
                print("submitted to Electrician - ", self.__count, " phone calls so far")

        elif StatesFacade(self.__state) == StatesFacade.SubmitToElectrician:
            # If electrician is complete, forward to technician
            if self.__electrician.checkOnStatus():
                self.__state += 1
                self.__technician.submitNetworkRequest()
                print("submitted to MIS - ", self.__count, "phone calls so far")

        elif StatesFacade(self.__state) == StatesFacade.SubmitToTechnician:
            # If technician is complete, job is done
            if self.__technician.checkOnStatus():
                return 1
            # The job is not entirely complete
            return 0

    def getNumberOfCalls(self):
        return self.__count


facilities = FacilitiesFacade()
facilities.submitNetworkRequest()

# Keep checking until job is complete 
while not(facilities.checkOnStatus()):
    pass

print("job completed after only ", facilities.getNumberOfCalls(), " phone calls")
