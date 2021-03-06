/**
 * Autogenerated by Thrift Compiler (0.13.0)
 *
 * DO NOT EDIT UNLESS YOU ARE SURE THAT YOU KNOW WHAT YOU ARE DOING
 *  @generated
 */
#include "eog_shared_types.h"

#include <algorithm>
#include <ostream>

#include <thrift/TToString.h>

namespace riverfall { namespace eog {


ServiceId_s::~ServiceId_s() noexcept {
}


void ServiceId_s::__set_serviceId(const int64_t val) {
  this->serviceId = val;
}

void ServiceId_s::__set_serviceName(const std::string& val) {
  this->serviceName = val;
}

void ServiceId_s::__set_serviceIp(const std::string& val) {
  this->serviceIp = val;
}

void ServiceId_s::__set_port(const int32_t val) {
  this->port = val;
}
std::ostream& operator<<(std::ostream& out, const ServiceId_s& obj)
{
  obj.printTo(out);
  return out;
}


uint32_t ServiceId_s::read(::apache::thrift::protocol::TProtocol* iprot) {

  ::apache::thrift::protocol::TInputRecursionTracker tracker(*iprot);
  uint32_t xfer = 0;
  std::string fname;
  ::apache::thrift::protocol::TType ftype;
  int16_t fid;

  xfer += iprot->readStructBegin(fname);

  using ::apache::thrift::protocol::TProtocolException;


  while (true)
  {
    xfer += iprot->readFieldBegin(fname, ftype, fid);
    if (ftype == ::apache::thrift::protocol::T_STOP) {
      break;
    }
    switch (fid)
    {
      case 1:
        if (ftype == ::apache::thrift::protocol::T_I64) {
          xfer += iprot->readI64(this->serviceId);
          this->__isset.serviceId = true;
        } else {
          xfer += iprot->skip(ftype);
        }
        break;
      case 2:
        if (ftype == ::apache::thrift::protocol::T_STRING) {
          xfer += iprot->readString(this->serviceName);
          this->__isset.serviceName = true;
        } else {
          xfer += iprot->skip(ftype);
        }
        break;
      case 3:
        if (ftype == ::apache::thrift::protocol::T_STRING) {
          xfer += iprot->readString(this->serviceIp);
          this->__isset.serviceIp = true;
        } else {
          xfer += iprot->skip(ftype);
        }
        break;
      case 4:
        if (ftype == ::apache::thrift::protocol::T_I32) {
          xfer += iprot->readI32(this->port);
          this->__isset.port = true;
        } else {
          xfer += iprot->skip(ftype);
        }
        break;
      default:
        xfer += iprot->skip(ftype);
        break;
    }
    xfer += iprot->readFieldEnd();
  }

  xfer += iprot->readStructEnd();

  return xfer;
}

uint32_t ServiceId_s::write(::apache::thrift::protocol::TProtocol* oprot) const {
  uint32_t xfer = 0;
  ::apache::thrift::protocol::TOutputRecursionTracker tracker(*oprot);
  xfer += oprot->writeStructBegin("ServiceId_s");

  xfer += oprot->writeFieldBegin("serviceId", ::apache::thrift::protocol::T_I64, 1);
  xfer += oprot->writeI64(this->serviceId);
  xfer += oprot->writeFieldEnd();

  xfer += oprot->writeFieldBegin("serviceName", ::apache::thrift::protocol::T_STRING, 2);
  xfer += oprot->writeString(this->serviceName);
  xfer += oprot->writeFieldEnd();

  xfer += oprot->writeFieldBegin("serviceIp", ::apache::thrift::protocol::T_STRING, 3);
  xfer += oprot->writeString(this->serviceIp);
  xfer += oprot->writeFieldEnd();

  xfer += oprot->writeFieldBegin("port", ::apache::thrift::protocol::T_I32, 4);
  xfer += oprot->writeI32(this->port);
  xfer += oprot->writeFieldEnd();

  xfer += oprot->writeFieldStop();
  xfer += oprot->writeStructEnd();
  return xfer;
}

void swap(ServiceId_s &a, ServiceId_s &b) {
  using ::std::swap;
  swap(a.serviceId, b.serviceId);
  swap(a.serviceName, b.serviceName);
  swap(a.serviceIp, b.serviceIp);
  swap(a.port, b.port);
  swap(a.__isset, b.__isset);
}

ServiceId_s::ServiceId_s(const ServiceId_s& other0) {
  serviceId = other0.serviceId;
  serviceName = other0.serviceName;
  serviceIp = other0.serviceIp;
  port = other0.port;
  __isset = other0.__isset;
}
ServiceId_s& ServiceId_s::operator=(const ServiceId_s& other1) {
  serviceId = other1.serviceId;
  serviceName = other1.serviceName;
  serviceIp = other1.serviceIp;
  port = other1.port;
  __isset = other1.__isset;
  return *this;
}
void ServiceId_s::printTo(std::ostream& out) const {
  using ::apache::thrift::to_string;
  out << "ServiceId_s(";
  out << "serviceId=" << to_string(serviceId);
  out << ", " << "serviceName=" << to_string(serviceName);
  out << ", " << "serviceIp=" << to_string(serviceIp);
  out << ", " << "port=" << to_string(port);
  out << ")";
}

}} // namespace
