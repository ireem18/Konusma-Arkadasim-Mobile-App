import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';

import { PageNedirPage } from './page-nedir.page';

const routes: Routes = [
  {
    path: '',
    component: PageNedirPage
  }
];

@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule],
})
export class PageNedirPageRoutingModule {}
