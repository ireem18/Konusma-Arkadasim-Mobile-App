import { Injectable } from '@angular/core';
import { HttpClient,HttpHeaders } from '@angular/common/http';
const httpOptions = {
  headers: new HttpHeaders({
    'Content-Type': 'application/json'
  })
}
@Injectable({
  providedIn: 'root'
})
export class UploadingService {
  constructor(private http: HttpClient) { }

  public uploadFormData(formData){
    return this.http.post<any>('http://127.0.0.1:8000/upload/',formData);
  }
}
