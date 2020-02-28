/**
 * Autogenerated by Thrift Compiler (0.13.0)
 *
 * DO NOT EDIT UNLESS YOU ARE SURE THAT YOU KNOW WHAT YOU ARE DOING
 *  @generated
 */
#ifndef eog_unit_TYPES_H
#define eog_unit_TYPES_H

#include <iosfwd>

#include <thrift/Thrift.h>
#include <thrift/TApplicationException.h>
#include <thrift/TBase.h>
#include <thrift/protocol/TProtocol.h>
#include <thrift/transport/TTransport.h>

#include <functional>
#include <memory>


namespace riverfall { namespace eog {

struct UnitType_e {
  enum type {
    Fighter = 0,
    Bomber = 1,
    Destroyer = 2,
    Frigate = 3,
    Transporter = 4
  };
};

extern const std::map<int, const char*> _UnitType_e_VALUES_TO_NAMES;

std::ostream& operator<<(std::ostream& out, const UnitType_e::type& val);

std::string to_string(const UnitType_e::type& val);

class Unit_s;

class Army_s;

typedef struct _Unit_s__isset {
  _Unit_s__isset() : attackArea(false), maxTargetCount(false), attack(false), health(false), armor(false), travelSpeed(false), maxMoveRange(false), cargo(false), id(false) {}
  bool attackArea :1;
  bool maxTargetCount :1;
  bool attack :1;
  bool health :1;
  bool armor :1;
  bool travelSpeed :1;
  bool maxMoveRange :1;
  bool cargo :1;
  bool id :1;
} _Unit_s__isset;

class Unit_s : public virtual ::apache::thrift::TBase {
 public:

  Unit_s(const Unit_s&);
  Unit_s& operator=(const Unit_s&);
  Unit_s() : attackArea(0), maxTargetCount(0), attack(0), health(0), armor(0), travelSpeed(0), maxMoveRange(0), cargo(0), id() {
  }

  virtual ~Unit_s() noexcept;
  int8_t attackArea;
  int8_t maxTargetCount;
  int64_t attack;
  int64_t health;
  int64_t armor;
  int64_t travelSpeed;
  int64_t maxMoveRange;
  int64_t cargo;
  std::string id;

  _Unit_s__isset __isset;

  void __set_attackArea(const int8_t val);

  void __set_maxTargetCount(const int8_t val);

  void __set_attack(const int64_t val);

  void __set_health(const int64_t val);

  void __set_armor(const int64_t val);

  void __set_travelSpeed(const int64_t val);

  void __set_maxMoveRange(const int64_t val);

  void __set_cargo(const int64_t val);

  void __set_id(const std::string& val);

  bool operator == (const Unit_s & rhs) const
  {
    if (!(attackArea == rhs.attackArea))
      return false;
    if (!(maxTargetCount == rhs.maxTargetCount))
      return false;
    if (!(attack == rhs.attack))
      return false;
    if (!(health == rhs.health))
      return false;
    if (!(armor == rhs.armor))
      return false;
    if (!(travelSpeed == rhs.travelSpeed))
      return false;
    if (!(maxMoveRange == rhs.maxMoveRange))
      return false;
    if (!(cargo == rhs.cargo))
      return false;
    if (!(id == rhs.id))
      return false;
    return true;
  }
  bool operator != (const Unit_s &rhs) const {
    return !(*this == rhs);
  }

  bool operator < (const Unit_s & ) const;

  uint32_t read(::apache::thrift::protocol::TProtocol* iprot);
  uint32_t write(::apache::thrift::protocol::TProtocol* oprot) const;

  virtual void printTo(std::ostream& out) const;
};

void swap(Unit_s &a, Unit_s &b);

std::ostream& operator<<(std::ostream& out, const Unit_s& obj);

typedef struct _Army_s__isset {
  _Army_s__isset() : id(false), unitList(false) {}
  bool id :1;
  bool unitList :1;
} _Army_s__isset;

class Army_s : public virtual ::apache::thrift::TBase {
 public:

  Army_s(const Army_s&);
  Army_s& operator=(const Army_s&);
  Army_s() : id() {
  }

  virtual ~Army_s() noexcept;
  std::string id;
  std::vector<Unit_s>  unitList;

  _Army_s__isset __isset;

  void __set_id(const std::string& val);

  void __set_unitList(const std::vector<Unit_s> & val);

  bool operator == (const Army_s & rhs) const
  {
    if (!(id == rhs.id))
      return false;
    if (!(unitList == rhs.unitList))
      return false;
    return true;
  }
  bool operator != (const Army_s &rhs) const {
    return !(*this == rhs);
  }

  bool operator < (const Army_s & ) const;

  uint32_t read(::apache::thrift::protocol::TProtocol* iprot);
  uint32_t write(::apache::thrift::protocol::TProtocol* oprot) const;

  virtual void printTo(std::ostream& out) const;
};

void swap(Army_s &a, Army_s &b);

std::ostream& operator<<(std::ostream& out, const Army_s& obj);

}} // namespace

#endif
