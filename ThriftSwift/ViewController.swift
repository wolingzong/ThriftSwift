//
//  ViewController.swift
//  ThriftSwift
//
//  Created by Kuray on 28.02.2020.
//  Copyright © 2020 Coursion. All rights reserved.
//

import UIKit
import Thrift

class ViewController: UIViewController {
    
    override func viewDidLoad() {
        super.viewDidLoad()
        // Do any additional setup after loading the view.
        
        
        do {
            
            let transport = try TSocketTransport(hostname: "109.78.62.218", port: 9000)
            try transport.open()
            print("hello")
            let proto = TBinaryProtocol(on: transport)
            let client = EOG_ConfigClient(inoutProtocol: proto)

            let serviceId = try client.GetServiceId()
            print(serviceId)
            
            DispatchQueue.main.asyncAfter(deadline: .now() + 2000, execute: {
                // code to execute
           
            })
            
            
        } catch let error {
            print("\(error)")
        }
        
    }
    
    
}


