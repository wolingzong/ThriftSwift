#
# Autogenerated by Thrift Compiler (0.13.0)
#
# DO NOT EDIT UNLESS YOU ARE SURE THAT YOU KNOW WHAT YOU ARE DOING
#
#  options string: py
#

from thrift.Thrift import TType, TMessageType, TFrozenDict, TException, TApplicationException
from thrift.protocol.TProtocol import TProtocolException
from thrift.TRecursive import fix_spec

import sys

from thrift.transport import TTransport
all_structs = []


class UnitType_e(object):
    Fighter = 0
    Bomber = 1
    Destroyer = 2
    Frigate = 3
    Transporter = 4

    _VALUES_TO_NAMES = {
        0: "Fighter",
        1: "Bomber",
        2: "Destroyer",
        3: "Frigate",
        4: "Transporter",
    }

    _NAMES_TO_VALUES = {
        "Fighter": 0,
        "Bomber": 1,
        "Destroyer": 2,
        "Frigate": 3,
        "Transporter": 4,
    }


class Unit_s(object):
    """
    Attributes:
     - attackArea
     - maxTargetCount
     - attack
     - health
     - armor
     - travelSpeed
     - maxMoveRange
     - cargo
     - id

    """


    def __init__(self, attackArea=None, maxTargetCount=None, attack=None, health=None, armor=None, travelSpeed=None, maxMoveRange=None, cargo=None, id=None,):
        self.attackArea = attackArea
        self.maxTargetCount = maxTargetCount
        self.attack = attack
        self.health = health
        self.armor = armor
        self.travelSpeed = travelSpeed
        self.maxMoveRange = maxMoveRange
        self.cargo = cargo
        self.id = id

    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, [self.__class__, self.thrift_spec])
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 1:
                if ftype == TType.BYTE:
                    self.attackArea = iprot.readByte()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.BYTE:
                    self.maxTargetCount = iprot.readByte()
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.I64:
                    self.attack = iprot.readI64()
                else:
                    iprot.skip(ftype)
            elif fid == 4:
                if ftype == TType.I64:
                    self.health = iprot.readI64()
                else:
                    iprot.skip(ftype)
            elif fid == 5:
                if ftype == TType.I64:
                    self.armor = iprot.readI64()
                else:
                    iprot.skip(ftype)
            elif fid == 6:
                if ftype == TType.I64:
                    self.travelSpeed = iprot.readI64()
                else:
                    iprot.skip(ftype)
            elif fid == 7:
                if ftype == TType.I64:
                    self.maxMoveRange = iprot.readI64()
                else:
                    iprot.skip(ftype)
            elif fid == 8:
                if ftype == TType.I64:
                    self.cargo = iprot.readI64()
                else:
                    iprot.skip(ftype)
            elif fid == 9:
                if ftype == TType.STRING:
                    self.id = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, [self.__class__, self.thrift_spec]))
            return
        oprot.writeStructBegin('Unit_s')
        if self.attackArea is not None:
            oprot.writeFieldBegin('attackArea', TType.BYTE, 1)
            oprot.writeByte(self.attackArea)
            oprot.writeFieldEnd()
        if self.maxTargetCount is not None:
            oprot.writeFieldBegin('maxTargetCount', TType.BYTE, 2)
            oprot.writeByte(self.maxTargetCount)
            oprot.writeFieldEnd()
        if self.attack is not None:
            oprot.writeFieldBegin('attack', TType.I64, 3)
            oprot.writeI64(self.attack)
            oprot.writeFieldEnd()
        if self.health is not None:
            oprot.writeFieldBegin('health', TType.I64, 4)
            oprot.writeI64(self.health)
            oprot.writeFieldEnd()
        if self.armor is not None:
            oprot.writeFieldBegin('armor', TType.I64, 5)
            oprot.writeI64(self.armor)
            oprot.writeFieldEnd()
        if self.travelSpeed is not None:
            oprot.writeFieldBegin('travelSpeed', TType.I64, 6)
            oprot.writeI64(self.travelSpeed)
            oprot.writeFieldEnd()
        if self.maxMoveRange is not None:
            oprot.writeFieldBegin('maxMoveRange', TType.I64, 7)
            oprot.writeI64(self.maxMoveRange)
            oprot.writeFieldEnd()
        if self.cargo is not None:
            oprot.writeFieldBegin('cargo', TType.I64, 8)
            oprot.writeI64(self.cargo)
            oprot.writeFieldEnd()
        if self.id is not None:
            oprot.writeFieldBegin('id', TType.STRING, 9)
            oprot.writeString(self.id.encode('utf-8') if sys.version_info[0] == 2 else self.id)
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        return

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)


class Army_s(object):
    """
    Attributes:
     - id
     - unitList

    """


    def __init__(self, id=None, unitList=None,):
        self.id = id
        self.unitList = unitList

    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, [self.__class__, self.thrift_spec])
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 1:
                if ftype == TType.STRING:
                    self.id = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.LIST:
                    self.unitList = []
                    (_etype3, _size0) = iprot.readListBegin()
                    for _i4 in range(_size0):
                        _elem5 = Unit_s()
                        _elem5.read(iprot)
                        self.unitList.append(_elem5)
                    iprot.readListEnd()
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, [self.__class__, self.thrift_spec]))
            return
        oprot.writeStructBegin('Army_s')
        if self.id is not None:
            oprot.writeFieldBegin('id', TType.STRING, 1)
            oprot.writeString(self.id.encode('utf-8') if sys.version_info[0] == 2 else self.id)
            oprot.writeFieldEnd()
        if self.unitList is not None:
            oprot.writeFieldBegin('unitList', TType.LIST, 2)
            oprot.writeListBegin(TType.STRUCT, len(self.unitList))
            for iter6 in self.unitList:
                iter6.write(oprot)
            oprot.writeListEnd()
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        return

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)
all_structs.append(Unit_s)
Unit_s.thrift_spec = (
    None,  # 0
    (1, TType.BYTE, 'attackArea', None, None, ),  # 1
    (2, TType.BYTE, 'maxTargetCount', None, None, ),  # 2
    (3, TType.I64, 'attack', None, None, ),  # 3
    (4, TType.I64, 'health', None, None, ),  # 4
    (5, TType.I64, 'armor', None, None, ),  # 5
    (6, TType.I64, 'travelSpeed', None, None, ),  # 6
    (7, TType.I64, 'maxMoveRange', None, None, ),  # 7
    (8, TType.I64, 'cargo', None, None, ),  # 8
    (9, TType.STRING, 'id', 'UTF8', None, ),  # 9
)
all_structs.append(Army_s)
Army_s.thrift_spec = (
    None,  # 0
    (1, TType.STRING, 'id', 'UTF8', None, ),  # 1
    (2, TType.LIST, 'unitList', (TType.STRUCT, [Unit_s, None], False), None, ),  # 2
)
fix_spec(all_structs)
del all_structs
