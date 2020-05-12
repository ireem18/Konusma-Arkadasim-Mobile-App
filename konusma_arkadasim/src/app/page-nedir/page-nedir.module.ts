import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';

import { IonicModule } from '@ionic/angular';

import { PageNedirPageRoutingModule } from './page-nedir-routing.module';

import { PageNedirPage } from './page-nedir.page';

@NgModule({
  imports: [
    CommonModule,
    FormsModule,
    IonicModule,
    PageNedirPageRoutingModule
  ],
  declarations: [PageNedirPage]
})
export class PageNedirPageModule {}
