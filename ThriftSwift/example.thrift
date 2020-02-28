namespace cpp riverfall.eog
namespace java riverfall.eog


struct ServiceId_s {
  1: i64 serviceId,
  2: string serviceName,
  3: string serviceIp,
  4: i32 port
}

service EOG_Service {
  ServiceId_s GetServiceId()
  void Heartbeat(1: ServiceId_s serviceId)
  void ClientConnected(1: ServiceId_s serviceId)
  void ClientAboutToDisconnect(1: ServiceId_s serviceId)

  void ConfigurationChanged(1: string configName, 2: string configuration)
}
