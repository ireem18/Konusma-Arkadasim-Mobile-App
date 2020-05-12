import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';
import { IonicModule } from '@ionic/angular';
import { PageKayitPageRoutingModule } from './page-kayit-routing.module';
import { PageKayitPage } from './page-kayit.page';
import { HttpClientModule } from '@angular/common/http';


@NgModule({
  imports: [
    CommonModule,
    FormsModule,
    IonicModule,
    PageKayitPageRoutingModule,
    HttpClientModule

  ],
  declarations: [PageKayitPage]
})
export class PageKayitPageModule {}
