import { Task } from '../../interfaces/task';
import { Component, OnInit } from '@angular/core';
import { TaskService } from 'src/app/services/task.service';


@Component({
  templateUrl: './tasks-list.component.html',
  styleUrls: ['./tasks-list.component.css'],
  providers: [TaskService]
})
export class TasksListComponent implements OnInit {
  pageTitle: string = 'Product List';
  tasks: Task[] = [];
  filteredTasks: Task[] = [];

  private _tasksFilter: string = '';

  constructor(private taskService: TaskService) {}


  ngOnInit() {
    this.getTasks();
  }


  set tasksFilter(substring: string) {
    this._tasksFilter = substring;
    this.filteredTasks = this.performFilter(substring);
  }


  get tasksFilter(): string {
    return this._tasksFilter;
  }


  performFilter(filterBy: string): Task[] {
    filterBy = filterBy.toLocaleLowerCase();
    return this.tasks.filter((task: Task) =>
      task.taskDescription.toLocaleLowerCase().includes(filterBy));
  }


  generateTasksList(tasks: any) {
    for (let object = 0; object < tasks.length; object++) {
      this.tasks.push(tasks[object]);
    }
  }


  getTasks(): void {
    this.taskService.getTasks()
      .subscribe((tasks: any) => (this.generateTasksList(tasks)));
  }
}
