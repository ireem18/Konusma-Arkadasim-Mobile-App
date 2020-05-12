import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';

import { IonicModule } from '@ionic/angular';

import { ProjectPagePageRoutingModule } from './project-page-routing.module';

import { ProjectPagePage } from './project-page.page';

import { FileUploadModule } from 'ng2-file-upload';
import { Routes, RouterModule } from '@angular/router';

const routes: Routes = [
  {
    path: '',
    component: ProjectPagePage
  }
];

@NgModule({
  imports: [
    CommonModule,
    FormsModule,
    IonicModule,
    ProjectPagePageRoutingModule,
    FileUploadModule
  ],
  declarations: [ProjectPagePage]
})
export class ProjectPagePageModule {}
