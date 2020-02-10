import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import {InputformComponent} from './inputform/inputform.component';
  import { from } from 'rxjs';

const routes: Routes = [
  {path: 'inputform',component : InputformComponent},
  {path: '',redirectTo:'/inputform',pathMatch:'full'}
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
