import { Component } from '@angular/core';
import { NavController } from '@ionic/angular';
import { dependenciesFromGlobalMetadata } from '@angular/compiler/src/render3/r3_factory';
import {PageGirisPage} from '../page-giris/page-giris.page';
import {PagekullanimPage} from '../pagekullanim/pagekullanim.page';
import {PageNedirPage} from '../page-nedir/page-nedir.page';
import {Router} from '@angular/router';



@Component({
  selector: 'app-home',
  templateUrl: 'home.page.html',
  styleUrls: ['home.page.scss'],
})
export class HomePage {
  [x: string]: any;
  dizi:string[];
  kosul:number;

  constructor(private router: Router) {
  
    this.dizi = ["Test1","Test2","Test3"];
    this.kosul = 1;
  }

deneme(){
  console.log("Butona tıklandı");
}
sayfaGecis1(){
  //Sayfa gecisinde kullanılacak metot NavController
  //Giris yapma sayfasına gider
  this.router.navigate(['page-giris']);
}
sayfaGecis2(){
 //Nasıl kullanılır sayfasına gider
  this.router.navigate(['pagekullanim']);
}
sayfaGecis3(){
  //Nedir sayfasına gider
  this.router.navigate(['page-nedir']);
}

}

