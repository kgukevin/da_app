import {Injectable} from '@angular/core';
import {HttpClient} from '@angular/common/http';
import {Report} from '../../Report';
import {Observable} from 'rxjs';
import {catchError} from 'rxjs/operators';

@Injectable({
  providedIn: 'root'
})
export class RestService {

  constructor(private http: HttpClient) {
  }

  inputUrl = 'http://127.0.0.1:5000/update/';
  reportUrl = 'http://127.0.0.1:5000/report/';
  calculatorUrl = 'http://127.0.0.1:5000/calculator/';

  readReport()
  {
    return this.http.get<Report[]>(this.reportUrl);
  }

  updateReport(report: JSON) {
    console.log(report);
    return this.http.put<any>(this.inputUrl, report);
  }

  calculateScore()
  {
    return this.http.get<number>(this.calculatorUrl);
  }

}
