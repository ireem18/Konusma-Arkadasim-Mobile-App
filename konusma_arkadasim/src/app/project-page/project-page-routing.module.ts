import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';

import { ProjectPagePage } from './project-page.page';

const routes: Routes = [
  {
    path: '',
    component: ProjectPagePage
  }
];

@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule],
})
export class ProjectPagePageRoutingModule {}
