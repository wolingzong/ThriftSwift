/**
 * Autogenerated by Thrift Compiler (0.13.0)
 *
 * DO NOT EDIT UNLESS YOU ARE SURE THAT YOU KNOW WHAT YOU ARE DOING
 *  @generated
 */

import Foundation

import Thrift


public final class BattleResult_s {

  public var winnerSide: Army_s

  public var loserSide: Army_s


  public init(winnerSide: Army_s, loserSide: Army_s) {
    self.winnerSide = winnerSide
    self.loserSide = loserSide
  }

}

public protocol EOG_BattleSimulation : EOG_Service {

  ///
  /// - Parameters:
  ///   - side1: 
  ///   - side2: 
  /// - Returns: BattleResult_s
  /// - Throws: EOG_Error
  func BattleSimulation(side1: Army_s, side2: Army_s) throws -> BattleResult_s

}

open class EOG_BattleSimulationClient : EOG_ServiceClient /* , EOG_BattleSimulation */ {

}

open class EOG_BattleSimulationProcessor /* EOG_BattleSimulation */ {

  typealias ProcessorHandlerDictionary = [String: (Int32, TProtocol, TProtocol, EOG_BattleSimulation) throws -> Void]

  public var service: EOG_BattleSimulation

  public required init(service: EOG_BattleSimulation) {
    self.service = service
  }

}


