import { Component, OnInit } from '@angular/core';
import { UserService } from '../user.service';
import { Router } from '@angular/router';
import {PageGirisPage} from '../page-giris/page-giris.page';
import { Observable } from 'rxjs';
import { HttpClient } from '@angular/common/http';

@Component({
  selector: 'app-page-kayit',
  templateUrl: './page-kayit.page.html',
  styleUrls: ['./page-kayit.page.scss'],
  providers: [UserService]
})
export class PageKayitPage implements OnInit {
  register;
  userDetails:any = [];
  articleDetails:any =[];
  dataFromService:any="";
  dataFromService2:any="";

  constructor(private userService:UserService,private router:Router,private http:HttpClient) { }

  ngOnInit() {
    this.register = {
      username:'',
      password:'',
      email:''
    };
  }
  registerUser(){
    this.userService.registerNewUser(this.register).subscribe(
      response =>{
        alert('Kişi '+ this.register.username + 'hesap oluturuldu');
        this.router.navigate(['page-giris']);

      }, err => {
        error => console.log('error ', error);
      }
      );
  }

  GetUsersDetails(){
    this.userService.GetUsers().subscribe((users)=> {
      var anyData = <any>users;
      this.userDetails = anyData.users;
    })
    //console.log(this.userDetails)
  }

  SendData(){
    var dataSend = {"user":  {"name":this.register.username,"email":this.register.email ,"password": this.register.password}};
    this.userService.Senddata(dataSend).subscribe(
    (dataReturnFromService)=>{
      this.dataFromService = JSON.stringify
      (dataReturnFromService);
      console.log(dataReturnFromService);
    })
  }

  goLoginPage(){
    this.router.navigate(['page-giris']);
  } 
  
}
