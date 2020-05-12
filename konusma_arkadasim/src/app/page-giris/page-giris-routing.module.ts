import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';

import { PageGirisPage } from './page-giris.page';

const routes: Routes = [
  {
    path: '',
    component: PageGirisPage
  }
];

@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule],
})
export class PageGirisPageRoutingModule {}
