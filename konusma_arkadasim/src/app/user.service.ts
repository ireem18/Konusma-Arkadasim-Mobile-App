import { Injectable } from '@angular/core';
import { HttpClient,HttpHeaders } from '@angular/common/http'
import { Observable } from 'rxjs';

const httpOptions = {
  headers: new HttpHeaders({
    'Content-Type': 'application/json'
  })
}
@Injectable({
  providedIn: 'root'
})
export class UserService {

  constructor(private http:HttpClient) { }

  registerNewUser(userData) : Observable<any> {
    return this.http.post('http://127.0.0.1:8000/api2/users/',userData);
  }
  LoginUser(userData) : Observable<any> {
    return this.http.post('http://127.0.0.1:8000/api2/auth/',userData);
  }

  GetUsers(){
    return this.http.get("http://127.0.0.1:8000/api2/users/?format=json");
    //http://127.0.0.1:8000/api/articles/?format=json
    
  }

  Senddata(dataSend){
    var url = "http://127.0.0.1:8000/api2/users/";
    return this.http.post(url,dataSend,
    {headers: new HttpHeaders(
    {"content-Type":"application/json"})});
  }
}
