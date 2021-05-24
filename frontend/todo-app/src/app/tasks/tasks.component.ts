import { Component, OnInit } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { TasksService } from './tasks.service';


@Component({
  selector: 'app-tasks',
  templateUrl: './tasks.component.html',
  styleUrls: ['./tasks.component.css'],
  providers: [TasksService]
})
export class TasksComponent implements OnInit {

  constructor(private tasksService: TasksService) { }

  ngOnInit() {
  }
}