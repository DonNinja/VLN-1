class Airplane():
    def __init__(self, insignia, plane_id):
        self.__insignia = insignia
        self.__id  = plane_id

    def setInsignia(self,newinsignia):
        self.__insignia = newinsignia

    def getInsignia(self):
        return self.__insignia
    
    def setPlaneId(self,newplaneid):
        self.__id = newplaneid

    def getPlaneId(self):
        return self.__id

    def __str__(self):
        return "{}\n{}".format(self.__insignia,self.__id)