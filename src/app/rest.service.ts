import {Injectable} from '@angular/core';
import {HttpClient} from '@angular/common/http';
import {Report} from '../../Report';
import { HttpHeaders } from '@angular/common/http';
import {Observable} from 'rxjs';
import {catchError} from 'rxjs/operators';

const httpOptions = {
  headers: new HttpHeaders({
    'Content-Type':  'application/json'
  })
};

@Injectable({
  providedIn: 'root'
})
export class RestService {

  constructor(private http: HttpClient) {
  }

  inputUrl = 'http://127.0.0.1:5000/inputdata/';
  weatherUrl = 'http://127.0.0.1:5000/weatherReport/';
  calculatorUrl = 'http://127.0.0.1:5000/calculator/';

  readWeather()
  {
    return this.http.get<Report[]>(this.weatherUrl);
  }

  updateWeather(report: JSON) {
    console.log(report);
    return this.http.put<any>(this.inputUrl + JSON.stringify(report), report);
  }

  calculateScore()
  {
    return this.http.get<number>(this.calculatorUrl);
  }

}
