import { Component, OnInit } from '@angular/core';
import { HttpClient, HttpHeaders, HttpHeaderResponse} from '@angular/common/http';

@Component({
  selector: 'app-inputform',
  templateUrl: './inputform.component.html',
  styleUrls: ['./inputform.component.css']
})
export class InputformComponent implements OnInit {

  public mr;
  public mt;
  public mp;
  public ma;
  public ms;
  public prediction;
  public flag  = false
  
  constructor(private http :HttpClient) { }
  ngOnInit() {
  }
  sendPostRequest() {
    
    this.flag = true
    var headers = new Headers();
    const httpOptions = {
      headers : new HttpHeaders({
        'Content-Type': 'application/json'
        
      })
    }
  
    let postData = {
            data : [this.mr,this.mt,this.mp,this.ma,this.ms]
            
    }
  
    this.http.post("http://127.0.0.1:5000/api", postData, httpOptions)
      .subscribe(data=>{

      this.prediction = JSON.stringify(data),  
      (response) => console.log(response)
     
      } ,
        (error) => console.log(error)
      )
      console.log(this.prediction)
      
      
     
    }
}
