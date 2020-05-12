import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';

import { PagekullanimPage } from './pagekullanim.page';

const routes: Routes = [
  {
    path: '',
    component: PagekullanimPage
  }
];

@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule],
})
export class PagekullanimPageRoutingModule {}
