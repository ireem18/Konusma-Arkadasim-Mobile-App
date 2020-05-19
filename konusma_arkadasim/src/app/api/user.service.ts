import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders, HttpHeaderResponse } from '@angular/common/http';

@Injectable({
  providedIn: 'root'
})
export class UserService {

 
  constructor(public http:HttpClient) { }

  GetUsersDJANGO(){
    return this.http.get("http://127.0.0.1:8000/api/words/");
  } 

  GetWordsDJANGO(){
    return this.http.get("http://127.0.0.1:8000/api/words/");
  } 
}
