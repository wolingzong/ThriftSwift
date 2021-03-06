/**
 * Autogenerated by Thrift Compiler (0.13.0)
 *
 * DO NOT EDIT UNLESS YOU ARE SURE THAT YOU KNOW WHAT YOU ARE DOING
 *  @generated
 */

import Foundation

import Thrift


public protocol EOG_Config : EOG_Service {

  ///
  /// - Parameters:
  ///   - configName: 
  /// - Returns: String
  /// - Throws: EOG_Error
  func GetConfiguration(configName: String) throws -> String

  ///
  /// - Parameters:
  ///   - configName: 
  ///   - configuration: 
  /// - Returns: Bool
  /// - Throws: EOG_Error
  func SetConfiguration(configName: String, configuration: String) throws -> Bool

  ///
  /// - Parameters:
  ///   - serviceId: 
  ///   - configName: 
  /// - Returns: Bool
  /// - Throws: EOG_Error
  func RegisterConfiguration(serviceId: ServiceId_s, configName: String) throws -> Bool

}

open class EOG_ConfigClient : EOG_ServiceClient /* , EOG_Config */ {

}

open class EOG_ConfigProcessor /* EOG_Config */ {

  typealias ProcessorHandlerDictionary = [String: (Int32, TProtocol, TProtocol, EOG_Config) throws -> Void]

  public var service: EOG_Config

  public required init(service: EOG_Config) {
    self.service = service
  }

}


