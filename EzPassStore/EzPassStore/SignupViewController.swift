//
//  SignupViewController.swift
//  EzPassStore
//
//  Created by Alexander Ou on 10/15/16.
//  Copyright © 2016 HashMappers. All rights reserved.
//

import UIKit

class SignupViewController: UIViewController {
    @IBOutlet weak var signupText: UILabel!
    //update the text on signup view
    var username:String = ""
    
    override func viewDidLoad() {
        super.viewDidLoad()
        //ignupText.text = username
        // Do any additional setup after loading the view.
    }

    override func didReceiveMemoryWarning() {
        super.didReceiveMemoryWarning()
        // Dispose of any resources that can be recreated.
    }
    

    /*
    // MARK: - Navigation

    // In a storyboard-based application, you will often want to do a little preparation before navigation
    override func prepare(for segue: UIStoryboardSegue, sender: Any?) {
        // Get the new view controller using segue.destinationViewController.
        // Pass the selected object to the new view controller.
    }
    */

}
