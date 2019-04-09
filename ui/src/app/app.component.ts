import { Component } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { of } from 'rxjs';
import { catchError } from 'rxjs/operators';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.scss']
})
export class AppComponent {
  title = 'ui';
  private headers = new HttpHeaders({ 'Content-Type': 'application/json' });
  message = '';

  constructor(private http: HttpClient) { }

  hello() {
    this.http.get<{message: string}>(`/hello`, {
      headers: this.headers,
      observe: 'body',
      responseType: 'json'
    }).pipe(
      catchError(val => {
        return of({message: 'oops... something is broken!'});
      })
    ).subscribe(data => this.message = data.message);
  }
}
