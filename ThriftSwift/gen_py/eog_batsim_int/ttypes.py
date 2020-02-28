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
import eog_shared.ttypes
import eog_unit.ttypes
import eog_exceptions.ttypes

from thrift.transport import TTransport
all_structs = []


class BattleResult_s(object):
    """
    Attributes:
     - winnerSide
     - loserSide

    """


    def __init__(self, winnerSide=None, loserSide=None,):
        self.winnerSide = winnerSide
        self.loserSide = loserSide

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
                if ftype == TType.STRUCT:
                    self.winnerSide = eog_unit.ttypes.Army_s()
                    self.winnerSide.read(iprot)
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.STRUCT:
                    self.loserSide = eog_unit.ttypes.Army_s()
                    self.loserSide.read(iprot)
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
        oprot.writeStructBegin('BattleResult_s')
        if self.winnerSide is not None:
            oprot.writeFieldBegin('winnerSide', TType.STRUCT, 1)
            self.winnerSide.write(oprot)
            oprot.writeFieldEnd()
        if self.loserSide is not None:
            oprot.writeFieldBegin('loserSide', TType.STRUCT, 2)
            self.loserSide.write(oprot)
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
all_structs.append(BattleResult_s)
BattleResult_s.thrift_spec = (
    None,  # 0
    (1, TType.STRUCT, 'winnerSide', [eog_unit.ttypes.Army_s, None], None, ),  # 1
    (2, TType.STRUCT, 'loserSide', [eog_unit.ttypes.Army_s, None], None, ),  # 2
)
fix_spec(all_structs)
del all_structs