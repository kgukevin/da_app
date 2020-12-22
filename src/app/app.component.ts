import {Component} from '@angular/core';
import {RestService} from './rest.service';
import {Report} from '../../Report';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {
  title = 'da-app';

  inputText = '';

  constructor(private rs: RestService) {
  }

  headers = [];

  report: Report[] = [];

  score: number;

  showData() {
    this.rs.readWeather()
      .subscribe
      (
        (response) => {
          this.report = response;
          console.log(this.report);
          this.headers.length = 0;
          for (const category in this.report[0]) {
            this.headers.push(category);
          }
        },
        (error) => {
          console.log('No Data Found' + error);
        }
      );
  }

  calculate() {
    this.rs.calculateScore()
      .subscribe
      (
        (response) => {
          this.score = +response;
        },
        (error) => {
          console.log('No Data Found' + error);
        }
      );
  }
}
