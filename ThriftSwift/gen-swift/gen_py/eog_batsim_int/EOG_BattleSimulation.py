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
import eog_shared.EOG_Service
import logging
from .ttypes import *
from thrift.Thrift import TProcessor
from thrift.transport import TTransport
all_structs = []


class Iface(eog_shared.EOG_Service.Iface):
    def BattleSimulation(self, side1, side2):
        """
        Parameters:
         - side1
         - side2

        """
        pass


class Client(eog_shared.EOG_Service.Client, Iface):
    def __init__(self, iprot, oprot=None):
        eog_shared.EOG_Service.Client.__init__(self, iprot, oprot)

    def BattleSimulation(self, side1, side2):
        """
        Parameters:
         - side1
         - side2

        """
        self.send_BattleSimulation(side1, side2)
        return self.recv_BattleSimulation()

    def send_BattleSimulation(self, side1, side2):
        self._oprot.writeMessageBegin('BattleSimulation', TMessageType.CALL, self._seqid)
        args = BattleSimulation_args()
        args.side1 = side1
        args.side2 = side2
        args.write(self._oprot)
        self._oprot.writeMessageEnd()
        self._oprot.trans.flush()

    def recv_BattleSimulation(self):
        iprot = self._iprot
        (fname, mtype, rseqid) = iprot.readMessageBegin()
        if mtype == TMessageType.EXCEPTION:
            x = TApplicationException()
            x.read(iprot)
            iprot.readMessageEnd()
            raise x
        result = BattleSimulation_result()
        result.read(iprot)
        iprot.readMessageEnd()
        if result.success is not None:
            return result.success
        if result.error is not None:
            raise result.error
        raise TApplicationException(TApplicationException.MISSING_RESULT, "BattleSimulation failed: unknown result")


class Processor(eog_shared.EOG_Service.Processor, Iface, TProcessor):
    def __init__(self, handler):
        eog_shared.EOG_Service.Processor.__init__(self, handler)
        self._processMap["BattleSimulation"] = Processor.process_BattleSimulation
        self._on_message_begin = None

    def on_message_begin(self, func):
        self._on_message_begin = func

    def process(self, iprot, oprot):
        (name, type, seqid) = iprot.readMessageBegin()
        if self._on_message_begin:
            self._on_message_begin(name, type, seqid)
        if name not in self._processMap:
            iprot.skip(TType.STRUCT)
            iprot.readMessageEnd()
            x = TApplicationException(TApplicationException.UNKNOWN_METHOD, 'Unknown function %s' % (name))
            oprot.writeMessageBegin(name, TMessageType.EXCEPTION, seqid)
            x.write(oprot)
            oprot.writeMessageEnd()
            oprot.trans.flush()
            return
        else:
            self._processMap[name](self, seqid, iprot, oprot)
        return True

    def process_BattleSimulation(self, seqid, iprot, oprot):
        args = BattleSimulation_args()
        args.read(iprot)
        iprot.readMessageEnd()
        result = BattleSimulation_result()
        try:
            result.success = self._handler.BattleSimulation(args.side1, args.side2)
            msg_type = TMessageType.REPLY
        except TTransport.TTransportException:
            raise
        except eog_exceptions.ttypes.EOG_Error as error:
            msg_type = TMessageType.REPLY
            result.error = error
        except TApplicationException as ex:
            logging.exception('TApplication exception in handler')
            msg_type = TMessageType.EXCEPTION
            result = ex
        except Exception:
            logging.exception('Unexpected exception in handler')
            msg_type = TMessageType.EXCEPTION
            result = TApplicationException(TApplicationException.INTERNAL_ERROR, 'Internal error')
        oprot.writeMessageBegin("BattleSimulation", msg_type, seqid)
        result.write(oprot)
        oprot.writeMessageEnd()
        oprot.trans.flush()

# HELPER FUNCTIONS AND STRUCTURES


class BattleSimulation_args(object):
    """
    Attributes:
     - side1
     - side2

    """


    def __init__(self, side1=None, side2=None,):
        self.side1 = side1
        self.side2 = side2

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
                    self.side1 = eog_unit.ttypes.Army_s()
                    self.side1.read(iprot)
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.STRUCT:
                    self.side2 = eog_unit.ttypes.Army_s()
                    self.side2.read(iprot)
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
        oprot.writeStructBegin('BattleSimulation_args')
        if self.side1 is not None:
            oprot.writeFieldBegin('side1', TType.STRUCT, 1)
            self.side1.write(oprot)
            oprot.writeFieldEnd()
        if self.side2 is not None:
            oprot.writeFieldBegin('side2', TType.STRUCT, 2)
            self.side2.write(oprot)
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
all_structs.append(BattleSimulation_args)
BattleSimulation_args.thrift_spec = (
    None,  # 0
    (1, TType.STRUCT, 'side1', [eog_unit.ttypes.Army_s, None], None, ),  # 1
    (2, TType.STRUCT, 'side2', [eog_unit.ttypes.Army_s, None], None, ),  # 2
)


class BattleSimulation_result(object):
    """
    Attributes:
     - success
     - error

    """


    def __init__(self, success=None, error=None,):
        self.success = success
        self.error = error

    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, [self.__class__, self.thrift_spec])
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 0:
                if ftype == TType.STRUCT:
                    self.success = BattleResult_s()
                    self.success.read(iprot)
                else:
                    iprot.skip(ftype)
            elif fid == 1:
                if ftype == TType.STRUCT:
                    self.error = eog_exceptions.ttypes.EOG_Error()
                    self.error.read(iprot)
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
        oprot.writeStructBegin('BattleSimulation_result')
        if self.success is not None:
            oprot.writeFieldBegin('success', TType.STRUCT, 0)
            self.success.write(oprot)
            oprot.writeFieldEnd()
        if self.error is not None:
            oprot.writeFieldBegin('error', TType.STRUCT, 1)
            self.error.write(oprot)
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
all_structs.append(BattleSimulation_result)
BattleSimulation_result.thrift_spec = (
    (0, TType.STRUCT, 'success', [BattleResult_s, None], None, ),  # 0
    (1, TType.STRUCT, 'error', [eog_exceptions.ttypes.EOG_Error, None], None, ),  # 1
)
fix_spec(all_structs)
del all_structs
