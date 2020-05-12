import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';

import { IonicModule } from '@ionic/angular';

import { PageGirisPageRoutingModule } from './page-giris-routing.module';

import { PageGirisPage } from './page-giris.page';

@NgModule({
  imports: [
    CommonModule,
    FormsModule,
    IonicModule,
    PageGirisPageRoutingModule
  ],
  declarations: [PageGirisPage]
})
export class PageGirisPageModule {}
