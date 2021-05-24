import { NgModule } from '@angular/core';
import { HomeComponent } from './home/home.component';
import { RouterModule, Routes } from '@angular/router';
import { TasksListComponent } from './tasks/tasks-list/tasks-list.component';
import { CreateTaskComponent } from './tasks/create-task/create-task.component';
import { CommonModule } from '@angular/common';


const routes: Routes = [
  {
    path: 'home',
    component: HomeComponent,
    data: { animation: 'HomePage' }
  },
  {
    path: 'tasks',
    component: TasksListComponent,
    data: { animation: 'TasksPage' },
  },
  {
    path: 'tasks/list',
    component: TasksListComponent,
    data: { animation: 'TasksPage' },
  },
  {
    path: 'tasks/add',
    component: CreateTaskComponent
  },
  {
    path: '',
    redirectTo: 'home',
    pathMatch: 'full'
  }
];


@NgModule({
  imports: [
    RouterModule.forRoot(routes)
  ],
  exports: [RouterModule]
})
export class AppRoutingModule { }