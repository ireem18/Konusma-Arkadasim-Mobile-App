import { Component, OnInit } from '@angular/core';
import { Router, NavigationExtras } from '@angular/router';
import {ProjectPagePage} from '../project-page/project-page.page';
import {PageKayitPage} from '../page-kayit/page-kayit.page';
import { UserService } from '../user.service';

@Component({
  selector: 'app-page-giris',
  templateUrl: './page-giris.page.html',
  styleUrls: ['./page-giris.page.scss'],
})
export class PageGirisPage implements OnInit {
  input;
  constructor(private router: Router, private userService:UserService) { }

  ngOnInit() {
    this.input = {
      username: '',
      password:''
  
    };
  }

  projectpagegiris(){
    //Proje sayfasına gider
     this.router.navigate(['project-page']);
   }

   sayfaGecis4(){
    //Kayıt olma sayfasına gider
     this.router.navigate(['page-kayit']);
   }
  

   onLoginUser(){
     let navigateExtra: NavigationExtras = {
       queryParams:{
         special: this.input.username,
       }
     }
    this.userService.LoginUser(this.input).subscribe(
      response =>{
        console.log(response);
        alert('Kişi '+ this.input.username + 'logged');
        this.router.navigate(['project-page'],navigateExtra);
      }, err => {
        error => console.log('error ', error);
      }
      );
  }

}
