/**
 * Autogenerated by Thrift Compiler (0.13.0)
 *
 * DO NOT EDIT UNLESS YOU ARE SURE THAT YOU KNOW WHAT YOU ARE DOING
 *  @generated
 */
#include "eog_exceptions_types.h"

#include <algorithm>
#include <ostream>

#include <thrift/TToString.h>

namespace riverfall { namespace eog {


EOG_Error::~EOG_Error() noexcept {
}


void EOG_Error::__set_errorCode(const int64_t val) {
  this->errorCode = val;
}

void EOG_Error::__set_errorMsg(const std::string& val) {
  this->errorMsg = val;
}
std::ostream& operator<<(std::ostream& out, const EOG_Error& obj)
{
  obj.printTo(out);
  return out;
}


uint32_t EOG_Error::read(::apache::thrift::protocol::TProtocol* iprot) {

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
          xfer += iprot->readI64(this->errorCode);
          this->__isset.errorCode = true;
        } else {
          xfer += iprot->skip(ftype);
        }
        break;
      case 2:
        if (ftype == ::apache::thrift::protocol::T_STRING) {
          xfer += iprot->readString(this->errorMsg);
          this->__isset.errorMsg = true;
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

uint32_t EOG_Error::write(::apache::thrift::protocol::TProtocol* oprot) const {
  uint32_t xfer = 0;
  ::apache::thrift::protocol::TOutputRecursionTracker tracker(*oprot);
  xfer += oprot->writeStructBegin("EOG_Error");

  xfer += oprot->writeFieldBegin("errorCode", ::apache::thrift::protocol::T_I64, 1);
  xfer += oprot->writeI64(this->errorCode);
  xfer += oprot->writeFieldEnd();

  xfer += oprot->writeFieldBegin("errorMsg", ::apache::thrift::protocol::T_STRING, 2);
  xfer += oprot->writeString(this->errorMsg);
  xfer += oprot->writeFieldEnd();

  xfer += oprot->writeFieldStop();
  xfer += oprot->writeStructEnd();
  return xfer;
}

void swap(EOG_Error &a, EOG_Error &b) {
  using ::std::swap;
  swap(a.errorCode, b.errorCode);
  swap(a.errorMsg, b.errorMsg);
  swap(a.__isset, b.__isset);
}

EOG_Error::EOG_Error(const EOG_Error& other0) : TException() {
  errorCode = other0.errorCode;
  errorMsg = other0.errorMsg;
  __isset = other0.__isset;
}
EOG_Error& EOG_Error::operator=(const EOG_Error& other1) {
  errorCode = other1.errorCode;
  errorMsg = other1.errorMsg;
  __isset = other1.__isset;
  return *this;
}
void EOG_Error::printTo(std::ostream& out) const {
  using ::apache::thrift::to_string;
  out << "EOG_Error(";
  out << "errorCode=" << to_string(errorCode);
  out << ", " << "errorMsg=" << to_string(errorMsg);
  out << ")";
}

const char* EOG_Error::what() const noexcept {
  try {
    std::stringstream ss;
    ss << "TException - service has thrown: " << *this;
    this->thriftTExceptionMessageHolder_ = ss.str();
    return this->thriftTExceptionMessageHolder_.c_str();
  } catch (const std::exception&) {
    return "TException - service has thrown: EOG_Error";
  }
}

}} // namespace
