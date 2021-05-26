import { Component, OnInit } from '@angular/core';
import { FormGroup, FormControl } from '@angular/forms';
import { Validators } from '@angular/forms';

@Component({
  selector: 'app-create-task',
  templateUrl: './create-task.component.html',
  styleUrls: ['./create-task.component.css']
})
export class CreateTaskComponent implements OnInit {

  priorities = [
    {
      'id': 1,
      'name': 'Low'
    },
    {
      'id': 2,
      'name': 'Medium'
    },
    {
      'id': 3,
      'name': 'High'
    }
  ];

  statusList = [
    {
      'id': 1,
      'name': 'Completed'
    },
    {
      'id': 2,
      'name': 'In progress'
    },
    {
      'id': 3,
      'name': 'Planning'
    },
    {
      'id': 4,
      'name': 'Not started'
    },
    {
      'id': 5,
      'name': 'Blocked'
    }
  ];

  tags = [
    {
      'id': 1,
      'name': 'New idea'
    },
    {
      'id': 2,
      'name': 'Front-End enhancement'
    },
    {
      'id': 3,
      'name': 'Back-End feature'
    },
    {
      'id': 4,
      'name': 'Database problem'
    },
    {
      'id': 5,
      'name': 'Technology deprecated'
    },
    {
      'id': 6,
      'name': 'Database feature'
    },
    {
      'id': 7,
      'name': 'Front-End issue'
    },
    {
      'id': 8,
      'name': 'Back-End bug'
    },
  ];

  taskTypes = [
    {
      'id': 1,
      'name': 'New project'
    },
    {
      'id': 2, 
      'name': 'College project'
    },
    {
      'id': 3,
      'name': 'Ongoing project'
    }
  ];

  newTaskGroup = new FormGroup({
    description: new FormControl('', Validators.required),
    status: new FormControl(this.statusList),
    taskType: new FormControl(''),
    priority: new FormControl(''),
    tag: new FormControl('')
  });
  constructor() { }

  ngOnInit(): void {
  }

  onSubmit() {
    console.warn(this.newTaskGroup.value);
  }
}
