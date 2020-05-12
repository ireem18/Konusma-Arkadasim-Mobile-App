import { Component, OnInit } from '@angular/core';
import { UserService } from '../user.service';
import { Router } from '@angular/router';
import {PageGirisPage} from '../page-giris/page-giris.page';


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

  constructor(private userService:UserService,private router:Router) { }

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
    })
    this.router.navigate(['page-giris']);
  }

  goLoginPage(){
    this.router.navigate(['page-giris']);
  }


}
