import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';

import { IonicModule } from '@ionic/angular';

import { PagekullanimPageRoutingModule } from './pagekullanim-routing.module';

import { PagekullanimPage } from './pagekullanim.page';

@NgModule({
  imports: [
    CommonModule,
    FormsModule,
    IonicModule,
    PagekullanimPageRoutingModule
  ],
  declarations: [PagekullanimPage]
})
export class PagekullanimPageModule {}
