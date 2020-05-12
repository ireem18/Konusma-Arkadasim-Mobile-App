import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';

import { PageKayitPage } from './page-kayit.page';

const routes: Routes = [
  {
    path: '',
    component: PageKayitPage
  }
];

@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule],
})
export class PageKayitPageRoutingModule {}
