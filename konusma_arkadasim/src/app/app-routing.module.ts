import { NgModule } from '@angular/core';
import { PreloadAllModules, RouterModule, Routes } from '@angular/router';

const routes: Routes = [
  { path: '', redirectTo: 'home', pathMatch: 'full' },
  { path: 'home', loadChildren: () => import('./home/home.module').then( m => m.HomePageModule)},
  {
    path: 'page-nedir',
    loadChildren: () => import('./page-nedir/page-nedir.module').then( m => m.PageNedirPageModule)
  },
  {
    path: 'page-giris',
    loadChildren: () => import('./page-giris/page-giris.module').then( m => m.PageGirisPageModule)
  },
  {
    path: 'pagekullanim',
    loadChildren: () => import('./pagekullanim/pagekullanim.module').then( m => m.PagekullanimPageModule)
  },
  {
    path: 'page-kayit',
    loadChildren: () => import('./page-kayit/page-kayit.module').then( m => m.PageKayitPageModule)
  },
  {
    path: 'project-page',
    loadChildren: () => import('./project-page/project-page.module').then( m => m.ProjectPagePageModule)
  },
  {
    path: 'offerpage',
    loadChildren: () => import('./offerpage/offerpage.module').then( m => m.OfferpagePageModule)
  },
];

@NgModule({
  imports: [
    RouterModule.forRoot(routes, { preloadingStrategy: PreloadAllModules })
  ],
  exports: [RouterModule]
})
export class AppRoutingModule { }
