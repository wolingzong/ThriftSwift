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
import eog_config_types.ttypes
import eog_exceptions.ttypes

from thrift.transport import TTransport
all_structs = []


class ServiceId_s(object):
    """
    Attributes:
     - serviceId
     - serviceName
     - serviceIp
     - port

    """


    def __init__(self, serviceId=None, serviceName=None, serviceIp=None, port=None,):
        self.serviceId = serviceId
        self.serviceName = serviceName
        self.serviceIp = serviceIp
        self.port = port

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
                if ftype == TType.I64:
                    self.serviceId = iprot.readI64()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.STRING:
                    self.serviceName = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.STRING:
                    self.serviceIp = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 4:
                if ftype == TType.I32:
                    self.port = iprot.readI32()
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
        oprot.writeStructBegin('ServiceId_s')
        if self.serviceId is not None:
            oprot.writeFieldBegin('serviceId', TType.I64, 1)
            oprot.writeI64(self.serviceId)
            oprot.writeFieldEnd()
        if self.serviceName is not None:
            oprot.writeFieldBegin('serviceName', TType.STRING, 2)
            oprot.writeString(self.serviceName.encode('utf-8') if sys.version_info[0] == 2 else self.serviceName)
            oprot.writeFieldEnd()
        if self.serviceIp is not None:
            oprot.writeFieldBegin('serviceIp', TType.STRING, 3)
            oprot.writeString(self.serviceIp.encode('utf-8') if sys.version_info[0] == 2 else self.serviceIp)
            oprot.writeFieldEnd()
        if self.port is not None:
            oprot.writeFieldBegin('port', TType.I32, 4)
            oprot.writeI32(self.port)
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
all_structs.append(ServiceId_s)
ServiceId_s.thrift_spec = (
    None,  # 0
    (1, TType.I64, 'serviceId', None, None, ),  # 1
    (2, TType.STRING, 'serviceName', 'UTF8', None, ),  # 2
    (3, TType.STRING, 'serviceIp', 'UTF8', None, ),  # 3
    (4, TType.I32, 'port', None, None, ),  # 4
)
fix_spec(all_structs)
del all_structs
