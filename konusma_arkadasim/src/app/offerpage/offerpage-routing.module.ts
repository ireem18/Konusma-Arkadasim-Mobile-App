import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';

import { OfferpagePage } from './offerpage.page';

const routes: Routes = [
  {
    path: '',
    component: OfferpagePage
  }
];

@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule],
})
export class OfferpagePageRoutingModule {}
