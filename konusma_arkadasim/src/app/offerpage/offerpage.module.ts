import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';

import { IonicModule } from '@ionic/angular';

import { OfferpagePageRoutingModule } from './offerpage-routing.module';

import { OfferpagePage } from './offerpage.page';
import { FileUploadModule } from 'ng2-file-upload';
import { Routes, RouterModule } from '@angular/router';
const routes: Routes = [
  {
    path: '',
    component: OfferpagePage
  }
];
@NgModule({
  imports: [
    CommonModule,
    FormsModule,
    IonicModule,
    OfferpagePageRoutingModule,
    RouterModule.forChild(routes),
    FileUploadModule
  ],
  declarations: [OfferpagePage]
})
export class OfferpagePageModule {}
